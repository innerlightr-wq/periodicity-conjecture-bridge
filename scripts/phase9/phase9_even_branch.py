"""
Phase 9, step C: the even branch on the hostile family -- exact integer surplus, the
gamma-dependent UNCONDITIONAL threshold, and an adversarial search for slopes that defeat it.

THE UNCONDITIONAL EVEN-BRANCH THRESHOLD.  For a root W of length ell and weight w, gamma_W := w/ell:
    log2 F(W) <= log2 ell + ceil(D(W)) log2 3 + max(ell, w log2 3)          [Phase 1/2 height bound]
    D(W)      <= gamma_W (1 - gamma_W) ell                                  [combinatorial cap, any word]
so with L_v = L_u + 1 = r ell + 1 and target root V (even weight, so the even branch),
    S >= ell * [ r - g(gamma_W) ] - log2 ell - log2 3,
    g(gamma) := max(1, gamma log2 3) + gamma (1 - gamma) log2 3 .
g is continuous, g(gamma) < log2 3 = 1.58496 for every gamma < 1, g(1/2) = 1.39624, and
g -> 1 as gamma -> 0.  So  r > g(gamma_W)  suffices, with NO discrepancy hypothesis and NO
hypothesis on the slope -- in particular no bounded-type and no growth condition.

This is strictly weaker than the uniform threshold log2 3 used in Phase 8 and is the
"sharper height estimate exploiting the actual root structure" the Phase 9 task asks for.
Everything below is exact (Fraction / big integers); F(V) is computed exactly, so the exact
surplus test does not rely on the bound at all.
"""
from fractions import Fraction
import itertools, math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import (convergents, admissible, stream, certified_prefix,
                                   lcp_pow, LOG23)
from phase9_intermediate_roots import c_W, F_of, log2_int, rote

L3 = Fraction(LOG23).limit_denominator(10 ** 12)

def g_of(gamma):
    """The unconditional even-branch threshold, exact in Fraction arithmetic."""
    return max(Fraction(1), gamma * L3) + gamma * (1 - gamma) * L3

def gamma_bracket(a):
    """gamma = [0; a_1+1, a_2, ...] as a Fraction bracket from the last two convergents."""
    p, q = convergents(a)
    lo, hi = Fraction(p[-2], q[-2]), Fraction(p[-1], q[-1])
    return (min(lo, hi), max(lo, hi))

def roots(a, c, maxlen=150000):
    om, K = certified_prefix(a, c, maxlen)
    u = [int(ch) for ch in om]
    p, q = convergents(a)
    st = stream(a, c)
    out = []
    for k in range(3, K + 1):
        for dd in range(1, a[k - 1] + 1):
            ell = dd * q[k - 1] + q[k - 2]
            L = lcp_pow(u, ell)
            if L is None:
                continue
            w = dd * p[k - 1] + p[k - 2]
            assert w == sum(u[:ell])
            r = Fraction(L, ell)
            gam = Fraction(w, ell)
            out.append(dict(k=k, d=dd, ell=ell, w=w, par=w % 2, r=r, L=L, gam=gam,
                            g=g_of(gam), clears=(r > g_of(gam)),
                            kind=("x" if dd == a[k-1] else "") + ("y" if dd == st["d"][k] else "") or "int"))
    return out, u, K

def exact_even_surplus(u, ell, L, seed):
    W = u[:ell]
    assert sum(W) % 2 == 0, "even branch requires even weight"
    v = rote(u, seed)
    V = v[:ell]
    Lv = lcp_pow(v, ell)
    if Lv is None:
        return None
    F = F_of(V)
    # discrepancy of V against its own density, exact, via integers: max |ell*k_i - i*w| / ell
    w = sum(V); run = 0; best = 0
    for i in range(ell + 1):
        if i and V[i - 1]:
            run += 1
        t = abs(ell * run - i * w)
        if t > best:
            best = t
    D = Fraction(best, ell)
    cap = Fraction(w * (ell - w), ell)              # gamma(1-gamma)*ell, exact
    return dict(Lv=Lv, transfer=(Lv == L + 1), S=Lv - log2_int(F), pos=((1 << Lv) > F),
                D=D, cap=cap)

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / C.  The even branch: exact surplus, sharpened threshold, adversarial search")
    P("=" * 78)
    P(f"    g(gamma) = max(1, gamma log2 3) + gamma(1-gamma) log2 3     [unconditional]")
    for gv in (Fraction(1,10), Fraction(1,5), Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(9,10)):
        P(f"      g({float(gv):.4f}) = {float(g_of(gv)):.6f}")
    P(f"      uniform Phase-8 bound was log2 3 = {LOG23:.6f}; g is strictly below it for gamma<1.")

    hostile = [
        ("[3,1,2,2,2,...]     ", [3, 1] + [2] * 14),
        ("[5,3,2,2,2,...]     ", [5, 3] + [2] * 13),
        ("[3,1,2,4,2,4,...]   ", [3, 1] + [2, 4] * 7),
        ("[3,1,4,4,4,...]     ", [3, 1] + [4] * 10),
        ("[3,1,2,4,6,8,...]   ", [3, 1] + [2, 4, 6, 8, 10, 12, 14]),
        ("[3,1,8,8,8,...]     ", [3, 1] + [8] * 7),
        ("[3,1,16,16,16,...]  ", [3, 1] + [16] * 5),
        ("[3,1,2,2,64,2,2,64] ", [3, 1] + [2, 2, 64] * 3),
        ("[3,1,100,2,100,2]   ", [3, 1] + [100, 2] * 3),
    ]
    intercepts = [
        ("c=0       (d_k=a_k even)", lambda a: [0] * len(a)),
        ("c=a_k-2   (d_k=2  even)", lambda a: [max(0, x - 2) for x in a]),
        ("keep-one  (d_k=1  odd) ", lambda a: [max(0, x - 1) for x in a]),
    ]

    P("\nC1  Adversarial search: is there an even-weight root with r > g(gamma) at large k?")
    P(f"    {'slope':<22}{'intercept':<25}{'gamma~':<9}{'k range':<10}"
      f"{'even-wt roots':<15}{'clearing g':<12}{'best (r - g)':<14}{'largest k clearing'}")
    fails = []
    keep = []
    for snm, a in hostile:
        glo, ghi = gamma_bracket(a)
        p, q = convergents(a)
        assert all(p[k] % 2 == 1 for k in range(1, len(a) + 1)), ("not all-odd numerators", snm)
        for inm, cf in intercepts:
            c = cf(a)
            if not admissible(a, c):
                continue
            rs, u, K = roots(a, c)
            ev = [r for r in rs if r["par"] == 0]
            cl = [r for r in ev if r["clears"]]
            best = max((r["r"] - r["g"] for r in ev), default=None)
            kmax = max((r["k"] for r in cl), default=None)
            krange = f"{min(r['k'] for r in rs)}..{max(r['k'] for r in rs)}" if rs else "-"
            P(f"    {snm:<22}{inm:<25}{float(glo):<9.5f}{krange:<10}{len(ev):<15}{len(cl):<12}"
              f"{float(best) if best is not None else float('nan'):<14.6f}{kmax}")
            if not cl:
                fails.append((snm, inm))
            keep.append((snm, inm, rs, u))
    P(f"\n    slope/intercept pairs with NO even-weight root clearing g: {len(fails)}")
    if fails:
        for f_ in fails:
            P(f"      {f_}")

    P("\nC2  Which d supplies it, and does it persist to every large k?")
    P(f"    {'slope':<22}{'intercept':<25}{'k':<4}{'d':<4}{'kind':<6}{'ell':<10}"
      f"{'gamma_W':<10}{'r':<10}{'g':<10}{'r-g'}")
    for snm, inm, rs, u in keep[:6]:
        ks = sorted({r["k"] for r in rs})[-3:]
        for k in ks:
            cand = [r for r in rs if r["k"] == k and r["par"] == 0 and r["clears"]]
            if not cand:
                P(f"    {snm:<22}{inm:<25}{k:<4}  -- no even-weight root clears g at this k --")
                continue
            r = max(cand, key=lambda z: z["r"] - z["g"])
            P(f"    {snm:<22}{inm:<25}{r['k']:<4}{r['d']:<4}{r['kind']:<6}{r['ell']:<10}"
              f"{float(r['gam']):<10.6f}{float(r['r']):<10.6f}{float(r['g']):<10.6f}"
              f"{float(r['r']-r['g']):.6f}")

    P("\nC3  EXACT integer surplus on the even branch at those roots (no bound used).")
    P(f"    {'slope':<22}{'intercept':<25}{'k':<4}{'d':<4}{'ell':<9}{'w':<9}"
      f"{'S (exact)':<12}{'2^Lv>F':<8}{'D(V)':<9}{'cap':<9}{'D<=cap'}")
    shown = 0
    nS = []
    for snm, inm, rs, u in keep:
        cand = sorted([r for r in rs if r["par"] == 0 and r["clears"] and r["ell"] >= 60],
                      key=lambda z: z["ell"])[-3:]
        for r in cand:
            for seed in (0, 1):
                res = exact_even_surplus(u, r["ell"], r["L"], seed)
                if res is None:
                    continue
                assert res["transfer"], ("transfer", snm, inm, r["k"])
                assert res["pos"], ("exact surplus not positive", snm, inm, r["k"], res["S"])
                assert res["D"] <= res["cap"], ("combinatorial cap violated", snm, r["k"])
                nS.append(res["S"])
                if seed == 0 and shown < 18:
                    P(f"    {snm:<22}{inm:<25}{r['k']:<4}{r['d']:<4}{r['ell']:<9}{r['w']:<9}"
                      f"{res['S']:<12.2f}{str(res['pos']):<8}{float(res['D']):<9.2f}"
                      f"{float(res['cap']):<9.1f}{res['D'] <= res['cap']}")
                    shown += 1
    P(f"\n    {len(nS)} exact even-branch surplus evaluations (both seeds); every one POSITIVE,")
    P(f"    every transfer L_v = L_u + 1 exact, every combinatorial discrepancy cap respected.")
    P(f"    min S = {min(nS):.2f}, max S = {max(nS):.2f}")

    P("\nC4  Growth in ell along one hostile slope, even branch (exact).")
    a = [3, 1] + [2] * 16
    c = [0] * len(a)
    rs, u, K = roots(a, c, maxlen=120000)
    P(f"    slope [3,1,2,2,2,...], intercept c = 0, gamma ~ {float(gamma_bracket(a)[0]):.6f}")
    P(f"    {'k':<4}{'d':<4}{'ell':<9}{'w':<9}{'r':<10}{'g':<10}{'ell*(r-g)':<12}{'S (exact)'}")
    for r in sorted([z for z in rs if z["par"] == 0 and z["clears"]], key=lambda z: z["ell"]):
        if r["ell"] < 20 or r["ell"] > 2600:
            continue
        res = exact_even_surplus(u, r["ell"], r["L"], 0)
        if res is None:
            continue
        P(f"    {r['k']:<4}{r['d']:<4}{r['ell']:<9}{r['w']:<9}{float(r['r']):<10.6f}"
          f"{float(r['g']):<10.6f}{float(r['ell']*(r['r']-r['g'])):<12.1f}{res['S']:.2f}")
    P("\nALL STEP-C CHECKS PASS.")

if __name__ == "__main__":
    main()
