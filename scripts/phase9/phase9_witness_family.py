"""
Phase 9, step A: the unified witness family, its exact lengths and weights, the
surplus-driver identity with the ATTAINMENT ROUTING made explicit, and the parity audit.

SYMBOLS (all fixed here once; BHZ = Berthe-Holton-Zamboni, Acta Arith. 122 (2006) 315-347).

  gamma       irrational slope in (0,1);  gamma = [0; A_1, A_2, A_3, ...]
  a_k         BHZ digits:  a_1 = A_1 - 1,  a_k = A_k for k >= 2   (BHZ Prop. 2.7)
  A_b         sup_k a_k   (<= sup_k A_k)
  p_k, q_k    convergents of gamma in BHZ's normalisation:
                 p_0 = 0, q_0 = 1,  p_1 = 1, q_1 = a_1 + 1,
                 p_k = a_k p_{k-1} + p_{k-2},  q_k = a_k q_{k-1} + q_{k-2}   (k >= 2)
              (so p_{-1} = 1, q_{-1} = 0)
  c_k         Ostrowski digits of the intercept; admissible iff
                 0 <= c_k <= a_k,  a_k >= 1 for k >= 2,  and c_k = a_k => c_{k-1} = 0
  d_k         := a_k - c_k   in [0, a_k]
  lam_k       := q_{k-1}/q_k          (lam_0 = 0)
  S_k         := sum_{j=1}^k d_j q_{j-1};   t_k := S_k/q_k   (t_0 = 0)
  m_k         := t_{k-1} + d_k        (so t_k = lam_k m_k,  m_{k+1} = lam_k m_k + d_{k+1})
  x'(k)       := S_{k+1}/q_k = m_{k+1}
  x (k)       := 1_{a_{k+2} = c_{k+2}} + x'(k)
  y (k)       := 1 + S_k/(q_k - c_k q_{k-1}) = 1 + m_k/(lam_{k-1} + d_k)
  ice(omega)  := limsup_k max(x'(k), y(k))        (BHZ Cor. 3.5)

THE UNIFIED WITNESS FAMILY.  For k >= 2 and an "effective digit" d in {1,...,a_k} put

      ell(k,d) := d q_{k-1} + q_{k-2}          (an intermediate / semistandard denominator)
      w  (k,d) := d p_{k-1} + p_{k-2}

  d = a_k   ->  ell = q_k,  w = p_k         : the x-witness.  ATTAINED for every k, exponent x(k).
  d = d_k   ->  ell = q_k - c_k q_{k-1},
                w   = p_k - c_k p_{k-1}     : the y-witness.  ATTAINED iff 0 < c_k < a_k,
                                              exponent y(k).
  other d   ->  intermediate root, no BHZ attainment guarantee; its prefix power is measured
                literally here.

  E(k,d) := (prefix power of ell(k,d)) - 2 ;  in particular E_k := y(k) - 2.

THE SURPLUS-DRIVER IDENTITY (Phase 8).   ell_k * E_k = q_{k-2} (m_{k-1} - 1),  ell_k = q_k - c_k q_{k-1}.
This script checks it AND the attainment routing, i.e. that the ell_k appearing in it is the
length of the root of the power actually exhibited:

  routing R1  0 < c_k < a_k        : y(k) attained directly, root length q_k - c_k q_{k-1} = ell_k.
  routing R2  c_k = a_k  (d_k = 0) : y(k) = x(k-2), root length q_{k-2};  and q_k - a_k q_{k-1}
                                     = q_{k-2}, so ell_k IS that length.
  routing R3  c_k = 0, c_{k+1} < a_{k+1} : y(k) <= x(k), root length q_k = ell_k.
  routing R4  c_k = 0, c_{k+1} = a_{k+1} : y(k) < y(k+1) = x(k-1), root length q_{k-1};
                                     and ell_{k+1} = q_{k+1} - a_{k+1} q_k = q_{k-1}.
"""
from fractions import Fraction
import itertools, math, random, sys

LOG23 = math.log2(3)
TAU = ({0: "0", 1: "01"}, {0: "10", 1: "1"})     # BHZ Sec. 2.3

# ------------------------------------------------------------------ arithmetic

def convergents(a):
    """Returns p, q as lists indexed 0..len(a) plus p[-1]=1, q[-1]=0 handled by callers."""
    p = [0, 1]; q = [1, a[0] + 1]
    for k in range(2, len(a) + 1):
        p.append(a[k - 1] * p[k - 1] + p[k - 2])
        q.append(a[k - 1] * q[k - 1] + q[k - 2])
    return p, q

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

def stream(a, c):
    """Exact lam, d, m, t, and the BHZ expressions, as dicts keyed by k."""
    p, q = convergents(a)
    n = len(a)
    lam = {0: Fraction(0)}
    for k in range(1, n + 1):
        lam[k] = Fraction(q[k - 1], q[k])
    d = {k: a[k - 1] - c[k - 1] for k in range(1, n + 1)}
    m = {}; t = {0: Fraction(0)}
    for k in range(1, n + 1):
        m[k] = t[k - 1] + d[k]
        t[k] = lam[k] * m[k]
    xp = {k: m[k + 1] for k in range(1, n)}
    x = {}
    for k in range(1, n):
        ind = 1 if (k + 2 <= n and a[k + 1] == c[k + 1]) else 0
        x[k] = ind + xp[k]
    y = {}
    for k in range(2, n + 1):
        y[k] = 1 + m[k] / (lam[k - 1] + d[k])
    return dict(p=p, q=q, lam=lam, d=d, m=m, t=t, xp=xp, x=x, y=y, n=n)

# ------------------------------------------------------------------ literal word

def apply_tau(i, w):
    tt = TAU[i]
    return "".join(tt[int(ch)] for ch in w)

def build(a, c, seed, K):
    w = seed
    for k in range(K, 0, -1):
        i = (k - 1) % 2
        for _ in range(a[k - 1]):
            w = apply_tau(i, w)
        w = w[c[k - 1]:]
    return w

def certified_prefix(a, c, maxlen=400000, pad=6):
    """Longest common prefix over two continuations starting with different letters ->
    a guaranteed prefix of omega (BHZ Lemma 2.4).  K is truncated to respect maxlen."""
    p, q = convergents(a)
    K = len(a)
    while K > 2 and q[K] * 3 > maxlen:
        K -= 1
    w0 = build(a, c, "01" * pad, K)
    w1 = build(a, c, "10" * pad, K)
    n = 0
    while n < min(len(w0), len(w1)) and w0[n] == w1[n]:
        n += 1
    return w0[:n], K

def lcp_pow(s, ell):
    if ell <= 0 or ell >= len(s):
        return None
    n = ell
    while n < len(s) and s[n] == s[n - ell]:
        n += 1
    return None if n >= len(s) else n

# ------------------------------------------------------------------ checks

def check_identity_and_routing(a, c, verbose=False):
    """Asserts the driver identity and that ell_k is the ACTUAL attained root length."""
    st = stream(a, c)
    q, lam, d, m, x, y = st["q"], st["lam"], st["d"], st["m"], st["x"], st["y"]
    rows = []
    for k in range(3, st["n"] - 1):
        if k not in y:
            continue
        ell_k = q[k] - c[k - 1] * q[k - 1]
        Ek = y[k] - 2
        # the identity
        assert ell_k * Ek == q[k - 2] * (m[k - 1] - 1), ("identity", a, c, k)
        # the routing
        ck = c[k - 1]
        if 0 < ck < a[k - 1]:
            route, val, rootlen = "R1 y(k)", y[k], q[k] - ck * q[k - 1]
        elif ck == a[k - 1]:
            route, val, rootlen = "R2 x(k-2)", x[k - 2], q[k - 2]
            assert val == y[k], ("R2 value", a, c, k)
            assert ell_k == q[k - 2], ("R2 length", a, c, k)
        elif k < st["n"] and c[k] < a[k]:
            route, val, rootlen = "R3 x(k)", x[k], q[k]
            assert val >= y[k], ("R3 dominance", a, c, k)
            assert ell_k == q[k], ("R3 length", a, c, k)
        else:
            route, val, rootlen = "R4 x(k-1)", x[k - 1], q[k - 1]
            assert val > y[k], ("R4 dominance", a, c, k)
            ell_kp1 = q[k + 1] - c[k] * q[k]
            assert ell_kp1 == q[k - 1], ("R4 length at k+1", a, c, k)
        rows.append((k, route, ell_k, rootlen, val, Fraction(ell_k) * Ek))
    return rows

def check_weights(a, c, maxlen=400000):
    """Literal verification that the root of length ell(k,d) has weight w(k,d)."""
    om, K = certified_prefix(a, c, maxlen)
    u = [int(ch) for ch in om]
    p, q = convergents(a)
    out = []
    for k in range(2, K + 1):
        for dd in range(1, a[k - 1] + 1):
            ell = dd * q[k - 1] + q[k - 2]
            if ell >= len(u):
                continue
            w_pred = dd * p[k - 1] + p[k - 2]
            w_act = sum(u[:ell])
            out.append((k, dd, ell, w_pred, w_act, w_pred == w_act))
    return out, u, K

def parity_char(a, K=None):
    """p_k parity sequence."""
    p, q = convergents(a)
    K = K or len(a)
    return [p[k] % 2 for k in range(1, K + 1)]

def main():
    rng = random.Random(909)
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / A.  Unified witness family: lengths, weights, identity, routing, parity")
    P("=" * 78)

    # ---------------- A1: the identity and the attainment routing
    P("\nA1  Driver identity  ell_k * E_k = q_(k-2) (m_(k-1) - 1)  AND the attainment routing.")
    P("    ell_k := q_k - c_k q_(k-1).  Checked: the identity, and that ell_k equals the root")
    P("    length of the power actually exhibited by BHZ Prop. 3.3 + Cor. 3.5's observations.")
    tot = 0; routes = {}
    slopes = [[2]*12, [3]*10, [1,2]*6, [2,4,2,6,2,8,2,10,2,4], [4]*9, [1,1,2]*4,
              [2,2,4,4,8,8,16,16,2,2]]
    for a in slopes:
        cnt = 0
        for cc in itertools.product(*[range(x + 1) for x in a]):
            cc = list(cc)
            if not admissible(a, cc):
                continue
            cnt += 1
            if cnt > 3000:
                break
            for (k, route, ell_k, rootlen, val, prod) in check_identity_and_routing(a, cc):
                routes[route] = routes.get(route, 0) + 1
                tot += 1
    P(f"    {tot} (slope, admissible digit string, k) instances; routing usage:")
    for r_, v in sorted(routes.items()):
        P(f"      {r_:<12} {v}")
    P("    ALL identity assertions and ALL routing length/dominance assertions pass.")
    P("    => in routings R1, R2, R3 the identity's ell_k IS the attained root length;")
    P("       in R4 the attained length q_(k-1) is the identity's ell_(k+1).  No case is left")
    P("       where the identity is applied to a length that is not actually realised.")

    # ---------------- A2: weights, verified literally
    P("\nA2  Literal weight verification:  w(k,d) = d p_(k-1) + p_(k-2)  for the prefix of")
    P("    length ell(k,d) = d q_(k-1) + q_(k-2), all d in 1..a_k (x-, y- and intermediate roots).")
    nok = nbad = 0
    for a in ([2]*11, [3]*9, [1,2]*6, [4,2,4,2,4,2,4], [2,4,6,8,2,4]):
        for cname, cc in (("c=0", [0]*len(a)),
                          ("keep-one", [max(0, x - 1) for x in a]),
                          ("c=a_k-2", [max(0, x - 2) for x in a])):
            if not admissible(a, cc):
                continue
            rows, u, K = check_weights(a, cc)
            for (k, dd, ell, wp, wa, ok) in rows:
                nok += ok; nbad += (not ok)
    P(f"    {nok} weight checks pass, {nbad} FAIL.")
    assert nbad == 0

    # ---------------- A3: parity characterisation
    P("\nA3  Parity of the convergent numerators, in BHZ's normalisation (p_1 = 1, p_2 = a_2).")
    P("    Claim (finite form):  p_k odd for EVERY k >= 1  <=>  a_2 odd and a_k even for all k >= 3.")
    cases = [("a_2 odd, then all even ", [5, 3] + [2] * 20, True),
             ("a_2 odd, then all even ", [2, 1] + [4, 6, 8, 10] * 5, True),
             ("all digits even        ", [2] * 22, False),
             ("a_2 even               ", [3, 2] + [2] * 20, False),
             ("one odd digit at k=7   ", [5, 3, 2, 2, 2, 2, 3] + [2] * 15, False),
             ("a_k = k                ", list(range(1, 23)), False)]
    P(f"    {'digit string':<26}{'p_k odd for all k<=20':<24}{'predicted':<11}{'first even p_k'}")
    for nm, a, pred in cases:
        par = parity_char(a, 20)
        allodd = all(v == 1 for v in par)
        first = next((i + 1 for i, v in enumerate(par) if v == 0), None)
        P(f"    {nm:<26}{str(allodd):<24}{str(pred):<11}{first}")
        assert allodd == pred, (nm,)
    P("\n    Asymptotic form, which is what the bridge needs.  With a_k even for all k > K the")
    P("    recursion gives p_{k+1} = p_{k-1} mod 2, so the parity pair is 2-periodic from K on:")
    P("    p_k is odd for all k >= K-1 iff BOTH p_{K-1}, p_K are odd, and otherwise p_k is EVEN")
    P("    for infinitely many k.  Conversely an odd a_k met at a state (1,1) forces p_k even.")
    P("    Hence:  p_k odd for all large k  =>  a_k even for all large k.")
    P(f"    {'digit string':<34}{'a_k even eventually':<21}{'p_k odd eventually':<20}{'p even i.o.'}")
    for nm, a in (("even tail, both seeds odd (5,3,2,2,...)", [5, 3] + [2] * 22),
                  ("even tail, one seed even (4,2,2,2,...) ", [4, 2] + [2] * 22),
                  ("even tail after odd at k=5            ", [5, 3, 2, 2, 3] + [2] * 20),
                  ("odd digit infinitely often            ", [5, 3] + [2, 2, 3] * 8)):
        par = parity_char(a, 24)
        tail = par[6:]
        P(f"    {nm:<34}{str(all(x % 2 == 0 for x in a[2:])):<21}"
          f"{str(all(v == 1 for v in tail)):<20}{str(any(v == 0 for v in tail))}")

    # ---------------- A4: the even-weight criterion on the all-odd-p family
    P("\nA4  On an all-odd-numerator slope, w(k,d) = d p_(k-1) + p_(k-2) == d + 1 (mod 2),")
    P("    so the EVEN-weight roots at scale k are exactly the ODD-d ones.  In particular:")
    P("      d = a_k (x-witness):  a_k even  =>  w = p_k ODD   -> odd branch")
    P("      d = d_k (y-witness):  w EVEN   <=>  d_k ODD")
    P("      d = 1   (intermediate): w = p_(k-1) + p_(k-2) == 0 (mod 2)  -> ALWAYS EVEN")
    P(f"    {'slope':<26}{'intercept':<14}{'k':<4}{'a_k':<6}{'d_k':<5}"
      f"{'w(k,a_k)%2':<12}{'w(k,d_k)%2':<12}{'w(k,1)%2'}")
    a = [5, 3] + [2, 4, 6, 8] * 4
    p, q = convergents(a)
    for cname, cc in (("keep-one", [max(0, x - 1) for x in a]),
                      ("c=a_k-2", [max(0, x - 2) for x in a]),
                      ("c=0", [0] * len(a))):
        if not admissible(a, cc):
            P(f"    {'[5,3,2,4,6,8,...]':<26}{cname:<14}not admissible")
            continue
        for k in (9, 12):
            dk = a[k - 1] - cc[k - 1]
            P(f"    {'[5,3,2,4,6,8,...]':<26}{cname:<14}{k:<4}{a[k-1]:<6}{dk:<5}"
              f"{(a[k-1]*p[k-1]+p[k-2])%2:<12}{(dk*p[k-1]+p[k-2])%2:<12}"
              f"{(p[k-1]+p[k-2])%2}")
    P("\n    So the d=1 intermediate root ALWAYS has even weight on this family.  Whether it is")
    P("    usable depends on its prefix power, which Phase 9 step B measures literally.")
    P("\nALL STEP-A CHECKS PASS.")

if __name__ == "__main__":
    main()
