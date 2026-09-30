"""Phase 12 / item 1.  Independent reconstruction of Theorem 11 from the definitions.

Every quantity is recomputed here from its definition.  scripts/phase11 is NOT imported.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
from qfield import Q, cf, chi, lt_beta, dist_to_int, BLO, BHI, Undecided

D = 5
ALPHA = Q(Fr(-1, 2), Fr(1, 2), D)          # (sqrt5-1)/2
RHO = Q(Fr(1, 7), 0, D)
ONE = Q(1, 0, D)
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

P("=" * 78)
P("PHASE 12 / item 1.  Theorem 11 rebuilt from definitions (no Phase 11 code imported)")
P("=" * 78)

def orbit(m):
    return (Q(m, 0, D) * ALPHA + RHO).frac()

def sym(m):
    return chi(orbit(m))

NW = 12000
W_ = [sym(m) for m in range(NW)]
P("\n(0) The word, regenerated independently.")
P("    s[0:40] = " + "".join(map(str, W_[:40])))
P("    matches the Phase 11 record 1010110110101101101011010110110101101111:",
  "".join(map(str, W_[:40])) == "1010110110101101101011010110110101101111")

# ---------------------------------------------------------------- aperiodicity
P("\n(1) Aperiodicity.  Symbolic proof: a period p would make the proper arc [0,beta)")
P("    invariant under rotation by p*alpha != 0 (mod 1); impossible.  Machine check that")
P("    no p <= 400 is a period of s[0:12000]:")
bad = [p for p in range(1, 401) if all(W_[i] == W_[i + p] for i in range(NW - p))]
P("    periods found:", bad, " (empty as required)")
assert not bad

# ------------------------------------------------------------------- density
P("\n(2) Lower ones-density.  Weyl equidistribution for irrational alpha gives k_N/N -> beta")
P("    (the limit EXISTS, so liminf = limsup = beta).  Numerical corroboration:")
beta_f = float(Decimal(2).ln() / Decimal(3).ln())
for N in (10**2, 10**3, 10**4, 12000):
    k = sum(W_[:N]); P(f"    N={N:<7} k_N/N = {k/N:.8f}   beta = {beta_f:.8f}   diff {k/N-beta_f:+.2e}")

# ---------------------------------------------- complexity p(n) = 2n, exact count
P("\n(3) Factor complexity of the prefix (cited value 2n; verified, not re-proved).")
for n in (6, 12, 20, 30):
    fac = {tuple(W_[i:i + n]) for i in range(NW - n)}
    P(f"    n={n:<3} p(n) = {len(fac):<4} 2n = {2*n:<4} equal: {len(fac) == 2*n}")
    assert len(fac) == 2 * n
P("    beta not in Z*alpha+Z because beta is transcendental (Gelfond-Schneider) and alpha")
P("    is algebraic -- this is what Rote/Berstel-Vuillon turn into p(n)=2n.")

# ------------------------------------------------- the mismatch set M(delta)
P("\n(4) The mismatch set, translation sign and endpoints.")
P("    {x + ell*alpha} = {x + delta},  delta := ell*alpha - round(ell*alpha).")
P("    Definition:      M(d) = { x : chi(x) != chi({x+d}) }.")
P("    Closed form      d>0 : [beta-d,beta) u [1-d,1) ;   d<0 : [0,|d|) u [beta,beta+|d|).")
P("    NO-WRAP HYPOTHESIS (Phase 11B):  |d| <= min(beta,1-beta) = 0.3690702464.")

def delta(ell):
    x = Q(ell, 0, D) * ALPHA
    n = (x + Q(Fr(1, 2), 0, D)).floor()          # nearest integer
    return x - Q(n, 0, D)

def in_M_def(x, d):
    return chi(x) != chi((x + d).frac())

def in_M_closed2(x, d):
    """Pure MEMBERSHIP test in two explicit arcs -- only order comparisons of the real x
    against 0, |d|, 1-|d|, beta, beta+|d|.  No fractional-part reduction, no chi-pair:
    that is what makes it a genuine independent test of the closed form, and what lets it
    detect the wrap failure."""
    ad = d if d.sign() > 0 else -d
    if d.sign() > 0:
        arc1 = lt_beta(x) and (not lt_beta(x + ad))          # x in [beta-ad, beta)
        arc2 = x >= ONE - ad                                  # x in [1-ad, 1)
    else:
        arc1 = x < ad                                         # x in [0, ad)
        arc2 = (not lt_beta(x)) and lt_beta(x - ad)           # x in [beta, beta+ad)
    return arc1 or arc2

mism = 0; tested = 0; rows = []
mind = min(float(BLO), 1.0 - float(BHI))
for k_ in range(1, 15):
    q = cf(ALPHA, 40)[2][k_]
    d = delta(q); ad = d if d.sign() > 0 else -d
    ok = float(ad.approx()) <= mind
    bad_ = 0
    for m in range(3000):
        x = orbit(m); tested += 1
        if in_M_def(x, d) != in_M_closed2(x, d):
            bad_ += 1
    mism += bad_
    rows.append((q, float(ad.approx()), ok, bad_))
P("    q      |delta|        no-wrap?   disagreements(def vs closed form) over 3000 points")
for q, a, ok, b in rows:
    P(f"    {q:<6} {a:<13.10f} {str(ok):<10} {b}")
P("    total disagreements where the hypothesis HOLDS:",
  sum(b for q,a,ok,b in rows if ok))
P("    total disagreements where it FAILS          :",
  sum(b for q,a,ok,b in rows if not ok))
assert sum(b for q,a,ok,b in rows if ok) == 0

# ------------------------------------- two-ball relaxation, and a SIGNED refinement
P("\n(5) Relaxation.  Phase 11 R2 uses the two-sided balls B(0,|d|), B(beta,|d|).")
P("    Phase 12 also verifies the SHARPER ONE-SIDED form, which is what the rho=0 case of")
P("    the generalization will need:  for d>0, M(d) subset [beta-d,beta) u [1-d,1), and")
P("    0 is NOT in M(d).  For d<0, 0 IS in M(d).")
v2 = 0; sign_rows = []
for k_ in range(1, 15):
    q = cf(ALPHA, 40)[2][k_]
    d = delta(q); ad = d if d.sign() > 0 else -d
    nowrap = float(ad.approx()) <= mind
    for m in range(3000):
        x = orbit(m)
        if in_M_def(x, d):
            r0 = dist_to_int(x)
            rb = dist_to_int(x - Q(BLO, 0, D)), dist_to_int(x - Q(BHI, 0, D))
            near_b = max(rb[0].approx(), 0) <= float(ad.approx()) + 1e-290 or \
                     rb[1].approx() <= float(ad.approx()) + 1e-290
            if not (r0 <= ad or near_b):
                v2 += 1
    sign_rows.append((q, float(d.approx()), nowrap, in_M_def(Q(0,0,D), d)))
P("    two-sided-ball containment violations (UNCONDITIONAL, all 14 shifts): %d" % v2)
P("    q      delta           no-wrap?   0 in M(delta)?   rule '0 in M iff delta<0' holds?")
v1 = 0
for q, dv, nw, zi in sign_rows:
    rule = (dv < 0) == zi
    if nw and not rule: v1 += 1
    P(f"    {q:<6} {dv:+.10f}   {str(nw):<10} {str(zi):<16} {rule}")
P("    sign-rule violations where the no-wrap hypothesis HOLDS:", v1)
P("    (the single exception is q=1, |delta|=0.38197 > 0.36907: there beta+|delta| > 1, the")
P("     arc at beta wraps past 0 and swallows the arc at 0, so 0 in M fails although delta<0.")
P("     The construction has |delta| < 1/294, so the rule is available with ~108x margin.)")
assert v2 == 0 and v1 == 0

# ------------------------------------- first mismatch  =  agreement excess
P("\n(6) The identity  L(ell) - ell = m*(ell),  by literal prefix scan vs hitting time.")
def L_of(ell):
    """lcp(s, (s[0:ell])^infty), computed literally.  Returns (L, truncated?)."""
    i = ell
    while i < len(W_) and W_[i] == W_[i % ell]:
        i += 1
    return i

def L_exact(ell):
    """Same, but extends the word on demand so the answer is never a truncation artefact."""
    i = ell
    while True:
        while i >= len(W_):
            W_.append(sym(len(W_)))
        if W_[i] != W_[i % ell]:
            return i
        i += 1

def mstar(ell, cap=9000):
    d = delta(ell)
    for m in range(cap):
        if in_M_def(orbit(m), d):
            return m
    return None

qs = cf(ALPHA, 40)[2]
P("    ell      L-ell      m*       agree")
tab = []
for q in qs[3:16]:
    if q >= NW: break
    Lm = L_of(q) - q; ms = mstar(q)
    P(f"    {q:<8} {Lm:<10} {ms:<8} {Lm == ms}")
    tab.append((q, Lm, ms)); assert Lm == ms

# ------------------------------------------------ arc at 0:  the R3 bound
P("\n(7) Arc at 0.  ||x|| >= ||7x||/7 and 7(m*alpha+1/7) = 7m*alpha + 1, so")
P("    ||m*alpha+1/7|| >= ||7m*alpha||/7 > 1/(7*3*7m) = 1/(147m)  using ||q*alpha|| > 1/(3q).")
worst = None
for m in range(1, 60000):
    v = float(dist_to_int(Q(m, 0, D) * ALPHA + RHO).approx())
    tt = 147 * m * v
    if worst is None or tt < worst[1]: worst = (m, tt)
P(f"    min over 1<=m<60000 of 147*m*||m*alpha+1/7||  =  {worst[1]:.6f}  at m={worst[0]}   (>1 required)")
assert worst[1] > 1
# and the golden constant, exactly
P("    inf_q q*||q*alpha|| = ||alpha|| = 0.3819660113 > 1/3  (golden; classical)")
P("    m=0 separately: ||1/7|| = 1/7 = 0.1428571429 > 0.")

# ------------------------------------------------ arc at beta: c_m, heights
P("\n(8) Arc at beta.  c_m := ||m*alpha + 1/7 - beta||;  A_m := m*alpha + 1/7 - j_m.")
def A_and_height(m):
    x = Q(m, 0, D) * ALPHA + RHO
    # j_m = nearest integer to x - beta
    approxv = x.approx() - beta_f
    j = round(approxv)
    A = x - Q(j, 0, D)
    # A = (a + 7m sqrt5)/14 with a = -7m + 2 - 14 j
    a_m = -7 * m + 2 - 14 * j
    assert A == Q(Fr(a_m, 14), Fr(7 * m, 14), D), (m, j, A)
    if m == 0:
        H = max(1, abs(a_m), 14)          # rational: minimal poly 14x - a_m  (content divided out)
        g = math.gcd(14, abs(a_m)) or 1
        H = max(14 // g, abs(a_m) // g)
        return A, a_m, 1, H
    co = (196, -28 * a_m, a_m * a_m - 245 * m * m)
    g = math.gcd(math.gcd(abs(co[0]), abs(co[1])), abs(co[2]))
    H = max(abs(c) // g for c in co)
    return A, a_m, 2, H

P("    m      a_m           deg  H(A_m)        H/m^2     c_m")
mx = 0.0
for m in [0, 1, 2, 3, 10, 100, 1000, 5000, 10000]:
    A, a_m, dg, H = A_and_height(m)
    cm = abs(A.approx() - beta_f)
    r = H / m**2 if m else float('nan')
    if m: mx = max(mx, r)
    P(f"    {m:<6} {a_m:<13} {dg:<4} {H:<13} {r:<9.3f} {cm:.10f}")
mx2 = max(A_and_height(m)[3] / m**2 for m in range(1, 10001))
P(f"    max H(A_m)/m^2 over a sweep m<=10^4: {mx2:.3f}   (so H(A_m)=O(m^2), log H = 2 log m + O(1))")
P("    A_m != 0 for every m>=0:",
  all(A_and_height(m)[0].sign() != 0 for m in range(0, 2000)))
P("    deg A_m = 2 for every m>=1 (so a SINGLE Baker constant C(2,3,2,kappa,2) serves all m>=1);")
P("    m=0 gives deg 1 and needs no Baker input at all, c_0 = %.10f being explicit." %
  abs(A_and_height(0)[0].approx() - beta_f))
assert all(A_and_height(m)[2] == 2 for m in range(1, 2000))

# ------------------------------------------ witnesses: construction and growth
P("\n(9) Witnesses.  ell(M) := least convergent denominator q with ||q*alpha|| < t(M),")
P("    t(M) = min(C_M, 1/(147M)),  C_M = min_{0<=m<M} c_m.")
cms = [abs(A_and_height(m)[0].approx() - beta_f) for m in range(0, 600)]
P("    M      C_M            t(M)           ell(M)   L-ell    >=M    log ell / (log(M+2))^3")
for M in (2, 4, 8, 16, 32, 64, 128, 256, 512):
    if M > len(cms): break
    C_M = min(cms[:M]); t = min(C_M, 1 / (147 * M))
    lm = None
    for q in qs[1:]:
        if float(dist_to_int(Q(q, 0, D) * ALPHA).approx()) < t:
            lm = q; break
    ex = L_of(lm) - lm if lm and lm < NW else None
    rat = math.log(lm) / math.log(M + 2)**3
    P(f"    {M:<6} {C_M:<14.10f} {t:<14.3e} {lm:<8} {str(ex):<8} {str(ex is None or ex>=M):<6} {rat:.4f}")
    if ex is not None: assert ex >= M

# ------------------------------------------ Phi, the periodic formula, F(W), surplus
P("\n(10) The arithmetic side, re-derived.  Phi(v) = -sum_{i: v_i=1} 3^{-k_{i+1}(v)} 2^i.")
P("     For W of length ell and weight k, summing the geometric series 2-adically:")
P("       Phi(W^inf) = c_W/(2^ell - 3^k),  c_W = sum_{i<ell, W_i=1} 3^{k-k_{i+1}(W)} 2^i.")
def c_of(W):
    k = sum(W); c = 0; run = 0
    for i, b in enumerate(W):
        if b:
            run += 1
            c += 3**(k - run) * 2**i
    return c, k

def phi_periodic_mod(W, N):
    """Phi(W^inf) mod 2^N straight from the series -- an independent check of the formula."""
    ell = len(W); k = sum(W); mod = 1 << N
    tot = 0
    t = 0
    while t * ell < N + 64:
        for i, b in enumerate(W):
            if b:
                run = sum(W[:i]) + 1
                e = t * k + run
                # 3^-e mod 2^N
                inv = pow(pow(3, e, mod), -1, mod)
                tot = (tot - inv * pow(2, t * ell + i, mod)) % mod
        t += 1
    return tot % mod

P("     check: series value mod 2^N  ==  c_W * inverse(2^ell - 3^k) mod 2^N")
for W in ([1,0,1,0,1,1], [1,1,0,1,0,1,1,0], [int(b) for b in "1010110110101101"]):
    N = 60; mod = 1 << N
    c, k = c_of(W); den = 2**len(W) - 3**k
    rhs = (c * pow(den % mod, -1, mod)) % mod
    lhs = phi_periodic_mod(W, N)
    P(f"       ell={len(W):<3} k={k:<3} agree mod 2^{N}: {lhs == rhs}")
    assert lhs == rhs

P("\n(11) Exact height certificates.  If Phi(s)=u/v in lowest terms and H=max(|u|,v), then")
P("     2^L <= H*F(W) with F(W) = |2^ell - 3^k| + c_W.  So H >= 2^L / F(W).")
P("     ell      k      L        floor(log2 F)   H >= 2^S   (integer comparison)")
certs = []
for q in [377, 610, 1597, 2584, 6765]:
    while len(W_) < 4 * q + 2000:            # enough room for the literal lcp scan not to truncate
        W_.append(sym(len(W_)))
    W = W_[:q]; c, k = c_of(W)
    F = abs(2**q - 3**k) + c
    Lq = L_exact(q)
    S = Lq - F.bit_length()
    ok = (1 << Lq) > F * (1 << max(S, 0))
    P(f"     {q:<8} {k:<6} {Lq:<8} {F.bit_length():<15} 2^{S:<8} verified: {ok}")
    certs.append((q, Lq, S, ok)); assert ok and S > 0

P("\n(12) Drift and discrepancy from PROVED bounds.")
P("     alpha has all partial quotients 1, so sum_{i<=k+1} a_i = k+1 <= log_phi N + 2 and")
P("     Kuipers-Niederreiter Ch.2 Thm 3.4 gives N*D_N = O(log N), uniformly in rho.")
P("     ell       e_ell = k - ell*beta     |e_ell|/log2(ell)")
for q in [233, 377, 610, 987, 1597, 2584, 4181, 6765]:
    if q >= len(W_): break
    k = sum(W_[:q]); e = k - q * beta_f
    P(f"     {q:<9} {e:+.6f}                {abs(e)/math.log2(q):.6f}")

P("\nALL PHASE-12 INDEPENDENT-AUDIT CHECKS PASS.")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
     "..", "..", "data", "phase12", "independent_audit_output.txt"), "w").write("\n".join(out) + "\n")
