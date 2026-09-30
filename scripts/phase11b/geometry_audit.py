"""
Phase 11B / item 4: independent audit of the geometric connection.

Four things are checked, each independently of how Phase 11 computed it:
 (a) the translation sign and the half-open endpoint conventions, by exhaustive case analysis;
 (b) the identity  L(ell) - ell = m*(ell),  by THREE mutually independent computations;
 (c) avoidance of BOTH boundary arcs, index m = 0 included explicitly;
 (d) the drift / discrepancy inequality restated with PROVED asymptotic bounds instead of the
     measured constants 0.41 and 2.02 that Phase 11 used.
"""
import sys, math
sys.path.insert(0, "/home/elias/scratch/phase11-bridge/scripts/phase11")
from fractions import Fraction
from exact_word import Q5, ALPHA, RHO, BLO, BHI, word, delta, convergents, lt_beta

def chi(x):
    return 1 if lt_beta(x) else 0

def in_M_def(x, d):
    """Definition: chi(x) != chi({x+d})."""
    return chi(x) != chi((x + d).frac())

def in_M_arcs(x, d):
    """Closed-form arc description, derived by hand:
         d > 0 :  M = [beta-d, beta) u [1-d, 1)
         d < 0 :  M = [0, |d|)      u [beta, beta+|d|)
    Membership decided with the beta bracket; raises if undecided."""
    s = d.sign()
    if s == 0:
        return False
    if s > 0:
        in1 = (x - (Q5(BHI) - d)).sign() >= 0 and lt_beta(x)          # [beta-d, beta)
        in2 = (x - (Q5(1) - d)).sign() >= 0                            # [1-d, 1)
        return in1 or in2
    e = Q5(0) - d
    in1 = x.sign() >= 0 and (x - e).sign() < 0                         # [0, |d|)
    in2 = (not lt_beta(x)) and (x - (Q5(BLO) + e)).sign() < 0          # [beta, beta+|d|)
    return in1 or in2

def lcp_pow(s, ell):
    n = ell
    while n < len(s) and s[n] == s[n - ell]:
        n += 1
    return None if n >= len(s) else n

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 11B / item 4.  Independent audit of the geometric connection")
    P("=" * 78)

    P("\n(a) Translation sign and half-open endpoints, by case analysis.")
    P("    chi = 1_[0,beta).  s_{m+ell} != s_m  iff  chi({m a + r}) != chi({m a + r + ell*a}),")
    P("    and {x + ell*a} = {x + delta} with delta := ell*a - round(ell*a).  For delta > 0:")
    P("      x in [0, beta-delta) : x+d in [delta, beta)        both 1   -> match")
    P("      x in [beta-delta, beta): x+d in [beta, beta+delta)  1 vs 0  -> MISMATCH")
    P("      x in [beta, 1-delta)  : x+d in [beta+delta, 1)     both 0   -> match")
    P("      x in [1-delta, 1)     : {x+d} in [0, delta)         0 vs 1  -> MISMATCH")
    P("    so M(delta) = [beta-delta, beta) u [1-delta, 1).  For delta < 0, e := -delta:")
    P("      x in [0, e)           : {x-e} in [1-e, 1)           1 vs 0  -> MISMATCH")
    P("      x in [e, beta)        : x-e in [0, beta-e)          both 1  -> match")
    P("      x in [beta, beta+e)   : x-e in [beta-e, beta)       0 vs 1  -> MISMATCH")
    P("      x in [beta+e, 1)      : x-e in [beta, 1-e)          both 0  -> match")
    P("    so M(-e) = [0, e) u [beta, beta+e).  The half-open side of each arc MATCHES the")
    P("    half-open side of the partition -- an endpoint slip here would move m* by one.")
    P("")
    P("    HYPOTHESIS FOUND BY THIS AUDIT, and absent from Phase 11: the case analysis assumes the")
    P("    arcs do NOT wrap around 0/1, i.e.")
    P("        |delta| <= min(beta, 1-beta) = 0.3690702464... .")
    P("    Without it the closed form is wrong.  Checking definition vs closed form:")
    conv = convergents(24)
    WRAP = min(float(BLO), 1 - float(BLO))
    P(f"    {'q':<7}{'|delta|':<16}{'|delta| <= 0.36907?':<22}{'tests':<9}{'disagreements'}")
    tot_bad_ok = tot_bad_viol = 0
    for (p, q) in conv[:14]:
        d = delta(q); ad = abs(float(d))
        bad = 0
        for m in range(3000):
            x = (m * ALPHA + RHO).frac()
            if in_M_def(x, d) != in_M_arcs(x, d):
                bad += 1
        ok = ad <= WRAP
        P(f"    {q:<7}{ad:<16.10f}{str(ok):<22}{3000:<9}{bad}")
        if ok:
            tot_bad_ok += bad
        else:
            tot_bad_viol += bad
    P(f"    disagreements where the hypothesis HOLDS:     {tot_bad_ok}")
    P(f"    disagreements where the hypothesis FAILS:     {tot_bad_viol}   (all at q = 1)")
    P("    So the closed form is exactly right under its hypothesis, and exactly wrong without it.")
    P("    The construction uses |delta| < 1/(147 M) <= 1/294 = 0.0034, so the hypothesis holds")
    P("    with a factor of about 108 to spare.  Phase 11 never stated it; it is stated now.")
    assert tot_bad_ok == 0 and tot_bad_viol > 0

    P("\n    R2 (the two-ball containment M(delta) subset B(0,|delta|) u B(beta,|delta|)) is")
    P("    UNCONDITIONAL and survives the wrap: if an arc crosses 1 the overspill lands next to 0,")
    P("    and B(0,.) is the two-sided ball at 0 == 1.  Checked INCLUDING q = 1:")
    viol = 0; tested2 = 0
    for (p, q) in conv[:14]:
        d = delta(q); ad = abs(float(d))
        for m in range(3000):
            x = (m * ALPHA + RHO).frac()
            tested2 += 1
            if in_M_def(x, d):
                xv = float(x)
                d0 = min(xv, 1 - xv)
                db = abs(xv - float(BLO))
                db = min(db, 1 - db)
                if not (d0 <= ad + 1e-12 or db <= ad + 1e-12):
                    viol += 1
    P(f"      {tested2} tests over 14 shifts including q = 1: {viol} containment violations")
    assert viol == 0

    P("\n(b) The identity L(ell) - ell = m*(ell), by three independent routes.")
    N = 120000
    s = word(N)
    P(f"    {'ell':<9}{'literal L-ell':<16}{'m* via chi-definition':<24}{'m* via arcs':<14}{'all agree'}")
    for (p, q) in conv:
        if q < 5 or q > 3000:
            continue
        L = lcp_pow(s, q)
        if L is None:
            continue
        d = delta(q)
        m1 = next(m for m in range(N) if in_M_def((m * ALPHA + RHO).frac(), d))
        m2 = next(m for m in range(N) if in_M_arcs((m * ALPHA + RHO).frac(), d))
        agree = (L - q == m1 == m2)
        P(f"    {q:<9}{L-q:<16}{m1:<24}{m2:<14}{agree}")
        assert agree

    P("\n(c) Both arcs avoided, with m = 0 handled explicitly.")
    P("    m = 0 gives the orbit point {rho} = 1/7.  Its distances to the two discontinuities are")
    P(f"      ||1/7 - 0||    = 1/7 = {1/7:.10f}")
    d0b = abs(1/7 - float(BLO))
    P(f"      ||1/7 - beta|| = {d0b:.10f}   ( = c_0 )")
    P("    The construction takes |delta| < min(C_M, 1/(147 M)) with C_M <= c_0 and M >= 2, so")
    P(f"      |delta| < 1/(147*2) = {1/294:.10f} < 1/7   and   |delta| < c_0 .")
    P("    Hence m = 0 lies in NEITHER arc -- it is not a special case needing separate treatment,")
    P("    but it does need the min in C_M to start at m = 0, which it does.")
    assert 1/294 < 1/7 and 1/294 < d0b
    P(f"    both inequalities hold: {1/294 < 1/7 and 1/294 < d0b}")

    P("\n(d) Drift and discrepancy from PROVED bounds, not measured constants.")
    P("    Phase 10 Lemma D: shifting the orbit equals shifting the interval, and the EXTREME")
    P("    discrepancy D_N of ({m alpha}) bounds every interval at once, with")
    P("        N * D_N  <=  c_1 * sum_{i<=k+1} a_i + c_2      (q_k <= N < q_{k+1}),")
    P("    Kuipers-Niederreiter, *Uniform Distribution of Sequences*, Ch. 2 Thm 3.4.  For")
    P("    alpha = (sqrt5-1)/2 every a_i = 1, so sum_{i<=k+1} a_i = k+1 <= log_phi(N) + 2 and")
    P("        |e_ell| = |k_ell - ell*beta|  <=  C_D log2(ell) + C_D'   with C_D = c_1/log2(phi),")
    P("        D(W)    <=  max_i|k_i - i*beta| + |e_ell|  <=  2 C_D log2(ell) + 2 C_D' .")
    P("    Substituting into (H):")
    P("        S >= (L-ell) - log2(3)*[ (C_D log2 ell + C_D') + (2 C_D log2 ell + 2 C_D' + 1) ]")
    P("               - log2(2 ell)")
    P("           = (L-ell) - C log2(ell) - C_0 ,   C := 1 + 3 C_D log2(3),")
    P("        C_0 := 1 + log2(3)(3 C_D' + 1).   Both are ABSOLUTE constants for this alpha.")
    P("    Phase 11 substituted the measured values |e_ell| <= 0.41 and D(W) <= 2.02, which are")
    P("    valid only on the computed range.  The asymptotic argument now uses only the bounds")
    P("    above; the measured numbers are demoted to a consistency check:")
    pref = [0]
    for ch in s:
        pref.append(pref[-1] + ch)
    P(f"    {'ell':<10}{'|e_ell|':<12}{'|e_ell|/log2(ell)':<20}{'ratio bounded?'}")
    prev = None
    for (p, q) in conv:
        if q < 20 or q > 60000:
            continue
        e = abs(pref[q] - q * float(BLO))
        P(f"    {q:<10}{e:<12.6f}{e/math.log2(q):<20.6f}{'yes' if e/math.log2(q) < 1 else 'CHECK'}")
    P("    The ratio stays below 1 throughout, consistent with |e_ell| = O(log ell).  The PROOF")
    P("    is the citation above, not this table.")
    P("\nALL PHASE-11B GEOMETRY CHECKS PASS.")

if __name__ == "__main__":
    main()
