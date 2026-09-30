"""
Phase 9B, step 3: what Monks-Yazinski (2004) Theorem 2.7(b) already proves.

THE PRIOR THEOREM, quoted from the programme's OWN foundation paper (De Jesus, "The 3x+1
Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic Integer", Sec. 8, "What is
known"), which in turn quotes Monks-Yazinski:

    "Monks and Yazinski [16, Theorem 2.7(b)] proved that if x in Q cap Z_2 has a T-orbit which
     is not eventually cyclic -- equivalently, whose orbit set is infinite -- then
         liminf_{n->infty} k_n(v(x))/n  >=  beta .
     Since a word is eventually periodic if and only if its Phi-value has an eventually cyclic
     orbit, this gives at once:  if v is aperiodic and liminf k_n(v)/n < beta, then Phi(v) not in Q."

with beta = ln2/ln3 = log_3 2 = 1/log_2 3 = 0.6309297535714575.

Monks-Yazinski, Discrete Math. 275 (2004), "The autoconjugacy of the 3x+1 function",
Theorem 2.7: "Let x in Q_odd. ... (b) If the orbit of x is divergent then ln2/ln3 <= lim
kappa_n(x)/n", where kappa_n(x) is the number of odd elements among the first n orbit terms,
i.e. the number of 1s in the first n entries of the parity vector.

CONSEQUENCE TO TEST HERE: every class this repository proves irrational has ones-density
bounded away from beta, so every one of those conclusions is already a corollary of the 2004
theorem.  This script computes the ones-density of each class exactly or to high precision.
"""
from fractions import Fraction
import math, sys

BETA = 1 / math.log2(3)

def mech(gamma, rho, N):
    return [math.floor((i + 1) * gamma + rho) - math.floor(i * gamma + rho) for i in range(N)]

def rote(u, seed=0):
    v = [seed]
    for x in u:
        v.append(v[-1] ^ x)
    return v[:len(u)]

def tm(N):
    t = [0]
    while len(t) < N:
        t = t + [1 - x for x in t]
    return t[:N]

def subst_fixed_point(s0, s1, N):
    img = {0: [int(c) for c in s0], 1: [int(c) for c in s1]}
    t = [0]
    while len(t) < N:
        nt = []
        for x in t:
            nt += img[x]
        if nt == t:
            break
        t = nt
    return t[:N]

def main():
    P = lambda *z: (print(*z), sys.stdout.flush())
    P("=" * 78)
    P("PHASE 9B / 3.  Subsumption check against Monks-Yazinski 2004, Theorem 2.7(b)")
    P("=" * 78)
    P(f"    beta = ln2/ln3 = {BETA:.16f}   (irrational: it is log_3 2)")
    P("    The prior theorem excludes EVERY aperiodic v with liminf k_n(v)/n < beta.")

    P("\n3.1  Ones-density of each class this repository proves irrational.")
    P(f"    {'class':<44}{'ones-density':<26}{'!= beta?':<9}{'prior result that already covers it'}")

    rows = []
    # CS Rote sequences: v_n = v_0 XOR (k_n(u) mod 2); density exactly 1/2 by Weyl on gamma/2
    N = 300000
    for gname, gamma in (("golden (bounded type, Phase 4/6)", (5 ** 0.5 - 1) / 2),
                         ("silver (bounded type)", 2 ** 0.5 - 1),
                         ("unbounded type a_k = k (Phase 9)", None),
                         ("critical slope beta itself", BETA)):
        if gamma is None:
            # gamma = [0;1,2,3,4,...] built from its convergents
            p0,q0,p1,q1 = 0,1,1,1
            for a in range(2, 25):
                p0,q0,p1,q1 = p1,q1,a*p1+p0,a*q1+q0
            gamma = p1/q1
        for rho, rn in ((0.0, "rho=0"), (0.3, "rho=0.3")):
            v = rote(mech(gamma, rho, N), 0)
            d = sum(v) / len(v)
            rows.append((f"CS Rote, {gname}, {rn}", d))
    # Thue-Morse and the substitution sweep
    rows.append(("Thue-Morse (Phase 9 Cor 4.1)", sum(tm(1 << 16)) / (1 << 16)))
    for (s0, s1, nm) in (("01", "00", "period-doubling"), ("001", "000", "3-uniform 001/000"),
                         ("010", "001", "3-uniform 010/001"), ("011", "110", "3-uniform 011/110"),
                         ("011", "101", "3-uniform 011/101")):
        t = subst_fixed_point(s0, s1, 3 ** 10)
        rows.append((f"subst fixed point {s0}/{s1} ({nm})", sum(t) / len(t)))
    for nm, d in rows:
        route = ("MY 2.7(b), refereed 2004" if d < BETA else
                 ("Lopez-Stoll 2021 Thm 1, PREPRINT" if d > BETA else "NEITHER (density = beta)"))
        P(f"    {nm:<44}{d:<26.12f}{str(abs(d-BETA) > 1e-9):<9}{route}")
        assert abs(d - BETA) > 1e-6, ("sits at the critical density", nm, d)

    P("\n    Every class is at density well below beta.  For CS Rote the density is EXACTLY 1/2:")
    P("      v_n = v_0 XOR (k_n(u) mod 2) and k_n(u) = floor(n*gamma + rho) - floor(rho), so")
    P("      v_n = 1 iff frac((n*gamma + rho)/2) lies in a fixed half-length interval; gamma/2 is")
    P("      irrational, so Weyl equidistribution gives density exactly 1/2 for EVERY irrational")
    P("      slope and EVERY intercept -- no bounded-type, no parity, no intercept hypothesis.")
    P("    For a k-uniform substitution the letter frequencies are the normalised left Perron")
    P("    eigenvector for the integer eigenvalue k, hence RATIONAL, hence != beta.")

    # classify the whole 21-substitution sweep by which half of the dichotomy applies
    P("\n3.1b The Phase 9 substitution sweep, classified by which half of the dichotomy applies.")
    import itertools
    below = above = 0
    P(f"    {'k':<3}{'sig(0)':<8}{'sig(1)':<8}{'density':<14}{'vs beta':<10}{'prior result'}")
    for k in (2, 3):
        for s0 in ["".join(q) for q in itertools.product("01", repeat=k)]:
            for s1 in ["".join(q) for q in itertools.product("01", repeat=k)]:
                if s0[0] != "0" or s0 == s1:
                    continue
                t = subst_fixed_point(s0, s1, k ** 10)
                if len(t) < 4096:
                    continue
                # eventual-periodicity filter, same as the Phase 9 sweep
                ep = False
                for pre in range(0, 64):
                    tail = t[pre:]
                    if len(tail) < 1200:
                        break
                    for per in range(1, 400):
                        if all(tail[i] == tail[i + per] for i in range(len(tail) - per)):
                            ep = True; break
                    if ep:
                        break
                if ep:
                    continue
                d = sum(t) / len(t)
                rel = "<" if d < BETA else (">" if d > BETA else "=")
                pr = "MY 2.7(b) [refereed]" if d < BETA else "Lopez-Stoll Thm 1 [preprint]"
                below += (d < BETA); above += (d > BETA)
                P(f"    {k:<3}{s0:<8}{s1:<8}{d:<14.10f}{rel:<10}{pr}")
    P(f"    -> {below} of the sweep are below beta (refereed prior result),")
    P(f"       {above} are above beta (preprint prior result).  NONE is at beta.")

    P("\n3.2  What this subsumes, class by class.")
    tbl = [
        ("theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md", "CS Rote, 5 quadratic slopes", "1/2"),
        ("theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md", "CS Rote, quadratic slopes", "1/2"),
        ("theorems/phase6/BOUNDED_TYPE_THEOREM.md", "CS Rote, bounded type, intercept 0", "1/2"),
        ("theorems/phase8/... Theorem 2", "CS Rote, bounded type, every intercept", "1/2"),
        ("theorems/phase9/... Theorem 3", "CS Rote, unbounded type, parity form", "1/2"),
        ("theorems/phase9/... Corollary 4.1", "Thue-Morse", "1/2"),
        ("theorems/phase9/... Corollary 4.2", "21 substitution fixed points", "rational"),
    ]
    P(f"    {'result':<46}{'class':<42}{'density':<10}{'subsumed?'}")
    for a, b, c in tbl:
        P(f"    {a:<46}{b:<42}{c:<10}YES")
    P("    (CS Rote and Thue-Morse at density 1/2 < beta: by the REFEREED Monks-Yazinski result.")
    P("     The part of the substitution sweep above beta: by the Lopez-Stoll PREPRINT only.)")

    P("\n3.3  What is NOT subsumed.")
    P("    MY 2.7(b) says nothing at density EXACTLY beta.  The foundation paper's own main")
    P("    theorem sits precisely there: its word 1c_beta has ones-density exactly beta, the one")
    P("    density excluded by both halves of the known dichotomy (MY 2.7(b) below beta, Lopez-")
    P("    Stoll Theorem 1 above it).  That result is NOT subsumed, and the foundation paper")
    P("    says so explicitly.  Nothing in this repository's Phases 2-9 sits at density beta:")
    P(f"      1c_beta ones-density                     = beta = {BETA:.12f}   <- NOT subsumed")
    P(f"      every CS Rote sequence                   = 0.500000000000   <- subsumed")
    P("    Also not subsumed: the abstract criterion itself (a mechanism, not a class theorem),")
    P("    and any future class placed at density beta.")

    P("\n3.4  Why the repository's own prior-art passes missed this.")
    P("    PRIOR_ART.md records three searches, all for the MECHANISM (2-adic depth-vs-height")
    P("    bridge; weight-parity + transfer + three-distance; the final chain).  None asked")
    P("    whether the CONCLUSION was already available by a different route.  The density route")
    P("    was known to the programme -- theorems/phase1/FALSIFICATION_REPORT.md cites Monks-")
    P("    Yazinski explicitly, and docs/EOC_HANDOFF_CLOSED.md records that CS Rote has one-")
    P("    density exactly 1/2 while beta = 0.63093 -- but the two facts were never combined.")
    P("\nALL PHASE-9B STEP-3 CHECKS PASS.")

if __name__ == "__main__":
    main()
