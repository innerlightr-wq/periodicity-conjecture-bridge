"""
Phase 8, step C/D: adversarial search for the true general-intercept margin, and
verification of the Phase-8 case tree that proves

    limsup_k max(x'(k), y(k)) >= 2 + delta(A),      delta(A) = 1/(2(A+1)^2)

for EVERY admissible Ostrowski digit sequence (c_k) of every irrational slope
whose partial quotients are bounded by A.

O(1)-per-step exact recurrences (each verified against BHZ Cor. 3.5 in
phase8_identities.py):
    lam_k = 1/(PQ_k + lam_{k-1}),  lam_0 = 0,  PQ = (a_1+1, a_2, a_3, ...)
    d_k = a_k - c_k ;  m_k = t_{k-1} + d_k ;  t_k = lam_k m_k
    x'(k) = m_{k+1} ;  y(k) = 1 + m_k/(lam_{k-1} + d_k)
"""
from fractions import Fraction
import itertools, math, random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase8_identities import q_bhz, bhz_terms, reform_terms, admissible, rand_admissible

def delta(A):
    return Fraction(1, 2 * (A + 1) ** 2)

def evaluate(a, c, tail_from, exact=True):
    """max over k >= tail_from of max(x'(k), y(k))."""
    one = Fraction(1) if exact else 1.0
    zero = Fraction(0) if exact else 0.0
    pq = [a[0] + 1] + list(a[1:])
    lam_prev = zero; t_prev = zero; best = zero
    for k in range(1, len(a) + 1):
        lam = one / (pq[k - 1] + lam_prev)
        d = a[k - 1] - c[k - 1]
        m = t_prev + d
        if k - 1 >= tail_from and m > best:      # x'(k-1) = m_k
            best = m
        if k >= 2:
            y = 1 + m / (lam_prev + d)
            if k >= tail_from and y > best:
                best = y
        lam_prev, t_prev = lam, lam * m
    return best

# ---------------------------------------------------------------- case tree

def case_tree_witness(a, c, k, terms, q, d):
    for j in (k, k - 1, k - 2):
        if d[j] == 0:
            return ("Z", terms[j - 2][0], int(q[j - 2]), f"x({j-2})=y({j})=1+m_{{{j-1}}}")
    if d[k] >= 2:
        return ("B", terms[k - 1][0], int(q[k - 1]), f"x({k-1})>=x'({k-1})=m_{{{k}}}")
    assert d[k] == 1 and d[k - 1] >= 1 and d[k - 2] >= 1
    ck = c[k - 1]
    if 0 < ck < a[k - 1]:
        return ("C-y", terms[k][2], int(q[k] - ck * q[k - 1]), f"y({k}) attained, 0<c_k<a_k")
    if c[k] == a[k]:
        return ("C-x(k-1)", terms[k - 1][0], int(q[k - 1]), f"x({k-1})=y({k+1})>y({k})")
    return ("C-x(k)", terms[k][0], int(q[k]), f"x({k})>=y({k})")

def check_case_tree(a, c, A):
    q = q_bhz(a)
    terms, _, _ = bhz_terms(a, c)
    lam, d, m, t, _ = reform_terms(a, c)
    worst = None; counts = {}
    for k in range(7, len(a) - 1):
        if (k - 2) not in terms or (k + 1) > len(a):
            continue
        br, r, ell, how = case_tree_witness(a, c, k, terms, q, d)
        counts[br] = counts.get(br, 0) + 1
        assert r >= 2 + delta(A), ("exponent floor", a, c, k, br, float(r))
        assert ell >= q[k - 4], ("root growth", a, c, k, br, ell, int(q[k - 4]))
        if worst is None or r < worst[0]:
            worst = (r, k, br, ell, how)
    return worst, counts

# ------------------------------------------------------------ C1 periodic

def admissible_cycle(A_terms, c):
    p = len(c)
    for i in range(p):
        if c[i] == A_terms[i % len(A_terms)] and c[(i - 1) % p] != 0:
            return False
    return True

def scan_periodic(A_terms, max_period_mult=6, reps=12, budget=300000):
    A = max(A_terms); base = len(A_terms)
    worst = None; n = 0
    for mult in range(1, max_period_mult + 1):
        p = base * mult
        if math.prod(A_terms[i % base] + 1 for i in range(p)) > budget:
            continue
        for c0 in itertools.product(*[range(A_terms[i % base] + 1) for i in range(p)]):
            if not admissible_cycle(A_terms, c0):
                continue
            a = (list(A_terms) * ((p * reps) // base + base))[:p * reps]
            c = (list(c0) * reps)[:len(a)]
            if len(a) != len(c) or not admissible(a, c):
                continue
            n += 1
            v = evaluate(a, c, len(a) - 3 * p, exact=False)
            if worst is None or v < worst[0]:
                worst = (v, list(c0), p, a, c)
    _, c0, p, a, c = worst
    return evaluate(a, c, len(a) - 3 * p, exact=True), c0, n, A

# ------------------------------------------------------------ C3 exhaustive

def exhaustive_min(A, n=20, window=4):
    """Exhaustive branch-and-bound over ALL admissible (c_k), constant a_k=A."""
    pq = [A + 1] + [A] * (n - 1)
    best = [float("inf"), None]
    tail_from = n - window
    nodes = [0]
    def rec(k, lam_prev, t_prev, running, c, prev):
        nodes[0] += 1
        if running >= best[0]:
            return
        if k > n:
            best[0] = running; best[1] = list(c); return
        lam = 1.0 / (pq[k - 1] + lam_prev)
        hi = A if (k == 1 or prev == 0) else A - 1
        for ck in range(0, max(0, hi) + 1):
            d = A - ck
            m = t_prev + d
            r = running
            if k - 1 >= tail_from and m > r: r = m
            if k >= 2:
                y = 1 + m / (lam_prev + d)
                if k >= tail_from and y > r: r = y
            if r < best[0]:
                rec(k + 1, lam, lam * m, r, c + [ck], ck)
    rec(1, 0.0, 0.0, 0.0, [], 0)
    return evaluate([A] * n, best[1], tail_from, exact=True), best[1], nodes[0]

def main():
    rng = random.Random(4242)
    P = lambda *a_: (print(*a_), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 8 / C.  Adversarial search for the general-intercept margin")
    P("=" * 78)
    P("Reference: for constant a_k=A and d_k==1 (c_k=a_k-1) the closed form is")
    P("    y(k) = 2 + 1/(A*beta_A),   beta_A = (A+sqrt(A^2+4))/2   -- the empirical infimum.")
    P("")
    P(f"{'A':>3} {'proved delta(A)':>16} {'observed inf margin':>20} {'1/(A beta_A)':>14}"
      f" {'obs/proved':>11}  worst cycle")
    for A in range(1, 11):
        beta = (A + math.sqrt(A * A + 4)) / 2
        vex, c0, n, _ = scan_periodic([A], max_period_mult=7 if A <= 3 else 4)
        P(f"{A:>3} {float(delta(A)):>16.8f} {float(vex-2):>20.8f} {1.0/(A*beta):>14.8f}"
          f" {float((vex-2)/delta(A)):>11.3f}  c={c0}")
        assert vex >= 2 + delta(A), (A, c0, float(vex))

    P("\nC1  exhaustive admissible periodic patterns, several multi-term slopes")
    for A_terms in ([1], [2], [3], [1, 2], [2, 1], [2, 1, 3], [4, 1], [1, 1, 3], [3, 2]):
        vex, c0, n, A = scan_periodic(A_terms)
        P(f"    a={str(A_terms):<12} A={A}  {n:7d} cycles tested  min margin={float(vex-2):.8f}"
          f"  floor={float(delta(A)):.8f}  worst c={c0}  CLEARS={vex >= 2+delta(A)}")
        assert vex >= 2 + delta(A)

    P("\nC2  greedy-minimising adversary, genuinely non-eventually-periodic slopes")
    P("    (a_k read off an irrational rotation, so (a_k) is not eventually periodic)")
    for A in (1, 2, 3, 4, 5, 6):
        phi = (1 + 5 ** 0.5) / 2
        a = [min(max(1 + int(((i * phi) % 1) * A), 1), A) for i in range(1, 81)]
        c = []; lam_prev = Fraction(0); t_prev = Fraction(0)
        pq = [a[0] + 1] + a[1:]
        for k in range(1, len(a) + 1):
            lam = Fraction(1) / (pq[k - 1] + lam_prev)
            hi = a[k - 1] if (k == 1 or c[-1] == 0) else a[k - 1] - 1
            bb = None
            for ck in range(0, max(0, hi) + 1):
                d = a[k - 1] - ck; m = t_prev + d
                sc = m if k < 2 else max(m, 1 + m / (lam_prev + d))
                if bb is None or sc < bb[0]:
                    bb = (sc, ck, m)
            c.append(bb[1]); lam_prev, t_prev = lam, lam * bb[2]
        v = evaluate(a, c, len(a) - 25)
        P(f"    A={A}  greedy limsup={float(v):.8f}  margin={float(v-2):.8f}"
          f"  d_k tail={[a[i]-c[i] for i in range(len(a)-10, len(a))]}"
          f"  CLEARS={v >= 2+delta(A)}")
        assert v >= 2 + delta(A)

    P("\nC3  exhaustive branch-and-bound minimax over ALL admissible (c_k), a_k=A constant")
    # A<=3 only: the admissible tree grows like (A+1)^n, so A=4 is ~10^10 nodes and
    # buys no new information -- the minimiser is already the d_k==1 tail at every A,
    # matching the closed form 2 + 1/(A beta_A) (see the table above).
    for A in (1, 2, 3):
        v, c, nodes = exhaustive_min(A, n=18, window=4)
        P(f"    A={A}: global min={float(v):.8f}  margin={float(v-2):.8f}  ({nodes} nodes)"
          f"  minimiser d_k tail={[A-x for x in c[-8:]]}  CLEARS={v >= 2+delta(A)}")
        assert v >= 2 + delta(A)

    P("\nD   Phase-8 case tree: exponent >= 2+delta(A) AND ATTAINED root >= q_(k-4)")
    agg = {}; worst = None; nseq = 0
    for A in range(1, 11):
        for _ in range(40):
            a = [rng.randint(1, A) for _ in range(30)]
            c = rand_admissible(a, rng)
            w, counts = check_case_tree(a, c, A); nseq += 1
            for b, v in counts.items(): agg[b] = agg.get(b, 0) + v
            if w and (worst is None or w[0] < worst[0]): worst = (w[0], A, w[2], w[4])
    for A_terms in ([1]*30, [2]*30, [3]*30, [1,2]*15, [2,1,3]*10, [4,1]*15, [5]*30, [6,1,2]*10):
        A = max(A_terms)
        fams = {"c=0": [0]*len(A_terms),
                "omega(-alpha)": [0 if k % 2 else A_terms[k-1] for k in range(1, len(A_terms)+1)],
                "d=1": [max(0, x-1) for x in A_terms]}
        prev = 0; cm = []
        for k, ak in enumerate(A_terms, 1):
            cm.append(ak if (k == 1 or prev == 0) else max(0, ak-1)); prev = cm[-1]
        fams["ev-maximal"] = cm
        for nm, c in fams.items():
            if not admissible(A_terms, c): continue
            w, counts = check_case_tree(A_terms, c, A); nseq += 1
            for b, v in counts.items(): agg[b] = agg.get(b, 0) + v
            if w and (worst is None or w[0] < worst[0]): worst = (w[0], A, w[2], w[4])
    P(f"    {nseq} digit sequences; branch usage: "
      + ", ".join(f"{b}={v}" for b, v in sorted(agg.items())))
    P(f"    ALL assertions pass.  Tightest observed branch exponent {float(worst[0]):.6f}"
      f" at A={worst[1]} via {worst[3]}")
    P("\nALL MARGIN CHECKS PASS.")

if __name__ == "__main__":
    main()
