"""
Phase 9B, step 1-2: INDEPENDENT reconstruction of  Phi(Thue-Morse) not in Q.

Nothing is imported from the Phase 9 scripts.  Every object is rebuilt from its definition and
cross-checked two ways.

CONVENTIONS, stated explicitly.

  Thue-Morse.  t_n := (popcount(n)) mod 2,  t = 0110100110010110...   Equivalently t is the
  fixed point of mu(0) = 01, mu(1) = 10 starting from 0.  Both are built here and compared.

  Conjugacy map.  T(x) = x/2 (x even), (3x+1)/2 (x odd) on Z_2.  Phi sends a parity vector
  v in {0,1}^N to the 2-adic integer it codes.  Source paper Prop. 2.1:
        Phi(v) = - sum_{i: v_i = 1} 3^{-k_{i+1}(v)} 2^i ,      k_j(v) := |v[0:j]|_1 .
  Source paper Prop. 2.2 (isometry):  v_2(Phi(a) - Phi(b)) = lcp(a,b).
  Source paper Prop. 4.1 (periodic value):  for W finite, ell = |W|, k = |W|_1,
        Phi(W^inf) = c_W / (2^ell - 3^k),    c_W = sum_{i<ell, W_i=1} 3^{k - k_{i+1}(W)} 2^i .
  Prop. 4.1 is DERIVED here from Prop. 2.1 by summing the geometric series, and checked
  numerically against a direct 2-adic evaluation, so the convention is not taken on trust.

  Discrepancy (the repository's definition, theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md):
        D(W) := max_{0 <= i <= ell} | k_i(W) - i*k/ell | ,
  i.e. the deviation of the prefix counts from the root's OWN density k/ell.  It is NOT a
  star-discrepancy of a rotation and NOT relative to any external density.
"""
from fractions import Fraction
import math, sys

LOG23 = math.log2(3)

# ---------------------------------------------------------------- Thue-Morse, two ways
def tm_popcount(n):
    return [bin(i).count("1") & 1 for i in range(n)]

def tm_morphism(n):
    t = [0]
    while len(t) < n:
        t = t + [1 - x for x in t]
    return t[:n]

def mu(w):
    out = []
    for x in w:
        out += [0, 1] if x == 0 else [1, 0]
    return out

# ---------------------------------------------------------------- basic word tools
def lcp_with_power(s, W):
    ell = len(W); n = 0
    while n < len(s) and s[n] == W[n % ell]:
        n += 1
    return None if n >= len(s) else n

def prefix_counts(W):
    out = [0]
    for x in W:
        out.append(out[-1] + x)
    return out

def discrepancy(W):
    """max_i |k_i - i*k/ell|, exact, as a Fraction."""
    ell = len(W); k = sum(W); pc = prefix_counts(W)
    best = 0
    for i in range(ell + 1):
        d = abs(ell * pc[i] - i * k)
        if d > best:
            best = d
    return Fraction(best, ell)

def c_of(W):
    k = sum(W); pc = prefix_counts(W); tot = 0
    for i, b in enumerate(W):
        if b:
            tot += 3 ** (k - pc[i + 1]) * (1 << i)
    return tot

def F_of(W):
    return abs((1 << len(W)) - 3 ** sum(W)) + c_of(W)

def log2_int(n):
    b = n.bit_length()
    return (b - 1) + math.log2(n / (1 << (b - 1)))

def is_periodic_prefix(s, maxpre, maxper):
    for pre in range(maxpre):
        tail = s[pre:]
        if len(tail) < 3 * maxper:
            break
        for p in range(1, maxper):
            if all(tail[i] == tail[i + p] for i in range(len(tail) - p)):
                return (pre, p)
    return None

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9B / 1-2.  Independent reconstruction of  Phi(Thue-Morse) not in Q")
    P("=" * 78)

    N = 1 << 18
    t1 = tm_popcount(N)
    t2 = tm_morphism(N)
    assert t1 == t2, "the two Thue-Morse definitions disagree"
    t = t1
    P(f"\n1.1  Thue-Morse built two independent ways (popcount parity; mu-iteration):")
    P(f"     agree on {N} letters.  t[0:32] = {''.join(map(str,t[:32]))}")

    # ---- convention check: derive Prop 4.1 from Prop 2.1 numerically in Z/2^M
    P("\n1.2  Convention check: Prop. 4.1 derived from Prop. 2.1, verified in Z/2^M.")
    M = 400
    for W in ([0,1,1,0], [1,0,1], [0,1,1,0,1,0,0,1]):
        ell, k = len(W), sum(W)
        # Prop 2.1 series, truncated, evaluated mod 2^M (3 is invertible mod 2^M)
        inv3 = pow(3, -1, 1 << M)
        pc = prefix_counts(W)
        tot = 0
        for j in range(0, (M // ell) + 3):
            for i, b in enumerate(W):
                if b:
                    tot = (tot - pow(inv3, j * k + pc[i + 1], 1 << M) * pow(2, j * ell + i, 1 << M)) % (1 << M)
        num, den = c_of(W), (1 << ell) - 3 ** k
        closed = (num * pow(den % (1 << M), -1, 1 << M)) % (1 << M)
        ok = (tot == closed)
        P(f"     W = {''.join(map(str,W))}: series == c_W/(2^ell - 3^k) mod 2^{M}:  {ok}")
        assert ok

    # ---- 1.3 the base root
    P("\n1.3  The base root.")
    W0 = t[:24]
    L0 = lcp_with_power(t, W0)
    P(f"     W_0 = t[0:24] = {''.join(map(str,W0))}")
    P(f"     |W_0| = {len(W0)},  |W_0|_1 = {sum(W0)},  density = {Fraction(sum(W0),24)}")
    P(f"     t[24:40] = {''.join(map(str,t[24:40]))}")
    P(f"     W_0[0:16] = {''.join(map(str,W0[:16]))}   equal: {t[24:40] == W0[:16]}")
    P(f"     t[40] = {t[40]},  W_0[16] = {W0[16]},  differ: {t[40] != W0[16]}")
    P(f"     => lcp(t, W_0^inf) = {L0} exactly;  prefix power = {Fraction(L0,24)} = 5/3")
    assert L0 == 40 and Fraction(L0, 24) == Fraction(5, 3)

    # ---- 1.4 propagation
    P("\n1.4  Propagation under mu.  Claim: lcp(mu(x), mu(y)) = 2 lcp(x,y) for x != y, because")
    P("     mu is 2-uniform and mu(0) = 01, mu(1) = 10 differ in their FIRST letter.  With")
    P("     mu(t) = t and mu(W^inf) = mu(W)^inf this gives lcp(t, mu(W)^inf) = 2 lcp(t, W^inf).")
    P(f"     {'m':<4}{'|W_m|':<9}{'|W_m|_1':<10}{'density':<10}{'lcp':<9}{'= 40*2^m?':<11}"
      f"{'power':<9}{'D(W_m)':<9}")
    W = W0
    rows = []
    for m in range(0, 13):
        L = lcp_with_power(t, W)
        if L is None:
            break
        D = discrepancy(W) if len(W) <= 60000 else None
        ok = (L == 40 * 2 ** m and len(W) == 24 * 2 ** m)
        P(f"     {m:<4}{len(W):<9}{sum(W):<10}{str(Fraction(sum(W),len(W))):<10}{L:<9}"
          f"{str(ok):<11}{str(Fraction(L,len(W))):<9}{(str(D) if D is not None else '-'):<9}")
        assert ok and Fraction(sum(W), len(W)) == Fraction(1, 2)
        if D is not None:
            assert D == Fraction(1, 2)
        rows.append((m, W, L))
        W = mu(W)
    P("     Also verified directly: W_m == t[0 : 24*2^m] for every m (mu maps prefixes of t")
    P("     to prefixes of t, since mu(t) = t).")
    for (m, Wm, _) in rows:
        assert Wm == t[:len(Wm)], ("W_m is not a prefix of t", m)

    # ---- 1.5 the discrepancy, proved
    P("\n1.5  D(W_m) = 1/2 for every m -- PROVED, not merely measured.")
    P("     Let S(N) := sum_{n<N} (-1)^{t_n}.  Since t_{2n} = t_n and t_{2n+1} = 1 - t_n, each")
    P("     pair (2n, 2n+1) contributes (-1)^{t_n} + (-1)^{1-t_n} = 0, so S(2M) = 0 for all M,")
    P("     and S(2M+1) = S(2M) + (-1)^{t_{2M}} = (-1)^{t_M} in {-1, +1}.  Hence |S(N)| <= 1.")
    P("     For a prefix of t of even length ell with k = ell/2, k_i - i/2 = -S(i)/2, so")
    P("     D = max_i |k_i - i/2| = 1/2 exactly.")
    Smax = 0
    S = 0
    for n in range(1 << 16):
        S += 1 if t[n] == 0 else -1
        Smax = max(Smax, abs(S))
        assert (S == 0) if (n + 1) % 2 == 0 else (abs(S) == 1), ("partial-sum law", n)
    P(f"     checked to N = 2^16: max |S(N)| = {Smax}, and S(even) = 0, |S(odd)| = 1 throughout.")

    # ---- 1.6 aperiodicity and W_m^inf != t
    P("\n1.6  t is aperiodic, so t != W_m^inf for every m.")
    per = is_periodic_prefix(t[:1 << 15], maxpre=200, maxper=3000)
    P(f"     no (preperiod < 200, period < 3000) found on a 2^15 prefix: {per is None}")
    P("     (classical: t is overlap-free, hence not eventually periodic -- Thue 1912).")
    P("     W_m^inf is periodic with period 24*2^m, so W_m^inf != t.  This is the only standing")
    P("     hypothesis the abstract criterion places on the pair (t, W_m).")
    assert per is None

    # ---- 2.1 which criterion is actually needed
    P("\n" + "=" * 78)
    P("2.  WHICH THRESHOLD IS ACTUALLY NEEDED")
    P("=" * 78)
    P("     Phase 1's EXACT inequality (theorems/phase1/REPETITION_HEIGHT_CRITERION.md):")
    P("         S >= ell*[ r - max(1, gamma log2 3) ] - ceil(D) log2 3 - log2 ell .")
    P(f"     At gamma = 1/2 the threshold is max(1, (log2 3)/2) = max(1, {LOG23/2:.6f}) = 1.")
    P(f"     r = 5/3 = {5/3:.6f} exceeds it by {5/3 - 1:.6f}.")
    P("     D(W_m) = 1/2 is BOUNDED, so ceil(D) log2 3 = log2 3 is a CONSTANT, not o(ell).")
    P("     => the pre-existing criterion already proves the theorem.  The Phase 9 threshold")
    P("        g(gamma) = max(1,gamma log2 3) + gamma(1-gamma) log2 3 = 1.396241 at gamma = 1/2")
    P("        is NOT needed here; it is the threshold one must use when NOTHING is known about")
    P("        D, and Thue-Morse is not such a case.")
    P("")
    P(f"     {'route':<46}{'threshold':<12}{'r - threshold':<15}{'needs D?'}")
    P(f"     {'Phase 1 exact inequality, gamma = 1/2':<46}{1.0:<12.6f}{5/3-1:<15.6f}{'D = o(ell)'}")
    P(f"     {'Phase 1 uniform packaging (sup over gamma)':<46}{LOG23:<12.6f}{5/3-LOG23:<15.6f}{'D = o(ell)'}")
    P(f"     {'Phase 9 g(gamma) at gamma = 1/2':<46}{1.396241:<12.6f}{5/3-1.396241:<15.6f}{'no'}")
    P("     All three clear, but the FIRST is the shortest chain and is the one to cite.")

    # ---- 2.2 numerator / denominator, and the asymptotic
    P("\n2.2  Exact numerator and denominator bounds, and the asymptotic S/|W| -> 2/3.")
    P("     delta_W = 2^ell - 3^{ell/2};  |delta_W| = 2^ell (1 - (sqrt3/2)^ell), so")
    P("         log2|delta_W| = ell + log2(1 - (sqrt3/2)^ell)  in  [ell - 0.048, ell]  for ell >= 24.")
    P("     c_W:  upper  c_W <= ell * 3^{ceil D} * max(2^ell, 3^{ell/2}) = 3 ell 2^ell  (D = 1/2),")
    P("           lower  c_W >= 2^{i*} where i* is the largest index with W_{i*} = 1; for these")
    P("                  roots i* = ell - 2, so c_W >= 2^{ell-2}.")
    P("     Hence  F = |delta| + c_W  satisfies   ell - 0.05 <= log2 F <= ell + log2(1 + 3 ell),")
    P("     and    S = (5/3) ell - log2 F  satisfies")
    P("         (2/3) ell - log2(1 + 3 ell)  <=  S  <=  (2/3) ell + 0.05 .")
    P("     So S/ell -> 2/3 with error O(log ell / ell):  a PROVED asymptotic, not a fit.")
    P("")
    P(f"     {'m':<4}{'ell':<8}{'lcp':<8}{'log2|delta|-ell':<18}{'log2 c_W - ell':<17}"
      f"{'log2 F - ell':<15}{'S':<12}{'S/ell':<9}{'2^lcp>F'}")
    for (m, Wm, L) in rows:
        ell = len(Wm)
        if ell > 6200:
            continue
        k = sum(Wm)
        delta = abs((1 << ell) - 3 ** k)
        cw = c_of(Wm)
        F = delta + cw
        S = L - log2_int(F)
        lo = (2/3) * ell - math.log2(1 + 3 * ell)
        hi = (2/3) * ell + 0.05
        assert lo <= S <= hi, ("asymptotic bracket failed", m, S, lo, hi)
        assert (1 << L) > F
        P(f"     {m:<4}{ell:<8}{L:<8}{log2_int(delta)-ell:<18.6f}{log2_int(cw)-ell:<17.6f}"
          f"{log2_int(F)-ell:<15.6f}{S:<12.4f}{S/ell:<9.6f}{str((1 << L) > F)}")
    P("     every row lies inside the PROVED bracket [ (2/3)ell - log2(1+3ell) , (2/3)ell + 0.05 ].")

    # ---- 2.3 the contradiction, for every hypothetical rational
    P("\n2.3  The arithmetic contradiction, for EVERY hypothetical rational value.")
    P("     Suppose Phi(t) = u/v in lowest terms; since Phi(t) in Z_2, v is odd.  Put")
    P("     H := max(|u|, v), a FIXED finite integer once u/v is chosen.  For each m set")
    P("         M_m := u*delta_m - v*c_{W_m}  =  v*delta_m*(Phi(t) - Phi(W_m^inf)).")
    P("     * delta_m != 0 (2^ell = 3^k forces ell = k = 0);  delta_m is odd.")
    P("     * M_m != 0, because Phi is injective and t != W_m^inf (step 1.6).")
    P("     * v_2(M_m) = v_2(v delta_m) + v_2(Phi(t) - Phi(W_m^inf)) = 0 + lcp(t, W_m^inf) = L_m,")
    P("       by Prop. 2.2 and v, delta_m both odd.  Hence |M_m| >= 2^{L_m}.")
    P("     * |M_m| <= |u||delta_m| + v c_{W_m} <= H (|delta_m| + c_{W_m}) = H F(W_m).")
    P("     So 2^{L_m} <= H F(W_m), i.e.  S_m = L_m - log2 F(W_m) <= log2 H  for EVERY m.")
    P("     But S_m >= (2/3)|W_m| - log2(1 + 3|W_m|) -> +infinity.  Contradiction for every")
    P("     choice of u/v.  Therefore Phi(t) is irrational.")
    P("")
    P("     Note the quantifier order: H is chosen AFTER u/v but BEFORE m, and the bound on S_m")
    P("     is uniform in m, so a single m with S_m > log2 H already refutes that u/v.")

    P("\n" + "-" * 78)
    P("CONCLUSION.  Phi(Thue-Morse) is irrational.  Shortest dependency chain:")
    P("   source paper Prop. 2.1 (series) -> Prop. 4.1 (periodic value, re-derived above)")
    P("   source paper Prop. 2.2 (2-adic isometry)")
    P("   theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md (c_W <= ell 3^{ceil D} max(2^ell,3^k))")
    P("   theorems/phase1/REPETITION_HEIGHT_CRITERION.md, EXACT inequality at gamma = 1/2")
    P("   + Thue-Morse facts: r = 5/3 at ell = 24*2^m, gamma = 1/2, D = 1/2, aperiodic.")
    P("   The Phase 9 threshold g(gamma) is NOT in this chain.")
    P("\nALL PHASE-9B STEP 1-2 CHECKS PASS.")

if __name__ == "__main__":
    main()
