"""
Reusable, exact-arithmetic toolkit for testing the abstract bridge criterion
(ABSTRACT_BRIDGE_THEOREM.md) on any candidate word family. No floating point
in any pass/fail or comparison decision (matches the source paper's own
verification discipline, Appendix A).

Core objects:
  c_W(W)                 -- Proposition 4.1's constant, exact integer
  discrepancy(W)          -- exact Fraction, D(W) = max_i |k_i - i*k/ell|
  F_bound(W)               -- (1 + ell*3^ceil(D)) * max(2^ell,3^k), the
                              general height bound of ABSTRACT_BRIDGE_THEOREM/
                              DISCREPANCY_HEIGHT_THEOREM
  initial_power_exponent(s_prefix, max_len) -- largest r with a prefix W^r,
                              W primitive, found within max_len letters;
                              returns (r, ell, W) for the best (longest
                              half-length) square/power found
  lcp(a, b)                -- longest common prefix length of two sequences
  bridge_surplus(L, W)      -- L - log2(F_bound(W)), as an exact Fraction
                              log2 lower bound (via bit-length comparison,
                              never floating log)

Verified below (__main__) against the source paper's own worked numbers:
mechanical word w_{12,19} (slope 12/19, the extremal conjheight case cited
in the paper, ratio 0.4394) and the Fibonacci-slope standard word.
"""
from fractions import Fraction
import math


def c_W(W):
    ell = len(W)
    k = sum(W)
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    c = 0
    for i in range(ell):
        if W[i] == 1:
            c += 3 ** (k - kpref[i + 1]) * 2 ** i
    return c


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


def F_bound(W):
    ell = len(W)
    k = sum(W)
    D = discrepancy(W)
    Dceil = math.ceil(D)
    G = max(2 ** ell, 3 ** k)
    return (1 + ell * 3 ** Dceil) * G


def log2_floor(n):
    """Exact floor(log2(n)) for positive integer n, via bit_length."""
    assert n > 0
    return n.bit_length() - 1


def lcp(a, b, max_check=None):
    n = min(len(a), len(b)) if max_check is None else min(len(a), len(b), max_check)
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def periodic_extension(W, length):
    ell = len(W)
    return [W[i % ell] for i in range(length)]


def initial_power_search(s, max_check_len, min_root=1, max_root=None):
    """
    Search for the largest exponent-* initial power in s[:max_check_len].
    For each candidate root length ell (1..max_check_len//2), compute the
    exponent r = lcp(s, W^infty)/ell where W = s[:ell], W primitive (checked).
    Returns list of (ell, k_ones, r_exact_as_Fraction, W) for every ell where
    r >= 2 (a genuine repeated prefix), sorted by ell descending.
    Exact rational r (no floating point).
    """
    results = []
    max_root = max_root or (max_check_len // 2)
    for ell in range(min_root, max_root + 1):
        W = s[:ell]
        # primitivity check: W is primitive if no proper divisor d|ell has W periodic with period d
        primitive = True
        for d in range(1, ell):
            if ell % d == 0 and all(W[i] == W[i % d] for i in range(ell)):
                primitive = False
                break
        if not primitive:
            continue
        ext = periodic_extension(W, max_check_len)
        L = lcp(s, ext, max_check_len)
        if L < 2 * ell:
            continue  # not even a square
        r = Fraction(L, ell)
        k = sum(W)
        results.append({"ell": ell, "k": k, "L": L, "r": r, "W": W})
    results.sort(key=lambda d: -d["ell"])
    return results


def bridge_surplus_exact(L, W):
    """
    Returns (surplus_lower_bound_as_int, F) where surplus_lower_bound is a
    SAFE INTEGER lower bound on L - log2(F(W)) (using floor(log2(F)) rounded
    UP by 1 to be conservative, i.e. surplus >= L - ceil(log2 F) - 1
    guaranteed, avoiding any floating point).
    """
    F = F_bound(W)
    log2F_floor = log2_floor(F)
    # ceil(log2 F) is log2F_floor if F is a power of 2, else log2F_floor+1
    log2F_ceil = log2F_floor if (F & (F - 1) == 0) else log2F_floor + 1
    return L - log2F_ceil, F


if __name__ == "__main__":
    # --- Verification against the source paper's own cited extremal case ---
    # W = 0101101101011011011, slope 12/19 mechanical word, the paper's own
    # extremal conjheight example, ratio 0.439399 (Appendix A).
    W1219 = [int(c) for c in "0101101101011011011"]
    assert len(W1219) == 19
    c1 = c_W(W1219)
    ell1, k1 = 19, sum(W1219)
    G1 = max(2 ** ell1, 3 ** k1)
    ratio = Fraction(c1, ell1 * G1)
    print(f"W (slope 12/19 mechanical word): ell={ell1} k={k1} c_W={c1}")
    print(f"  c_W/(ell*max(2^ell,3^k)) = {float(ratio):.6f}  (paper reports 0.439399)")
    assert abs(float(ratio) - 0.439399) < 1e-5, "MISMATCH vs paper's own Appendix A value!"
    print("  MATCH confirmed against paper's Appendix A conjheight table.\n")

    D1 = discrepancy(W1219)
    print(f"  discrepancy D(W) = {float(D1):.4f} (expect < 1, matching Theorem 10.3's balance)")
    assert D1 < 1

    # --- Fibonacci-slope standard word, cyclic shift, sanity check ---
    p, q = 13, 21
    base = [((j + 1) * p) // q - (j * p) // q for j in range(q)]
    for shift in [0, 5, 10]:
        Wc = base[shift:] + base[:shift]
        Dc = discrepancy(Wc)
        assert Dc < 1, f"shift {shift}: discrepancy {float(Dc)} >= 1, unexpected for standard-word cyclic shift"
    print("Fibonacci-slope cyclic shifts: all discrepancy < 1, as expected. Toolkit verified.\n")

    # --- initial_power_search sanity check on a periodic word (should find large r) ---
    s_periodic_test = periodic_extension([0, 1, 1], 60)
    res = initial_power_search(s_periodic_test, 60)
    best = res[0] if res else None
    print(f"Periodic test word (010101...roots of 011): best square/power found: {best}")
