"""
For each (ell,k), brute-force the MAXIMUM possible discrepancy D(W) over ALL
arrangements of k ones among ell positions, and compare to the closed form
D_max = k*(ell-k)/ell (i.e. theta=gamma(1-gamma), single-block conjecture).
Also directly check, for the single-block word 0^(ell-k)1^k, whether the
surplus S = 2*ell - log2(F(W)) stays positive as ell grows, using the
EXACT c_W (not just the crude bound), across a range of densities gamma.
"""
from fractions import Fraction
import itertools, math

def discrepancy_exact(W):
    ell = len(W)
    k = sum(W)
    kpref = [0]*(ell+1)
    for i in range(ell):
        kpref[i+1] = kpref[i] + W[i]
    Dmax = Fraction(0)
    for i in range(ell+1):
        diff = Fraction(kpref[i]) - Fraction(i*k, ell)
        Dmax = max(Dmax, abs(diff))
    return Dmax

def c_W_exact(W):
    ell = len(W); k = sum(W)
    kpref = [0]*(ell+1)
    for i in range(ell):
        kpref[i+1] = kpref[i] + W[i]
    total = 0
    for i in range(ell):
        if W[i] == 1:
            total += 3**(k - kpref[i+1]) * 2**i
    return total

print("=== Brute-force worst-case discrepancy vs closed form k(ell-k)/ell ===")
for ell in range(2, 13):
    for k in range(1, ell):
        best = Fraction(0)
        best_W = None
        for positions in itertools.combinations(range(ell), k):
            W = [0]*ell
            for p in positions: W[p]=1
            D = discrepancy_exact(W)
            if D > best:
                best = D
                best_W = tuple(W)
        closed_form = Fraction(k*(ell-k), ell)
        match = (best == closed_form)
        if not match:
            print(f"  MISMATCH ell={ell} k={k}: brute_max={best} closed_form={closed_form} W={best_W}")
print("Done brute-force comparison (only mismatches printed above; none = all match)")

print("\n=== Surplus S = 2*ell - log2(F(W)) for single-block 0^(ell-k)1^k, EXACT c_W, growing ell ===")
log2_3 = math.log2(3)
for gamma_num, gamma_den in [(1,4),(1,2),(3,4),(9,10),(99,100)]:
    print(f"\n-- density k/ell -> {gamma_num}/{gamma_den} --")
    for ell in [20, 50, 100, 200, 400, 800]:
        k = round(ell * gamma_num / gamma_den)
        if k == 0 or k == ell: continue
        W = [0]*(ell-k) + [1]*k
        cW = c_W_exact(W)
        delta_term = max(2**ell, 3**k)  # the |delta| term in F(W) = max(2^ell,3^k)+c_W
        F = delta_term + cW
        L = 2*ell  # initial square exponent r=2
        S = L - math.log2(F)
        print(f"   ell={ell:4d} k={k:4d} gamma={k/ell:.4f}  log2(c_W)={math.log2(cW):.2f}  "
              f"log2(F)={math.log2(F):.2f}  S=2ell-log2F={S:.2f}")
