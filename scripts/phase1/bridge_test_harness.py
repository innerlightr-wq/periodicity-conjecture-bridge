"""
Shared exact-arithmetic harness for testing the periodic-approximation bridge
on any candidate infinite word s (given as a prefix-generating function).
No floating point enters any pass/fail decision. Reused across
ROTE_COMPUTATIONAL_AUDIT.md and ROTATION_CODING_AUDIT.md.
"""
from fractions import Fraction
import math


def discrepancy_exact(W):
    """D(W) = max_i |k_i(W) - i*k/ell|, i=0..ell, exact via Fraction."""
    ell = len(W)
    k = sum(W)
    if ell == 0:
        return Fraction(0)
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    Dmax = Fraction(0)
    for i in range(ell + 1):
        diff = Fraction(kpref[i]) - Fraction(i * k, ell)
        Dmax = max(Dmax, abs(diff))
    return Dmax


def c_W_exact(W):
    """c_W = sum_{i<ell, W_i=1} 3^{k-k_{i+1}(W)} 2^i, Proposition 4.1's constant."""
    ell = len(W)
    k = sum(W)
    kpref = [0] * (ell + 1)
    for i in range(ell):
        kpref[i + 1] = kpref[i] + W[i]
    total = 0
    for i in range(ell):
        if W[i] == 1:
            total += 3 ** (k - kpref[i + 1]) * 2 ** i
    return total


def find_initial_powers(s_prefix, max_half_length, r_min=2.0):
    """
    s_prefix: list of 0/1, a prefix of the candidate infinite word.
    Returns list of (ell, L, r_achieved) for each half-length ell<=max_half_length
    at which s_prefix begins with (root of length ell)^r, r_achieved = L/ell,
    L = lcp(s_prefix, W^inf), W=s_prefix[:ell] -- ONLY when r_achieved >= r_min
    (default 2.0, i.e. a GENUINE SQUARE in the combinatorics-on-words sense --
    note L >= ell trivially for EVERY ell since W^inf starts with W by
    construction, so r>=1 is not meaningful on its own and must not be used
    as the reporting threshold; r>=2 is the correct "initial square" test,
    matching Theorem 10.2's own definition).
    """
    results = []
    n = len(s_prefix)
    for ell in range(1, max_half_length + 1):
        if ell > n:
            break
        if r_min * ell > n:
            break  # cannot possibly witness r>=r_min within available prefix
        W = s_prefix[:ell]
        L = 0
        while L < n and s_prefix[L] == W[L % ell]:
            L += 1
        r_achieved = L / ell
        if r_achieved >= r_min:
            results.append((ell, L, r_achieved))
    return results


def surplus_exact(L, W):
    """
    S_s(W) = L - log2(|2^ell - 3^k| + c_W), the proof-native surplus
    (SURPLUS_INVARIANT.md). Returns a float (log2 of a huge exact integer;
    the integer itself is computed exactly, only the final log2 is a float
    for reporting -- no decision is based on the float beyond sign/magnitude
    inspection, consistent with "report exact integer bounds" where the
    decision matters).
    """
    ell = len(W)
    k = sum(W)
    delta = abs(2 ** ell - 3 ** k)
    cW = c_W_exact(W)
    F = delta + cW
    return L - math.log2(F), F


def report_word(name, s_prefix, max_half_length=2000):
    print(f"=== {name} (prefix length {len(s_prefix)}) ===")
    powers = find_initial_powers(s_prefix, max_half_length)
    if not powers:
        print(f"  No initial power with r>1 found below half-length {max_half_length}.")
        return []
    print(f"  Found {len(powers)} initial powers with r>1, half-lengths up to {powers[-1][0]}.")
    rows = []
    for ell, L, r in powers[-10:]:  # report the 10 deepest found
        W = s_prefix[:ell]
        k = sum(W)
        D = discrepancy_exact(W)
        S, F = surplus_exact(L, W)
        gamma = k / ell
        row = dict(ell=ell, L=L, r=r, k=k, gamma=gamma, D=float(D), S=S, log2F=math.log2(F))
        rows.append(row)
        print(f"    ell={ell:5d} L={L:6d} r={r:.4f} k={k:5d} gamma={gamma:.4f} "
              f"D={float(D):.2f} D/ell={float(D)/ell:.4f} S={S:.2f} log2F={math.log2(F):.2f}")
    return rows
