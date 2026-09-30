"""Phase 13 / item 5.  An EXPLICIT algebraic-coefficient estimate, and what it costs.

Source, read first-hand (Waldschmidt, *Linear independence of logarithms of algebraic numbers*,
Theorem 10.1; the book version is Diophantine Approximation on Linear Algebraic Groups,
Grundlehren 326, Springer 2000):

  l_1,...,l_m logarithms of algebraic numbers, a_i = exp(l_i); b_1,...,b_m ALGEBRAIC;
  D = [Q(a_1..a_m, b_1..b_m) : Q];  A_1,...,A_m, B real >= e with
      log A_i >= h(a_i),   D log A_i >= e |l_i|,   log B >= h(1 : b_1 : ... : b_m),
      B >= (50 m D log A)^{3m},   A = max A_i .
  If  Lambda = b_1 l_1 + ... + b_m l_m  is non-zero then
      |Lambda| > exp{ -(50m)^{3m} D^{m+2} (log B)^2 log A_1 ... log A_m } .

Note the exponent on log B is exactly 2 -- BETTER than Baker 1967's kappa > 2, and still NOT
polynomial in B.  A polynomial bound is exactly Baker's own conjecture "kappa = 1", unproved.
"""
import math
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

L3, L2 = math.log(3), math.log(2)
E = math.e

P("=" * 96)
P("PHASE 13 / item 5.  Explicit constant for  Lambda_m = A_m log 3 - log 2,  A_m algebraic")
P("=" * 96)
P("")
P("Hypothesis check, m = 2, a_1 = 3, a_2 = 2, b_1 = A_m, b_2 = -1:")
P("  a_1, a_2 non-zero algebraic                                  : yes (rational integers)")
P("  b_1 = A_m non-zero  (A_m > beta - 1/2 = 0.13093 > 0)         : yes, Phase 12/13")
P("  b_2 = -1 non-zero algebraic                                  : yes")
P("  Lambda_m != 0   (else log_3 2 = A_m algebraic)               : yes, Gelfond-Schneider")
P("  h(3) = log 3 = %.6f ;  h(2) = log 2 = %.6f  (Weil height of a rational integer n is log n)" % (L3, L2))
P("  |l_1| = log 3, |l_2| = log 2")
P("  D = [Q(A_m) : Q] = [Q(alpha, rho) : Q]   (2 and 3 are rational, so they add nothing)")
P("")
P("  D    log A_1 (>=max(1,h(3),e log3/D))  log A_2   c_1 = (50m)^{3m} D^{m+2} logA_1 logA_2")
rows = []
for D in (2, 3, 4, 6):
    lA1 = max(1.0, L3, E * L3 / D)
    lA2 = max(1.0, L2, E * L2 / D)
    c1 = (50 * 2) ** 6 * D ** 4 * lA1 * lA2
    Bmin = (50 * 2 * D * max(lA1, lA2)) ** 6
    rows.append((D, lA1, lA2, c1, Bmin))
    P(f"  {D:<4} {lA1:<37.6f} {lA2:<9.6f} {c1:.6g}   (B >= {Bmin:.4g}, log B >= {math.log(Bmin):.3f})")
P("")
P("So, with  log B_m := max( log B_min , log H(A_m) + 2 )  and  H(A_m) <= C_h m^D :")
P("")
P("    c_m = |Lambda_m| / log 3  >  exp( -c_1 (log B_m)^2 ) / log 3 ,      c_1 EXPLICIT above.")
P("")
P("The witness bound and the price.  log ell(M) <= max( c_1 (log B_M)^2 , D^2 log M ) + O(1), and")
P("the surplus is  S >= M - (C/ln2) log ell(M) - C_0.  Taking C = 1 (optimistic, for orientation")
P("only -- the true C also needs the Kuipers-Niederreiter constants) the surplus turns positive at")
P("roughly the M solving  M = 1.45 * c_1 (log B_M)^2 :")
P("")
P("  D    c_1          M where M = 1.45 c_1 (log B_M)^2   log10 ell(M) there")
for D, lA1, lA2, c1, Bmin in rows:
    lBmin = math.log(Bmin)
    M = 10.0
    for _ in range(400):
        lB = max(lBmin, D * math.log(M) + 2 + math.log(200.0))
        M = 1.45 * c1 * lB * lB
    lB = max(lBmin, D * math.log(M) + 2 + math.log(200.0))
    P(f"  {D:<4} {c1:<12.4g} {M:<34.6g} {c1*lB*lB/math.log(10):.4g}")
P("")
P("READING.  The constant is explicit but astronomical: the first M at which the *effective*")
P("argument yields a positive surplus is around 10^17, at a witness length ell of about")
P("10^(2*10^13) -- utterly beyond computation.  So the explicit route does NOT produce usable")
P("numbers; it produces a WRITTEN-DOWN bound where previously there was only 'effectively")
P("computable in principle'.  The five finite certificates (H >= 2^462 ... 2^15998) remain the")
P("only numerically useful height floors, and they are Baker-free.")
P("")
P("WHAT IS AND IS NOT SETTLED ABOUT THE SHAPE:")
P("  Baker 1967 (III, Thm 2)            : exp(-C (log B)^kappa), kappa > 2, C not supplied")
P("  Waldschmidt Thm 10.1               : exp(-c_1 (log B)^2),   c_1 SUPPLIED (above)")
P("  polynomial, i.e. B^{-C}            : equivalent to kappa = 1, which is BAKER'S OWN")
P("                                       CONJECTURE (MR0220680: 'It is conjectured that")
P("                                       Theorems 3.1 and 3.2 essentially hold with k = 1').")
P("                                       NOT available.  Phase 12's hope that fixed degree")
P("                                       might give a polynomial bound is therefore NOT")
P("                                       supported by the literature, and is withdrawn.")
P("")
P("NO VALID REDUCTION TO INTEGER COEFFICIENTS EXISTS.  Clearing denominators in")
P("  q * Lambda_m = (qm)(alpha log 3) + (p - q j_m) log 3 - q log 2      (rho = p/q)")
P("gives integer coefficients, but the first logarithm is  alpha log 3 = log(3^alpha), and 3^alpha")
P("is TRANSCENDENTAL by Gelfond-Schneider (alpha algebraic irrational).  Linear-forms-in-logarithms")
P("theorems require algebraic arguments, so Laurent-Mignotte-Nesterenko and Baker-Wustholz do not")
P("apply, with or without clearing denominators.")
P("")
P("PHASE-13 EXPLICIT-CONSTANT COMPUTATION COMPLETE.")
import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
     "data", "phase13", "explicit_constants_output.txt"), "w").write("\n".join(out) + "\n")
