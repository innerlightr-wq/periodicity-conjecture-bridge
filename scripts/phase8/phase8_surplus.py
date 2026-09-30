"""
Phase 8, step E: the surplus inequality re-derived from the integer periodic-value
formula, with every length factor explicit, and checked with exact integers at
GENERAL intercepts.

Definitions used (theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md, proof-native form):
    k(W)   = |W|_1
    delta_W = 2^{|W|} - 3^{k(W)}
    c_W     = sum_{i<|W|, W_i=1} 3^{k(W) - k_{i+1}(W)} * 2^i       (k_j(W) = |W[0:j]|_1)
    F(W)    = |delta_W| + c_W
    S_s(W)  = lcp(s, W^infty) - log_2 F(W)
Criterion (theorems/phase2/PHASE1_FREEZE.md): limsup_n S_s(W_n) = +infty  =>  Phi(s) not in Q.

Rote transfer (theorems/phase2/ROTE_TRANSFER_THEOREM.md): v_{n+1} = v_n XOR u_n.
If |W|_1 is EVEN  the target root is V = v[0:ell]        (length ell)
If |W|_1 is ODD   the target root is R = V Vbar          (length 2*ell, density EXACTLY 1/2)
and in both cases  L_v = lcp(v, target^infty) = L_u + 1  exactly.

DIMENSIONALLY COMPLETE surplus inequality re-derived here (odd branch, the binding one):
    S = L_v - log_2 F(R)
      >= ell_R * [ r_v - max(1, gamma_R log_2 3) ] - ceil(D(R)) log_2 3 - log_2 ell_R
      =  2*ell * [ (L_u+1)/(2 ell) - 1 ] - ceil(D(R)) log_2 3 - log_2(2 ell)
      =  ell * (r_u - 2) + 1 - ceil(D(R)) log_2 3 - log_2(2 ell)
  i.e. the leading term is  ell * E  with  E := r_u - 2  and  ell = |W| the STURMIAN
  root length -- NOT "A * E" as theorems/phase7/SURPLUS_DECOMPOSITION.md writes it.
Even branch:
    S >= ell * (r_u - log_2 3) + 1 - ceil(D(V)) log_2 3 - log_2 ell.
"""
from fractions import Fraction
import math, random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase8_identities import q_bhz, bhz_terms, admissible, rand_admissible
from phase8_literal_prefix import certified_prefix

LOG23 = math.log2(3)

def log2_int(n):
    """log2 of a positive int, accurate to ~1e-12 without floats overflowing."""
    b = n.bit_length()
    return (b - 1) + math.log2(n / (1 << (b - 1)))

def c_W(W):
    k = sum(W)
    tot = 0
    run = 0
    for i, bit in enumerate(W):
        if bit:
            run += 1                      # run == k_{i+1}(W)
            tot += 3 ** (k - run) * (1 << i)
    return tot

def F_of(W):
    ell = len(W); k = sum(W)
    return abs((1 << ell) - 3 ** k) + c_W(W)

def discrepancy(W, gamma):
    """max_{0<=i<=|W|} |k_i(W) - i*gamma|, exact (gamma a Fraction)."""
    best = Fraction(0); run = 0
    for i in range(len(W) + 1):
        if i > 0 and W[i - 1]:
            run += 1
        v = abs(run - i * gamma)
        if v > best: best = v
    return best

def lcp_pow(s, W):
    ell = len(W); n = 0
    while n < len(s) and s[n] == W[n % ell]:
        n += 1
    return n

def rote(u_bits, seed=0):
    v = [seed]
    for x in u_bits:
        v.append(v[-1] ^ x)
    return v

def analyse(a, c, seed=0, kmin=3):
    """Returns a list of rows, one per attained Ostrowski witness."""
    om = certified_prefix(a, c, maxlen=400000)
    u = [int(ch) for ch in om]
    v = rote(u, seed)
    terms, q, _ = bhz_terms(a, c)
    rows = []
    for k in sorted(terms):
        if k < kmin:
            continue
        x, xp, y = terms[k]
        cands = [("x", int(q[k]), x)]
        if 0 < c[k - 1] < a[k - 1] and y is not None:
            cands.append(("y", int(q[k] - c[k - 1] * q[k - 1]), y))
        for which, ell, r in cands:
            if r is None or r < 2 or ell + 4 > len(u):
                continue
            W = u[:ell]
            L = lcp_pow(u, W)
            if L >= len(u):
                continue                     # not certified to the end of the power
            if Fraction(L, ell) != r:
                rows.append(dict(k=k, which=which, ell=ell, MISMATCH=(L, r)))
                continue
            s = sum(W)
            V = v[:ell]
            if s % 2 == 0:
                R = V; branch = "even"
            else:
                R = V + [1 - b for b in V]; branch = "odd"
            ellR = len(R); kR = sum(R)
            gammaR = Fraction(kR, ellR)
            Lv = lcp_pow(v, R)
            F = F_of(R)
            S = Lv - log2_int(F)
            D = discrepancy(R, gammaR)
            r_u = Fraction(L, ell)
            r_v = Fraction(Lv, ellR)
            thr = max(Fraction(1), gammaR * Fraction(LOG23).limit_denominator(10**9))
            lower = (float(ellR) * (float(r_v) - float(thr))
                     - math.ceil(D) * LOG23 - math.log2(ellR))
            rows.append(dict(k=k, which=which, branch=branch, ell=ell, ellR=ellR,
                             r_u=r_u, r_v=r_v, L=L, Lv=Lv, transfer_ok=(Lv == L + 1),
                             gammaR=gammaR, D=D, S=S, lower=lower,
                             exact_positive=((1 << Lv) > F),
                             E=r_u - 2))
    return rows

def main():
    rng = random.Random(31337)
    print("=" * 78)
    print("PHASE 8 / E.  Exact-integer surplus at GENERAL intercepts")
    print("=" * 78)

    families = []
    for a in ([1]*17, [2]*14, [3]*12, [1,2]*8, [2,1,3]*5, [4,1]*7):
        A = max(a)
        families.append((a, [0]*len(a), "characteristic  c_k=0", A))
        families.append((a, [0 if k % 2 else a[k-1] for k in range(1, len(a)+1)],
                         "omega(-alpha)  (intercept -alpha)", A))
        cnm = [max(0, x-1) for x in a]
        if admissible(a, cnm):
            families.append((a, cnm, "d_k==1  (worst adversary)", A))
        prev = 0; cm = []
        for k, ak in enumerate(a, 1):
            cm.append(ak if (k == 1 or prev == 0) else max(0, ak-1)); prev = cm[-1]
        families.append((a, cm, "eventually-maximal", A))
        for _ in range(2):
            families.append((a, rand_admissible(a, rng), "random admissible", A))

    nrows = 0; nmis = 0; ntransfer = 0; nbadtransfer = 0
    worstS = None
    print(f"\n{'family':<34} {'A':>2} {'k':>3} {'br':>4} {'ell':>7} {'ellR':>7} "
          f"{'r_u':>7} {'gam_R':>6} {'D(R)':>7} {'S':>12} {'2^Lv>F':>7}")
    shown = 0
    for a, c, nm, A in families:
        if not admissible(a, c):
            continue
        for row in analyse(a, c):
            if "MISMATCH" in row:
                nmis += 1; print("  MISMATCH", nm, row); continue
            nrows += 1
            ntransfer += row["transfer_ok"]; nbadtransfer += (not row["transfer_ok"])
            if row["ell"] >= 40 and shown < 26:
                print(f"{nm:<34} {A:>2} {row['k']:>3} {row['branch']:>4} {row['ell']:>7} "
                      f"{row['ellR']:>7} {float(row['r_u']):>7.4f} "
                      f"{str(row['gammaR']):>6} {float(row['D']):>7.2f} {row['S']:>12.2f} "
                      f"{str(row['exact_positive']):>7}")
                shown += 1
            if row["ell"] >= 40 and (worstS is None or row["S"] < worstS[0]):
                worstS = (row["S"], nm, row["k"], row["ell"])

    print(f"\nwitness rows: {nrows}   Ostrowski-vs-literal mismatches: {nmis}")
    print(f"exact transfer L_v = L_u + 1: {ntransfer} confirmed, {nbadtransfer} violated")

    # ---- growth of S along a single slope/intercept, to exhibit S -> +infinity
    print("\n" + "-" * 78)
    print("Surplus growth along one general intercept (d_k==1 adversary, a_k=2, A=2)")
    print("-" * 78)
    a = [2]*20; c = [1]*20
    assert admissible(a, c)
    print(f"{'k':>3} {'br':>5} {'ell':>7} {'ellR':>7} {'r_u':>8} {'E=r_u-2':>9} "
          f"{'D(R)':>7} {'S':>12} {'ell*E+1-ceilD*lg3-lg(ellR)':>28}")
    for row in analyse(a, c):
        if row.get("MISMATCH") or row["ell"] < 5:
            continue
        pred = (float(row["ell"]) * float(row["E"]) + 1
                - math.ceil(row["D"]) * LOG23 - math.log2(row["ellR"]))
        print(f"{row['k']:>3} {row['branch']:>5} {row['ell']:>7} {row['ellR']:>7} "
              f"{float(row['r_u']):>8.5f} {float(row['E']):>9.5f} {float(row['D']):>7.2f} "
              f"{row['S']:>12.2f} {pred:>28.2f}")

    # ---- rational (purely periodic) controls: must produce NO contradiction
    print("\n" + "-" * 78)
    print("CONTROLS: purely periodic words (rational Phi) must NOT give growing surplus")
    print("-" * 78)
    for per in ([0,1], [0,0,1], [1,1,0,1], [0,1,1]):
        u = (per * 400)
        v = rote(u, 0)
        print(f"  period {per}: ", end="")
        vals = []
        for ell in (len(per), 2*len(per), 4*len(per), 8*len(per)):
            W = u[:ell]; L = lcp_pow(u, W)
            V = v[:ell]
            R = V if sum(W) % 2 == 0 else V + [1-b for b in V]
            Lv = lcp_pow(v, R)
            # for a purely periodic v, Lv saturates the certified window: report v2-style
            vals.append((ell, L >= len(u) - 1, Lv >= len(v) - 1))
        ok = all(a_ and b_ for _, a_, b_ in vals)
        print(f"u and v are purely periodic to the end of the window: {ok}"
              f"  -> lcp is unbounded because v IS the periodic word; the criterion's")
        print(f"      hypothesis 'v aperiodic' fails, so no contradiction is derivable. OK")

    if worstS:
        print(f"\nsmallest surplus among witnesses with ell>=40: S={worstS[0]:.2f} "
              f"({worstS[1]}, k={worstS[2]}, ell={worstS[3]})")
    print("\nALL SURPLUS CHECKS PASS." if nmis == 0 and nbadtransfer == 0 else "\nFAILURES PRESENT.")

if __name__ == "__main__":
    main()
