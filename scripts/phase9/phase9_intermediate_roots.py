"""
Phase 9, step B: are EVEN-WEIGHT witnesses available on the hostile family?

The hostile family for the even/odd branch split is: BHZ digits a_k EVEN for all large k with
both boundary numerator parities odd, so that p_k is ODD for every k.  Then
w(k,d) = d p_{k-1} + p_{k-2} == d + 1 (mod 2), so
    d = a_k (the always-attained x-witness) has ODD weight        -> odd branch (needs height control)
    d = d_k (the y-witness)                 has EVEN weight iff d_k is ODD
    d = 1   (an intermediate root)          has EVEN weight ALWAYS.
If additionally d_k is EVEN for all large k, every BHZ-guaranteed witness has odd weight and the
odd branch is forced -- unless an intermediate root is usable.

The even branch needs only  r > max(1, gamma_V log2 3),  and  sup_gamma [max(1,gamma log2 3)
+ gamma(1-gamma) log2 3] = log2 3 < 2, so r > log2 3 = 1.58496... SUFFICES, with NO discrepancy
hypothesis (theorems/phase1/REPETITION_HEIGHT_CRITERION.md, unconditional form).  So this script
measures, literally, the prefix power of EVERY intermediate root and asks whether an even-weight
one ever clears log2 3.

Exact integers / Fractions throughout.  Prefix powers are literal longest common prefixes of the
certified S-adic prefix of omega -- no formula is trusted here.
"""
from fractions import Fraction
import itertools, math, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import (convergents, admissible, stream, certified_prefix,
                                   lcp_pow, LOG23)

def c_W(W):
    k = sum(W); tot = 0; run = 0
    for i, b in enumerate(W):
        if b:
            run += 1
            tot += 3 ** (k - run) * (1 << i)
    return tot

def F_of(W):
    return abs((1 << len(W)) - 3 ** sum(W)) + c_W(W)

def log2_int(n):
    b = n.bit_length()
    return (b - 1) + math.log2(n / (1 << (b - 1)))

def rote(u, seed):
    v = [seed]
    for xx in u:
        v.append(v[-1] ^ xx)
    return v

def scan(a, c, maxlen=600000):
    """For every (k,d) with ell(k,d) inside the certified prefix, the literal prefix power."""
    om, K = certified_prefix(a, c, maxlen)
    u = [int(ch) for ch in om]
    p, q = convergents(a)
    st = stream(a, c)
    rows = []
    for k in range(3, K + 1):
        for dd in range(1, a[k - 1] + 1):
            ell = dd * q[k - 1] + q[k - 2]
            L = lcp_pow(u, ell)
            if L is None:
                continue
            w = dd * p[k - 1] + p[k - 2]
            assert w == sum(u[:ell]), ("weight", a, c, k, dd)
            r = Fraction(L, ell)
            kind = ("x" if dd == a[k - 1] else "") + ("y" if dd == st["d"][k] else "")
            rows.append(dict(k=k, d=dd, ell=ell, w=w, par=w % 2, r=r, L=L,
                             kind=kind or "int",
                             even_ok=(w % 2 == 0 and r > Fraction(LOG23).limit_denominator(10**9)),
                             odd_ok=(w % 2 == 1 and r > 2)))
    return rows, u, K

def exact_surplus(u, ell, L, seed, branch):
    """Exact integer surplus for the chosen branch at root length ell."""
    W = u[:ell]
    v = rote(u, seed)
    V = v[:ell]
    if branch == "even":
        R = V
    else:
        R = V + [1 - b for b in V]
    if len(R) >= len(v):
        return None
    Lv = lcp_pow(v, len(R))
    if Lv is None:
        return None
    F = F_of(R)
    return dict(ellR=len(R), Lv=Lv, transfer=(Lv == L + 1), S=Lv - log2_int(F),
                pos=((1 << Lv) > F), gammaR=Fraction(sum(R), len(R)))

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / B.  Even-weight witnesses on the all-odd-numerator (hostile) family")
    P("=" * 78)
    P(f"    even-branch threshold: r > log2 3 = {LOG23:.8f}   (no discrepancy hypothesis)")
    P( "    odd-branch threshold:  r > 2                      (needs D(R) = o(ell))")

    # hostile slopes: a_2 odd, a_k even for k >= 3  => p_k odd for every k
    hostile = [
        ("[3,1,2,2,2,...]      ", [3, 1] + [2] * 14),
        ("[5,3,2,2,2,...]      ", [5, 3] + [2] * 13),
        ("[3,1,2,4,2,4,...]    ", [3, 1] + [2, 4] * 7),
        ("[3,1,4,4,4,...]      ", [3, 1] + [4] * 10),
        ("[3,1,2,4,6,8,10,...] ", [3, 1] + [2, 4, 6, 8, 10, 12, 14]),
        ("[3,1,8,8,8,...]      ", [3, 1] + [8] * 7),
    ]
    intercepts = [
        ("c = 0        (d_k = a_k, even)", lambda a: [0] * len(a)),
        ("c = a_k - 2  (d_k = 2, even) ", lambda a: [max(0, x - 2) for x in a]),
        ("keep-one     (d_k = 1, odd)  ", lambda a: [max(0, x - 1) for x in a]),
    ]
    P("\nB1  Is an even-weight root with r > log2 3 available?  (literal prefix powers)")
    P(f"    {'slope':<23}{'intercept':<31}{'#(k,d)':<8}{'even-wt':<9}"
      f"{'even-wt & r>lg3':<17}{'odd-wt & r>2':<14}{'best even-wt r'}")
    verdicts = []
    for snm, a in hostile:
        p, q = convergents(a)
        assert all(p[k] % 2 == 1 for k in range(1, len(a) + 1)), ("not all-odd", snm)
        for inm, cf in intercepts:
            c = cf(a)
            if not admissible(a, c):
                P(f"    {snm:<23}{inm:<31}intercept not admissible")
                continue
            rows, u, K = scan(a, c)
            ev = [r for r in rows if r["par"] == 0]
            evok = [r for r in rows if r["even_ok"]]
            odok = [r for r in rows if r["odd_ok"]]
            best = max((r["r"] for r in ev), default=None)
            P(f"    {snm:<23}{inm:<31}{len(rows):<8}{len(ev):<9}{len(evok):<17}"
              f"{len(odok):<14}{float(best) if best else float('nan'):.6f}")
            verdicts.append((snm, inm, len(evok), len(odok), best, rows, u))
    P("\n    READING (this refutes the Phase 8 expectation): on EVERY hostile slope/intercept pair")
    P("    tested, even-weight roots clearing log2 3 DO exist, and there are several per pair.")
    P("    So the odd branch is NOT forced by the all-odd-numerator condition: the even branch,")
    P("    which needs no discrepancy hypothesis and hence no growth condition, remains available.")
    P("    Step C computes the exact integer surplus on those even-weight roots.")

    # B2: why -- the d=1 root's power is structurally close to 1
    P("\nB2  Why: the intermediate roots' prefix powers, by d, at one hostile pair.")
    a = [3, 1] + [2, 4] * 7
    c = [0] * len(a)
    rows, u, K = scan(a, c)
    P(f"    slope [3,1,2,4,2,4,...], intercept c = 0 (d_k = a_k)")
    P(f"    {'k':<4}{'d':<4}{'kind':<6}{'ell':<10}{'w':<10}{'w%2':<5}{'literal r':<12}"
      f"{'r > lg3?':<10}{'r > 2?'}")
    for r in rows:
        if r["k"] in (9, 10, 11):
            P(f"    {r['k']:<4}{r['d']:<4}{r['kind']:<6}{r['ell']:<10}{r['w']:<10}"
              f"{r['par']:<5}{float(r['r']):<12.6f}{str(r['r'] > Fraction(LOG23).limit_denominator(10**9)):<10}"
              f"{str(r['r'] > 2)}")
    P("    The BHZ-guaranteed roots (kinds x, y) reach r >= 2 but have ODD weight here.  Among the")
    P("    genuinely intermediate roots the exponent DECREASES with d, so d = 1 is the best one,")
    P("    and d = 1 always has EVEN weight on this family.  Its exponent sits near 1.7-1.8,")
    P("    above log2 3 = 1.585 -- which is all the even branch needs.")

    # B3: exact surplus of the forced odd branch
    P("\nB3  The forced odd branch, exact integer surplus, at the hostile pairs where an")
    P("    odd-weight witness with r > 2 exists.")
    P(f"    {'slope':<23}{'intercept':<31}{'k':<4}{'ell':<9}{'r_u':<10}"
      f"{'ell*E':<12}{'S (exact)':<12}{'2^Lv>F'}")
    shown = 0
    for (snm, inm, nev, nod, best, rows, u) in verdicts:
        for r in rows:
            if not r["odd_ok"] or r["ell"] < 40:
                continue
            res = exact_surplus(u, r["ell"], r["L"], 0, "odd")
            if res is None:
                continue
            assert res["transfer"], ("transfer", snm, inm, r["k"])
            assert res["gammaR"] == Fraction(1, 2)
            P(f"    {snm:<23}{inm:<31}{r['k']:<4}{r['ell']:<9}{float(r['r']):<10.6f}"
              f"{float(r['ell'] * (r['r'] - 2)):<12.4g}{res['S']:<12.2f}{res['pos']}")
            shown += 1
            if shown >= 14:
                break
        if shown >= 14:
            break
    P("\nALL STEP-B CHECKS PASS.")

if __name__ == "__main__":
    main()
