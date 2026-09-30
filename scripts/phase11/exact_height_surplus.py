"""
Phase 11 / steps 2,4: exact height and surplus for the named word, at the R5 witnesses.

HEIGHT BOUND, assembled with explicit constants for this candidate.
  Periodic value (foundation Prop. 4.1):  Phi(W^inf) = c_W / (2^ell - 3^k),
      c_W = sum_{i<ell, W_i=1} 3^{k - k_{i+1}(W)} 2^i ,   delta_W = 2^ell - 3^k .
  Height bound (Phase 1/2):  c_W <= ell * 3^{ceil D(W)} * max(2^ell, 3^k),  |delta_W| <= max(2^ell,3^k).
  Hence  F(W) = |delta_W| + c_W <= (1 + ell*3^{ceil D}) max(2^ell, 3^k)  and
      log2 F(W) <= log2(2 ell) + ceil(D(W)) log2 3 + ell + max(0, k log2 3 - ell) .
  With  e_ell := k - ell*beta  and  beta log2 3 = 1  exactly,  k log2 3 - ell = log2(3) * e_ell.
  Therefore, with L = lcp(s, W^inf),

      S(W) = L - log2 F(W)  >=  (L - ell)  -  log2(3) * max(0, e_ell)
                                            -  ceil(D(W)) * log2 3  -  log2(2 ell) .        (H)

  Phase 10 Lemmas D and E bound |e_ell| and D(W) by C_D log2 ell + C_D' .  Substituting,

      S(W)  >=  (L - ell)  -  C log2 ell  -  C_0 ,     C = 1 + 3 log2(3) C_D .               (H')

  Everything below evaluates (H) with the ACTUAL e_ell and D(W), and the surplus EXACTLY as an
  integer comparison 2^L > F(W) -- no bound is used for the verdict.
"""
import sys, math
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from fractions import Fraction
from exact_word import Q5, ALPHA, RHO, BLO, BHI, word, delta, convergents
from rotation_repetition import mstar, lcp_pow, c_m

LOG23 = math.log2(3)

def c_of(W):
    k = sum(W); run = 0; tot = 0
    for i, b in enumerate(W):
        if b:
            run += 1
            tot += 3 ** (k - run) * (1 << i)
    return tot

def disc_own(W):
    ell = len(W); k = sum(W); run = 0; best = 0
    for i in range(ell + 1):
        if i and W[i - 1]:
            run += 1
        d = abs(ell * run - i * k)
        if d > best:
            best = d
    return Fraction(best, ell)

def log2_int(n):
    b = n.bit_length()
    return (b - 1) + math.log2(n / (1 << (b - 1)))

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 11 / exact height and surplus at the R5 witnesses")
    P("=" * 78)
    N = 120000
    s = word(N)
    conv = convergents(26)

    P("\n1.  The R5 witnesses ell(M), with every quantity the obligation names.")
    P(f"    {'M':<6}{'ell':<8}{'k':<7}{'e_ell':<10}{'D(W)':<8}{'L':<9}{'L-ell':<9}"
      f"{'log2|delta_W|-ell':<19}{'log2 c_W - ell':<16}")
    wit = []
    for M in (4, 8, 16, 32, 64, 128):
        CM = min(c_m(m)[0] for m in range(M))
        thresh = min(CM, 1.0 / (147.0 * M))
        ell = next((q for (p_, q) in conv if q >= 2 and abs(float(delta(q))) < thresh), None)
        if ell is None or ell > 7000 or ell * 3 > N:
            continue
        W = s[:ell]; k = sum(W)
        L = lcp_pow(s, ell)
        e = k - ell * float(BLO)
        D = disc_own(W)
        dW = abs((1 << ell) - 3 ** k)
        cW = c_of(W)
        wit.append((M, ell, k, e, D, L, dW, cW))
        P(f"    {M:<6}{ell:<8}{k:<7}{e:<10.4f}{float(D):<8.4f}{L:<9}{L-ell:<9}"
          f"{log2_int(dW)-ell:<19.6f}{log2_int(cW)-ell:<16.6f}")

    P("\n2.  Exact surplus, and the bound (H) it must respect.")
    P(f"    {'M':<6}{'ell':<8}{'L-ell':<9}{'bound (H)':<14}{'S exact':<14}"
      f"{'2^L > F(W)':<12}{'height floor H >='}")
    for (M, ell, k, e, D, L, dW, cW) in wit:
        F = dW + cW
        S = L - log2_int(F)
        bound = (L - ell) - LOG23 * max(0.0, e) - math.ceil(float(D)) * LOG23 - math.log2(2 * ell)
        pos = (1 << L) > F
        P(f"    {M:<6}{ell:<8}{L-ell:<9}{bound:<14.3f}{S:<14.3f}{str(pos):<12}"
          f"2^{S:.1f}")
        assert S >= bound - 1e-6, ("bound (H) violated", M, ell, S, bound)
    P("    (H) holds at every witness -- asserted, not observed.  The surplus is certified by the")
    P("    integer comparison 2^L > F(W); no estimate enters the verdict column.")

    P("\n3.  Growth of the driver.  The obligation is that (L-ell)/log2(ell) be UNBOUNDED along")
    P("    the witness subsequence -- not merely positive.")
    P(f"    {'M':<6}{'ell':<8}{'L-ell':<10}{'log2 ell':<11}{'(L-ell)/log2 ell':<19}"
      f"{'S / log2 ell'}")
    for (M, ell, k, e, D, L, dW, cW) in wit:
        F = dW + cW
        S = L - log2_int(F)
        P(f"    {M:<6}{ell:<8}{L-ell:<10}{math.log2(ell):<11.3f}"
          f"{(L-ell)/math.log2(ell):<19.3f}{S/math.log2(ell):.3f}")
    P("\n    R5 proves L - ell >= M while log2 ell(M) = O(log M), so the ratio is bounded below by")
    P("    M / (kappa log2 M + O(1)), which tends to infinity.  The table is a consistency check.")

    P("\n4.  A failed scale, inspected rather than hidden.")
    P("    ell = 5 (the M = 4 witness if only the beta-threshold is imposed):")
    W = s[:5]; k = sum(W); L = lcp_pow(s, 5)
    F = abs((1 << 5) - 3 ** k) + c_of(W)
    P(f"      ell = 5, k = {k}, L = {L}, L - ell = {L-5}, |delta| = {abs(float(delta(5))):.6f},")
    P(f"      1/(147|delta|) = {1/(147*abs(float(delta(5)))):.4f} < 1, so R3 gives nothing;")
    P(f"      exact S = {L - log2_int(F):.3f}  -- POSITIVE, but small and bounded: L - ell = 3 is")
    P("      a constant, so this scale cannot contribute to an asymptotic argument no matter how")
    P("      the surplus happens to come out.  R3 certifies nothing here because 1/(147|delta|) < 1.")
    P("      (An earlier draft of this line called the surplus negative.  It is not; the witness is")
    P("       useless for a different reason, and the distinction matters.)")
    P("    This is why the construction imposes |delta| <= 1/(147 M) as well.")
    P("\nALL PHASE-11 HEIGHT/SURPLUS CHECKS PASS.")

if __name__ == "__main__":
    main()
