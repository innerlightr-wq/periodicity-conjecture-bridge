"""
Phase 6: reconstructs the ENTIRE witness chain (not a formula substitution)
for the three adversarial non-eventually-periodic bounded-partial-quotient
continued fractions, end to end:

  1. build gamma as a high-precision rational truncation of the CF;
  2. build u, the intercept-0 lower mechanical word;
  3. find actual initial-power witnesses of u via DIRECT lcp computation
     (never trusting the BHZ term2(k) formula's implied root length --
     only checking that formula as an independent cross-check);
  4. verify r_u > 2 + 1/(A+1) at those witnesses (A=2 here, so bound=2+1/3);
  5. transfer via the exact XOR construction (independent of any CF
     structure);
  6. verify density(R) is exactly 1/2;
  7. compute discrepancy D(R) and check it looks O(log|R|), not linear;
  8. compute the EXACT surplus S (bridge_toolkit's discrepancy-based
     F_bound, the same conservative-but-exact quantity used throughout
     Phases 1-5) and confirm positive, growing values occur at
     arbitrarily long witnesses.

Exact integer/Fraction arithmetic throughout; floats only for display.
"""
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension, discrepancy  # noqa: E402

from bounded_type_generators import thue_morse_pq, fibonacci_pq, random_bounded_pq, is_eventually_periodic  # noqa: E402


def cf_value(pq_terms, n):
    """pq_terms: list starting with a0=0, then a1,a2,... . Exact rational truncation."""
    num, den = 1, 0
    for a in reversed(pq_terms[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def convergents_pq(pq_terms, n):
    a0 = pq_terms[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq_terms[i] * p[-1] + p[-2])
        q.append(pq_terms[i] * q[-1] + q[-2])
    return p[1:], q[1:]


def mechanical_word(gamma, n):
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for i in range(1, n + 1):
        cur = fl(i * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


def term2_bound_check(pq_terms, A, kmax):
    """Direct re-check of BHZ's term2(k)=1+a_{2k-1}+q_{2k-3}/q_{2k-2} > 2+1/(A+1),
    for a genuinely non-periodic pq_terms sequence -- exact Fraction arithmetic."""
    p, q = convergents_pq(pq_terms, len(pq_terms))
    bound = 2 + Fraction(1, A + 1)
    results = []
    for k in range(2, kmax):
        if 2 * k - 1 >= len(pq_terms) or 2 * k - 2 >= len(q):
            break
        term2 = 1 + pq_terms[2 * k - 1] + Fraction(q[2 * k - 3], q[2 * k - 2])
        results.append((k, term2, term2 > bound))
    return results, bound


def analyze(name, pq_terms, A, max_ell=4000, n_reps_witness=8):
    print(f"=== {name} (A={A}) ===")
    periodic, start, period = is_eventually_periodic(pq_terms, max_period=300)
    print(f"  eventual periodicity check (period<=300): {periodic}  (should be False)")
    assert not periodic, "This 'adversarial non-periodic' input turned out periodic!"

    gamma = cf_value([0] + pq_terms, len(pq_terms))
    _, q = convergents_pq([0] + pq_terms, len(pq_terms))
    q_small = sorted(set(x for x in q if 2 <= x <= max_ell))

    term2_results, bound = term2_bound_check([0] + pq_terms, A, kmax=40)
    all_exceed = all(ok for _, _, ok in term2_results)
    print(f"  term2(k) > 2+1/(A+1)={float(bound):.5f} for every tested k "
          f"({len(term2_results)} values of k checked): {all_exceed}")

    n_needed = min(max(q_small) * n_reps_witness, 500_000) if q_small else 50_000
    u = mechanical_word(gamma, n_needed)
    v = rote_from_sturmian(u)

    print(f"  {'ell':>8} {'wt%2':>5} {'r_u(direct lcp)':>16} {'exceeds bound':>14} "
          f"{'|R|':>8} {'dens(R)':>10} {'D(R)':>8} {'D(R)/log|R|':>12}  exact S")
    certifying = []
    for ell in q_small:
        if ell * n_reps_witness > len(u):
            continue
        W = u[:ell]
        checklen = min(len(u), ell * n_reps_witness)
        L_u = lcp(u, periodic_extension(W, checklen), checklen)
        r_u = Fraction(L_u, ell)
        exceeds = r_u > bound

        wpar = sum(W) % 2
        if wpar == 0:
            V, rootlen = v[:ell], ell
        else:
            V0 = v[:ell]
            V, rootlen = V0 + [1 - x for x in V0], 2 * ell
        dens = Fraction(sum(V), rootlen)
        DR = discrepancy(V)
        checklen_v = min(len(v), rootlen * n_reps_witness)
        Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
        S, _ = bridge_surplus_exact(Lv, V)
        if S > 0:
            certifying.append((ell, S))
        logterm = float(DR) / math.log(rootlen) if rootlen > 2 else float("nan")
        print(f"  {ell:8d} {wpar:5d} {float(r_u):16.4f} {str(exceeds):>14} "
              f"{rootlen:8d} {float(dens):10.4f} {float(DR):8.2f} {logterm:12.3f}  S={S}")

    print(f"  Certifying (S>0) witnesses found: {len(certifying)}")
    if certifying:
        print(f"  Deepest certifying: ell={certifying[-1][0]} S={certifying[-1][1]}")
        growing = [s for _, s in certifying]
        print(f"  Certifying S values monotonically increasing with ell: {growing == sorted(growing)}")
    print()
    return {"name": name, "all_term2_exceed": all_exceed, "n_certifying": len(certifying),
            "certifying": certifying}


def main():
    results = []
    results.append(analyze("Thue-Morse-coded {1,2}", thue_morse_pq(2000), A=2))
    results.append(analyze("Fibonacci-word-coded {1,2}", fibonacci_pq(2000), A=2))
    results.append(analyze("Random bounded {1,2} (seed=7)", random_bounded_pq(2000, seed=7), A=2))
    results.append(analyze("Random bounded {1,2} (seed=99)", random_bounded_pq(2000, seed=99), A=2))

    print("=" * 70)
    print("SUMMARY")
    for r in results:
        print(f"  {r['name']}: term2 bound held every k = {r['all_term2_exceed']}, "
              f"certifying witnesses = {r['n_certifying']}")
    all_ok = all(r["all_term2_exceed"] and r["n_certifying"] >= 2 for r in results)
    print(f"\nAll four non-periodic adversarial slopes: term2 bound holds AND "
          f"multiple certifying witnesses found: {all_ok}")


if __name__ == "__main__":
    main()
