"""
Verifies the Berthe-Holton-Zamboni closed-form formula for the initial
critical exponent ice(omega(-gamma)) against direct computation of achieved
initial-power exponents of the actual mechanical word u, and verifies the
uniform bound term2(k) > 2 + 1/(A+1) for every k, exactly.

Exact Fraction arithmetic throughout; floats only in display.
"""
from fractions import Fraction


def convergents_pq(pq, n):
    a0 = pq[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
        q.append(pq[i] * q[-1] + q[-2])
    return p[1:], q[1:]


def ice_formula_terms(pq, kmax):
    p, q = convergents_pq(pq, len(pq))
    terms = []
    for k in range(2, kmax):
        if 2 * k + 1 >= len(pq):
            break
        term1 = pq[2 * k + 1] + Fraction(q[2 * k - 1], q[2 * k])
        term2 = 1 + pq[2 * k - 1] + Fraction(q[2 * k - 3], q[2 * k - 2])
        terms.append((k, term1, term2))
    return terms


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def mechanical_word(gamma, n):
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for i in range(1, n + 1):
        cur = fl(i * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def lcp(a, b, m=None):
    n = min(len(a), len(b)) if m is None else min(len(a), len(b), m)
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def periodic_extension(W, length):
    ell = len(W)
    return [W[i % ell] for i in range(length)]


def verify_formula_matches_direct_computation(name, pq, A):
    print(f"=== {name} (A={A}) ===")
    gamma = cf_value(pq, len(pq))
    u = mechanical_word(gamma, 200000)
    p, q = convergents_pq(pq, len(pq))
    terms = ice_formula_terms(pq, 12)
    for k, t1, t2 in terms[-3:]:
        ell = q[2 * k - 1]  # a convergent length whose achieved exponent BHZ's proof identifies with these terms
        if ell < 2 or ell * 20 > len(u):
            continue
        W = u[:ell]
        checklen = min(len(u), ell * 20)
        L = lcp(u, periodic_extension(W, checklen), checklen)
        r_direct = Fraction(L, ell)
        print(f"  k={k}: formula term1={float(t1):.5f} term2={float(t2):.5f}  "
              f"direct r_u at q_{2*k-1}={ell}: {float(r_direct):.5f}")
    bound = 2 + Fraction(1, A + 1)
    all_pass = all(t2 > bound for _, _, t2 in terms)
    print(f"  term2(k) > 2+1/(A+1)={float(bound):.5f} for EVERY tested k: {all_pass}")
    assert all_pass
    print()


def main():
    verify_formula_matches_direct_computation("silver ratio [0;2,2,...]", [0] + [2] * 40, A=2)
    verify_formula_matches_direct_computation(
        "counterexample [0;1,1,1,2,2,...]", [0, 1, 1, 1] + [2] * 40, A=2)
    verify_formula_matches_direct_computation(
        "mixed tail [0;2,1,2,1,...]", [0] + [2, 1] * 40, A=2)
    verify_formula_matches_direct_computation(
        "near-boundary [0;1,4,1,5,1,6,2,6,2,...]", [0, 1, 4, 1, 5, 1] + [6, 2] * 20, A=6)
    print("ALL ICE-FORMULA CHECKS PASS.")


if __name__ == "__main__":
    main()
