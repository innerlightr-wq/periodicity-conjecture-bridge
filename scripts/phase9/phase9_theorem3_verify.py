"""
Phase 9, step G: end-to-end verification of THEOREM 3 and its corollaries.

THEOREM 3.  gamma irrational, NO hypothesis on its partial quotients.  u any Sturmian word of
slope gamma (any intercept, either convention).  If infinitely many k >= 3 satisfy
    (i)   0 < c_k < a_k
    (ii)  d_{k-1} >= 1
    (iii) d_k p_{k-1} + p_{k-2}  even
then Phi(v) not in Q for either CS Rote lift (either seed) and every shift.

This script, for each tested (slope, intercept):
  * checks (i),(ii),(iii) at each k;
  * at the qualifying k, verifies LITERALLY that the prefix of length ell_k is the root of an
    attained power of exponent y(k) >= 2 with the predicted EVEN weight;
  * performs the XOR transfer at both seeds and verifies L_v = L_u + 1 exactly;
  * evaluates F(V) EXACTLY (no bound) and asserts 2^{L_v} > F(V), plus the growth of S;
  * confirms the theorem's own inequality S >= ell*(y(k) - g(gamma_V)) - log2 ell - log2 3.
"""
from fractions import Fraction
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import (convergents, admissible, stream, certified_prefix,
                                   lcp_pow, LOG23)
from phase9_even_branch import g_of, gamma_bracket
from phase9_intermediate_roots import F_of, log2_int, rote

L3 = Fraction(LOG23).limit_denominator(10 ** 12)

def theorem3_scales(a, c):
    p, q = convergents(a)
    st = stream(a, c)
    out = []
    for k in range(3, len(a) - 1):
        if k not in st["y"]:
            continue
        if not (0 < c[k - 1] < a[k - 1]):
            continue                                  # (i)
        if st["d"][k - 1] < 1:
            continue                                  # (ii)
        w = st["d"][k] * p[k - 1] + p[k - 2]
        if w % 2 != 0:
            continue                                  # (iii)
        out.append((k, st["d"][k] * q[k - 1] + q[k - 2], w, st["y"][k]))
    return out

def verify(a, c, maxlen=400000, ellcap=2600):
    om, K = certified_prefix(a, c, maxlen)
    u = [int(ch) for ch in om]
    rows = []
    for (k, ell, w, yk) in theorem3_scales(a, c):
        if ell + 2 >= len(u) or ell > ellcap:
            continue
        L = lcp_pow(u, ell)
        if L is None:
            continue
        assert sum(u[:ell]) == w, ("weight law (W-y) violated", a, c, k)
        assert w % 2 == 0
        assert Fraction(L, ell) == yk, ("exponent != y(k)", a, c, k, L, ell, yk)
        assert yk >= 2, ("y(k) < 2", a, c, k)
        for seed in (0, 1):
            v = rote(u, seed)
            V = v[:ell]
            Lv = lcp_pow(v, ell)
            if Lv is None:
                continue
            assert Lv == L + 1, ("transfer", a, c, k, seed)
            F = F_of(V)
            S = Lv - log2_int(F)
            assert (1 << Lv) > F, ("exact surplus not positive", a, c, k, seed, S)
            gam = Fraction(sum(V), ell)
            bound = float(ell) * (float(yk) - float(g_of(gam))) - math.log2(ell) - LOG23
            assert S >= bound - 1e-6, ("theorem inequality violated", a, c, k, seed, S, bound)
            rows.append(dict(k=k, ell=ell, w=w, y=yk, seed=seed, S=S, gam=gam,
                             g=g_of(gam), bound=bound))
    return rows

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / G.  End-to-end verification of Theorem 3")
    P("=" * 78)

    fams = [
        ("Cor 3.1: a=[3,1] + even, keep-one   ", [3, 1] + [2, 4, 6, 8, 2, 4, 6, 8, 2, 4],
                                                 lambda a: [max(0, x - 1) for x in a]),
        ("Cor 3.1: a=[5,3] + even, keep-one   ", [5, 3] + [4, 2, 8, 2, 4, 6, 2, 4],
                                                 lambda a: [max(0, x - 1) for x in a]),
        ("Cor 3.2 UNBOUNDED: a_k=2k, keep-one ", [3, 1] + [2 * k for k in range(2, 12)],
                                                 lambda a: [max(0, x - 1) for x in a]),
        ("Cor 3.2 UNBOUNDED: a_k=2^k, keep-one", [3, 1] + [2 ** k for k in range(2, 9)],
                                                 lambda a: [max(0, x - 1) for x in a]),
        ("UNBOUNDED a_k=k, c=a_k-2            ", list(range(1, 15)),
                                                 lambda a: [max(0, x - 2) for x in a]),
        ("UNBOUNDED a_k=k!, c=a_k-2           ", [math.factorial(i) for i in range(1, 9)],
                                                 lambda a: [max(0, x - 2) for x in a]),
        ("bounded control a_k in {1,2,3}, rand", [2, 1, 3, 2, 1, 1, 3, 2, 2, 1, 3, 2, 1, 3],
                                                 lambda a: [max(0, x - 1) for x in a]),
    ]
    P(f"\n    {'family':<38}{'sup a_k':<10}{'#Thm3 scales':<14}{'#exact checks':<15}"
      f"{'min S':<11}{'max S'}")
    tot = 0
    for nm, a, cf in fams:
        c = cf(a)
        if not admissible(a, c):
            P(f"    {nm:<38}intercept not admissible")
            continue
        sc = theorem3_scales(a, c)
        rows = verify(a, c)
        tot += len(rows)
        P(f"    {nm:<38}{max(a):<10}{len(sc):<14}{len(rows):<15}"
          f"{(min(r['S'] for r in rows) if rows else float('nan')):<11.2f}"
          f"{(max(r['S'] for r in rows) if rows else float('nan')):.2f}")
    P(f"\n    {tot} exact end-to-end verifications; every assertion holds:")
    P("      weight law (W-y) exact, exponent == y(k) >= 2, transfer L_v = L_u + 1,")
    P("      2^{L_v} > F(V) as exact integers, and S >= ell(y(k) - g(gamma_V)) - log2 ell - log2 3.")

    P("\n    Growth along one UNBOUNDED-type family (a_k = 2k, keep-one):")
    a = [3, 1] + [2 * k for k in range(2, 12)]
    c = [max(0, x - 1) for x in a]
    rows = verify(a, c, maxlen=900000, ellcap=2600)
    P(f"    {'k':<4}{'a_k':<6}{'ell':<8}{'w':<8}{'y(k)':<12}{'gamma_V':<10}{'g':<10}"
      f"{'theorem bound':<15}{'S (exact)'}")
    for r in [z for z in rows if z["seed"] == 0]:
        P(f"    {r['k']:<4}{a[r['k']-1]:<6}{r['ell']:<8}{r['w']:<8}{float(r['y']):<12.6f}"
          f"{float(r['gam']):<10.6f}{float(r['g']):<10.6f}{r['bound']:<15.2f}{r['S']:.2f}")
    P("\n    sup_k a_k = %d, i.e. UNBOUNDED partial quotients -- outside Phase 8 Theorem 2." % max(a))
    P("\nALL THEOREM-3 VERIFICATIONS PASS.")

if __name__ == "__main__":
    main()
