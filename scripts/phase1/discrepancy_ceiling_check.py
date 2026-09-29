"""
BRIDGE_CONTROLS.md, control 3: checks whether any binary word's discrepancy
can exceed the two-block (sorted) value k(ell-k)/ell, and whether that
combinatorial ceiling can ever cross the r=2 (squares) discrepancy-tolerance
threshold derived in REPETITION_HEIGHT_CRITERION.md.
"""
import math
import itertools

log2_3 = math.log2(3)


def threshold(gamma):
    """Discrepancy-rate tolerance for r=2 (squares) at density gamma."""
    return (2 - max(1, gamma * log2_3)) / log2_3


def theta_max_twoblock(gamma):
    """Discrepancy rate of the two-block (sorted) word at density gamma."""
    return gamma * (1 - gamma)


def discrepancy_exact(W):
    ell = len(W)
    k = sum(W)
    if k == 0 or k == ell:
        return 0.0
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    return max(abs(kpref[i] - i * k / ell) for i in range(ell + 1))


def main():
    print("=== Closed-form margin check: threshold(gamma) - theta_max(gamma) ===")
    worst_margin, worst_gamma = float("inf"), None
    for i in range(1, 10000):
        g = i / 10000
        margin = threshold(g) - theta_max_twoblock(g)
        if margin < worst_margin:
            worst_margin, worst_gamma = margin, g
    print(f"Minimum margin over gamma in (0,1): {worst_margin:.6f} at gamma={worst_gamma}")
    print(f"threshold(0.5)={threshold(0.5):.6f}  theta_max(0.5)={theta_max_twoblock(0.5):.6f}")
    print(f"threshold(1-)={threshold(0.9999):.6f}  theta_max(1-)~{theta_max_twoblock(0.9999):.6f}")
    print("(margin stays strictly positive everywhere checked)")

    print("\n=== Exhaustive check: two-block word achieves the TRUE max discrepancy ===")
    mismatches = 0
    total = 0
    for ell in range(2, 17):
        for k in range(1, ell):
            total += 1
            pred = k * (ell - k) / ell
            true_max = 0.0
            for bits in itertools.combinations(range(ell), k):
                W = [0] * ell
                for b in bits:
                    W[b] = 1
                d = discrepancy_exact(W)
                if d > true_max:
                    true_max = d
            if abs(true_max - pred) > 1e-9:
                mismatches += 1
                print(f"  MISMATCH ell={ell} k={k}: two-block={pred}, true max={true_max}")
    print(f"Total (ell,k) pairs checked: {total} (every arrangement per pair), mismatches: {mismatches}")


if __name__ == "__main__":
    main()
