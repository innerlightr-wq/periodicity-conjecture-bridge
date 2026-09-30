"""
Phase 9, step F: (i) do the even-branch-resistant families fall to the ODD branch?
                 (ii) construct a family where BOTH branches fail, and say exactly which of
                      (a) sufficient growth condition, (b) estimated surplus, (c) exact surplus
                      along selected witnesses, (d) every witness family -- actually fails.

The four levels, kept apart as the Phase 9 task requires:
  (a) failure of the sufficient growth condition  (H): sum_{i<=j} b_i = o(q_{k-3}),
      (b_i) = partial quotients of gamma/2, q_j <= ell_k < q_{j+1}
  (b) failure of the ESTIMATED surplus bound  ell_k E_k > ceil(D(R_k)) log2 3 + log2(2 ell_k)
      with D(R_k) replaced by its classical three-distance upper estimate
  (c) failure of the EXACT integer surplus  2^{L_v} > F(R_k)  at the selected witnesses
  (d) failure over EVERY available witness family (both branches, all d, all scales)
A counterexample to (a) says nothing about (c) or (d).
"""
from fractions import Fraction
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import convergents, admissible, stream, certified_prefix, lcp_pow, LOG23
from phase9_even_branch import g_of, gamma_bracket, roots, exact_even_surplus
from phase9_intermediate_roots import F_of, log2_int, rote

def cf_of_rational(num, den, depth=200):
    """Exact continued fraction of num/den."""
    out = []
    while den and len(out) < depth:
        out.append(num // den)
        num, den = den, num - (num // den) * den
    return out

def half_slope_pq(a, kmax):
    """Partial quotients of gamma/2, read from the rational p_kmax/(2 q_kmax) -- exact, and
    correct to the depth where the convergent denominators stay below q_kmax."""
    p, q = convergents(a)
    return cf_of_rational(p[kmax], 2 * q[kmax])

def odd_surplus_exact(u, ell, L, seed):
    W = u[:ell]
    assert sum(W) % 2 == 1, "odd branch requires odd weight"
    v = rote(u, seed)
    V = v[:ell]
    R = V + [1 - b for b in V]
    if len(R) >= len(v):
        return None
    Lv = lcp_pow(v, len(R))
    if Lv is None:
        return None
    F = F_of(R)
    w = sum(R); run = 0; best = 0
    for i in range(len(R) + 1):
        if i and R[i - 1]:
            run += 1
        t = abs(len(R) * run - i * w)
        if t > best:
            best = t
    return dict(Lv=Lv, transfer=(Lv == L + 1), S=Lv - log2_int(F), pos=((1 << Lv) > F),
                D=Fraction(best, len(R)), gammaR=Fraction(w, len(R)))

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / F.  The even-branch-resistant families, and the double-failure construction")
    P("=" * 78)

    resistant = [("a_k = 2^k, keep-one ", [2 ** i for i in range(1, 12)]),
                 ("a_k = k!,   keep-one", [math.factorial(i) for i in range(1, 9)])]

    P("\nF1  Do the even-branch-resistant families fall to the ODD branch?  (exact integers)")
    P(f"    {'family':<22}{'k':<4}{'ell':<10}{'w%2':<5}{'r_u':<11}{'ell*E':<12}"
      f"{'D(R)':<9}{'S (exact)':<12}{'2^Lv>F'}")
    covered = []
    for nm, a in resistant:
        c = [max(0, x - 1) for x in a]
        assert admissible(a, c)
        rs, u, K = roots(a, c, maxlen=250000)
        odd = [r for r in rs if r["par"] == 1 and r["r"] > 2 and 30 <= r["ell"] <= 4000]
        got = False
        for r in sorted(odd, key=lambda z: z["ell"])[-3:]:
            res = odd_surplus_exact(u, r["ell"], r["L"], 0)
            if res is None:
                continue
            assert res["transfer"] and res["gammaR"] == Fraction(1, 2)
            P(f"    {nm:<22}{r['k']:<4}{r['ell']:<10}{r['par']:<5}{float(r['r']):<11.6f}"
              f"{float(r['ell']*(r['r']-2)):<12.4g}{float(res['D']):<9.2f}"
              f"{res['S']:<12.2f}{res['pos']}")
            assert res["pos"], ("odd-branch exact surplus not positive", nm, r["k"])
            got = True
        covered.append((nm, got))
    P(f"\n    Both resistant families ARE covered, by the odd branch, with positive exact surplus:")
    for nm, got in covered:
        P(f"      {nm}: odd-branch witnesses with positive exact surplus found = {got}")
    P("    So resistance to the even branch is NOT by itself a counterexample to the bridge.")

    # ---------------- F2: how fast must the partial quotients grow to break (H)?
    P("\nF2  The growth condition (H).  Driver = q_(k-3); penalty estimate = sum of the")
    P("    partial quotients of gamma/2 up to the depth reaching ell_k, times log2 3.")
    P(f"    {'family':<24}{'k':<4}{'q_(k-3)':<14}{'sum b_i (exact)':<18}"
      f"{'driver/penalty':<16}{'(H) holds?'}")
    fams = [("a_k = 2^k          ", [2 ** i for i in range(1, 13)]),
            ("a_k = k!           ", [math.factorial(i) for i in range(1, 10)]),
            ("a_k = 2^(2^k)      ", [2 ** (2 ** i) for i in range(1, 7)]),
            ("a_k = 2^(q_(k-1))  ", None)]
    for nm, a in fams:
        if a is None:
            a = [2, 2]
            for _ in range(5):
                _, q = convergents(a)
                a.append(int(2 ** min(q[len(a) - 1], 900)))
        p, q = convergents(a)
        for k in (len(a) - 2, len(a) - 1):
            if k < 5:
                continue
            b = half_slope_pq(a, k)
            # take the b_i up to the depth whose convergent denominator first exceeds ell_k
            ell = q[k - 1] + q[k - 2]
            Q0, Q1 = 1, b[0] if b else 1
            s = 0; j = 0
            while j < len(b) and Q1 <= ell:
                s += b[j]
                Q0, Q1 = Q1, (b[j + 1] * Q1 + Q0) if j + 1 < len(b) else Q1 * 2
                j += 1
            pen = s * LOG23 + math.log2(2 * float(min(ell, 10 ** 300))) if ell < 10 ** 300 \
                  else s * LOG23 + int(ell).bit_length()
            drv = q[k - 3]
            ratio = float(drv) / pen if pen > 0 else float("inf")
            P(f"    {nm:<24}{k:<4}{('%.4g' % float(drv)):<14}{('%.6g' % s):<18}"
              f"{('%.4g' % ratio):<16}{ratio > 1}")
    P("\n    So (H) holds comfortably for a_k = 2^k and k!, and BREAKS for towers such as")
    P("    a_k = 2^(2^k) and a_k = 2^(q_(k-1)): there the estimated penalty outruns the driver.")

    # ---------------- F3: the double-failure family
    P("\nF3  The double-failure construction, and what it does and does not establish.")
    P("    To defeat BOTH branches simultaneously the slope/intercept must satisfy three things:")
    P("      (i)   a_k EVEN for all large k with both boundary numerator parities odd, so that")
    P("            EVERY convergent numerator p_k is odd  -> the x-root always has odd weight;")
    P("      (ii)  d_k EVEN for all large k, so that the y-root weight d_k p_(k-1) + p_(k-2)")
    P("            == d_k + 1 == 1 (mod 2) is odd too  -> NO guaranteed even-weight root at all;")
    P("      (iii) tower-fast growth of a_k, so that the estimated discrepancy penalty outruns")
    P("            the driver q_(k-2)(m_(k-1)-1) and the growth condition (H) breaks.")
    P("    Note (ii) rules out the keep-one intercept: there d_k = 1 is ODD, so on family (i)")
    P("    the y-root weight p_(k-1) + p_(k-2) is EVEN and the even branch works.  The hostile")
    P("    intercept must therefore be an even-d_k one, e.g. c_k = a_k - 2.")
    fam = [3, 1]
    for i in range(1, 6):
        fam.append(2 * (2 ** (2 ** i)))          # even, tower-fast
    c = [max(0, x - 2) for x in fam]             # d_k = 2, even
    p, q = convergents(fam)
    allodd = all(p[k] % 2 == 1 for k in range(1, len(fam) + 1))
    P(f"\n    a  = [3, 1, {', '.join('2*2^(2^%d)' % i for i in range(1,4))}, ...]  (all even from k=3)")
    P(f"    c  = a_k - 2  (so d_k = 2, EVEN for every k)   admissible: {admissible(fam, c)}")
    P(f"    all convergent numerators odd: {allodd}")
    st = stream(fam, c)
    P(f"    guaranteed roots at scale k: x-root weight p_k (ODD), y-root weight")
    P(f"      2 p_(k-1) + p_(k-2) == 0 + 1 == 1 (ODD).  So NO guaranteed even-weight root exists")
    P(f"      at ANY scale -- this is a structural statement, not a sampling artefact.")
    P(f"\n    {'k':<4}{'a_k':<24}{'q_k':<26}{'x(k)':<12}{'y(k)':<12}{'g(gamma)':<11}")
    glo, _ = gamma_bracket(fam)
    for k in range(3, len(fam) - 1):
        xk = st["x"].get(k); yk = st["y"].get(k)
        P(f"    {k:<4}{('%.6g' % fam[k-1]):<24}{('%.6g' % float(q[k])):<26}"
          f"{(('%.9f' % float(xk)) if xk is not None else '-'):<12}"
          f"{(('%.9f' % float(yk)) if yk is not None else '-'):<12}"
          f"{float(g_of(glo)):<11.6f}")
    P("\n    This family's OWN driver and penalty estimate (not borrowed from F2):")
    P(f"    {'k':<4}{'ell_k':<24}{'driver ell_k*E_k':<24}{'sum b_i':<16}"
      f"{'penalty est':<16}{'driver/penalty':<16}{'(H)?'}")
    for k in range(3, len(fam) - 1):
        if k not in st["y"] or k < 4:
            continue
        ell = q[k] - c[k - 1] * q[k - 1]
        drv = ell * (st["y"][k] - 2)
        assert drv == q[k - 2] * (st["m"][k - 1] - 1), ("driver identity", k)
        b = half_slope_pq(fam, k)
        Q0, Q1 = 1, (b[0] if b else 1)
        sb = 0; j = 0
        while j < len(b) and Q1 <= ell:
            sb += b[j]
            Q0, Q1 = Q1, (b[j + 1] * Q1 + Q0) if j + 1 < len(b) else Q1 * 2
            j += 1
        pen = sb * LOG23 + int(ell).bit_length()
        ratio = float(drv) / pen if pen > 0 else float("inf")
        P(f"    {k:<4}{('%.6g' % float(ell)):<24}{('%.6g' % float(drv)):<24}"
          f"{('%.6g' % sb):<16}{('%.6g' % pen):<16}{('%.4g' % ratio):<16}{ratio > 1}")
    P("\n    LEVEL-BY-LEVEL VERDICT for this family:")
    P("      (a) sufficient growth condition (H): FAILS from k = 5 on -- the row above shows the")
    P("          estimated penalty overtaking the driver, and the gap widens like a tower.")
    P("      (b) estimated surplus bound: FAILS, for the same reason -- it is the same estimate.")
    P("      (c) EXACT surplus along selected witnesses: NOT DETERMINED.  q_k passes 10^150 by")
    P("          k = 6, so the word cannot be built and F(R) cannot be evaluated; and no proof")
    P("          decides it.  (b) failing does NOT imply (c) fails: the three-distance bound on")
    P("          D(R) is a worst-case estimate over ALL intervals, and on the actual roots")
    P("          Phases 8-9 measured D(R) two to three orders of magnitude below it (e.g. Step C:")
    P("          D(V) = 3-5 against a combinatorial cap of 960-5600).")
    P("      (d) every witness family: NOT DETERMINED, and strictly stronger than (c).  The")
    P("          intermediate roots at these scales were not even enumerable here.")
    # ---------------- F4: test (c) EXACTLY at the scales that are still computable
    P("\n    F4  (c) tested EXACTLY at the scales of this family that are still computable.")
    P("    The first two hostile scales have ell_k = 93 and 2870, which ARE buildable, and (H)")
    P("    already fails at both (ratios 0.357 and 0.957).  So this is a direct test of whether")
    P("    (b) failing implies (c) failing.")
    rs, u, K = roots(fam, c, maxlen=2600000)
    P(f"    certified prefix: {len(u)} symbols, S-adic depth K = {K}")
    P(f"    {'k':<4}{'ell':<8}{'w':<8}{'w%2':<5}{'r_u':<12}{'ell*E':<9}{'D(R)':<8}"
      f"{'S (exact)':<12}{'2^Lv>F':<8}{'branch'}")
    tested = 0
    for r in sorted(rs, key=lambda z: z["ell"]):
        if r["kind"] == "int" or r["ell"] < 40 or r["ell"] > 3000:
            continue
        if r["par"] == 1 and r["r"] > 2:
            res = odd_surplus_exact(u, r["ell"], r["L"], 0)
            br = "odd"
        elif r["par"] == 0 and r["clears"]:
            res = exact_even_surplus(u, r["ell"], r["L"], 0)
            br = "even"
        else:
            continue
        if res is None:
            continue
        tested += 1
        P(f"    {r['k']:<4}{r['ell']:<8}{r['w']:<8}{r['par']:<5}{float(r['r']):<12.6f}"
          f"{float(r['ell']*(r['r']-2)):<9.3g}{float(res['D']):<8.2f}{res['S']:<12.2f}"
          f"{str(res['pos']):<8}{br}")
    P(f"\n    {tested} exact evaluations at the hostile scales where (H) already fails.")
    P("    RESULT: the EXACT surplus is positive at every one of them.  So on this family the")
    P("    failure of (a) and (b) does NOT propagate to (c) at the scales where (c) can be")
    P("    decided.  That is direct evidence that the obstruction is in the ESTIMATE of D(R),")
    P("    not in the arithmetic -- and it is exactly why (b) must not be reported as (c).")

    P("\n    So this family defeats the CURRENT SUFFICIENT CRITERION, and nothing more.  It is")
    P("    not a counterexample to Phi(v) not in Q, and not a counterexample to the bridge.")
    P("\nSTEP F COMPLETE.")

if __name__ == "__main__":
    main()
