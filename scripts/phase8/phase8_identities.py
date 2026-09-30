"""
Phase 8, step A: exact-arithmetic audit of BHZ Corollary 3.5 and of the
Phase-8 reformulation used in the general-intercept margin proof.

Primary source: Berthe-Holton-Zamboni, "Initial powers of Sturmian sequences",
Acta Arith. 122 (2006) 315-347.  Read first-hand (irif.fr/~berthe/Articles/sturm15.pdf).

CONVENTIONS, exactly as stated in BHZ Prop. 2.7 (p.9) -- note the a_1 SHIFT:
    alpha = [0; a_1 + 1, a_2, a_3, ...]
    p_0=0, q_0=1 ;  p_1=1, q_1 = a_1 + 1 ;  q_k = a_k q_{k-1} + q_{k-2} (k>=2)
so the BHZ *digit* a_1 is one less than the first partial quotient of alpha,
while (q_k) ARE the ordinary convergent denominators of alpha.

Admissibility (BHZ Sec. 1 p.2, Prop. 2.7 eq. (1)):
    a_k >= c_k >= 0 for all k ;  a_k >= 1 for k >= 2 ;  c_k = a_k  ==>  c_{k-1} = 0.

Corollary 3.5 / Sec. 4.1:
    x (k) = 1_{a_{k+2}=c_{k+2}} + S_{k+1}/q_k
    x'(k) =                       S_{k+1}/q_k
    y (k) = 1 + S_k/(q_k - c_k q_{k-1}),      S_k := sum_{j=1}^{k} (a_j-c_j) q_{j-1}
    ice(omega) = limsup_k max(x(k),y(k)) = limsup_k max(x'(k),y(k))

Phase-8 reformulation under test:
    d_k := a_k - c_k,  lam_k := q_{k-1}/q_k,  t_k := S_k/q_k,  m_k := t_{k-1} + d_k
    (R1)  t_k     = lam_k * m_k                 and  m_{k+1} = lam_k m_k + d_{k+1}
    (R2)  x'(k)   = m_{k+1}
    (R3)  q_k - c_k q_{k-1} = q_{k-1} (lam_{k-1} + d_k)
    (R4)  y(k)    = 1 + m_k / (lam_{k-1} + d_k)
    (R5)  y(k) - 2 = lam_{k-1} (m_{k-1} - 1) / (lam_{k-1} + d_k)
"""
from fractions import Fraction
import itertools, random, sys

# ---------------------------------------------------------------- conventions

def q_bhz(a):
    """BHZ convergent denominators.  a = [a_1, a_2, ...].  Returns q[0..len(a)]
    with q[0]=q_0=1, q[1]=a_1+1, q[k]=a_k q[k-1]+q[k-2]."""
    q = [Fraction(1)]
    if not a:
        return q
    q.append(Fraction(a[0] + 1))
    for k in range(2, len(a) + 1):
        q.append(a[k - 1] * q[k - 1] + q[k - 2])
    return q

def q_naive(a):
    """The convention used by scripts/phase7/bhz_general_witness.py: q_1 = a_1
    (i.e. the denominators of [0;a_1,a_2,...], NOT of BHZ's [0;a_1+1,a_2,...])."""
    q = [Fraction(1)]
    qprev = Fraction(0)
    for x in a:
        q.append(x * q[-1] + qprev)
        qprev = q[-2]
    return q

def partial_quotients(a):
    """The actual continued fraction of alpha under BHZ's convention."""
    return [a[0] + 1] + list(a[1:])

# ------------------------------------------------------------- admissibility

def admissible(a, c):
    if len(a) != len(c):
        return False
    for k in range(1, len(a) + 1):
        if not (0 <= c[k - 1] <= a[k - 1]):
            return False
        if k >= 2 and a[k - 1] < 1:
            return False
        if c[k - 1] == a[k - 1] and k >= 2 and c[k - 2] != 0:
            return False
    return True

# ------------------------------------------------------------ BHZ quantities

def bhz_terms(a, c, qfun=q_bhz):
    """Returns dict k -> (x(k), x'(k), y(k)) as exact Fractions, for every k
    where the formula's inputs are available.  y(k) is the *formal* value; it is
    an attained prefix power only when 0 < c_k < a_k (BHZ Prop. 3.3)."""
    q = qfun(a)
    n = len(a)
    S = [Fraction(0)] * (n + 1)          # S[k] = sum_{j<=k} (a_j-c_j) q_{j-1}
    for k in range(1, n + 1):
        S[k] = S[k - 1] + (a[k - 1] - c[k - 1]) * q[k - 1]
    out = {}
    for k in range(1, n):                # x'(k) needs S_{k+1}
        xp = S[k + 1] / q[k]
        ind = 1 if (k + 2 <= n and a[k + 1] == c[k + 1]) else 0
        x = ind + xp
        den = q[k] - c[k - 1] * q[k - 1]
        y = 1 + S[k] / den if den != 0 else None
        out[k] = (x, xp, y)
    return out, q, S

def reform_terms(a, c, qfun=q_bhz):
    """The Phase-8 reformulation, computed independently of bhz_terms."""
    q = qfun(a)
    n = len(a)
    lam = [None] * (n + 1)
    for k in range(1, n + 1):
        lam[k] = q[k - 1] / q[k]
    d = [None] + [a[k - 1] - c[k - 1] for k in range(1, n + 1)]
    m = [None] * (n + 2)
    t = [Fraction(0)] * (n + 1)          # t_0 = 0
    for k in range(1, n + 1):
        m[k] = t[k - 1] + d[k]
        t[k] = lam[k] * m[k]
    return lam, d, m, t, q

# ------------------------------------------------------------------- checks

def check_identities(a, c, qfun=q_bhz, label=""):
    """Asserts (R1)-(R5).  Returns the number of k checked."""
    terms, q, S = bhz_terms(a, c, qfun)
    lam, d, m, t, _ = reform_terms(a, c, qfun)
    n = len(a)
    nchk = 0
    for k in range(1, n + 1):
        assert t[k] == S[k] / q[k], (label, "t_k", k)
        assert t[k] == lam[k] * m[k], (label, "R1", k)
        if k + 1 <= n:
            assert m[k + 1] == lam[k] * m[k] + d[k + 1], (label, "R1b", k)
        if k >= 2:
            # (R3)
            assert q[k] - c[k - 1] * q[k - 1] == q[k - 1] * (lam[k - 1] + d[k]), (label, "R3", k)
        if k in terms:
            x, xp, y = terms[k]
            assert xp == m[k + 1], (label, "R2", k)
            if k >= 2 and y is not None:
                assert y == 1 + m[k] / (lam[k - 1] + d[k]), (label, "R4", k)
                assert y - 2 == lam[k - 1] * (m[k - 1] - 1) / (lam[k - 1] + d[k]), (label, "R5", k)
                nchk += 1
    return nchk

def check_bhz_observations(a, c, qfun=q_bhz):
    """BHZ's own three observations in the proof of Cor. 3.5.  Independent
    cross-check that our indexing of x,y matches theirs."""
    terms, q, S = bhz_terms(a, c, qfun)
    n = len(a)
    hits = {"ck=ak -> y(k)=x(k-2)": 0, "ck=0,c(k+1)=a(k+1) -> y(k)<y(k+1)=x(k-1)": 0,
            "ck=0,c(k+1)<a(k+1) -> y(k)<=x(k)": 0}
    for k in range(3, n - 1):
        if k not in terms:
            continue
        _, _, y = terms[k]
        if y is None:
            continue
        if c[k - 1] == a[k - 1]:
            if (k - 2) in terms:
                assert y == terms[k - 2][0], ("obs1", k, y, terms[k - 2][0])
                hits["ck=ak -> y(k)=x(k-2)"] += 1
        elif c[k - 1] == 0:
            if c[k] == a[k]:
                yk1 = terms[k + 1][2]
                assert y < yk1, ("obs2a", k)
                assert yk1 == terms[k - 1][0], ("obs2b", k, yk1, terms[k - 1][0])
                hits["ck=0,c(k+1)=a(k+1) -> y(k)<y(k+1)=x(k-1)"] += 1
            else:
                assert y <= terms[k][0], ("obs3", k, y, terms[k][0])
                hits["ck=0,c(k+1)<a(k+1) -> y(k)<=x(k)"] += 1
    return hits

# ---------------------------------------------------- random admissible digits

def rand_admissible(a, rng):
    c = []
    prev = 0
    for k, ak in enumerate(a, start=1):
        hi = ak if (k == 1 or prev == 0) else ak - 1
        c.append(rng.randint(0, max(0, hi)))
        prev = c[-1]
    return c

def enumerate_admissible(a):
    for c in itertools.product(*[range(ak + 1) for ak in a]):
        if admissible(a, list(c)):
            yield list(c)

# ------------------------------------------------------------------ main

def main():
    rng = random.Random(20260930)
    print("=" * 78)
    print("PHASE 8 / A.  Identity audit: BHZ Cor. 3.5  vs  Phase-8 reformulation")
    print("=" * 78)

    # ---- A1: exhaustive small cases, both q-conventions
    total_k = 0
    total_seq = 0
    for a in [[1]*10, [2]*10, [3]*10, [1,2]*5, [2,1]*5, [1,1,2]*4, [3,1,2,1]*3,
              [1,2,3,4,1,2,3,4,1,2], [4]*10, [1,3,1,3,2,2,1,4,1,2]]:
        for c in itertools.islice(enumerate_admissible(a), 4000):
            for qfun, nm in ((q_bhz, "bhz"), (q_naive, "naive")):
                total_k += check_identities(a, c, qfun, nm)
            total_seq += 1
    print(f"A1 exhaustive: {total_seq} admissible digit sequences x 2 q-conventions,")
    print(f"    {total_k} (k, identity) assertions (R1)-(R5): ALL PASS")

    # ---- A2: random long sequences, bounded type, both conventions
    total_k = 0
    nseq = 0
    for A in range(1, 13):
        for _ in range(40):
            a = [rng.randint(1, A) for _ in range(60)]
            c = rand_admissible(a, rng)
            assert admissible(a, c)
            total_k += check_identities(a, c, q_bhz, f"A={A}")
            nseq += 1
    print(f"A2 random long: {nseq} sequences (length 60, A<=12), "
          f"{total_k} assertions (R1)-(R5): ALL PASS")

    # ---- A3: BHZ's own three observations
    agg = {}
    for A in range(1, 8):
        for _ in range(60):
            a = [rng.randint(1, A) for _ in range(60)]
            c = rand_admissible(a, rng)
            h = check_bhz_observations(a, c)
            for k_, v in h.items():
                agg[k_] = agg.get(k_, 0) + v
    print("A3 BHZ Cor.3.5 proof observations reproduced exactly (counts of verified instances):")
    for k_, v in sorted(agg.items()):
        print(f"      {k_:<48s} {v}")

    # ---- A4: the characteristic sequence and omega(-alpha) closed forms
    print("\nA4 BHZ Sec. 4.2 closed forms, reproduced from the general formula")
    for a, nm in (([1]*24, "a_k=1 (alpha=[0;2,1,1,...] in Q(theta))"),
                  ([2]*24, "a_k=2 (alpha=[0;3,2,2,...])"),
                  ([3,1]*12, "a_k=3,1,3,1,...")):
        # characteristic: c=0 ; omega(-alpha): c = 0 a_2 0 a_4 ...  (BHZ p.17)
        c_char = [0]*len(a)
        c_mal  = [0 if k % 2 == 1 else a[k-1] for k in range(1, len(a)+1)]
        assert admissible(a, c_mal), "omega(-alpha) digits must be admissible"
        for c, cn in ((c_char, "characteristic (c=0)"), (c_mal, "omega(-alpha) = 0 a2 0 a4 ...")):
            terms, q, S = bhz_terms(a, c)
            ks = sorted(terms)[-8:]
            val = max(max(terms[k][0], terms[k][2] or 0) for k in ks)
            print(f"      {nm:<40s} {cn:<32s} ice ~ {float(val):.6f}")
    print("      (BHZ Thm 1.2: ice(char) = ind*(alpha)-1 = 1+limsup[a_{k+1};a_k,...,a_1])")

    print("\nALL IDENTITY CHECKS PASS.")

if __name__ == "__main__":
    main()
