"""
Phase 5, Section 3: independently verify which BHZ-defined Sturmian sequence
(coding of R_alpha or R~_alpha at intercept -alpha or 1-alpha) coincides
with THIS project's mechanical word u_n = floor((n+1)*gamma) - floor(n*gamma).

Built directly from BHZ's own stated definitions (read from the primary
source PDF, not from any Phase 1-4 file):

  R_alpha(z)  = z+alpha        if z in [-alpha, 1-2alpha)
              = z+alpha-1      if z in [1-2alpha, 1-alpha)
  R~_alpha(z) = z+alpha        if z in (-alpha, 1-2alpha]
              = z+alpha-1      if z in (1-2alpha, 1-alpha]

  omega(x)_k = 0  <=>  R_alpha^k(x)  in [-alpha,1-2alpha)   [R_alpha coding]
  omega~(x)_k = 0 <=>  R~_alpha^k(x) in (-alpha,1-2alpha]   [R~_alpha coding]

  omega(-alpha)  : intercept x=-alpha,  under R_alpha
  omega(1-alpha) : intercept x=1-alpha, under R~_alpha

Exact Fraction arithmetic throughout (alpha taken as a high-precision
continued-fraction convergent, so all interval-membership tests are exact
rational comparisons, never floating point).
"""
from fractions import Fraction


def cf_convergent(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def R_alpha_orbit_coding(alpha, x0, n_terms):
    """omega(x0) under R_alpha, R_alpha as defined by BHZ (half-open [ , ))."""
    seq = []
    x = x0
    lo, mid, hi = -alpha, 1 - 2 * alpha, 1 - alpha
    for _ in range(n_terms):
        if lo <= x < mid:
            seq.append(0)
            x = x + alpha
        else:
            seq.append(1)
            x = x + alpha - 1
    return seq


def Rtilde_alpha_orbit_coding(alpha, x0, n_terms):
    """omega~(x0) under R~_alpha, BHZ definition (half-open ( , ])."""
    seq = []
    x = x0
    lo, mid, hi = -alpha, 1 - 2 * alpha, 1 - alpha
    for _ in range(n_terms):
        if lo < x <= mid:
            seq.append(0)
            x = x + alpha
        else:
            seq.append(1)
            x = x + alpha - 1
    return seq


def mechanical_word(gamma, n):
    """THIS PROJECT's u: u_n = floor((n+1)*gamma) - floor(n*gamma)."""
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for i in range(1, n + 1):
        cur = fl(i * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def main():
    prec = 60
    n_terms = 2000

    slopes = {
        "golden [0;1,1,1,...]": [0] + [1] * prec,
        "silver [0;2,2,2,...]": [0] + [2] * prec,
        "mixed [0;1,4,1,5,1,6,2,...]": [0, 1, 4, 1, 5, 1] + [6, 2] * 30,
    }

    for name, pq in slopes.items():
        gamma = cf_convergent(pq, len(pq))
        u_ours = mechanical_word(gamma, n_terms)

        omega_minus_alpha = R_alpha_orbit_coding(gamma, -gamma, n_terms)
        omega_1_minus_alpha = Rtilde_alpha_orbit_coding(gamma, 1 - gamma, n_terms)

        match_minus = (u_ours == omega_minus_alpha)
        match_1minus = (u_ours == omega_1_minus_alpha)

        print(f"=== {name} ===")
        print(f"  u_ours[:20]              = {u_ours[:20]}")
        print(f"  omega(-alpha)[:20]       = {omega_minus_alpha[:20]}")
        print(f"  omega(1-alpha)[:20]      = {omega_1_minus_alpha[:20]}")
        print(f"  u_ours == omega(-alpha)   over {n_terms} terms: {match_minus}")
        print(f"  u_ours == omega(1-alpha)  over {n_terms} terms: {match_1minus}")
        if not match_minus:
            for i in range(len(u_ours)):
                if u_ours[i] != omega_minus_alpha[i]:
                    print(f"    first mismatch vs omega(-alpha) at index {i}: "
                          f"u={u_ours[i]} omega(-alpha)={omega_minus_alpha[i]}")
                    break
        print()

    print("Conclusion printed per-slope above; see BHZ_PRIMARY_SOURCE_AUDIT.md for the reading.")


if __name__ == "__main__":
    main()
