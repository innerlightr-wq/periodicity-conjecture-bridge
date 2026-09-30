"""
Phase 8, step I: diagnostics for the ice = 2 boundary (unbounded partial quotients).

BHZ Theorem 1.1: X_alpha contains a sequence with ice(omega) = 2 exactly iff for each pair
(s,t) of positive integers with s > 1 there are only finitely many k with
(a_k,a_{k+1}) = (s,t) or (a_k,a_{k+1},a_{k+2}) = (1,1,t).  Every such alpha has unbounded
partial quotients.  BHZ Sec. 5.3 gives the explicit minimising (c_k).

At such an intercept the ODD-weight branch has margin exactly 0 (r_v = r_u/2 = 1).  The
EVEN-weight branch does not: at r_u = 2 the requirement is only r_u > max(1, gamma_V log2 3),
and sup_gamma [max(1,gamma log2 3) + gamma(1-gamma) log2 3] = log2 3 < 2, so the even branch
closes with NO discrepancy hypothesis and NO hypothesis on gamma at all.

So the whole unbounded-type question reduces to a PARITY question.  By BHZ Prop. 3.3 every
initial power of exponent >= 2 has root a cyclic permutation of
    tau_0^{a_1} o ... o tau_{k-1}^{a_k}(i)              (length q_k,               weight p_k)
 or tau_0^{a_1} o ... o tau_{k-1}^{a_k - c_k}(i)         (length q_k - c_k q_{k-1}, weight p_k - c_k p_{k-1})
(the weights are BHZ Lemma 2.6).  The even-weight branch is available at scale k iff that
weight is even.  This script measures how often it is.
"""
from fractions import Fraction
import math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase8_identities import q_bhz, bhz_terms, admissible

def pq_bhz(a):
    """BHZ convergents: p_0=0, q_0=1, p_1=1, q_1=a_1+1, then a_k recursion."""
    p = [0, 1]; q = [1, a[0] + 1]
    for k in range(2, len(a) + 1):
        p.append(a[k - 1] * p[k - 1] + p[k - 2])
        q.append(a[k - 1] * q[k - 1] + q[k - 2])
    return p, q

def bhz_minimiser(a):
    """BHZ Sec. 5.3's explicit (c_k) achieving ice = 2 when the Thm 1.1 condition holds."""
    c = []
    for k in range(1, len(a) + 1):
        ak = a[k - 1]
        a1 = a[k - 2] if k >= 2 else None
        a2 = a[k - 3] if k >= 3 else None
        if ak > 1 and a1 is not None and a1 > 1:
            ck = ak - 1
        elif ak > 1 and a1 == 1 and a2 == 1:
            ck = ak - 1
        elif ak > 1 and a1 == 1 and a2 is not None and a2 > 1:
            ck = ak
        elif ak == 1 and a1 is not None and a1 > 1:
            ck = 0
        elif ak == 1 and a1 == 1:
            ck = ak
        else:
            ck = max(0, ak - 1)
        c.append(max(0, min(ck, ak)))
    # repair the first few entries so the whole string is admissible
    for k in range(1, len(c) + 1):
        if c[k - 1] == a[k - 1] and k >= 2 and c[k - 2] != 0:
            c[k - 1] = a[k - 1] - 1
    return c

def thm11_ok(a, tail_from=3):
    """Does (a_k) satisfy BHZ Thm 1.1's condition on the tail?"""
    seen2 = {}; seen3 = {}
    for k in range(tail_from, len(a) - 2):
        s, t = a[k - 1], a[k]
        if s > 1:
            seen2[(s, t)] = seen2.get((s, t), 0) + 1
        if a[k - 1] == 1 and a[k] == 1:
            seen3[a[k + 1]] = seen3.get(a[k + 1], 0) + 1
    return (max(seen2.values(), default=0) <= 1) and (max(seen3.values(), default=0) <= 1)

def main():
    print("=" * 78)
    print("PHASE 8 / I.  The ice = 2 boundary: where the method dies, and what survives")
    print("=" * 78)

    print("\n1)  Even-branch threshold at r_u = 2, with the UNCONDITIONAL discrepancy cap.")
    L = math.log2(3)
    worst = max((max(1, g * L) + g * (1 - g) * L, g)
                for g in [i / 20000 for i in range(1, 20001)])
    print(f"    sup_gamma [ max(1, gamma log2 3) + gamma(1-gamma) log2 3 ] = {worst[0]:.6f}"
          f"  at gamma = {worst[1]:.4f}")
    print(f"    log2 3 = {L:.6f} < 2, so the even branch keeps margin >= 2 - log2 3 ="
          f" {2 - L:.6f} at r_u = 2 exactly,")
    print("    with NO discrepancy hypothesis and NO hypothesis on gamma.  The odd branch has")
    print("    r_v = r_u/2 = 1 exactly, i.e. margin 0.  So the boundary is a PARITY question.")
    assert abs(worst[0] - L) < 1e-4

    print("\n2)  Explicit ice = 2 slopes (BHZ Thm 1.1) and the BHZ Sec. 5.3 minimiser.")
    families = [
        ("a_k = k            ", [k for k in range(1, 40)]),
        ("a_k = k^2          ", [k * k for k in range(1, 30)]),
        ("a_k = 2^k          ", [2 ** k for k in range(1, 22)]),
        ("a_k = k, one 1 each", [1 if k % 3 == 0 else k for k in range(1, 40)]),
    ]
    print(f"    {'slope digits':<22}{'Thm1.1 cond':<13}{'ice tail (last 8 k)':<21}"
          f"{'x(k) tail max':<15}{'y(k) tail max'}")
    rows = []
    for nm, a in families:
        c = bhz_minimiser(a)
        if not admissible(a, c):
            print(f"    {nm:<22}{'-':<13}minimiser not admissible; skipped")
            continue
        terms, q, _ = bhz_terms(a, c)
        ks = [k for k in terms if k > len(a) - 9]
        xm = max(terms[k][0] for k in ks)
        ym = max(terms[k][2] for k in ks if terms[k][2] is not None)
        ice = max(xm, ym)
        print(f"    {nm:<22}{str(thm11_ok(a)):<13}{float(ice):<21.10f}"
              f"{float(xm):<15.10f}{float(ym):.10f}")
        rows.append((nm, a, c))
    print("    (ice sits at or just above 2: these are the slopes where the margin vanishes.)")

    print("\n3)  Weight parity of the witness roots (BHZ Lemma 2.6: weights are p_k and")
    print("    p_k - c_k p_{k-1}).  The even branch is available at scale k iff even.")
    print(f"    {'slope digits':<22}{'k range':<12}{'x-roots even':<14}{'y-roots even':<14}"
          f"{'either even':<13}{'longest all-odd run'}")
    for nm, a, c in rows:
        p, q = pq_bhz(a)
        kx = [k for k in range(3, len(a)) if p[k] % 2 == 0]
        ky = [k for k in range(3, len(a)) if (p[k] - c[k - 1] * p[k - 1]) % 2 == 0]
        either = sorted(set(kx) | set(ky))
        ks = list(range(3, len(a)))
        run = best = 0
        for k in ks:
            if k in either:
                run = 0
            else:
                run += 1; best = max(best, run)
        print(f"    {nm:<22}{f'3..{len(a)-1}':<12}{f'{len(kx)}/{len(ks)}':<14}"
              f"{f'{len(ky)}/{len(ks)}':<14}{f'{len(either)}/{len(ks)}':<13}{best}")

    print("\n4)  Can the even branch be unavailable forever?  YES, but only on a thin family.")
    print("    p_{k+1} = a_{k+1} p_k + p_{k-1} with p_0 = 0, p_1 = 1.  So p_2 = a_2, and once")
    print("    (p_{k-1},p_k) = (1,1) the next is odd iff a_{k+1} is even.  Hence")
    print("        p_k odd for every k >= 1   <=>   a_2 odd and a_k even for all k >= 3.")
    print("    (Note p_2 = a_2, so an all-even digit string fails immediately: p_2 is even.)")
    def p_parities(a, K):
        p0, p1 = 0, 1
        out = [p1]
        for k in range(2, K):
            p0, p1 = p1, (a[k - 1] * p1 + p0)
            out.append(p1 % 2)
        return out
    tests = [("a_2 odd then all even  ", [3, 1] + [2] * 24, True),
             ("all digits even        ", [2] * 26, False),
             ("a_2 odd, one odd later ", [3, 1, 2, 2, 3] + [2] * 21, False),
             ("a_k = k                ", list(range(1, 27)), False)]
    print(f"    {'digit string':<26}{'p_k odd for all k<=25?':<25}{'predicted'}")
    for nm, a, pred in tests:
        allodd = all(x % 2 == 1 for x in p_parities(a, 26))
        print(f"    {nm:<26}{str(allodd):<25}{pred}")
        assert allodd == pred, (nm, allodd, pred)
    print("    So at intercept 0 the even branch CAN be unavailable at every scale -- exactly the")
    print("    single bad cycle the Phase 3 automaton found.  At a general intercept the y-roots")
    print("    have weight p_k - c_k p_{k-1}, so an odd c_k with p_{k-1} odd flips the parity:")
    print("    general intercepts have strictly more even-weight opportunities than intercept 0.")

    print("\n4b) The quantitative route: an EXACT identity for the odd-branch surplus driver.")
    print("    For EVERY k and EVERY admissible (c_k), bounded type or not, the y-witness has")
    print("        ell_k = q_{k-1}(lam_{k-1} + d_k),   E_k = y(k) - 2 = lam_{k-1}(m_{k-1}-1)/(lam_{k-1}+d_k),")
    print("    so the root length and the denominator cancel EXACTLY:")
    print("        ell_k * E_k = q_{k-1} lam_{k-1} (m_{k-1} - 1) = q_{k-2} * (m_{k-1} - 1).")
    print("    On a keep-one tail (d_{k-1} = 1) this is q_{k-2} lam_{k-2} m_{k-2} = q_{k-3} m_{k-2}.")
    print("    Since m_{k-2} >= 1 this is >= q_{k-3} -> infinity, EVEN WHEN E_k -> 0.  The odd")
    print("    branch therefore survives ice = 2 provided  q_{k-3} m_{k-2}  beats the penalties")
    print("    ceil(D(R_k)) log2 3 + log2(2 ell_k).  Measured:")
    print(f"    {'slope':<20}{'k':<4}{'ell_k':>14}{'ell_k*E_k (exact)':>19}{'q_(k-3)':>12}"
          f"{'log2(2 ell_k)':>14}{'sum a_i':>10}{'ratio vs log':>13}")
    from phase8_identities import reform_terms
    for nm, a, c in rows:
        lam, d, m, t, q = reform_terms(a, c)
        terms, _, _ = bhz_terms(a, c)
        p, _ = pq_bhz(a)
        for k in [len(a) - 6, len(a) - 3]:
            if k < 6 or k not in terms or terms[k][2] is None:
                continue
            ell = q[k] - c[k - 1] * q[k - 1]
            E = terms[k][2] - 2
            prod = ell * E
            ident = q[k - 2] * (m[k - 1] - 1)                     # general identity
            ident2 = q[k - 3] * m[k - 2] if d[k - 1] == 1 else None  # keep-one tail form
            suma = sum(a[:k])
            lg = math.log2(2 * float(ell)) if ell < 10 ** 300 else float(int(ell).bit_length())
            print(f"    {nm.strip():<20}{k:<4}{float(ell):>14.4g}{float(prod):>19.6g}"
                  f"{float(q[k-3]):>12.4g}{lg:>14.2f}{suma:>10}{float(prod)/lg:>13.4g}")
            assert prod == ident, ("general identity", nm, k, float(prod), float(ident))
            if ident2 is not None:
                assert prod == ident2, ("keep-one form", nm, k, float(prod), float(ident2))
    print("    ell_k*E_k = q_(k-2)*(m_(k-1)-1) asserted exactly at every k tested (general form),")
    print("    and = q_(k-3)*m_(k-2) wherever d_(k-1) = 1.")

    # exhaustive check of the general identity, all admissible (c_k), several slopes
    import itertools
    from phase8_identities import admissible as _adm
    nchk = 0
    for a in ([2]*9, [3]*8, [1,2]*4, [1,3,2,1,2,3,1,2], [4,1,2,3,1,2,2,1]):
        lamq = q_bhz(a)
        for cc in itertools.product(*[range(x + 1) for x in a]):
            cc = list(cc)
            if not _adm(a, cc):
                continue
            lam, d, m, t, q = reform_terms(a, cc)
            terms, _, _ = bhz_terms(a, cc)
            for k in range(2, len(a)):
                if k not in terms or terms[k][2] is None:
                    continue
                ell = q[k] - cc[k - 1] * q[k - 1]
                assert ell * (terms[k][2] - 2) == q[k - 2] * (m[k - 1] - 1), (a, cc, k)
                nchk += 1
    print(f"    Exhaustive: {nchk} (slope, admissible digit string, k) instances of the general")
    print("    identity across 5 slopes -- no exception.")
    print("    Verdict: the surplus driver grows like q_(k-3), the penalty like log2 q_(k-1) plus")
    print("    the discrepancy.  For polynomially or exponentially growing partial quotients the")
    print("    driver wins easily; it can only lose if the partial quotients grow so fast that")
    print("    log q_{k-1} outruns q_{k-3}, i.e. log a_{k-1} >> q_{k-3}.")

    print("\n5)  The reduced target, stated exactly:")
    print("    (E)  For every Sturmian word u (ANY slope, ANY intercept), are there infinitely")
    print("         many initial powers W^r of u with r >= 2 and |W|_1 EVEN?")
    print("    If (E) holds, then Phi(v) not in Q for both CS Rote lifts of EVERY Sturmian word,")
    print("    with no bounded-type hypothesis anywhere -- the p(n) = 2n rung closes completely.")
    print("    (E) is a parity statement about p_k and p_k - c_k p_{k-1}, i.e. about convergent")
    print("    NUMERATORS and Ostrowski digits -- elementary arithmetic, not new combinatorics.")
    print("\nALL ICE-2 BOUNDARY CHECKS PASS.")

if __name__ == "__main__":
    main()
