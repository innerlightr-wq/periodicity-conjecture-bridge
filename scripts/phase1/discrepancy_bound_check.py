"""
Exact-integer verification of the general discrepancy-height bound:
  c_W <= ell * 3^D * max(2^ell, 3^k)
where D = max_i |k_i(W) - i*k/ell| (i=0..ell), k_i = # ones among W[0:i].
No floating point enters any pass/fail decision (D is compared via
cross-multiplication with exact Fractions).
"""
from fractions import Fraction
import itertools, random

def c_W_exact(W):
    ell = len(W)
    k = sum(W)
    # k_{i+1}(W) = ones among W[0..i], i.e. prefix count up to index i+1
    kpref = [0]*(ell+1)
    for i in range(ell):
        kpref[i+1] = kpref[i] + W[i]
    total = 0
    for i in range(ell):
        if W[i] == 1:
            total += 3**(k - kpref[i+1]) * 2**i
    return total, k, ell

def discrepancy_exact(W):
    ell = len(W)
    k = sum(W)
    kpref = [0]*(ell+1)
    for i in range(ell):
        kpref[i+1] = kpref[i] + W[i]
    # D = max_i |k_i - i*k/ell|, exact via Fraction, report as a Fraction upper bound (ceiling to int use)
    Dmax = Fraction(0)
    for i in range(ell+1):
        diff = Fraction(kpref[i]) - Fraction(i*k, ell)
        Dmax = max(Dmax, abs(diff))
    return Dmax

def check_bound(W, verbose=False):
    cW, k, ell = c_W_exact(W)
    D = discrepancy_exact(W)
    import math
    # need integer D' >= D for the theorem (D must be an upper bound, so use ceiling)
    Dceil = math.ceil(D) if D == int(D) else math.floor(D) + 1
    if D == int(D):
        Dceil = int(D)
    bound = ell * 3**Dceil * max(2**ell, 3**k)
    ok = cW <= bound
    if verbose or not ok:
        print(f"W={''.join(map(str,W))} ell={ell} k={k} c_W={cW} D_exact={D} D_ceil={Dceil} "
              f"bound={bound} OK={ok}")
    return ok

def main():
    random.seed(20260929)
    total = 0
    failures = 0

    # exhaustive over all words up to length 16
    for ell in range(1, 17):
        for bits in itertools.product([0,1], repeat=ell):
            W = list(bits)
            if sum(W) == 0:
                continue
            total += 1
            if not check_bound(W):
                failures += 1

    print(f"Exhaustive ell<=16: {total} words checked, {failures} failures")

    # random longer words to extend coverage
    total2 = 0
    failures2 = 0
    for _ in range(2000):
        ell = random.randint(17, 200)
        k = random.randint(1, ell)
        positions = sorted(random.sample(range(ell), k))
        W = [0]*ell
        for p in positions:
            W[p] = 1
        total2 += 1
        if not check_bound(W):
            failures2 += 1
    print(f"Random ell in [17,200]: {total2} words checked, {failures2} failures")

    # adversarial: cluster ones at the end (Remark 4.3 style), varying a
    print("\n--- Adversarial 0^a 1^a family (matches Remark 4.3) ---")
    for a in [5, 10, 15, 20, 25]:
        W = [0]*a + [1]*a
        check_bound(W, verbose=True)

    # near-balanced (Sturmian-like) mechanical words for sanity (D should be < 1)
    print("\n--- Mechanical words (should have D<1, matching Lemma 4.2's exact case) ---")
    for (p, q) in [(1,1),(1,2),(2,3),(5,8),(12,19)]:
        ones_positions = set((j*q)//p for j in range(p))
        W = [1 if i in ones_positions else 0 for i in range(q)]
        D = discrepancy_exact(W)
        check_bound(W, verbose=True)

if __name__ == "__main__":
    main()
