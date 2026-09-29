"""
Phase 5, Section 6: searches for odd-weight V where R=V.Vbar is non-primitive
(exhaustive, small lengths), and separately checks primitivity of the ACTUAL
R's arising from Phase 4's tested slopes/witnesses (re-generated here
independently, not imported from Phase 4 scripts).
"""
from fractions import Fraction
import sys
import os


def fundamental_period(W):
    ell = len(W)
    for d in range(1, ell + 1):
        if ell % d == 0 and all(W[i] == W[i % d] for i in range(ell)):
            return d
    return ell


def exhaustive_search(max_ell=8):
    examples = []
    for ell in range(1, max_ell + 1):
        for bits in range(2 ** ell):
            V = [(bits >> i) & 1 for i in range(ell)][::-1]
            if sum(V) % 2 == 0:
                continue
            Vbar = [1 - x for x in V]
            R = V + Vbar
            p = fundamental_period(R)
            if p < len(R):
                examples.append((V, p, len(R)))
    return examples


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


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


def check_phase4_slopes():
    """Independently regenerate the R's used in Phase 4's tested slopes and
    check each for primitivity."""
    slopes = {
        "golden": [0] + [1] * 30,
        "silver": [0] + [2] * 30,
        "near-boundary": [0, 1, 4, 1, 5, 1] + [6, 2] * 20,
    }
    results = []
    for name, pq in slopes.items():
        gamma = cf_value(pq, len(pq))
        u = mechanical_word(gamma, 400000)
        v = rote_from_sturmian(u)
        # test a handful of convergent-ish lengths
        for ell in [5, 13, 34, 89, 233, 610, 1000, 5000]:
            if ell >= len(u):
                continue
            W = u[:ell]
            if sum(W) % 2 == 0:
                continue  # only odd-weight -> R route relevant here
            V = v[:ell]
            Vbar = [1 - x for x in V]
            R = V + Vbar
            p = fundamental_period(R)
            results.append((name, ell, p, len(R), p == len(R)))
    return results


def main():
    print("=== Exhaustive small-length search for non-primitive R=V.Vbar ===")
    examples = exhaustive_search(8)
    print(f"Found {len(examples)} non-primitive cases, V length <= 8:")
    for V, p, full in examples:
        print(f"  V={V} -> R period={p} (full={full})")

    print("\n=== Primitivity check on ACTUAL R's from Phase 4 tested slopes ===")
    results = check_phase4_slopes()
    for name, ell, p, full, is_prim in results:
        print(f"  {name}: ell={ell:5d} R_period={p:6d} R_full_length={full:6d} primitive={is_prim}")
    all_primitive = all(r[4] for r in results)
    print(f"\nAll actual Phase-4-slope R's checked are primitive: {all_primitive}")


if __name__ == "__main__":
    main()
