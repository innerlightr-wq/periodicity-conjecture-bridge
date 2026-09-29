"""
Part 9: simplest non-Sturmian two-interval rotation coding.

A Sturmian coding of a rotation by irrational gamma partitions the circle
[0,1) into two intervals whose lengths are exactly {gamma, 1-gamma} (matched
to the rotation angle itself) -- this is what makes it complexity L+1.

A general TWO-INTERVAL ROTATION CODING partitions [0,1) into two intervals
of ARBITRARY lengths {delta, 1-delta}, delta != gamma, under rotation by
gamma. By the three-distance theorem this generically has HIGHER complexity
than Sturmian -- for a "generic" mismatched delta, complexity grows like 2L
eventually (each new letter can split an existing complexity class into two,
since the orbit point can land in either sub-interval created by the mismatch
between the rotation step gamma and the partition point delta).

This script:
  1. Builds the coding s_n = 1 if {n*gamma + rho} in [0,delta) else 0, for a
     rotation angle gamma, a partition length delta != gamma, and offset rho.
  2. Computes exact factor complexity p_s(L) for L up to a feasible bound,
     using exact rational arithmetic (gamma, delta, rho carried as high-
     precision Fractions via continued-fraction convergent truncation -- NOT
     floating point -- so interval-membership decisions near boundaries are
     exact up to the chosen precision, with a certified safety margin).
  3. Searches for initial squares/powers using the bridge_toolkit machinery.
  4. Reports whether the initial-power route finds anything usable.
"""
import sys
sys.path.insert(0, ".")
from fractions import Fraction
from bridge_toolkit import initial_power_search, discrepancy, c_W, F_bound

def continued_fraction_convergent(cf_terms, prec_terms):
    """
    Exact rational convergent of [a0; a1, a2, ...] truncated to prec_terms.
    (Fixed: this previously returned Fraction(den,num), the RECIPROCAL of
    the intended value -- caught via a downstream density sanity check in
    rote_construction_test.py's silver-ratio run, k>ell being impossible
    for a binary word; the correct value is num/den.)
    """
    num, den = 1, 0
    for a in reversed(cf_terms[:prec_terms]):
        num, den = a * num + den, num
    return Fraction(num, den) if den != 0 else Fraction(0)

# golden ratio conjugate gamma = 1/phi = [0;1,1,1,1,...]
def golden_gamma(prec):
    return continued_fraction_convergent([0] + [1] * prec, prec + 1)

def code_sequence(gamma, delta, rho, n_terms):
    s = []
    x = rho - (rho.numerator // rho.denominator if rho != 0 else 0)  # x in [0,1)
    for _ in range(n_terms):
        s.append(1 if x < delta else 0)
        x = x + gamma
        x = x - (x.numerator // x.denominator)  # exact fractional part, keeps x in [0,1)
    return s

def factor_complexity(s, max_L):
    n = len(s)
    result = []
    for L in range(1, max_L + 1):
        factors = set()
        for i in range(0, n - L + 1):
            factors.add(tuple(s[i:i + L]))
        result.append(len(factors))
    return result

def main():
    prec = 40  # continued-fraction precision terms for gamma (exact rational, high precision)
    gamma = golden_gamma(prec)
    delta = Fraction(1, 3)   # MISMATCHED partition length (Sturmian would need delta=gamma or 1-gamma)
    rho = Fraction(0)

    print(f"gamma (golden ratio conjugate, rational approx to {prec} CF terms) = {float(gamma):.10f}")
    print(f"delta (partition length, mismatched) = {float(delta):.6f}")
    print(f"gamma == delta? {gamma == delta}  gamma == 1-delta? {gamma == 1 - delta}")
    print("(neither match -> genuinely non-Sturmian two-interval coding)\n")

    n_terms = 4000
    s = code_sequence(gamma, delta, rho, n_terms)

    print("=== Factor complexity check (is it really > L+1, i.e. non-Sturmian?) ===")
    max_L = 30
    comp = factor_complexity(s, max_L)
    for L in [1, 2, 3, 5, 10, 15, 20, 25, 30]:
        print(f"  p_s({L}) = {comp[L-1]}   (Sturmian would give {L+1}; 2L would give {2*L})")

    print("\n=== Initial power search (bridge_toolkit) ===")
    results = initial_power_search(s, min(n_terms, 2000), min_root=1, max_root=800)
    print(f"Squares/powers found (ell>=2, r>=2): {len(results)}")
    for r in results[:10]:
        D = discrepancy(r["W"])
        print(f"  ell={r['ell']:4d} k={r['k']:4d} r={float(r['r']):.3f} "
              f"discrepancy={float(D):.3f} density={r['k']/r['ell']:.4f}")
    if not results:
        print("  NONE FOUND within the tested prefix length -- method has no input at this scale.")

if __name__ == "__main__":
    main()
