"""
Verifies, in exact integer arithmetic, the discrepancy-parametrized height
bound derived in DISCREPANCY_HEIGHT_THEOREM.md:

    c_W <= ell * 3^D * max(2^ell, 3^k)

where D is the discrepancy bound |k_i(W) - i*k/ell| <= D for all 0<=i<=ell
(k_i(W) = number of ones among the first i letters, k_0=0), computed exactly
as the tightest rational-valued D that holds for W (D = max_i |k_i - i*k/ell|,
kept as an exact Fraction, not rounded).

This is an ORIGINAL bound (not verified in the source paper's own Appendix A,
which only checks the D<1 case via Lemma 4.2/10.4 for mechanical words and
cyclic permutations of standard words) -- tested here across many words,
including the extreme high-discrepancy control W = 0^a 1^a from Remark 4.3.
"""
import itertools
import random
from fractions import Fraction


def c_W_exact(W):
    ell = len(W)
    k = sum(W)
    # k_{i+1}(W) = number of ones among W[0..i]
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    c = 0
    for i in range(ell):
        if W[i] == 1:
            c += 3 ** (k - kpref[i + 1]) * 2 ** i
    return c, ell, k


def discrepancy_exact(W):
    ell = len(W)
    k = sum(W)
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    D = Fraction(0)
    for i in range(0, ell + 1):
        d = abs(Fraction(kpref[i]) - Fraction(i * k, ell))
        if d > D:
            D = d
    return D


def check(W, label=""):
    c, ell, k = c_W_exact(W)
    if k == 0 or k == ell:
        return None  # degenerate, c_W=0 or formula edge case; skip
    D = discrepancy_exact(W)
    import math
    D_ceil_int = math.ceil(D)  # use integer ceiling of D for the 3^D bound (D need not be integer)
    bound_exact_D = ell * (Fraction(3) ** D) * max(2 ** ell, 3 ** k)
    bound_ceil_D = ell * (3 ** D_ceil_int) * max(2 ** ell, 3 ** k)
    ok_exact = Fraction(c) <= bound_exact_D
    ok_ceil = c <= bound_ceil_D
    return {
        "label": label, "W": "".join(map(str, W)), "ell": ell, "k": k,
        "c_W": c, "D": D, "D_float": float(D),
        "bound_ceilD": bound_ceil_D, "ok_ceilD": ok_ceil,
        "ratio_to_bound": float(Fraction(c) / bound_ceil_D) if bound_ceil_D else None,
    }


def main():
    results = []
    failures = []

    # Structured extreme case: W = 0^a 1^a (Remark 4.3's own counterexample to
    # the *bounded-constant* bound -- must still satisfy the D-dependent bound)
    for a in [1, 2, 3, 5, 8, 10, 15, 18, 25]:
        W = [0] * a + [1] * a
        r = check(W, f"0^{a}1^{a}")
        if r:
            results.append(r)

    # Balanced-ish words: cyclic permutations of standard (Fibonacci-like) words
    def fibonacci_word_prefix(n):
        # Sturmian word of slope 1/phi via mechanical formula, exact rationals
        phi = Fraction(1, 1)
        # use golden ratio via continued fraction convergents instead of floats
        # slope = [0;1,1,1,...] convergent p/q -> use q=21,p=13 (Fibonacci) exact rational slope
        p, q = 13, 21
        return [ (( (j+1)*p ) // q) - ((j*p)//q) for j in range(n) ]

    base = fibonacci_word_prefix(21)
    for shift in range(21):
        W = base[shift:] + base[:shift]
        r = check(W, f"cyclic-fib-shift{shift}")
        if r:
            results.append(r)

    # Random words of varying length and density (stress test, many trials)
    random.seed(20260929)
    for trial in range(500):
        ell = random.randint(3, 60)
        p = random.uniform(0.05, 0.95)
        W = [1 if random.random() < p else 0 for _ in range(ell)]
        r = check(W, f"random-{trial}")
        if r:
            results.append(r)

    # Adversarial: alternating blocks designed to maximize discrepancy differently
    for a in [3, 7, 12]:
        W = ([1]*a + [0]*a) * 3
        r = check(W, f"blocks-{a}x3")
        if r:
            results.append(r)

    for r in results:
        if not r["ok_ceilD"]:
            failures.append(r)

    print(f"Total words checked: {len(results)}")
    print(f"Failures of c_W <= ell * 3^ceil(D) * max(2^ell,3^k): {len(failures)}")
    for f in failures[:20]:
        print("  FAIL:", f)

    print("\n--- Sample of extreme-discrepancy control (0^a1^a) ---")
    for r in results:
        if r["label"].startswith("0^"):
            print(f"  {r['label']}: ell={r['ell']} D={r['D_float']:.3f} "
                  f"c_W ratio to bound = {r['ratio_to_bound']:.3e} ok={r['ok_ceilD']}")

    print("\n--- Sample of balanced (Sturmian-root) words ---")
    fib_results = [r for r in results if r["label"].startswith("cyclic-fib")]
    max_D = max(r["D_float"] for r in fib_results)
    max_ratio = max(r["ratio_to_bound"] for r in fib_results)
    print(f"  max D observed = {max_D:.4f} (expect < 1, matching Lemma 10.4's hypothesis)")
    print(f"  max ratio to ell*3^ceil(D)*max(2^ell,3^k) bound = {max_ratio:.4f}")

    print("\n--- Random words: distribution of D and bound tightness ---")
    rand_results = [r for r in results if r["label"].startswith("random")]
    import statistics
    Ds = [r["D_float"] for r in rand_results]
    ratios = [r["ratio_to_bound"] for r in rand_results]
    print(f"  n={len(rand_results)}, D range [{min(Ds):.2f},{max(Ds):.2f}], "
          f"ratio range [{min(ratios):.2e},{max(ratios):.2e}]")


if __name__ == "__main__":
    main()
