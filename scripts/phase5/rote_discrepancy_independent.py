"""
Phase 5, Section 8: independently checks D(R) (discrepancy of the odd-weight
Rote root R=V.Vbar against its own true density 1/2) tracks D(V) plus a
non-growing gap term, for a bounded-partial-quotient slope -- i.e. supports
D(R)=O(log ell) without assuming it.

Exact Fraction arithmetic; floats only in the printed table.
"""
from fractions import Fraction


def cf_convergent(pq, n):
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


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


def discrepancy(W, target_density=None):
    ell = len(W)
    k = sum(W)
    dens = Fraction(k, ell) if target_density is None else target_density
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    D = Fraction(0)
    for i in range(ell + 1):
        d = abs(Fraction(kpref[i]) - i * dens)
        if d > D:
            D = d
    return D


def main():
    golden = cf_convergent([0] + [1] * 60, 60)
    u = mechanical_word(golden, 3000)
    v = rote_from_sturmian(u)

    print(f"{'ell':>5} {'D(V) own-density':>18} {'ell*|gammaV-1/2|':>18} {'D(R) at 1/2':>14}")
    for ell in [10, 50, 100, 300, 700, 1400, 2900]:
        if ell >= len(v):
            continue
        V = v[:ell]
        Vbar = [1 - x for x in V]
        R = V + Vbar
        DV = discrepancy(V)
        gamma_V = Fraction(sum(V), ell)
        gap = abs(gamma_V - Fraction(1, 2)) * ell
        DR = discrepancy(R, target_density=Fraction(1, 2))
        print(f"{ell:5d} {float(DV):18.3f} {float(gap):18.3f} {float(DR):14.3f}")
        # sanity: the derived bound D(R) <= 2*D(V) + gap
        assert DR <= 2 * DV + gap, f"BOUND VIOLATED at ell={ell}: D(R)={DR} > 2*D(V)+gap={2*DV+gap}"
    print("\nBound D(R) <= 2*D(V) + ell*|gammaV-1/2| holds at every tested ell (assertion passed).")


if __name__ == "__main__":
    main()
