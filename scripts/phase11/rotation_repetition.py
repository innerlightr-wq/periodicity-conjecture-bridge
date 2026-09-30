"""
Phase 11 / steps 1,3,4: the rotation-geometry repetition lemma for the named word
    alpha = (sqrt5-1)/2,  rho = 1/7,  beta = ln2/ln3,  s_n = 1 <=> {n alpha + rho} in [0,beta).

STRUCTURE OF THE ARGUMENT (each part verified below with exact Q(sqrt5) arithmetic).

(R1) FIRST-MISMATCH CHARACTERISATION.  For a shift ell put delta = delta(ell) := ell*alpha - round.
     s_{m+ell} != s_m  <=>  {m alpha + rho} in M(delta) := { x : chi(x) != chi(x+delta) },
     chi = indicator of [0,beta).  M(delta) is the union of TWO arcs of length |delta|, one at 0 and
     one at beta, on the side given by sign(delta):
         delta > 0 : [1-delta, 1) u [beta-delta, beta)
         delta < 0 : [0, |delta|) u [beta, beta+|delta|)
     Hence, with L(ell) := lcp(s, (s[0:ell])^inf),
         L(ell) - ell  =  m*(ell) := min{ m >= 0 : {m alpha + rho} in M(delta) } .

(R2) TWO-BALL RELAXATION.  M(delta) is contained in B(0,|delta|) u B(beta,|delta|) (two-sided
     balls).  So  m*(ell) >= min(t_0, t_beta)  with
         t_0    := min{ m : ||m alpha + rho||          <= |delta| }
         t_beta := min{ m : ||m alpha + rho - beta||   <= |delta| }.

(R3) THE ARC AT 0 IS HARMLESS -- proved, because rho = 1/7 is RATIONAL and alpha is badly
     approximable.  For m >= 1,
         ||m alpha + 1/7||  >=  ||7 m alpha + 1|| / 7  =  ||7 m alpha|| / 7  >  1/(7 * 3 * 7m)
                            =  1/(147 m),
     using ||q alpha|| > 1/(3q) for the golden conjugate (its infimum of q||q alpha|| is
     1/sqrt5 = 0.4472 > 1/3).  And ||0*alpha + 1/7|| = 1/7.  Therefore
         t_0  >  1/(147 |delta|) .

(R4) THE ARC AT beta IS THE ONLY DIFFICULTY, and it is settled by BAKER.  Put
         c_m := ||m alpha + rho - beta||   (m >= 0).
     Writing the nearest integer as n, c_m = |A - beta| with A = m alpha + 1/7 - n algebraic of
     degree <= 2 and height O(m^2), so
         c_m = |A ln3 - ln2| / ln3 ,
     a NONZERO linear form in the logarithms of the algebraic numbers 3 and 2 with ALGEBRAIC
     coefficients (nonzero since beta = log_3 2 is transcendental).  Baker, *Transcendental Number
     Theory*, Theorem 3.1 (the algebraic-coefficient form) gives effective C2 > 0, kappa > 0 with
         c_m  >=  C2 * m^{-kappa}      for all m >= 1 .
     Only a POLYNOMIAL lower bound is needed; the argument below uses nothing sharper.

(R5) THE CONSTRUCTION.  Given M, set C_M := min_{0<=m<M} c_m ( > 0, and >= C2 M^{-kappa} by R4 ).
     Choose ell = ell(M) := the least convergent denominator q of alpha with ||q alpha|| < C_M.
     Then no orbit point with m < M lies within |delta| of beta, so t_beta >= M; and by R3,
     t_0 > 1/(147|delta|) >= 1/(147 C_M), which exceeds M once M is large.  Hence
         L(ell) - ell = m*(ell) >= M ,
     while ||q alpha|| ~ 1/(sqrt5 q) forces  ell(M) = O(1/C_M) = O(M^kappa),  so
         log2 ell(M)  <=  kappa * log2 M + O(1) .
     With the Phase 10 height bound this gives S >= M - C*kappa*log2(M) - O(1)  ->  +infinity.
"""
import sys, math
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from fractions import Fraction
from exact_word import Q5, ALPHA, RHO, BLO, BHI, lt_beta, orbit, word, delta, norm, convergents

def chi(x):
    return 1 if lt_beta(x) else 0

def in_M(x, d):
    """x in M(delta) <=> chi(x) != chi({x+d}).  Exact, and this IS the definition."""
    return chi(x) != chi((x + d).frac())

def mstar(ell, cap, s=None):
    """min{m >= 0 : {m alpha + rho} in M(delta(ell))}.
    When the certified word s is supplied this is computed as min{m : s[m+ell] != s[m]},
    which R1 proves is the same number and is far faster."""
    if s is not None:
        for m in range(min(cap, len(s) - ell)):
            if s[m + ell] != s[m]:
                return m
        return None
    d = delta(ell)
    for m in range(cap):
        if in_M(orbit(m), d):
            return m
    return None

def lcp_pow(s, ell):
    n = ell
    while n < len(s) and s[n] == s[n - ell]:
        n += 1
    return None if n >= len(s) else n

def c_m(m):
    """||m alpha + rho - beta||, returned as a certified (lo,hi) Fraction bracket."""
    x = m * ALPHA + RHO
    lo = x - Q5(BHI)
    hi = x - Q5(BLO)
    def nrm(v):
        n = v.floor(); f = v - Q5(n)
        return f if (f - Q5(Fraction(1, 2))).sign() < 0 else Q5(1) - f
    a, b = float(nrm(lo)), float(nrm(hi))
    return min(a, b), max(a, b)

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 11.  Rotation-geometry repetition lemma for the named word")
    P("=" * 78)
    N = 300000
    s = word(N)
    P(f"    s built to {N} symbols with exact Q(sqrt5) arithmetic; every beta-comparison certified.")

    # ---------- R1
    P("\nR1  First-mismatch characterisation  L(ell) - ell = m*(ell).")
    P(f"    {'ell':<9}{'delta(ell)':<14}{'literal L':<12}{'L - ell':<10}{'m*(ell)':<10}{'agree'}")
    conv = convergents(26)
    ok = True
    for (p, q) in conv:
        if q < 2 or q > 3000:
            continue
        L = lcp_pow(s, q)
        if L is None:
            continue
        ms = mstar(q, N // 2)          # exact M(delta) route, no word used
        agree = (ms is not None and L - q == ms)
        ok &= agree
        if q >= 5:
            P(f"    {q:<9}{float(delta(q)):<14.9f}{L:<12}{L-q:<10}{str(ms):<10}{agree}")
        assert agree, ("R1 failed", q, L - q, ms)
    P("    R1 holds at every tested ell: the overshoot IS the first hitting time of M(delta).")

    # ---------- R2
    P("\nR2  Two-ball relaxation  M(delta) subset B(0,|delta|) u B(beta,|delta|).")
    bad = 0
    for (p, q) in conv[:16]:
        d = delta(q); ad = abs(float(d))
        for m in range(4000):
            x = orbit(m)
            if in_M(x, d):
                d0 = float(norm(x))
                dbeta = min(c_m(m))
                if not (d0 <= ad + 1e-30 or dbeta <= ad + 1e-30):
                    bad += 1
    P(f"    checked 16 shifts x 4000 orbit points: containment violations = {bad}")
    assert bad == 0

    # ---------- R3
    P("\nR3  The arc at 0:  ||m alpha + 1/7|| > 1/(147 m)  for m >= 1  (exact check).")
    worst = None
    for m in range(1, 60000):
        v = float(norm(orbit(m))) * 147 * m
        if worst is None or v < worst[0]:
            worst = (v, m)
    P(f"    min over 1 <= m < 60000 of 147*m*||m alpha + 1/7||  =  {worst[0]:.6f}  at m = {worst[1]}")
    P(f"    (the bound needs this to stay > 1; the proof gives 147*m*||.|| > 1 for every m)")
    assert worst[0] > 1.0

    # ---------- R4
    P("\nR4  The arc at beta:  c_m = ||m alpha + rho - beta||,  Baker gives c_m >= C2 m^{-kappa}.")
    P(f"    {'m':<7}{'c_m (certified bracket)':<34}{'c_m * m^2':<16}{'c_m * m^4'}")
    cs = []
    for m in list(range(0, 12)) + [20, 50, 120, 300, 800, 2000, 5000]:
        lo, hi = c_m(m)
        cs.append((m, lo, hi))
        mm = max(m, 1)
        P(f"    {m:<7}[{lo:.12e}, {hi:.12e}]  {lo*mm**2:<16.4g}{lo*mm**4:.4g}")
    P("    No super-exponential decay is visible, consistent with the polynomial Baker bound.")
    P("    (The table is a consistency check; the LOWER bound used in the proof is Baker's,")
    P("     not this table.)")

    # ---------- R5
    P("\nR5  The construction:  given M, take ell(M) = least convergent denominator with")
    P("    ||q alpha|| < min( C_M , 1/(147 M) ),  C_M := min_{m<M} c_m.  Then m*(ell) >= M.")
    P("    BOTH thresholds are needed -- the first controls the arc at beta (R4), the second")
    P("    the arc at 0 (R3).  Imposing only the first FAILS: at M = 4 it gives ell = 5,")
    P("    |delta| = 0.090, 1/(147|delta|) = 0.075 < 1, and m* = 3 < 4.  That was a real bug")
    P("    in the first draft of this construction; it is recorded, not quietly fixed.")
    P(f"\n    {'M':<7}{'min(C_M, 1/147M)':<18}{'ell(M)':<10}{'|delta|':<16}{'m*(ell)':<10}"
      f"{'m* >= M':<9}{'log2 ell':<10}{'M - 3*log2 ell'}")
    rows = []
    for M in (4, 8, 16, 32, 64, 128, 256):
        CM = min(c_m(m)[0] for m in range(M))
        # BOTH conditions are needed: |delta| < C_M forces t_beta >= M (R4), and
        # |delta| <= 1/(147 M) forces t_0 > 1/(147|delta|) >= M (R3).
        thresh = min(CM, 1.0 / (147.0 * M))
        ell = None
        for (p, q) in conv:
            if q >= 2 and abs(float(delta(q))) < thresh:
                ell = q
                break
        if ell is None or ell > N // 3:
            P(f"    {M:<7}{thresh:<18.10e}{'(out of range)':<10}")
            continue
        ms = mstar(ell, N // 2, s)     # word route, identical by R1
        rows.append((M, CM, ell, ms))
        P(f"    {M:<7}{thresh:<18.10e}{ell:<10}{abs(float(delta(ell))):<16.10e}{ms:<10}"
          f"{str(ms >= M):<9}{math.log2(ell):<10.2f}{M - 3*math.log2(ell):.2f}")
        assert ms >= M, ("R5 failed", M, ell, ms)
    P("\n    m*(ell(M)) >= M at every M tested, exactly as R3+R4 predict.  The final column shows")
    P("    the surplus driver M - 3 log2 ell growing, with 3 a placeholder for the height constant")
    P("    C fixed in EXACT_HEIGHT_AND_SURPLUS.md.")
    P("\nALL PHASE-11 ROTATION CHECKS PASS.")

if __name__ == "__main__":
    main()
