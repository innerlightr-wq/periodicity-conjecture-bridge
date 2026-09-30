"""Phase 14 / item 3.  Explicit C, C_0 and f(M) for alpha = (sqrt5-1)/2, rho = 1/7.

The discrepancy input is Kuipers-Niederreiter, *Uniform Distribution of Sequences*, Chapter 2,
Theorem 3.4, read first-hand:

    Suppose the irrational a = [a_0; a_1, a_2, ...] has bounded partial quotients, say a_i <= K
    for i >= 1.  Then the discrepancy D_N(w) of w = (n a) satisfies N D_N(w) = O(log N).  More
    exactly,                                                                            (3.16)
        N D_N(w)  <=  3 + ( 1/log(phi) + K/log(K+1) ) log N ,      phi = (1+sqrt5)/2 .

(Natural logarithms; D_N is the EXTREME discrepancy.  The theorem is credited there to
Niederreiter, improving Ostrowski.)  Everything below is derived from (3.16) and checked.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "phase12"))
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
from qfield import Q, cf, chi, dist_to_int, BLO, BHI

getcontext().prec = 80
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

D5 = 5
ALPHA = Q(Fr(-1, 2), Fr(1, 2), D5)
RHO = Q(Fr(1, 7), 0, D5)
PHI = (1 + math.sqrt(5)) / 2
BETA = float(Decimal(2).ln() / Decimal(3).ln())
LOG23 = math.log2(3)

P("=" * 94)
P("PHASE 14 / item 3.  Explicit constants for alpha = (sqrt5-1)/2, rho = 1/7, interval [0,beta)")
P("=" * 94)

# ---------------------------------------------------------------- (A) the KN constant
K_pq = 1                                    # every partial quotient of the golden conjugate is 1
c_K = 1 / math.log(PHI) + K_pq / math.log(K_pq + 1)
P("\n(A) Kuipers-Niederreiter Ch.2 Thm 3.4, specialised.  All partial quotients are 1, so K = 1:")
P(f"    c_K := 1/ln(phi) + K/ln(K+1) = {1/math.log(PHI):.6f} + {K_pq/math.log(K_pq+1):.6f} = {c_K:.6f}")
P(f"    => N D_N({{n alpha}}) <= 3 + {c_K:.6f} ln N        (extreme discrepancy, unshifted)")

P("\n    VERIFICATION of that inequality, computed directly from the definition")
P("    D_N = max_i (i/N - x_(i)) + max_i (x_(i) - (i-1)/N)  on the sorted points x_(i) = {i*alpha}.")
P("    N        N*D_N        3 + c_K ln N     slack     ok")
def extreme_disc(pts):
    xs = sorted(pts); N = len(xs)
    a = max(Decimal(i + 1) / N - xs[i] for i in range(N))
    b = max(xs[i] - Decimal(i) / N for i in range(N))
    return a + b
al_d = Decimal(-1) / 2 + Decimal(5).sqrt() / 2
worst = None
for N in (10, 50, 200, 1000, 5000, 20000, 60000):
    pts = []
    x = Decimal(0)
    for n in range(1, N + 1):
        x = (x + al_d) % 1
        pts.append(x)
    nd = float(extreme_disc(pts) * N)
    bd = 3 + c_K * math.log(N)
    ok = nd <= bd
    worst = min(worst, bd - nd) if worst is not None else bd - nd
    P(f"    {N:<8} {nd:<12.6f} {bd:<16.6f} {bd-nd:<9.4f} {ok}")
    assert ok, N
P(f"    minimum slack over the tested range: {worst:.4f}  (the inequality is the cited theorem;")
P("     this table is a corroboration of the reading of (3.16), not a proof of it)")

# ------------------------------------------------- (B) from D_N to the prefix drift
P("\n(B) From (3.16) to the drift of OUR word.  Two adjustments, each stated and each safe:")
P("    (i) the intercept.  A(I;N) for ({m alpha + rho}) counts {m alpha} in I - rho, which mod 1")
P("        is one interval or two; two intervals cost two applications of D_N.  For rho = 1/7 the")
P("        set [0,beta) - 1/7 = [-1/7, beta-1/7) DOES wrap, so the factor 2 is used, not assumed away.")
P("    (ii) the index range.  KN counts n = 1..N; we count m = 0..N-1.  The symmetric difference is")
P("        one point, contributing at most 1.")
P("    Hence, with Delta(N) := max_{1<=i<=N} |k_i - i*beta| :")
C_D = 2 * c_K * math.log(2)          # a*ln N = (a*ln2)*log2 N -- MULTIPLY, not divide
C_Dp = 7.0
P(f"        Delta(N) <= 2(3 + c_K ln N) + 1 = 7 + {2*c_K:.6f} ln N = {C_D:.6f} log2(N) + 7.")
P(f"        (conversion: ln N = ln2 * log2 N, so the coefficient is 2*c_K*ln2 = {C_D:.6f}.)")
P(f"    So C_D = {C_D:.6f} and C_D' = {C_Dp:.1f}.")

P("\n    VERIFICATION against the actual word (exact counts, certified beta-bracket):")
P("    N        max|k_i - i beta|   C_D log2 N + 7   slack    ok")
W = []
def sym(m): return chi((Q(m, 0, D5) * ALPHA + RHO).frac())
def word(n):
    while len(W) < n: W.append(sym(len(W)))
    return W
NMAX = 60000
word(NMAX)
run = 0; best = []
mx_running = 0.0
checkpoints = {10, 100, 1000, 10000, 30000, 60000}
for i in range(1, NMAX + 1):
    run += W[i - 1]
    mx_running = max(mx_running, abs(run - i * BETA))
    if i in checkpoints:
        bd = C_D * math.log2(i) + C_Dp
        P(f"    {i:<8} {mx_running:<19.6f} {bd:<16.6f} {bd-mx_running:<8.4f} {mx_running <= bd}")
        assert mx_running <= bd

# ------------------------------------------- (C) the surplus inequality, with numbers
P("\n(C) The arithmetic surplus.  From theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md,")
P("    c_W <= ell * 3^ceil(D(W)) * max(2^ell, 3^k)  and  F(W) = |2^ell - 3^k| + c_W, so")
P("        log2 F(W) <= 1 + log2(ell) + ceil(D(W)) log2(3) + max(ell, k log2 3).")
P("    Since beta*log2(3) = 1 EXACTLY, with e_ell := k - ell*beta,")
P("        max(ell, k log2 3) = ell + log2(3) max(0, e_ell),")
P("    so  S(W) >= (L - ell) - log2(3) max(0,e_ell) - ceil(D(W)) log2(3) - log2(ell) - 1.")
P("    D(W) is the word's deviation from its OWN density k/ell; since")
P("        |k_i - i k/ell| <= |k_i - i beta| + |e_ell| <= 2 Delta(ell),")
P("    and |e_ell| <= Delta(ell), substituting Delta(ell) <= C_D log2 ell + C_D' gives")
C = 3 * C_D * LOG23 + 1
C0 = 3 * C_Dp * LOG23 + LOG23 + 1
P("")
P(f"        S(W) >= (L - ell) - C log2(ell) - C_0,     C = 3 C_D log2(3) + 1 = {C:.6f}")
P(f"                                                   C_0 = 3 C_D' log2 3 + log2 3 + 1 = {C0:.6f}")
P("")
P("    VERIFICATION against exactly computed surpluses at convergent denominators:")
P("    ell     k      L        S exact    (L-ell) - C log2 ell - C_0    holds")
def L_exact(ell):
    i = ell
    while True:
        word(i + 400)
        if W[i] != W[i % ell]: return i
        i += 1
def c_of(Wd):
    k = sum(Wd); c = 0; run = 0
    for i, b in enumerate(Wd):
        if b:
            run += 1; c += 3 ** (k - run) * 2 ** i
    return c, k
qs = cf(ALPHA, 40)[2]
for q in qs[4:16]:
    if q > 7000: break
    Wd = word(q + 10)[:q]; c, k = c_of(Wd)
    F = abs(2 ** q - 3 ** k) + c
    L = L_exact(q)
    S_exact = L - math.log2(F)
    rhs = (L - q) - C * math.log2(q) - C0
    P(f"    {q:<7} {k:<6} {L:<8} {S_exact:<10.3f} {rhs:<29.3f} {S_exact >= rhs}")
    assert S_exact >= rhs

# --------------------------------------- (D) the Waldschmidt side, audited
P("\n(D) Audit of the Waldschmidt estimate (Thm 10.1) as applied.")
P("    Form: Lambda_m = A_m log 3 - log 2, so n = 2 logarithms, alpha_1 = 3, alpha_2 = 2,")
P("    b_1 = A_m, b_2 = -1.   D = [Q(3,2,A_m,-1):Q] = [Q(A_m):Q] = 2 for m >= 1.")
lA1 = max(1.0, math.log(3), math.e * math.log(3) / 2)
lA2 = max(1.0, math.log(2), math.e * math.log(2) / 2)
c1 = (50 * 2) ** 6 * 2 ** 4 * lA1 * lA2
Bmin = (50 * 2 * 2 * max(lA1, lA2)) ** 6
P(f"    log A_1 = max(1, h(3), e|log 3|/D) = max(1, {math.log(3):.6f}, {math.e*math.log(3)/2:.6f}) = {lA1:.6f}")
P(f"    log A_2 = max(1, h(2), e|log 2|/D) = max(1, {math.log(2):.6f}, {math.e*math.log(2)/2:.6f}) = {lA2:.6f}")
P(f"    c_1 = (50n)^(3n) D^(n+2) log A_1 log A_2 = 100^6 * 2^4 * {lA1:.6f} * {lA2:.6f} = {c1:.6g}")
P(f"    B >= (50 n D log A)^(3n) = {Bmin:.6g}, i.e. log B >= {math.log(Bmin):.4f}")
P("")
P("    HEIGHT CONVENTION -- the one place the Phase 13 note was loose.  Waldschmidt's hypothesis is")
P("    log B >= h(1 : b_1 : ... : b_n) with h the ABSOLUTE LOGARITHMIC WEIL height, whereas")
P("    H(A_m) below is the CLASSICAL height (largest |coefficient| of the primitive minimal")
P("    polynomial).  The two are related by h(a) = (1/d) log M(P) and M(P) <= ||P||_2 <=")
P("    sqrt(d+1) H, so for d = 2,  h(A_m) <= (log H(A_m) + log sqrt 3)/2.  Also h(-1) = 0 and")
P("    h(1:b_1:b_2) <= h(b_1) + h(b_2).  Hence")
P("        h(1 : A_m : -1) <= (log H(A_m))/2 + 0.275 .")
P("    Phase 13 used log B = log H(A_m) + 2, which is LARGER, hence still admissible: both")
P("    hypotheses on B are lower bounds, and the conclusion is monotone decreasing in B, so")
P("    overestimating B is safe.  It is also wasteful by a factor of about 4 in the exponent;")
P("    the sharper choice is used from here on.")
P("")
P("    HEIGHT BOUND, proved rather than measured.  A_m = (a_m + 7m sqrt5)/14 with")
P("    a_m = -7m + 2 - 14 j_m and |j_m| <= m+2, so |a_m| <= 21m + 30, and the (not necessarily")
P("    primitive) minimal polynomial is 196 x^2 - 28 a_m x + (a_m^2 - 245 m^2).  For m >= 1:")
P("        196 <= 196 m^2,   28|a_m| <= 588m + 840 <= 1428 m^2,")
P("        |a_m^2 - 245 m^2| <= max((21m+30)^2, 245 m^2) <= 2601 m^2,")
P("    so  H(A_m) <= 2601 m^2  for every m >= 1.")
CH = 2601
P("    VERIFICATION (exact integer heights):")
def A_and_H(m):
    x = Q(m, 0, D5) * ALPHA + RHO
    j = round(x.approx() - BETA)
    a_m = -7 * m + 2 - 14 * j
    assert x - Q(j, 0, D5) == Q(Fr(a_m, 14), Fr(7 * m, 14), D5)
    if m == 0:
        return abs(a_m) or 1
    co = (196, -28 * a_m, a_m * a_m - 245 * m * m)
    g = math.gcd(math.gcd(abs(co[0]), abs(co[1])), abs(co[2]))
    return max(abs(c) // g for c in co)
mx = max(A_and_H(m) / m ** 2 for m in range(1, 20001))
P(f"    max H(A_m)/m^2 over 1 <= m <= 20000 : {mx:.2f}   (proved bound {CH}; the bound is not tight,")
P("     but it is proved, and a tighter measured value must not be substituted for a proof)")
assert mx <= CH

# --------------------------------------- (E) f(M)
P("\n(E) The explicit height bound f(M).")
P("    Starting-index restrictions, stated in full:")
P("      * M >= 2 (the construction quantifies over M >= 2);")
P("      * the witness ell(M) is a convergent denominator q_k with k >= 2, which is what makes")
P("        |delta| <= min(beta,1-beta) = 0.36907 hold (it fails at q_1 = 1);")
P("      * m ranges over 0 <= m < M; the bound H(A_m) <= 2601 m^2 is for m >= 1, and m = 0 is")
P("        handled explicitly by c_0 = ||1/7 - beta|| = 0.4880726107, no theorem needed;")
P("      * Baker/Waldschmidt is applied only for m >= 1, where deg A_m = 2 exactly.")
c0_exp = abs((RHO.approx() - BETA))
P(f"      * c_0 = {c0_exp:.10f}")
P("")
P("    t(M) := min( C_M, 1/(147 M) ),  C_M := min_{0<=m<M} c_m.  By (D),")
P("      C_M >= min( c_0, exp(-c_1 (log B_M)^2) / log 3 ) >= exp(-c_1 (log B_M)^2 - 1),")
P("      log B_M := max( log B_min, (log(2601 M^2))/2 + 0.275 ).")
P("    ell(M) < (A+1)/t(M) = 2/t(M), so")
P("      log2 ell(M) <= 1 + max( (c_1 (log B_M)^2 + 1)/ln 2, log2(147 M) ),")
P("    and finally")
P("")
P("      f(M) := M - C * [ 1 + max( (c_1 (log B_M)^2 + 1)/ln2, log2(147 M) ) ] - C_0 ,")
P(f"      C = {C:.6f},  C_0 = {C0:.6f},  c_1 = {c1:.6g},  log B_min = {math.log(Bmin):.4f}.")
P("")
def logB(M):
    return max(math.log(Bmin), math.log(CH * M * M) / 2 + 0.275)
def log2ell(M):
    lb = logB(M)
    return 1 + max((c1 * lb * lb + 1) / math.log(2), math.log2(147 * M))
def f(M):
    return M - C * log2ell(M) - C0
P("    M            log B_M     log2 ell(M)      f(M)")
for e in (1, 3, 6, 12, 17, 18, 19, 20, 25, 40):
    M = 10.0 ** e
    P(f"    1e{e:<11} {logB(M):<11.3f} {log2ell(M):<16.6g} {f(M):+.6g}")
lo, hi = 1e15, 1e25
while hi / lo > 1 + 1e-12:
    mid = math.sqrt(lo * hi)
    if f(mid) > 0: hi = mid
    else: lo = mid
M0 = hi
P("")
P(f"    CERTIFIED THRESHOLD:  f(M) > 0 for every integer M >= M_0 with M_0 = {M0:.6g}")
P(f"      (f is increasing beyond this point: f(M) - f(M/2) > 0 for all larger M, since M grows")
P(f"       linearly while log2 ell(M) grows like (log M)^2.)")
P(f"    At M = 1e20 the bound reads  H >= 2^{f(1e20):.6g}.")
assert f(M0 * 1.0001) > 0 and f(M0 * 0.999) < 0

# --------------------------------------- (F) the four height notions
P("")
P("    MONOTONICITY, proved rather than asserted.  On the branch where the Baker term dominates,")
P("      f(M) = M - (C c_1/ln2)(log B_M)^2 - C - C_0 - C/ln2,   log B_M = log(sqrt(2601) M) + 0.275,")
P("    so  f'(M) = 1 - 2 C c_1 (log B_M) / (M ln 2) > 0  as soon as  M > 2 C c_1 (log B_M)/ln 2.")
Mmono = 2 * C * c1 * logB(M0) / math.log(2)
P(f"    At M = M_0 that threshold is {Mmono:.4g} < M_0 = {M0:.6g}, so f is strictly increasing on")
P("    [M_0, infinity) and f(M) > 0 there.  Fine-grid check:")
bad = sum(1 for k in range(200) if f(M0 * (1.05 ** (k + 1))) <= f(M0 * (1.05 ** k)))
P(f"    non-increasing steps on a 1.05-ratio grid from M_0 over 200 steps: {bad}")
assert bad == 0 and Mmono < M0

P("\n(G) Parameter dependence (item 4).  What is uniform over the family and what is not.")
P("    Let A = max partial quotient of alpha, and D = [Q(alpha,rho):Q].")
P("    UNIFORM given A:   c_A = 1/ln(phi) + A/ln(A+1);  C_D = 2 c_A ln 2;  C = 3 C_D log2(3) + 1.")
P("    UNIVERSAL:         C_0 = 3*7*log2(3) + log2(3) + 1 = %.6f, independent of alpha and rho." % C0)
P("    UNIFORM given D:   c_1 = 100^6 D^4 log A_1 log A_2  with log A_i = max(1, ln a_i, e ln a_i / D).")
P("    NOT UNIFORM:       C_h in H(A_m) <= C_h m^D, and c_L in ||m alpha + rho|| >= c_L m^{-D^2},")
P("                       both of which depend on the actual alpha and rho.")
P("")
P("    A    c_A        C_D        C           |   D    c_1")
for A in (1, 2, 3, 5, 10):
    cA = 1 / math.log(PHI) + A / math.log(A + 1)
    CDa = 2 * cA * math.log(2); Ca = 3 * CDa * LOG23 + 1
    row = f"    {A:<4} {cA:<10.6f} {CDa:<10.6f} {Ca:<11.6f}"
    if A in (1, 2, 3, 5):
        Dd = {1: 2, 2: 3, 3: 4, 5: 6}[A]
        l1 = max(1.0, math.log(3), math.e * math.log(3) / Dd)
        l2 = max(1.0, math.log(2), math.e * math.log(2) / Dd)
        row += f" |   {Dd:<4} {(50*2)**6 * Dd**4 * l1 * l2:.6g}"
    P(row)
P("")
P("    CONSEQUENCE, stated plainly: C and C_0 ARE numerical for the whole family (C via A alone,")
P("    C_0 absolutely), and c_1 is numerical once D is fixed.  But f(M) is NOT uniformly numerical")
P("    for the family, because log B_M needs C_h and t(M) needs c_L, and neither is bounded over")
P("    all (alpha, rho) of a given (A, D).  For any SINGLE explicit (alpha, rho) both are a finite")
P("    computation, so f(M) is numerical case by case -- which is what was done above for the named")
P("    example, and is not claimed for the family.")

P("\n(F) Four different heights, which must not be conflated.")
P("    1. HEIGHTS OF THE APPROXIMANTS.  Phi(W^inf) = c_W/(2^ell - 3^k) is an actual rational that")
P("       matches s on a prefix of length L. Its height is about 2^ell. These exist, and are large,")
P("       and prove nothing by themselves.")
P("    2. THE HYPOTHETICAL VALUE.  The proof supposes Phi(s) = u/v with H = max(|u|,v) FIXED, then")
P("       derives a contradiction. The quantifier order matters: H is chosen before M.")
P("    3. PRACTICAL FINITE CERTIFICATES.  Exact integer comparisons 2^L > F(W) 2^S at computed")
P("       witnesses: H >= 2^462, 2^838, 2^872, 2^2469, 2^15998.  No analytic input; these are the")
P("       only numerically useful floors.")
P("    4. THE THEORETICAL THRESHOLD.  f(M) above.  It first turns positive near M_0 = %.3g, at a" % M0)
P("       witness length of about 2^%.4g -- entirely beyond computation, and worth nothing" % log2ell(M0))
P("       numerically.  Its value is that it is written down rather than merely 'effective'.")
P("    Rows 3 and 4 answer different questions and neither improves the other.")

P("\nALL PHASE-14 EXPLICIT-CONSTANT CHECKS PASS.")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
     "data", "phase14", "explicit_constants_output.txt"), "w").write("\n".join(out) + "\n")
