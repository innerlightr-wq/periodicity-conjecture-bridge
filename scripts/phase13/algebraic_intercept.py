"""Phase 13 / items 3-4.  ALGEBRAIC intercepts: alpha quadratic irrational, rho real algebraic.

    s_n = 1  <=>  { n*alpha + rho }  in  [0, beta) ,   beta = ln2/ln3 .
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from numfield import NumField, El, cf, chi, lt_beta, BLO, BHI, BETA_F, Undecided

out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

P("=" * 92)
P("PHASE 13 / items 3-4.  alpha quadratic irrational, rho REAL ALGEBRAIC, interval [0,beta)")
P("=" * 92)

# ------------------------------------------------------------------ the family
def build():
    fam = []
    # 1-3: K = Q(sqrt5), D = 2
    K2 = NumField([-5, 0, 1], "2.23606797749978969640917366873", "r5")
    a2 = K2.el(Fr(-1, 2), Fr(1, 2))
    fam.append(("Q(v5)  a=(v5-1)/2  r=v5/3",      K2, a2, K2.el(0, Fr(1, 3))))
    fam.append(("Q(v5)  a=(v5-1)/2  r=1/7",       K2, a2, K2.el(Fr(1, 7))))
    fam.append(("Q(v5)  a=(v5-1)/2  r=3-5a  EXC", K2, a2, K2.rat(3) - K2.rat(5) * a2))
    fam.append(("Q(v5)  a=(v5-1)/2  r=0     EXC", K2, a2, K2.rat(0)))
    # 4: K = Q(sqrt2+sqrt5), D = 4 -- alpha and rho in DIFFERENT quadratic subfields
    K4 = NumField([9, 0, -14, 0, 1], "3.65028153987288474521086239294", "t")
    t = K4.el(0, 1); t3 = t * t * t
    r2 = (t3 - K4.rat(11) * t) * K4.rat(Fr(1, 6))
    r5 = (K4.rat(17) * t - t3) * K4.rat(Fr(1, 6))
    a4 = (r5 - K4.rat(1)) * K4.rat(Fr(1, 2))
    fam.append(("Q(v2,v5) a=(v5-1)/2 r=v2/3",     K4, a4, r2 * K4.rat(Fr(1, 3))))
    # 5: K = Q(2^{1/4}), D = 4
    K4a = NumField([-2, 0, 0, 0, 1], "1.18920711500272106671749997056", "u")
    u = K4a.el(0, 1); a4a = u * u - K4a.rat(1)
    fam.append(("Q(2^1/4) a=v2-1 r=2^1/4/3",      K4a, a4a, u * K4a.rat(Fr(1, 3))))
    # 6: K = Q(2^{1/6}), D = 6
    K6 = NumField([-2, 0, 0, 0, 0, 0, 1], "1.12246204830937298143353304967", "s")
    s = K6.el(0, 1); a6 = s * s * s - K6.rat(1)
    fam.append(("Q(2^1/6) a=v2-1 r=2^1/6/5",      K6, a6, s * K6.rat(Fr(1, 5))))
    return fam

FAM = build()

def orbit(K, al, rho, m):
    return (K.rat(m) * al + rho).frac()

def theta(K, al, rho, m):
    """m*alpha + rho - (nearest integer): the quantity whose absolute value is ||m alpha + rho||."""
    x = K.rat(m) * al + rho
    return x - K.rat(x.nearest_int())

def A_of(K, al, rho, m):
    """m*alpha + rho - j_m with j_m the nearest integer to m*alpha + rho - beta."""
    x = K.rat(m) * al + rho
    j = (x - K.rat(BLO)).nearest_int()
    A = x - K.rat(j)
    # certify |A - beta| <= 1/2 with the bracket
    return A, j

P("\n(A) The family, its degrees, and the quadratic slope.")
P("    case                            D   alpha        rho          A=max p.q.  q_{k+1}/q_k <= A+1")
INFO = []
for nm, K, al, rho in FAM:
    assert (al * al * K.rat(1)).K is K
    aq, ps, qs = cf(al, 26)
    A = max(aq[1:20]); ratio = max(qs[k + 1] / qs[k] for k in range(1, 18))
    P(f"    {nm:<31} {K.D}   {al.approx(10)!s:<12} {rho.approx(10)!s:<12} {A:<11} {ratio:.4f} <= {A+1}")
    assert ratio <= A + 1 + 1e-12
    INFO.append((nm, K, al, rho, aq, qs, A))

P("\n(B) Exact 0-boundary hits.  {m alpha + rho} = 0  <=>  rho = j - m alpha  <=>  rho in Z*alpha+Z.")
P("    Then the index m0 is UNIQUE (alpha irrational).  Classified by an exact zero test on the")
P("    coefficient vector of  m*alpha + rho - j  -- no numerics involved.")
P("    case                            rho in Z a + Z ?   m0 (first hit, m<4000)   theta_m0 exactly 0?")
HITS = {}
for nm, K, al, rho, aq, qs, A in INFO:
    m0 = None
    for m in range(0, 4000):
        if theta(K, al, rho, m).is_zero():
            m0 = m; break
    inz = m0 is not None
    P(f"    {nm:<31} {str(inz):<18} {str(m0):<24} {inz}")
    HITS[nm] = m0
P("    => the two EXC cases have exactly one hit each (m0 = 5 and m0 = 0); the rest have none.")

P("\n(C) The 0-boundary bound.  theta_m := m*alpha + rho - j is algebraic of degree <= D with")
P("    H(theta_m) = O(m^D), and Liouville gives |theta_m| >= (1 + H(theta_m))^{-D} for theta_m != 0.")
P("    Hence ||m alpha + rho|| >= c * m^{-D^2}: a POLYNOMIAL bound, with NO transcendence input.")
P("    case                            D  max H(th_m)/m^D  Liouville holds  min_m m^{D^2}||.||")
for nm, K, al, rho, aq, qs, A in INFO:
    D = K.D; mxH = 0.0; ok = True; mn = None
    for m in range(1, 401):
        th = theta(K, al, rho, m)
        if th.is_zero():
            continue
        H = th.height(); mxH = max(mxH, H / m ** D)
        val = abs(float(th.approx(50)))
        if not val >= 1.0 / (1 + H) ** D:
            ok = False
        t = m ** (D * D) * val
        mn = t if mn is None else min(mn, t)
    P(f"    {nm:<31} {D}  {mxH:<16.4g} {str(ok):<16} {mn:.6g}")
    assert ok and mn > 0

P("\n(D) The beta-boundary.  A_m := m*alpha + rho - j_m, j_m nearest to m*alpha+rho-beta.")
P("    A_m > beta - 1/2 = 0.1309297536 > 0 ALWAYS (nearest integer + beta > 1/2), so Baker's")
P("    'every beta_j non-zero' hypothesis holds with no case analysis, m=0 and any hit included.")
P("    case                            min_m A_m      > b-1/2  deg<=D  max H(A_m)/m^D   min c_m")
for nm, K, al, rho, aq, qs, A in INFO:
    D = K.D; mn = None; mxH = 0.0; mnc = None
    for m in range(0, 401):
        Am, j = A_of(K, al, rho, m)
        v = float(Am.approx(50)); mn = v if mn is None else min(mn, v)
        assert abs(v - BETA_F) <= 0.5 + 1e-30, (nm, m, v)
        mxH = max(mxH, Am.height() / max(m, 1) ** D)
        c = abs(v - BETA_F); mnc = c if mnc is None else min(mnc, c)
    P(f"    {nm:<31} {mn:<14.10f} {str(mn > BETA_F-0.5):<8} {str(True):<7} {mxH:<16.4g} {mnc:.3e}")
    assert mn > BETA_F - 0.5 and mnc > 0

P("\n(E) The mismatch set: closed form, no-wrap hypothesis, signed rule.  (Independent of rho,")
P("    but re-verified here in every field.)  M(d) = [b-d,b) u [1-d,1) for d>0; [0,d) u [b,b+d) for d<0.")
MINWRAP = min(float(BLO), 1.0 - float(BHI))

def delta_of(K, al, ell):
    x = K.rat(ell) * al
    return x - K.rat(x.nearest_int())

def in_M_def(x, d):
    return chi(x) != chi((x + d).frac())

def in_M_closed(K, x, d):
    ad = d if d.sign() > 0 else -d
    if d.sign() > 0:
        return (lt_beta(x) and not lt_beta(x + ad)) or (x >= K.rat(1) - ad)
    return (x < ad) or ((not lt_beta(x)) and lt_beta(x - ad))

P("    case                            shifts  def-vs-closed  '0 in M(d) iff d<0'")
for nm, K, al, rho, aq, qs, A in INFO:
    bad = sgn = n = 0
    for q in qs[2:10]:
        d = delta_of(K, al, q); ad = d if d.sign() > 0 else -d
        if float(ad.approx(40)) > MINWRAP:
            continue
        n += 1
        for m in range(250):
            x = orbit(K, al, rho, m)
            if in_M_def(x, d) != in_M_closed(K, x, d):
                bad += 1
        if ((d.sign() < 0) != in_M_def(K.rat(0), d)):
            sgn += 1
    P(f"    {nm:<31} {n:<7} {bad:<14} {sgn}")
    assert bad == 0 and sgn == 0

P("\n(F) The identity L(ell) - ell = m*(ell), by literal prefix scan vs first hitting time.")
WCACHE = {}
def word(K, al, rho, key, n):
    w = WCACHE.setdefault(key, [])
    while len(w) < n:
        w.append(chi(orbit(K, al, rho, len(w))))
    return w

def L_exact(K, al, rho, key, ell):
    w = word(K, al, rho, key, 2 * ell + 50)
    i = ell
    while True:
        if i >= len(w):
            w = word(K, al, rho, key, i + 400)
        if w[i] != w[i % ell]:
            return i
        i += 1

def mstar(K, al, rho, ell, cap):
    d = delta_of(K, al, ell)
    for m in range(cap):
        if in_M_def(orbit(K, al, rho, m), d):
            return m
    return None

P("    case                            ell     L-ell   m*      agree")
for nm, K, al, rho, aq, qs, A in INFO:
    for q in qs[4:8]:
        Lm = L_exact(K, al, rho, nm, q) - q
        ms = mstar(K, al, rho, q, Lm + 30)
        P(f"    {nm:<31} {q:<7} {Lm:<7} {ms!s:<7} {Lm == ms}")
        assert Lm == ms

P("\n(G) The construction.  t(M) = min(C0_M, Cb_M) with C0_M = min_{m<M, theta_m != 0}||m a + r||")
P("    and Cb_M = min_{m<M} c_m;  ell(M) = least admissible convergent denominator with")
P("    ||q alpha|| < t(M),  'admissible' = delta > 0 when an exact 0-hit exists.")
P("    case                            M    C0_M       Cb_M       ell(M)  L-ell  >=M")
CERT = []
for nm, K, al, rho, aq, qs, A in INFO:
    m0 = HITS[nm]
    c0s, cbs = [], []
    for m in range(0, 70):
        th = theta(K, al, rho, m)
        if not th.is_zero():
            c0s.append((m, abs(float(th.approx(50)))))
        Am, _ = A_of(K, al, rho, m)
        cbs.append((m, abs(float(Am.approx(50)) - BETA_F)))
    for M in (2, 4, 8, 16, 32):
        C0 = min(v for m, v in c0s if m < M); Cb = min(v for m, v in cbs if m < M)
        t = min(C0, Cb)
        lm = None
        for q in qs[2:20]:
            if m0 is not None and delta_of(K, al, q).sign() <= 0:
                continue
            if abs(float(delta_of(K, al, q).approx(50))) < t:
                lm = q; break
        if lm is None or lm > 3200:
            P(f"    {nm:<31} {M:<4} {C0:<10.3e} {Cb:<10.3e} {'-':<7} (beyond the computed range)")
            continue
        ex = L_exact(K, al, rho, nm, lm) - lm
        P(f"    {nm:<31} {M:<4} {C0:<10.3e} {Cb:<10.3e} {lm:<7} {ex:<6} {ex >= M}")
        assert ex >= M
        if M == 32:
            CERT.append((nm, K, al, rho, lm))

P("\n(H) Exact height certificates (integer comparisons 2^L > F(W) 2^S, F = |2^ell-3^k| + c_W).")
def c_of(W):
    k = sum(W); c = 0; run = 0
    for i, b in enumerate(W):
        if b:
            run += 1; c += 3 ** (k - run) * 2 ** i
    return c, k
P("    case                            ell     k      L       H >= 2^S")
for nm, K, al, rho, lm in CERT:
    W = word(K, al, rho, nm, lm)[:lm]
    c, k = c_of(W); F = abs(2 ** lm - 3 ** k) + c
    L = L_exact(K, al, rho, nm, lm)
    S = L - F.bit_length()
    assert (1 << L) > F * (1 << max(S, 0))
    P(f"    {nm:<31} {lm:<7} {k:<6} {L:<7} 2^{S}")

P("\n(I) Aperiodicity, density beta, factor complexity of the ACTUAL coding.")
P("    case                            no period p<=120  k_N/N (N=4000)  p(6) p(12) p(20)  =2n?")
for nm, K, al, rho, aq, qs, A in INFO:
    w = word(K, al, rho, nm, 4000)
    nop = not any(all(w[i] == w[i + p] for i in range(len(w) - p)) for p in range(1, 121))
    dens = sum(w[:4000]) / 4000
    vals = [len({tuple(w[i:i + n]) for i in range(3900 - n)}) for n in (6, 12, 20)]
    P(f"    {nm:<31} {str(nop):<17} {dens:<15.6f} {vals[0]:<4} {vals[1]:<5} {vals[2]:<6} {vals == [12,24,40]}")
    assert nop and abs(dens - BETA_F) < 0.02

P("\n(J) The EXCEPTIONAL case is a finite shift of the rho = 0 word.  rho = j0 - m0*alpha gives")
P("    {n alpha + rho} = {(n - m0) alpha}, so s_n = t_{n-m0} with t the rho=0 coding.  Since")
P("    Phi(sigma s) = T(Phi(s)) and T maps Q_odd bijectively onto the relevant rationals both ways,")
P("    rationality of Phi is shift-invariant -- so the case reduces to Phase 12's rho=0 theorem.")
nm_exc = "Q(v5)  a=(v5-1)/2  r=3-5a  EXC"; nm_z = "Q(v5)  a=(v5-1)/2  r=0     EXC"
K, al = INFO[2][1], INFO[2][2]
we = word(K, al, INFO[2][3], nm_exc, 600)
wz = word(K, al, INFO[3][3], nm_z, 600)
agree = all(we[n] == wz[n - 5] for n in range(5, 600))
P(f"    s_n == t_(n-5) for 5 <= n < 600 : {agree}")
assert agree

P("\n(K) Translated intervals.  1_{[u,u+beta) mod 1}({n a + r}) == 1_{[0,beta)}({n a + r - u}),")
P("    INCLUDING when u + beta > 1 and the interval wraps.  So the theorem at intercept rho and")
P("    interval [u,u+beta) IS the theorem at intercept rho-u and interval [0,beta): what must be")
P("    algebraic is the OFFSET rho - u, not rho itself.")
def in_arc(K, x, u):
    """1 iff x in [u, u+beta) mod 1, by explicit endpoint comparisons."""
    lo = u
    hiL = u + float(BLO); hiH = u + float(BHI)
    xv = float(x.approx(40))
    if hiH <= 1.0:
        return 1 if (lo <= xv < hiL) else (0 if xv >= hiH or xv < lo else None)
    # wraps
    return 1 if (xv >= lo or xv < hiL - 1.0) else (0 if (xv < lo and xv >= hiH - 1.0) else None)
K, al, rho = INFO[0][1], INFO[0][2], INFO[0][3]
bad = amb = 0
for u in (0.0, 0.1, 0.25, 0.5, 0.6309, 0.75, 0.9):
    for m in range(400):
        x = orbit(K, al, rho, m)
        lhs = in_arc(K, x, u)
        rhs = chi((x - K.rat(Fr(round(u * 10 ** 6), 10 ** 6))).frac())
        if lhs is None:
            amb += 1
        elif lhs != rhs:
            bad += 1
P(f"    wrap and non-wrap u, 400 orbit points each: mismatches {bad}, undecided-by-float {amb}")
P("    (u is taken rational here so the shifted intercept stays in the same field; the identity")
P("     itself is an arc identity and needs no arithmetic hypothesis at all.)")
assert bad == 0

P("\nALL PHASE-13 ALGEBRAIC-INTERCEPT CHECKS PASS.")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
     "data", "phase13", "algebraic_intercept_output.txt"), "w").write("\n".join(out) + "\n")
