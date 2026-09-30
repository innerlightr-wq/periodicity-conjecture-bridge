"""Phase 12 / item 3.  The general theorem: alpha quadratic irrational, rho rational.

Every qualification the general statement needs is tested here on a family of (alpha, rho),
rho = 0 included.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
from qfield import Q, cf, chi, lt_beta, dist_to_int, BLO, BHI

getcontext().prec = 320
BETA = float(Decimal(2).ln() / Decimal(3).ln())
MINWRAP = min(float(BLO), 1.0 - float(BHI))
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

P("=" * 78)
P("PHASE 12 / item 3.  alpha quadratic irrational in (0,1), rho rational, chi = 1_[0,beta)")
P("=" * 78)

# ---- the family.  (name, a, b, D)  meaning alpha = a + b*sqrt(D), each in (0,1) ----
FAM = [
    ("(sqrt5-1)/2", Fr(-1, 2), Fr(1, 2), 5),
    ("sqrt2-1",     Fr(-1),    Fr(1),    2),
    ("sqrt3-1",     Fr(-1),    Fr(1),    3),
    ("(sqrt13-3)/2",Fr(-3, 2), Fr(1, 2), 13),
    ("(sqrt29-5)/2",Fr(-5, 2), Fr(1, 2), 29),
]
RHOS = [Fr(0), Fr(1, 7), Fr(1, 2), Fr(3, 11), Fr(2, 5)]

P("\n(A) Slopes: algebraicity, bounded partial quotients A, and q_{k+1} <= (A+1) q_k.")
P("    alpha            min poly                 a_i (first 14)          A    max q_{k+1}/q_k")
SL = []
for nm, a, b, D in FAM:
    al = Q(a, b, D)
    assert 0 < al.approx() < 1
    # minimal polynomial x^2 - 2a x + (a^2 - D b^2)
    num = (a * a - D * b * b)
    aq, ps, qs = cf(al, 42)
    A = max(aq[1:30])
    ratio = max(qs[k + 1] / qs[k] for k in range(1, 28))
    P(f"    {nm:<16} x^2 {-2*a:+}x {num:+}        {str(aq[1:15]):<23} {A:<4} {ratio:.4f} <= {A+1}")
    assert ratio <= A + 1 + 1e-12
    SL.append((nm, al, aq, ps, qs, A))

P("\n(B) The beta-boundary is NEVER hit, and the 0-boundary only at m=0 with rho=0.")
P("    m*alpha+rho = beta (mod 1) would make beta = m*alpha + p/q - j algebraic: impossible")
P("    (Gelfond-Schneider).  m*alpha+rho in Z with m>=1 would make alpha rational: impossible.")
P("    m=0: the orbit point is {rho}, which is 0 exactly when rho = 0.")
P("    alpha            rho     A_0 = rho - j_0        A_0 > 0?   c_0 = ||rho-beta||")
for nm, al, aq, ps, qs, A in SL[:1]:
    for r in RHOS:
        x = Q(r, 0, al.D)
        j0 = round(float(r) - BETA)
        A0 = x - Q(j0, 0, al.D)
        c0 = abs(A0.approx() - BETA)
        P(f"    {nm:<16} {str(r):<7} {A0.approx():+.10f}        {str(A0.sign()>0):<10} {c0:.10f}")
        assert c0 > 0 and A0.sign() > 0
P("")
P("    A CLEANER NONVANISHING ARGUMENT, found by this audit and replacing Phase 11B's:")
P("    j_m is the NEAREST integer to  m*alpha+rho-beta, so |A_m - beta| <= 1/2; and beta > 1/2.")
P("    Hence  A_m  >  beta - 1/2  =  %.10f  >  0   for EVERY m >= 0, every alpha, every rho." % (BETA-0.5))
P("    So Baker's hypothesis 'beta_1 non-zero' needs no case analysis at all -- in particular")
P("    m=0 is not exceptional for it (Phase 11B argued nonvanishing from alpha irrational for")
P("    m>=1 and from 1/7 not integral for m=0; the one-line bound above covers both at once).")
P("    Verified over the whole family:")
P("    alpha            rho     min_{0<=m<=3000} A_m      > beta-1/2 ?")
for nm, al, aq, ps, qs, A in SL:
    for r in RHOS:
        vals = []
        for m in range(0, 3001):
            x = Q(m, 0, al.D) * al + Q(r, 0, al.D)
            j = round(x.approx() - BETA)
            vals.append((x - Q(j, 0, al.D)).approx())
        P(f"    {nm:<16} {str(r):<7} {min(vals):<24.10f} {min(vals) > BETA-0.5-1e-12}")
        assert min(vals) > BETA - 0.5 - 1e-12

P("\n(C) The mismatch set: closed form, no-wrap hypothesis, and the SIGNED refinement.")
P("    alpha            rho     shifts  |delta|<=0.36907 all?  def-vs-closed  0 in M(d) iff d<0")

def delta_of(al, ell):
    x = Q(ell, 0, al.D) * al
    n = (x + Q(Fr(1, 2), 0, al.D)).floor()
    return x - Q(n, 0, al.D)

def in_M_def(al, x, d):
    return chi(x) != chi((x + d).frac())

def in_M_closed(al, x, d):
    ad = d if d.sign() > 0 else -d
    if d.sign() > 0:
        return (lt_beta(x) and not lt_beta(x + ad)) or (x >= Q(1, 0, al.D) - ad)
    return (x < ad) or ((not lt_beta(x)) and lt_beta(x - ad))

for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7)):
        bad = 0; signbad = 0; nsh = 0; allnw = True
        for q in qs[2:12]:
            d = delta_of(al, q); ad = d if d.sign() > 0 else -d
            if float(ad.approx()) > MINWRAP:
                allnw = False; continue
            nsh += 1
            for m in range(400):
                x = (Q(m, 0, al.D) * al + Q(r, 0, al.D)).frac()
                if in_M_def(al, x, d) != in_M_closed(al, x, d): bad += 1
            if ((d.sign() < 0) != in_M_def(al, Q(0, 0, al.D), d)): signbad += 1
        P(f"    {nm:<16} {str(r):<7} {nsh:<7} {str(allnw):<22} {bad:<14} {signbad}")
        assert bad == 0 and signbad == 0

P("\n(D) Arc at 0.  rho = p/q in lowest terms, A = max partial quotient, K := (A+2)q^2.")
P("    ||m*alpha+p/q|| >= ||q(m*alpha+p/q)||/q = ||qm*alpha||/q > 1/((A+2)q^2 m) = 1/(Km).")
P("    alpha            rho     q    K       min_{1<=m<20000} K*m*||m alpha+rho||   ||rho||")
KTAB = {}
for nm, al, aq, ps, qs, A in SL:
    for r in RHOS:
        qq = r.denominator; K = (A + 2) * qq * qq
        worst = min(K * m * float(dist_to_int(Q(m, 0, al.D) * al + Q(r, 0, al.D)).approx())
                    for m in range(1, 20000))
        nr = float(dist_to_int(Q(r, 0, al.D)).approx())
        P(f"    {nm:<16} {str(r):<7} {qq:<4} {K:<7} {worst:<21.6f} {nr:.10f}")
        assert worst > 1
        KTAB[(nm, r)] = K
P("    => t_0 > 1/(K|delta|) for the m>=1 part, in every case.")
P("    m=0: rho!=0 gives ||rho|| >= 1/q > 1/(K*M) >= |delta| for M>=2 since K >= 3q^2 > q;")
P("         rho=0 gives ||0||=0, so the two-sided ball is useless -- the SIGNED form of (C)")
P("         is what carries rho=0, restricted to convergents with delta > 0.")
P("    alpha            rho=0: how many of q_2..q_20 have delta>0 (need infinitely many)")
for nm, al, aq, ps, qs, A in SL:
    pos = [q for q in qs[2:21] if delta_of(al, q).sign() > 0]
    P(f"    {nm:<16} {len(pos)} of 19   e.g. {pos[:6]}")
    assert len(pos) >= 8

P("\n(E) Arc at beta.  A_m = m*alpha + p/q - j_m = (a_m + b_m sqrt(D))/g,  g = w*q.")
P("    Uniform degree 2 (m>=1) and height O(m^2), with the constant depending on alpha,rho.")
P("    alpha            rho     max_{1<=m<=3000} H(A_m)/m^2   deg=2 all?  A_m != 0 all?")
def A_of(al, r, m):
    x = Q(m, 0, al.D) * al + Q(r, 0, al.D)
    j = round(x.approx() - BETA)
    return x - Q(j, 0, al.D)

def height(A):
    """classical height: max |coeff| of the primitive minimal polynomial."""
    a, b, D = A.a, A.b, A.D
    if b == 0:
        n, d = a.numerator, a.denominator
        return max(abs(d), abs(n)) if (n or d) else 1
    g = a.denominator * b.denominator          # common denominator (not nec. minimal)
    aa = a * g; bb = b * g
    assert aa.denominator == 1 and bb.denominator == 1
    aa = int(aa); bb = int(bb)
    co = (g * g, -2 * g * aa, aa * aa - D * bb * bb)
    gg = math.gcd(math.gcd(abs(co[0]), abs(co[1])), abs(co[2])) or 1
    return max(abs(c) // gg for c in co)

for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7), Fr(3, 11)):
        mx = 0; d2 = True; nz = True
        for m in range(1, 3001):
            Am = A_of(al, r, m)
            if Am.b == 0: d2 = False
            if Am.sign() <= 0: nz = False
            mx = max(mx, height(Am) / m**2)
        P(f"    {nm:<16} {str(r):<7} {mx:<28.2f} {str(d2):<11} {nz}")
        assert d2 and nz
P("    => log H(A_m) = 2 log m + O(1), so Baker gives c_m >= exp(-c1 (log(m+2))^kappa)")
P("       with c1 = c1(alpha,rho,kappa) effective, UNIFORMLY in m >= 1.")

P("\n(F) The construction, end to end.  t(M) = min(C_M, 1/(K M));  ell(M) = least admissible")
P("    convergent denominator with ||q alpha|| < t(M)  ('admissible' = delta>0 when rho=0).")
P("    alpha            rho     M     C_M         ell(M)   L-ell   >=M")
def word_gen(al, r, n, cache):
    while len(cache) < n:
        m = len(cache)
        cache.append(chi((Q(m, 0, al.D) * al + Q(r, 0, al.D)).frac()))
    return cache

for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7)):
        cache = []; K = KTAB[(nm, r)]
        cms = [abs(A_of(al, r, m).approx() - BETA) for m in range(0, 70)]
        for M in (2, 4, 8, 16, 32):
            C_M = min(cms[:M]); t = min(C_M, 1.0 / (K * M))
            lm = None
            for q in qs[2:26]:
                if r == 0 and delta_of(al, q).sign() <= 0: continue
                if float(dist_to_int(Q(q, 0, al.D) * al).approx()) < t:
                    lm = q; break
            if lm is None or lm > 30000: 
                P(f"    {nm:<16} {str(r):<7} {M:<5} {C_M:<11.8f} {'-':<8} (beyond the computed range)")
                continue
            w = word_gen(al, r, 6 * lm + 400, cache)
            i = lm
            while i < len(w) and w[i] == w[i % lm]: i += 1
            ex = i - lm
            P(f"    {nm:<16} {str(r):<7} {M:<5} {C_M:<11.8f} {lm:<8} {ex:<7} {ex >= M}")
            assert ex >= M

P("\n(G) Drift and discrepancy, uniformly in rho.  For bounded-type alpha, Kuipers-Niederreiter")
P("    Ch.2 Thm 3.4 gives N*D_N({m alpha}) <= c1' sum_{i<=k+1} a_i + c2' <= c1' A (k+1) + c2',")
P("    and q_k <= N with q_k growing geometrically gives k = O(log N).  A shift by rho turns one")
P("    interval into at most two, so D_N({m alpha + rho}) <= 2 D_N({m alpha}): uniform in rho.")
P("    alpha            rho     max_{N<=20000} |k_N - N beta| / log2(N)")
for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7), Fr(1, 2)):
        cache = word_gen(al, r, 20001, [])
        k = 0; mx = 0.0
        for N in range(1, 20001):
            k += cache[N - 1]
            if N > 2: mx = max(mx, abs(k - N * BETA) / math.log2(N))
        P(f"    {nm:<16} {str(r):<7} {mx:.6f}")
        assert mx < 3.0

P("\n(H) Complexity of the actual coding (needed only for the COVERAGE claim, not the proof).")
P("    alpha            rho     p(6) p(12) p(20)   all = 2n?")
for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7)):
        cache = word_gen(al, r, 20001, [])
        vals = []
        for n in (6, 12, 20):
            vals.append(len({tuple(cache[i:i + n]) for i in range(20000 - n)}))
        P(f"    {nm:<16} {str(r):<7} {vals[0]:<4} {vals[1]:<5} {vals[2]:<7} {vals == [12, 24, 40]}")

P("\n(I) The quantitative content transfers: exact height floors for the general family.")
P("    If Phi(s)=u/v in lowest terms, H=max(|u|,v), then H >= 2^L / F(W), F = |2^ell-3^k| + c_W.")
P("    Every entry is an exact integer comparison.")
P("    alpha            rho     ell     k       L        H >= 2^S")
def c_of(W):
    k = sum(W); c = 0; run = 0
    for i, b in enumerate(W):
        if b:
            run += 1
            c += 3**(k - run) * 2**i
    return c, k
for nm, al, aq, ps, qs, A in SL:
    for r in (Fr(0), Fr(1, 7)):
        K = KTAB[(nm, r)]
        cms = [abs(A_of(al, r, m).approx() - BETA) for m in range(0, 70)]
        M = 32; C_M = min(cms[:M]); tt = min(C_M, 1.0 / (K * M))
        lm = None
        for q in qs[2:26]:
            if r == 0 and delta_of(al, q).sign() <= 0: continue
            if float(dist_to_int(Q(q, 0, al.D) * al).approx()) < tt:
                lm = q; break
        if lm is None or lm > 6000: continue
        cache = []
        w = word_gen(al, r, 8 * lm + 4000, cache)
        i = lm
        while i < len(w) and w[i] == w[i % lm]: i += 1
        W = w[:lm]; c, k = c_of(W); F = abs(2**lm - 3**k) + c
        S = i - F.bit_length()
        assert (1 << i) > F * (1 << max(S, 0))
        P(f"    {nm:<16} {str(r):<7} {lm:<7} {k:<7} {i:<8} 2^{S}")

P("\nALL PHASE-12 GENERALIZATION CHECKS PASS.")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
     "..", "..", "data", "phase12", "general_quadratic_output.txt"), "w").write("\n".join(out) + "\n")
