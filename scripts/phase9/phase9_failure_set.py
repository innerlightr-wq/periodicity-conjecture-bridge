"""
Phase 9, step E: the failure set of the even branch, using only BHZ-GUARANTEED roots, and
what is left on it.

Guaranteed attained roots at scale k (BHZ Prop. 3.3), with the weight law of step D2:
   x-root : length q_k,                   weight p_k                  (exact when x(k) >= 1),
            exponent x(k),  attained for every k
   y-root : length d_k q_{k-1} + q_{k-2}, weight d_k p_{k-1} + p_{k-2} (exact always),
            exponent y(k),  attained iff 0 < c_k < a_k

Even branch fires at scale k if some guaranteed root has EVEN weight and exponent > g(gamma_W),
    g(gamma) = max(1, gamma log2 3) + gamma(1-gamma) log2 3   <   log2 3   for gamma < 1,
which requires NO discrepancy hypothesis and NO hypothesis on the slope.

Parity bookkeeping.  With P_k := (p_{k-1}, p_k) mod 2 in {(0,1),(1,0),(1,1)} (never (0,0),
since gcd(p_k,p_{k-1}) = 1):
    x-root weight p_k even            <=>  P_k = (1,0)
    y-root weight even                <=>  P_{k-1} = (0,1) and d_k even,
                                       or  P_{k-1} = (1,1) and d_k odd
                                      (never when P_{k-1} = (1,0))
Transitions: (0,1) -> (1, a_{k+1} mod 2);  (1,0) -> (0,1);  (1,1) -> (1, (a_{k+1}+1) mod 2).
"""
from fractions import Fraction
import itertools, random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase9_witness_family import convergents, admissible, stream, certified_prefix, lcp_pow, LOG23
from phase9_even_branch import g_of, gamma_bracket, roots, exact_even_surplus
from phase9_weight_stress import rand_admissible

def guaranteed_even_scales(a, c, kmin=4):
    """Scales k where a GUARANTEED root has even weight and exponent > g(gamma_W)."""
    p, q = convergents(a)
    st = stream(a, c)
    glo, ghi = gamma_bracket(a)
    hits = []
    for k in range(kmin, len(a) - 1):
        # x-root
        if k in st["x"] and st["x"][k] >= 1:
            w, ell = p[k], q[k]
            if w % 2 == 0 and st["x"][k] > g_of(Fraction(w, ell)):
                hits.append((k, "x", ell, w, st["x"][k]))
        # y-root
        if 0 < c[k - 1] < a[k - 1] and k in st["y"]:
            dk = st["d"][k]
            ell = dk * q[k - 1] + q[k - 2]
            w = dk * p[k - 1] + p[k - 2]
            if w % 2 == 0 and st["y"][k] > g_of(Fraction(w, ell)):
                hits.append((k, "y", ell, w, st["y"][k]))
    return hits

def main():
    rng = random.Random(555)
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9 / E.  Failure set of the guaranteed-root even branch, and what survives on it")
    P("=" * 78)

    # ---------------- E1: how large is the covered class?
    P("\nE1  Coverage of Theorem 3 (guaranteed roots only) over random slopes and intercepts,")
    P("    INCLUDING unbounded-type slopes with fast-growing partial quotients.")
    fams = [
        ("bounded, a_k in 1..4   ", lambda rng: [rng.randint(1, 4) for _ in range(16)]),
        ("bounded, a_k in 1..12  ", lambda rng: [rng.randint(1, 12) for _ in range(14)]),
        ("a_k = k                ", lambda rng: list(range(1, 15))),
        ("a_k = 2^k              ", lambda rng: [2 ** i for i in range(1, 13)]),
        ("a_k = k!               ", lambda rng: [max(1, __import__('math').factorial(i)) for i in range(1, 11)]),
        ("all even, a_k in 2..8  ", lambda rng: [3, 1] + [2 * rng.randint(1, 4) for _ in range(12)]),
        ("all even, fast (2^k)   ", lambda rng: [3, 1] + [2 ** i for i in range(1, 11)]),
    ]
    icepts = [("c=0", lambda a: [0]*len(a)),
              ("keep-one", lambda a: [max(0, x-1) for x in a]),
              ("c=a-2", lambda a: [max(0, x-2) for x in a]),
              ("random", None)]
    P(f"    {'slope family':<25}{'intercept':<12}{'#tested':<9}{'covered':<9}"
      f"{'coverage':<10}{'median #even scales'}")
    failures = []
    for fnm, fgen in fams:
        for inm, igen in icepts:
            tested = cov = 0; counts = []
            for _ in range(30):
                a = fgen(rng)
                c = igen(a) if igen else rand_admissible(a, rng)
                if not admissible(a, c):
                    continue
                tested += 1
                h = guaranteed_even_scales(a, c)
                counts.append(len(h))
                if h:
                    cov += 1
                else:
                    failures.append((fnm, inm, a, c))
            if tested:
                counts.sort()
                P(f"    {fnm:<25}{inm:<12}{tested:<9}{cov:<9}{cov/tested*100:<10.1f}"
                  f"{counts[len(counts)//2]}")
    # de-duplicate: the deterministic slope families repeat
    uniq = []
    seen_ = set()
    for f_ in failures:
        key = (f_[0], f_[1], tuple(f_[2]), tuple(f_[3]))
        if key not in seen_:
            seen_.add(key); uniq.append(f_)
    failures = uniq
    P(f"\n    DISTINCT slope/intercept pairs with NO guaranteed even-weight witness: {len(failures)}")

    # ---------------- E2: what do the failures look like?
    P("\nE2  Structure of the failure set.")
    if not failures:
        P("    (empty in this sample)")
    else:
        P(f"    {'slope family':<25}{'intercept':<12}{'a[:8]':<26}{'c[:8]':<26}"
          f"{'a_k even for k>=3?':<19}{'p_k all odd?'}")
        seen = set()
        for (fnm, inm, a, c) in failures[:16]:
            p, q = convergents(a)
            allodd = all(p[k] % 2 == 1 for k in range(1, len(a) + 1))
            evtail = all(x % 2 == 0 for x in a[2:])
            P(f"    {fnm:<25}{inm:<12}{str(a[:8]):<26}{str(c[:8]):<26}"
              f"{str(evtail):<19}{allodd}")
        nboth = sum(1 for (_, _, a, c) in failures
                    if all(x % 2 == 0 for x in a[2:])
                    and all(convergents(a)[0][k] % 2 == 1 for k in range(1, len(a)+1)))
        P(f"\n    of {len(failures)} failures, {nboth} have BOTH an eventually-even digit tail and")
        P(f"    all-odd convergent numerators -- i.e. they sit exactly in the hostile family.")

    # ---------------- E3: on the failure set, do intermediate roots rescue it?
    P("\nE3  On the failure set: does an INTERMEDIATE root supply an even-weight power with")
    P("    exponent > g(gamma)?  (literal prefix powers, actual weights, exact surplus)")
    P(f"    {'a[:7]':<24}{'c[:7]':<24}{'best int (k,d)':<16}{'ell':<8}{'w%2':<5}"
      f"{'r':<10}{'g':<10}{'exact S':<10}{'2^Lv>F'}")
    nres = 0; nfail2 = 0
    for (fnm, inm, a, c) in failures[:24]:
        try:
            rs, u, K = roots(a, c, maxlen=150000)
        except Exception as e:
            P(f"    {str(a[:7]):<24}{str(c[:7]):<24}  (skipped: {type(e).__name__})")
            continue
        cand = [r for r in rs if r["par"] == 0 and r["clears"] and r["kind"] == "int"]
        if not cand:
            nfail2 += 1
            P(f"    {str(a[:7]):<24}{str(c[:7]):<24}  -- NO intermediate even-weight root clears g --")
            continue
        r = max(cand, key=lambda z: z["ell"] if z["ell"] <= 2600 else 0)
        res = exact_even_surplus(u, r["ell"], r["L"], 0) if r["ell"] <= 2600 else None
        nres += 1
        P(f"    {str(a[:7]):<24}{str(c[:7]):<24}{str((r['k'],r['d'])):<16}{r['ell']:<8}"
          f"{r['par']:<5}{float(r['r']):<10.6f}{float(r['g']):<10.6f}"
          f"{(f'{res[chr(83)]:.1f}' if res else 'n/a'):<10}{res['pos'] if res else '-'}")
        if res:
            assert res["pos"], ("exact surplus not positive", a, c)
            assert res["transfer"]
    P(f"\n    failure-set pairs rescued by an intermediate even-weight root: {nres}")
    P(f"    failure-set pairs with NO even-weight root at all (guaranteed or intermediate): {nfail2}")
    P("\nSTEP E COMPLETE.")

if __name__ == "__main__":
    main()
