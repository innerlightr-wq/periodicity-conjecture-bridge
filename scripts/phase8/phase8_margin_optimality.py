"""
Phase 8, step H: what exactly is proved about the sharp general-intercept margin.

Four tiers, kept strictly apart (see theorems/phase8/PHASE8_MARGIN_STATUS.md):

  T1  PUBLISHED SUFFICIENT   BHZ 2006 Prop. 5.1/5.2:  ice >= 2 + 1/(2(A_b+1)^2 + 1)
  T2  PROVED, STRONGER       Phase 8 Thm 1:           ice >= 2 + 1/(2(A_b+1)^2),
                             with ATTAINED witnesses at every scale, root >= q_{k-4}
  T3  PROVED UPPER BOUND     keep-one closed form:    ice = 2 + 1/(A beta_A) exactly,
                             for any slope whose BHZ digits are eventually == A
  T3b PROVED OPTIMALITY      for those same slopes with A >= 2: no admissible (c_k) beats
                             the keep-one tail.  (A = 1 Fibonacci: BHZ Prop. 4.3.)
  T4  NUMERICAL ONLY         that keep-one is optimal on slopes whose digit tail is NOT
                             eventually constant.  NOT promoted to a theorem.

beta_A := the unique root > 1 of  beta^2 = A beta + 1,  i.e. (A + sqrt(A^2+4))/2.
Equivalently beta_A = lim_k q_k/q_{k-1} for any slope whose partial quotients are
eventually == A, and 1/beta_A = lim_k lam_k with lam_k = q_{k-1}/q_k.

Theorem 2 uses T1/T2 ONLY.  T3/T3b/T4 are not load-bearing anywhere.
"""
from fractions import Fraction
import itertools, math, random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase8_identities import q_bhz, bhz_terms, admissible, rand_admissible

def beta_exact_sq(A):
    """beta_A is quadratic; return it as a high-precision Fraction bracket via the
    convergents of [A; A, A, ...] = beta_A."""
    p0, p1 = Fraction(1), Fraction(A)
    for _ in range(80):
        p0, p1 = p1, A + 1 / p1
    return p1

def ice_tail(a, c, window=10):
    terms, _, _ = bhz_terms(a, c)
    ks = [k for k in terms if k > len(a) - 1 - window]
    return max(max(terms[k][0], terms[k][2] or 0) for k in ks)

def stream_vals(a, c):
    """Exact (k, x'(k), y(k), d_k, lam_k, m_k) stream, O(1) per step."""
    pq = [a[0] + 1] + list(a[1:])
    lam_prev = Fraction(0); t_prev = Fraction(0)
    out = []
    for k in range(1, len(a) + 1):
        lam = Fraction(1) / (pq[k - 1] + lam_prev)
        d = a[k - 1] - c[k - 1]
        m = t_prev + d
        y = (1 + m / (lam_prev + d)) if k >= 2 else None
        out.append((k, m, y, d, lam, m))       # x'(k-1) = m
        lam_prev, t_prev = lam, lam * m
    return out

def main():
    rng = random.Random(97)
    P = lambda *a_: (print(*a_), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 8 / H.  Margin status: what is proved, and at what scope")
    P("=" * 78)

    # ---------------- T1 vs T2 vs T3, numerically laid out
    P("\nT1/T2/T3 side by side.  A_b = sup of the BHZ digits a_k.")
    P(f"{'A_b':>4} {'T1 published 1/(2(A+1)^2+1)':>28} {'T2 Phase 8 1/(2(A+1)^2)':>25}"
      f" {'T3 sharp 1/(A beta_A)':>22} {'T3/T2':>7}")
    for A in range(1, 11):
        t1 = Fraction(1, 2 * (A + 1) ** 2 + 1)
        t2 = Fraction(1, 2 * (A + 1) ** 2)
        b = beta_exact_sq(A)
        t3 = 1 / (A * b)
        P(f"{A:>4} {float(t1):>28.8f} {float(t2):>25.8f} {float(t3):>22.8f}"
          f" {float(t3/t2):>7.3f}")
        assert t1 < t2 <= t3, (A, float(t1), float(t2), float(t3))
    P("  T1 < T2 <= T3 at every A: the two lower bounds are consistent with the sharp value.")

    # ---------------- T3: the keep-one closed form, verified exactly
    P("\nT3  keep-one closed form.  Slope with BHZ digits a_k == A; c_k = a_k - 1, so d_k == 1.")
    P("    Fixed point of m -> lam m + 1 is m* = beta/(beta-1); with lam = 1/beta and")
    P("    beta^2 - 1 = A beta,  y = 1 + m*/(lam+1) = 1 + beta^2/(beta^2-1) = 2 + 1/(A beta).")
    P(f"{'A':>3} {'y(k) at k=60 (exact)':>24} {'2 + 1/(A beta_A)':>18} {'x prime(k) at k=60':>20}"
      f" {'x <= y?':>8}")
    for A in range(1, 9):
        a = [A] * 62; c = [A - 1] * 62
        assert admissible(a, c)
        vals = stream_vals(a, c)
        k, m, y, d, lam, _ = vals[59]
        b = beta_exact_sq(A)
        pred = 2 + 1 / (A * b)
        P(f"{A:>3} {float(y):>24.12f} {float(pred):>18.12f} {float(m):>20.12f}"
          f" {str(m <= y):>8}")
        assert abs(float(y) - float(pred)) < 1e-10, (A, float(y), float(pred))

    # ---------------- T3b: optimality for eventually-constant digit tails, A >= 2
    P("\nT3b optimality for eventually-constant BHZ digit tails, A >= 2.  Three cases:")
    P("    (1) d_k == 1 eventually            -> limsup = 2 + 1/(A beta_A)      [T3]")
    P("    (2) d_k == 0 infinitely often      -> y(k) = 1 + a_{k-1} + t_{k-2} >= 1 + A")
    P("    (3) d_k >= 2 i.o., d_j >= 1 large  -> x'(k-1) = m_k >= 2 + lam_{k-1} -> 2 + 1/beta_A")
    P("    For A >= 2 both (2) and (3) STRICTLY exceed 2 + 1/(A beta_A):")
    P(f"{'A':>3} {'2+1/(A beta) [case 1]':>22} {'1+A [case 2]':>14} {'2+1/beta [case 3]':>19}"
      f" {'min(2,3) > case 1?':>19}")
    for A in range(2, 11):
        b = beta_exact_sq(A)
        c1 = 2 + 1 / (A * b); c2 = Fraction(1 + A); c3 = 2 + 1 / b
        P(f"{A:>3} {float(c1):>22.8f} {float(c2):>14.8f} {float(c3):>19.8f}"
          f" {str(min(c2, c3) > c1):>19}")
        assert min(c2, c3) > c1, (A,)
    P("    So the infimum is attained exactly on the keep-one tails.  PROVED at this scope.")
    P("    A = 1 is NOT covered by this argument (case 2 gives only 2 + t_{k-2}).  For the")
    P("    genuine Fibonacci slope [0;1,1,1,...] BHZ Prop. 4.3 settles it: every omega outside")
    P("    the shift orbit of the characteristic sequence begins in arbitrarily large cubes")
    P("    (ice >= 3), and the orbit members have ice = 1 + theta = 2.618034.")

    # Pointwise confirmation of the case bounds.  The case analysis is POINTWISE --
    # case (2) bounds y(k) at each k with d_k = 0, case (3) bounds x'(k-1) at each k with
    # d_k >= 2 and d_{k-1} >= 1 -- so that is what we check.  (Checking a finite-window
    # limsup instead would be wrong: an index satisfying a case can fall outside the window.)
    P("\n    Pointwise confirmation of the case inequalities (exact arithmetic, 4000 random")
    P("    admissible sequences per A, length 40, constant BHZ digits a_k == A):")
    P(f"{'A':>3} {'case-2 indices':>15} {'min y(k) there':>15} {'1+A':>8}"
      f" {'case-3 indices':>15} {'min m_k there':>14} {'2+1/beta':>10}")
    for A in range(2, 8):
        a = [A] * 40
        y0 = []; m2 = []
        for _ in range(4000):
            c = rand_admissible(a, rng)
            vals = stream_vals(a, c)
            d = [v[3] for v in vals]
            for i, (k, m, y, dk, lam, _) in enumerate(vals):
                if k < 5 or k > len(a) - 2:
                    continue
                if dk == 0:
                    y0.append(y)                          # case (2): y(k) >= 1 + A
                elif dk >= 2 and d[k - 2] >= 1:
                    m2.append(m)                          # case (3): x'(k-1) = m_k
        b = beta_exact_sq(A)
        P(f"{A:>3} {len(y0):>15} {float(min(y0)):>15.8f} {1+A:>8}"
          f" {len(m2):>15} {float(min(m2)):>14.8f} {float(2+1/b):>10.6f}")
        assert min(y0) >= 1 + A, (A, "case 2", float(min(y0)))
        assert min(m2) >= 2 + 1 / b, (A, "case 3", float(min(m2)), float(2 + 1/b))
    P("    Both pointwise inequalities hold with no exception, at every A tested.")

    # ---------------- T4: non-constant digit tails -- NUMERICAL ONLY
    P("\nT4  slopes whose BHZ digit tail is NOT eventually constant: keep-one is observed")
    P("    to be optimal, but the T3b case analysis does not apply (lam_k does not converge,")
    P("    and cases (2)/(3) are compared against a limsup that is no longer a single value).")
    P("    This is recorded as NUMERICAL EVIDENCE ONLY and is not used by Theorem 2.")
    P(f"{'slope digits (a_k)':<22} {'A_b':>4} {'T2 floor':>11} {'min ice - 2 over':>17}"
      f" {'keep-one ice - 2':>17} {'keep-one optimal?':>18}")
    for A_terms in ([1, 2], [2, 1], [2, 3], [1, 3], [2, 1, 3], [1, 1, 2], [3, 2], [1, 2, 2]):
        A_b = max(A_terms); base = len(A_terms)
        t2 = Fraction(1, 2 * (A_b + 1) ** 2)
        best = None
        for mult in (1, 2, 3):
            p = base * mult
            if math.prod(A_terms[i % base] + 1 for i in range(p)) > 200000:
                continue
            for c0 in itertools.product(*[range(A_terms[i % base] + 1) for i in range(p)]):
                ok = all(not (c0[i] == A_terms[i % base] and c0[(i - 1) % p] != 0)
                         for i in range(p))
                if not ok:
                    continue
                reps = 40 // p + 2
                a = (A_terms * (p * reps // base + base))[:p * reps]
                c = (list(c0) * reps)[:len(a)]
                if len(a) != len(c) or not admissible(a, c):
                    continue
                v = ice_tail(a, c, window=3 * p)
                if best is None or v < best[0]:
                    best = (v, list(c0))
        reps = 40 // base + 2
        a = (A_terms * reps)
        ck = [max(0, x - 1) for x in a]
        ko = ice_tail(a, ck, window=3 * base) if admissible(a, ck) else None
        P(f"{str(A_terms):<22} {A_b:>4} {float(t2):>11.6f} {float(best[0]-2):>17.8f}"
          f" {float(ko-2) if ko else float('nan'):>17.8f}"
          f" {str(ko is not None and abs(float(ko-best[0])) < 1e-6):>18}")
        assert best[0] >= 2 + t2, (A_terms, float(best[0]))

    P("\nSTATUS SUMMARY")
    P("  Theorem 2 needs only:  ice >= 2 + delta,  delta = delta(A_b) > 0 fixed.  T1 suffices;")
    P("  T2 is what Phase 8 proves and is what supplies the attained witnesses.")
    P("  The sharp value 1/(A beta_A) is PROVED to be the infimum only for eventually-constant")
    P("  BHZ digit tails with A >= 2 (T3b), plus the Fibonacci slope via BHZ Prop. 4.3.")
    P("  For every other bounded-type slope the sharp value is NUMERICAL EVIDENCE, not a theorem.")
    P("\nALL MARGIN-STATUS CHECKS PASS.")

if __name__ == "__main__":
    main()
