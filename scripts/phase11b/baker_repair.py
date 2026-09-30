"""
Phase 11B: repair of Theorem 11's analytic dependency.

WITHDRAWN.  Phase 11 asserted  c_m >= C2 * m^{-kappa}  ("polynomial"), citing Baker,
*Transcendental Number Theory*, Thm 3.1.  That is NOT what the source gives for ALGEBRAIC
coefficients.  The correct statement, read first-hand:

  Baker, "Linear forms in the logarithms of algebraic numbers III", Mathematika 14 (1967),
  THEOREM 2.  Let alpha_1,...,alpha_n and beta_1,...,beta_n be non-zero algebraic numbers.
  Suppose that either log alpha_1,...,log alpha_n or beta_1,...,beta_n are linearly independent
  over the rationals.  Suppose further that kappa > n, and let d and B denote respectively the
  maximum of the degrees and heights of beta_1,...,beta_n.  Then
                | beta_1 log alpha_1 + ... + beta_n log alpha_n |  >  C e^{-(log B)^kappa}
  for an effectively computable C = C(n, alpha_1,...,alpha_n, kappa, d) > 0.

So the justified bound is STRETCHED EXPONENTIAL IN log B, not polynomial in B.  This script
verifies that the repaired argument still closes, and checks every quantity it needs.
"""
import sys, math
sys.path.insert(0, "/home/elias/scratch/phase11-bridge/scripts/phase11")
from fractions import Fraction
from exact_word import Q5, ALPHA, RHO, BLO, BHI, word, delta, convergents, lt_beta
from rotation_repetition import mstar, lcp_pow, c_m

def A_height(m):
    """A_m = m*alpha + 1/7 - j_m = (a + b sqrt5)/14 with b = 7m.  Classical height of A_m
    = max|coeff| of its minimal polynomial 196 x^2 - 28 a x + (a^2 - 5 b^2)."""
    x = m * ALPHA + RHO
    beta_mid = (BLO + BHI) / 2
    j = (x - Q5(beta_mid)).floor()
    for cand in (j, j + 1):
        v = x - Q5(cand)
        if abs(float(v) - float(Q5(beta_mid))) <= 0.5 + 1e-12:
            j = cand
    A = x - Q5(j)                       # = (a + b sqrt5)/14
    a = A.a * 14; b = A.b * 14
    assert a.denominator == 1 and b.denominator == 1, (a, b)
    a, b = int(a), int(b)
    return max(196, 28 * abs(a), abs(a * a - 5 * b * b)), a, b, j

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 11B.  Repair of the analytic dependency")
    P("=" * 78)

    P("\n1.  A_m: explicit form, uniform degree and height bounds.")
    P("    A_m = m*alpha + 1/7 - j_m,  alpha = (sqrt5-1)/2,  j_m = nearest integer to m*alpha+1/7-beta.")
    P("    Writing over the common denominator 14:  A_m = (a_m + 7m*sqrt5)/14,  a_m = -7m + 2 - 14 j_m.")
    P("    deg A_m = 2 for every m >= 1 (A_m irrational); deg A_0 = 1.  Minimal polynomial of")
    P("    A_m (m>=1): 196 x^2 - 28 a_m x + (a_m^2 - 5*(7m)^2), so the classical height is")
    P("    H(A_m) = max(196, 28|a_m|, |a_m^2 - 245 m^2|) = O(m^2).")
    P(f"\n    {'m':<8}{'a_m':<12}{'b_m=7m':<10}{'H(A_m)':<16}{'H(A_m)/m^2':<14}{'A_m != 0'}")
    worst = 0
    for m in (0, 1, 2, 5, 20, 100, 1000, 10000):
        H, a, b, j = A_height(m)
        mm = max(m, 1)
        worst = max(worst, H / mm ** 2)
        Anz = not (a == 0 and b == 0)
        P(f"    {m:<8}{a:<12}{b:<10}{H:<16}{H/mm**2:<14.2f}{Anz}")
        assert Anz
    P(f"    H(A_m) <= {worst:.0f} * m^2 on the sample; the closed form above gives H(A_m) = O(m^2)")
    P("    unconditionally, so  log H(A_m) = 2 log m + O(1).")

    P("\n2.  Nonvanishing of Lambda_m = A_m log 3 - log 2, and the m = 0 case.")
    P("    Lambda_m = 0 would give log_3 2 = A_m, an algebraic number -- contradicting the")
    P("    transcendence of log_3 2 (Gelfond-Schneider).  So Lambda_m != 0 for EVERY m >= 0,")
    P("    including m = 0 where A_0 = 1/7 - j_0 is rational and nonzero.")
    P("    Baker's Theorem 2 hypotheses, checked: alpha_1 = 3, alpha_2 = 2 are non-zero algebraic;")
    P("    beta_1 = A_m != 0 and beta_2 = -1 != 0 are algebraic; and log 3, log 2 are linearly")
    P("    independent over Q (a log2 + b log3 = 0 with (a,b) != 0 rational forces 2^a = 3^{-b}).")
    P("    So Theorem 2 applies with n = 2, any kappa > 2, d = 2:")
    P("        c_m = |Lambda_m| / log 3  >  (C/log 3) * exp( -(log H(A_m))^kappa )")
    P("            >=  exp( -c_1 * (log(m+2))^kappa )        for effective c_1 and any fixed kappa > 2.")
    P("    THIS IS THE STRONGEST BOUND THE SOURCE SUPPORTS.  The polynomial form is withdrawn.")

    P("\n3.  C_M and the witness size, with bounded consecutive denominator ratios.")
    P("    C_M := min_{0<=m<M} c_m  >=  exp( -c_1 (log(M+2))^kappa ).")
    P("    For alpha = (sqrt5-1)/2 the convergent denominators are Fibonacci, so")
    P("        q_{k+1} = q_k + q_{k-1} <= 2 q_k     (bounded ratio, used explicitly below),")
    P("    and the classical two-sided estimate 1/(q_{k+1}+q_k) < ||q_k alpha|| < 1/q_{k+1} holds.")
    P("    Let t := min(C_M, 1/(147 M)) and let ell(M) = q_k be the LEAST convergent denominator")
    P("    with ||q_k alpha|| < t.  Minimality gives ||q_{k-1} alpha|| >= t, and ||q_{k-1} alpha||")
    P("    < 1/q_k, hence")
    P("        ell(M) = q_k  <  1/t  =  max( 1/C_M , 147 M ) .")
    P("    Also ||q_k alpha|| > 1/(q_{k+1}+q_k) >= 1/(3 q_k), so t > 1/(3 ell(M)), i.e.")
    P("        ell(M)  >  1/(3t)  >=  147 M / 3  =  49 M   ->   infinity .")
    P("    Since kappa > 2, exp(c_1 (log(M+2))^kappa) eventually exceeds 147M, so for large M")
    P("        log ell(M)  <=  c_1 (log(M+2))^kappa ,   i.e.   log ell(M) = O( (log(M+2))^kappa ).")
    P("    A POLYNOMIAL bound on C_M is NOT needed for this.")
    P(f"\n    Verification of the two denominator facts used:")
    conv = convergents(30)
    ratio_ok = all(conv[i+1][1] <= 2 * conv[i][1] for i in range(len(conv) - 1))
    two_sided = True
    for i in range(1, len(conv) - 1):
        q, qn = conv[i][1], conv[i+1][1]
        nq = abs(float(delta(q)))
        if not (1.0/(qn + q) < nq < 1.0/qn):
            two_sided = False
    P(f"      q_(k+1) <= 2 q_k for all tested k : {ratio_ok}")
    P(f"      1/(q_(k+1)+q_k) < ||q_k alpha|| < 1/q_(k+1) : {two_sided}")
    assert ratio_ok and two_sided

    P("\n4.  The height penalty is o(M), so S -> infinity.")
    P("    (H') gives  S >= (L - ell) - C log2(ell) - C_0  with C, C_0 absolute for this alpha.")
    P("    R5 gives L - ell >= M, and step 3 gives log2 ell(M) <= (c_1/ln2)(log(M+2))^kappa.  So")
    P("        S  >=  M  -  (C c_1/ln 2) (log(M+2))^kappa  -  C_0 .")
    P("    For any FIXED kappa, (log(M+2))^kappa / M -> 0, so the penalty is o(M) and S -> +infinity.")
    P(f"\n    {'M':<10}{'(log(M+2))^3':<16}{'penalty/M  (C c_1/ln2 = 1)':<28}{'M - penalty'}")
    for M in (10**2, 10**3, 10**6, 10**12, 10**30, 10**100):
        pen = (math.log(M + 2)) ** 3
        P(f"    {('1e%d' % round(math.log10(M))):<10}{pen:<16.4g}{pen/M:<28.4g}{M - pen:.6g}")
    P("    The ratio falls to 0; the third column is the entire content of 'o(M)'.")

    P("\n5.  What survives WITHOUT Baker: the finite height certificates.")
    P("    The certificates H >= 2^S at the computed witnesses are exact integer facts")
    P("    (2^L > F(W)) and use NO analytic input at all.  Baker is needed only to know that")
    P("    the family continues for every M, i.e. for the asymptotic conclusion.")
    P("\nALL PHASE-11B CHECKS PASS.")

if __name__ == "__main__":
    main()
