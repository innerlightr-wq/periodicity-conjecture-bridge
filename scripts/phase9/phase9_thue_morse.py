"""
Phase 9, step H2: the Thue-Morse word.  The repository's standing structural-ceiling claim
(theorems/phase1/FULL_PERIODICITY_GAP.md Q4, repeated in LADDER.md, THEOREM_STATUS.md and the
deposited note) says Thue-Morse has no initial square, hence "every purely repetition-based
method" is structurally inapplicable to it.

The first half is true.  The conclusion does not follow, because the criterion's threshold is
g(gamma) = max(1, gamma log2 3) + gamma(1-gamma) log2 3, and g(1/2) = 1.39624 < 5/3.

Facts, each checked exactly below:
  F1  t := Thue-Morse = mu^inf(0), mu(0) = 01, mu(1) = 10.  W_0 := t[0:24] has
      lcp(t, W_0^inf) = 40, i.e. prefix power exactly 5/3, and |W_0|_1 = 12 (density 1/2).
  F2  mu is 2-uniform, mu(t) = t, and mu(0), mu(1) differ in their first letter, so
      lcp(mu(x), mu(y)) = 2 lcp(x, y) exactly.  Hence W_m := mu^m(W_0) satisfies
      |W_m| = 24*2^m,  |W_m|_1 = 12*2^m,  lcp(t, W_m^inf) = 40*2^m,  prefix power 5/3,
      for EVERY m >= 0 -- an infinite family of initial powers with FIXED exponent 5/3.
  F3  the +-1 Thue-Morse partial sums satisfy |sum_{n<N} (-1)^{t_n}| <= 1, so the prefix
      discrepancy is D(W_m) <= 1/2, BOUNDED, uniformly in m.
  F4  therefore  S_m = lcp - log2 F(W_m)  >=  (5/3 - 1) |W_m| - log2|W_m| - log2 3  ->  +infinity,
      and the abstract criterion gives  Phi(t) not in Q.
Everything is verified with exact integers: 2^{lcp} > F(W_m) is an integer comparison.
"""
from fractions import Fraction
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_intermediate_roots import c_W, F_of, log2_int
LOG23 = math.log2(3)

def g_of(g):
    return max(Fraction(1), g * Fraction(LOG23).limit_denominator(10**12)) \
           + g * (1 - g) * Fraction(LOG23).limit_denominator(10**12)

def tm_prefix(n):
    s = [0]
    while len(s) < n:
        s = s + [1 - x for x in s]
    return s[:n]

def mu(w):
    out = []
    for x in w:
        out += [0, 1] if x == 0 else [1, 0]
    return out

def lcp_pow(s, W):
    ell = len(W); n = 0
    while n < len(s) and s[n] == W[n % ell]:
        n += 1
    return None if n >= len(s) else n

def disc(W):
    """max_i |k_i(W) - i*gamma| exactly, gamma = |W|_1/|W|."""
    ell = len(W); w = sum(W); run = 0; best = 0
    for i in range(ell + 1):
        if i and W[i - 1]:
            run += 1
        d = abs(ell * run - i * w)
        if d > best:
            best = d
    return Fraction(best, ell)

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / H2.  Thue-Morse: the structural-ceiling claim is not what it says it is")
    P("=" * 78)
    t = tm_prefix(1 << 18)

    P("\nF1  base case.")
    W0 = t[:24]
    L0 = lcp_pow(t, W0)
    P(f"    W_0 = t[0:24] = {''.join(map(str,W0))}")
    P(f"    |W_0| = 24, |W_0|_1 = {sum(W0)}, gamma = {Fraction(sum(W0),24)}")
    P(f"    lcp(t, W_0^inf) = {L0}    prefix power = {Fraction(L0,24)} = {float(Fraction(L0,24)):.6f}")
    assert Fraction(L0, 24) == Fraction(5, 3), "base case exponent is not 5/3"

    P("\nF2  the morphism step, checked directly: W_{m+1} = mu(W_m).")
    P(f"    {'m':<4}{'|W_m|':<9}{'|W_m|_1':<10}{'gamma':<9}{'lcp':<9}{'power':<10}"
      f"{'= 5/3?':<8}{'D(W_m)':<9}")
    Ws = []
    W = W0
    for m in range(0, 12):
        L = lcp_pow(t, W)
        if L is None:
            break
        D = disc(W) if len(W) <= 30000 else None
        P(f"    {m:<4}{len(W):<9}{sum(W):<10}{str(Fraction(sum(W),len(W))):<9}{L:<9}"
          f"{str(Fraction(L,len(W))):<10}{str(Fraction(L,len(W)) == Fraction(5,3)):<8}"
          f"{(str(D) if D is not None else '-'):<9}")
        assert Fraction(L, len(W)) == Fraction(5, 3), ("exponent broke at m =", m)
        assert Fraction(sum(W), len(W)) == Fraction(1, 2)
        if D is not None:
            assert D <= Fraction(1, 2), ("discrepancy exceeded 1/2 at m =", m)
        Ws.append((m, W, L))
        W = mu(W)
    P("    lcp(mu(x),mu(y)) = 2 lcp(x,y) because mu is 2-uniform and mu(0), mu(1) differ in")
    P("    their first letter; and mu(t) = t.  So the exponent 5/3 and the density 1/2 are")
    P("    preserved at every step -- an INFINITE family of initial powers of fixed exponent.")

    P("\nF3/F4  EXACT integer surplus.  S = lcp - log2 F(W),  F(W) = |2^|W| - 3^{|W|_1}| + c_W.")
    P(f"    threshold g(1/2) = {float(g_of(Fraction(1,2))):.6f} < 5/3 = 1.666667, margin "
      f"{float(Fraction(5,3) - g_of(Fraction(1,2))):.6f}")
    P(f"    {'m':<4}{'|W|':<8}{'lcp':<8}{'D':<7}{'log2 F (exact)':<18}"
      f"{'S (exact)':<14}{'2^lcp > F':<11}{'theorem bound'}")
    for (m, W, L) in Ws:
        if len(W) > 6200:
            continue
        F = F_of(W)
        S = L - log2_int(F)
        D = disc(W)
        bound = float(len(W)) * (5/3 - float(g_of(Fraction(1,2)))) - math.log2(len(W)) - LOG23
        P(f"    {m:<4}{len(W):<8}{L:<8}{str(D):<7}{log2_int(F):<18.4f}"
          f"{S:<14.4f}{str((1 << L) > F):<11}{bound:.2f}")
        assert (1 << L) > F, ("exact surplus not positive at m =", m)
        assert S >= bound - 1e-6, ("theorem bound violated at m =", m)
    P("\n    The exact surplus is positive and grows linearly in |W|; the ratio S/|W| tends to")
    P("    5/3 - 1 = 2/3, since log2|delta_W| = |W| + log2|1 - (sqrt3/2)^{|W|}| = |W| - o(1)")
    P("    and log2 c_W <= log2|W| + ceil(D) log2 3 + |W| with D <= 1/2.")

    P("\n" + "-" * 78)
    P("CONCLUSION.  limsup [ lcp(t, W^inf) - log2 F(W) ] = +infinity along W_m = mu^m(t[0:24]),")
    P("so by theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md,")
    P("")
    P("        Phi(Thue-Morse) NOT IN Q .")
    P("")
    P("This CONTRADICTS the standing scope claim of theorems/phase1/FULL_PERIODICITY_GAP.md Q4")
    P("(repeated in LADDER.md, THEOREM_STATUS.md, and Revision 2 of the deposited note) that")
    P("Thue-Morse is structurally beyond every repetition-based method.  The error: that claim")
    P("reads 'no initial SQUARE' as 'no usable initial power', but the criterion's threshold is")
    P("g(gamma) < log2 3 < 2, and at density 1/2 an exponent of 5/3 clears it with margin 0.270.")
    P("Thue-Morse is not a ceiling for this method at all.")
    P("\nALL THUE-MORSE CHECKS PASS.")

if __name__ == "__main__":
    main()
