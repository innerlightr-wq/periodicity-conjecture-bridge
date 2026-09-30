"""
Phase 9, step I: sweep automatic sequences with Theorem 4.

The Thue-Morse argument is generic.  Let sigma be a k-uniform substitution on {0,1} with
aperiodic fixed point t = sigma^inf(0).  Then for finite words x != y,
    lcp(sigma(x), sigma(y)) = k * lcp(x,y) + lcp(sigma(a), sigma(b)),
where a != b are the first differing letters; put cst := lcp(sigma(0), sigma(1)) (a constant,
0 if the images differ in their first letter).  With W_0 a prefix of t and W_m := sigma^m(W_0),
    |W_m| = k^m |W_0|,        lcp(t, W_m^inf) = k^m L_0 + cst*(k^m - 1)/(k - 1),
so the prefix power r_m = lcp/|W_m| is NON-DECREASING in m and converges to
    r_inf = (L_0 + cst/(k-1)) / |W_0| .
The densities gamma_m converge to the letter frequency gamma* of 1 in t, and the prefix
discrepancy of a primitive uniform substitution's fixed point is O(|W|^theta) with
theta = log|lambda_2| / log k < 1, hence o(|W|).  So Theorem 4 applies as soon as
    r_inf > g(gamma*),      g(gamma) = max(1, gamma log2 3) + gamma(1-gamma) log2 3,
and the conclusion is Phi(t) NOT IN Q.

This script enumerates all 2- and 3-uniform substitutions on {0,1}, keeps the ones with an
aperiodic-looking fixed point, and tests the criterion -- with the EXACT integer surplus.
"""
from fractions import Fraction
import itertools, math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_intermediate_roots import F_of, log2_int
LOG23 = math.log2(3)
L3 = Fraction(LOG23).limit_denominator(10 ** 12)

def g_of(g):
    return max(Fraction(1), g * L3) + g * (1 - g) * L3

def fixed_point(s0, s1, n):
    img = {0: [int(c) for c in s0], 1: [int(c) for c in s1]}
    t = [0]
    while len(t) < n:
        nt = []
        for x in t:
            nt += img[x]
        if nt == t:
            break
        t = nt
    return t[:n], img

def lcp_pow(s, W):
    ell = len(W); n = 0
    while n < len(s) and s[n] == W[n % ell]:
        n += 1
    return None if n >= len(s) else n

def looks_aperiodic(t, maxper=400, maxpre=64):
    """Rejects EVENTUALLY periodic prefixes, not merely purely periodic ones -- the
    Periodicity Conjecture excludes eventually periodic words, so they must not be
    counted as failures."""
    for pre in range(0, maxpre):
        tail = t[pre:]
        if len(tail) < 2 * maxper:
            break
        for p in range(1, maxper):
            if all(tail[i] == tail[i + p] for i in range(len(tail) - p)):
                return False
    return True

def disc(W):
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
    P("PHASE 9 / I.  Theorem 4 applied to fixed points of uniform substitutions")
    P("=" * 78)
    results = []
    for k in (2, 3):
        for s0 in ["".join(p) for p in itertools.product("01", repeat=k)]:
            for s1 in ["".join(p) for p in itertools.product("01", repeat=k)]:
                if s0[0] != "0":
                    continue                      # need sigma(0) to start with 0 for a fixed point
                if s0 == s1:
                    continue
                t, img = fixed_point(s0, s1, 1 << 16)
                if len(t) < 4096 or not looks_aperiodic(t):
                    continue
                cst = 0
                a, b = img[0], img[1]
                while cst < k and a[cst] == b[cst]:
                    cst += 1
                # best prefix power over a window, and the induced limit
                best = None
                for ell in range(2, 600):
                    L = lcp_pow(t, t[:ell])
                    if L is None:
                        break
                    r_inf = Fraction(L * (k - 1) + cst, ell * (k - 1))
                    w = sum(t[:ell])
                    if best is None or r_inf > best[0]:
                        best = (r_inf, ell, L, w)
                if best is None:
                    continue
                r_inf, ell0, L0, w0 = best
                gam = Fraction(w0, ell0)
                results.append((k, s0, s1, t, ell0, L0, r_inf, gam, cst))
    P(f"\n    {len(results)} uniform substitutions with an aperiodic fixed point.")
    P(f"    {'k':<3}{'sig(0)':<8}{'sig(1)':<8}{'best ell':<10}{'lcp':<7}{'r_inf':<11}"
      f"{'gamma':<10}{'g(gamma)':<11}{'r>g?':<7}{'exact S at m=4':<16}{'2^L>F'}")
    nwin = 0
    for (k, s0, s1, t, ell0, L0, r_inf, gam, cst) in results:
        ok = r_inf > g_of(gam)
        Sstr, posstr = "-", "-"
        if ok:
            nwin += 1
            # iterate sigma m times on the base root and evaluate the EXACT surplus
            img = {0: [int(c) for c in s0], 1: [int(c) for c in s1]}
            W = t[:ell0]
            for m in range(5):
                if len(W) * k > 3000:
                    break
                nW = []
                for x in W:
                    nW += img[x]
                W = nW
            L = lcp_pow(t, W)
            if L is not None and len(W) <= 3000:
                F = F_of(W)
                S = L - log2_int(F)
                Sstr = f"{S:.2f}"
                posstr = str((1 << L) > F)
                assert (1 << L) > F or S < 0, ("inconsistent", s0, s1)
        P(f"    {k:<3}{s0:<8}{s1:<8}{ell0:<10}{L0:<7}{float(r_inf):<11.6f}"
          f"{float(gam):<10.6f}{float(g_of(gam)):<11.6f}{str(ok):<7}{Sstr:<16}{posstr}")
    P(f"\n    substitutions whose fixed point Theorem 4 reaches: {nwin} of {len(results)}")
    P("\n    NAMED CASES:")
    for (k, s0, s1, t, ell0, L0, r_inf, gam, cst) in results:
        nm = {("2","01","10"): "Thue-Morse",
              ("2","01","00"): "period-doubling",
              ("3","010","201"): None}.get((str(k), s0, s1))
        if nm:
            P(f"      {nm:<20} sigma(0)={s0}, sigma(1)={s1}: r_inf = {float(r_inf):.6f}, "
              f"gamma = {float(gam)}, g = {float(g_of(gam)):.6f}, reached = {r_inf > g_of(gam)}")
    P("\n    The two substitutions with r_inf = 1 in an earlier pass (sigma(1) = 11 and 111) are")
    P("    EVENTUALLY PERIODIC fixed points and are now excluded: the Periodicity Conjecture says")
    P("    nothing about them, so they were never failures.")
    P("\n    Caveats, explicitly: (i) aperiodicity is tested on a finite prefix, not proved;")
    P("    (ii) the discrepancy bound D(W) = o(|W|) is quoted for PRIMITIVE uniform substitutions")
    P("    and is not verified here per row -- the exact surplus column is what is certified;")
    P("    (iii) r_inf is the LIMIT of the prefix powers; the exact-surplus column confirms the")
    P("    conclusion at a finite m, which is what the criterion actually needs.")
    P("\nSTEP I COMPLETE.")

if __name__ == "__main__":
    main()
