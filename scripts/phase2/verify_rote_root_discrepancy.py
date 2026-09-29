"""
Corroborates ROTE_ROOT_DISCREPANCY.md's claim: for bounded-partial-quotient
Sturmian slopes, the CS Rote root V (=v[0:ell], v the mod-2 partial sum of
the Sturmian mechanical word u) has discrepancy D(V) = O(log ell), not
merely o(ell) or O(ell).

Exact Fraction arithmetic for discrepancy; floating point used only for
the final log-ratio DISPLAY, never for any decision.
"""
from fractions import Fraction
import math


def cf_convergent(partial_quotients, n_terms):
    num, den = 1, 0
    for a in reversed(partial_quotients[:n_terms]):
        num, den = a * num + den, num
    return Fraction(num, den)


def mechanical_word(gamma, n_terms):
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for n in range(1, n_terms + 1):
        cur = fl(n * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def discrepancy(W):
    ell = len(W)
    k = sum(W)
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    D = Fraction(0)
    for i in range(ell + 1):
        d = abs(Fraction(kpref[i]) - Fraction(i * k, ell))
        if d > D:
            D = d
    return D


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v


def scan(name, gamma, n_terms, lengths):
    u = mechanical_word(gamma, n_terms)
    v = rote_from_sturmian(u)[:-1]
    print(f"=== {name}: gamma={float(gamma):.8f} ===")
    print(f"{'ell':>6} {'D(V)':>8} {'D/ell':>10} {'D/log(ell)':>12}")
    for ell in lengths:
        if ell > len(v):
            continue
        V = v[:ell]
        D = float(discrepancy(V))
        print(f"{ell:6d} {D:8.2f} {D/ell:10.5f} {D/math.log(ell):12.4f}")
    print()


def main():
    prec = 80
    golden = cf_convergent([0] + [1] * prec, prec + 1)
    silver = cf_convergent([0] + [2] * prec, prec + 1)
    unbounded = cf_convergent([0] + list(range(1, 60)), 60)

    lengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 8000]
    scan("golden ratio conjugate [0;1,1,1,...] (bounded PQ)", golden, 9000, lengths)
    scan("silver ratio [0;2,2,2,...] (bounded PQ)", silver, 9000, lengths)
    scan("unbounded PQ [0;1,2,3,4,...] -- NOT covered by the proof, contrast only",
         unbounded, 20000, [10, 50, 200, 1000, 5000, 15000])


if __name__ == "__main__":
    main()
