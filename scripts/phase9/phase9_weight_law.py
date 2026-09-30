"""
Phase 9, step D2: the exact law for the witness-root weight.

D1 found that  w(k,d) = d p_{k-1} + p_{k-2}  is NOT universally exact.  This script pins down
the law.  Hypothesis, from BHZ Prop. 3.3 + Lemma 2.6 + invariance of weight under cyclic
permutation:

  (W-y)  If 0 < c_k < a_k then the prefix of length q_k - c_k q_{k-1} IS the root of an attained
         initial power (BHZ Prop. 3.3, second case), that root is a cyclic permutation of
         tau_0^{a_1} o ... o tau_{k-1}^{a_k-c_k}(i), and cyclic permutation preserves weight, so
         its weight is EXACTLY p_k - c_k p_{k-1} = d_k p_{k-1} + p_{k-2}.

  (W-x)  The prefix of length q_k is the root of an attained initial power only when x(k) >= 1.
         When x(k) >= 1 its weight is EXACTLY p_k; when x(k) < 1 the prefix of length q_k is not
         a power root at all and its weight may deviate by +-1.

  (W-int) A genuinely intermediate length (1 <= d < a_k, d != d_k) carries no BHZ attainment
         guarantee, so its weight may deviate by +-1 and must be read off the word.
"""
from fractions import Fraction
import random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import convergents, admissible, certified_prefix, stream
from phase9_weight_stress import rand_admissible

def main():
    rng = random.Random(2024)
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / D2.  The exact weight law for witness roots")
    P("=" * 78)
    slopes = [[2]*11, [3]*9, [1,2]*6, [3,1]+[2]*8, [4,2,4,2,4,2,4], [1,1,2]*4,
              [2,4,6,8,2,4], [5,3]+[2]*8, [1,3,1,3,2,2,1,4], [6,2,6,2,6,2]]
    # buckets: (kind, attained?) -> {offset: count}
    B = {}
    for a in slopes:
        p, q = convergents(a)
        cs = [[0]*len(a), [max(0,x-1) for x in a], [max(0,x-2) for x in a]]
        cs += [rand_admissible(a, rng) for _ in range(26)]
        for c in cs:
            if not admissible(a, c):
                continue
            st = stream(a, c)
            om, K = certified_prefix(a, c, maxlen=250000)
            u = [int(ch) for ch in om]
            pref = [0]
            for ch in u:
                pref.append(pref[-1] + ch)
            for k in range(2, K + 1):
                for dd in range(1, a[k-1] + 1):
                    ell = dd*q[k-1] + q[k-2]
                    if ell >= len(u):
                        continue
                    off = pref[ell] - (dd*p[k-1] + p[k-2])
                    if dd == st["d"][k] and 0 < c[k-1] < a[k-1]:
                        key = "y-root, BHZ-attained (0<c_k<a_k)"
                    elif dd == a[k-1]:
                        xk = st["x"].get(k)
                        if xk is None:
                            continue
                        key = ("x-root, x(k) >= 1" if xk >= 1 else "x-root, x(k) < 1  (NOT a power root)")
                    else:
                        key = "intermediate, no attainment guarantee"
                    B.setdefault(key, {}).setdefault(off, 0)
                    B[key][off] += 1
    P(f"\n    {'class':<42}{'off=-1':<9}{'off=0':<9}{'off=+1':<9}{'exact?'}")
    for key in sorted(B):
        row = B[key]
        n = sum(row.values())
        ex = (row.get(0, 0) == n)
        P(f"    {key:<42}{row.get(-1,0):<9}{row.get(0,0):<9}{row.get(1,0):<9}"
          f"{'YES  ('+str(n)+'/'+str(n)+')' if ex else 'NO  '+str(n-row.get(0,0))+'/'+str(n)}")
    ok_y = B.get("y-root, BHZ-attained (0<c_k<a_k)", {})
    ok_x = B.get("x-root, x(k) >= 1", {})
    P("\n    VERDICT ON THE WEIGHT LAW:")
    P(f"      (W-y) y-root, 0 < c_k < a_k          : exact in {ok_y.get(0,0)}/{sum(ok_y.values())} cases")
    P(f"      (W-x) x-root with x(k) >= 1          : exact in {ok_x.get(0,0)}/{sum(ok_x.values())} cases")
    bad = B.get("x-root, x(k) < 1  (NOT a power root)", {})
    P(f"      x-root with x(k) < 1                 : deviates in "
      f"{sum(bad.values())-bad.get(0,0)}/{sum(bad.values())} cases  <-- the source of the D1 x-deviations")
    it = B.get("intermediate, no attainment guarantee", {})
    P(f"      intermediate                         : deviates in "
      f"{sum(it.values())-it.get(0,0)}/{sum(it.values())} cases  <-- must read the actual weight")
    assert ok_y.get(0,0) == sum(ok_y.values()), "the y-root weight law FAILED"
    P("\n    So the parity argument is safe exactly on the BHZ-attained y-roots, and on x-roots")
    P("    whose exponent is at least 1.  For intermediate roots the parity must be computed")
    P("    from the word -- which is what scripts/phase9/phase9_even_branch.py does (it asserts")
    P("    w == sum(u[:ell]) on every root it uses).")
    P("\nSTEP D2 COMPLETE.")

if __name__ == "__main__":
    main()
