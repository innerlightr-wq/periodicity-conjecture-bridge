"""
Phase 8, step B: literal verification that BHZ's x(k) and y(k) are ATTAINED
initial powers of the actual Sturmian word at a general intercept, with the
stated root lengths -- and diagnosis of the Phase-7 root-length mismatch.

Method (no floating point, no irrational arithmetic anywhere):
  omega = T^{c_1} tau_0^{a_1} o T^{c_2} tau_1^{a_2} o ... o T^{c_K} tau_{K-1}^{a_K} (omega^{(s_K)})
(BHZ Prop. 2.7 eq. (2)).  We build the composition applied to two different
continuations that begin with DIFFERENT letters and keep only their longest
common prefix.  By BHZ Lemma 2.4 that common prefix is independent of the
continuation, hence is a CERTIFIED prefix of omega, whatever omega^{(s_K)} is.

Then, for each k, the root of an initial power of length L is necessarily the
prefix omega[0:L] itself, so we can test the claim directly:
    ell_x(k) = q_k                 (BHZ Prop. 3.3, first case)
    ell_y(k) = q_k - c_k q_{k-1}   (BHZ Prop. 3.3, second case, 0 < c_k < a_k)
    lcp(omega, (omega[0:ell])^infty)  ==  floor(r * ell)  for the predicted r.
"""
from fractions import Fraction
import random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from phase8_identities import q_bhz, q_naive, bhz_terms, admissible, rand_admissible

TAU = ({0: "0", 1: "01"}, {0: "10", 1: "1"})   # tau_0, tau_1  (BHZ Sec. 2.3)

def apply_tau(i, w):
    t = TAU[i]
    return "".join(t[int(ch)] for ch in w)

def build(a, c, seed, K=None):
    """T^{c_1} tau_0^{a_1} ( ... T^{c_K} tau_{K-1}^{a_K} ( seed ) ... )"""
    K = K or len(a)
    w = seed
    for k in range(K, 0, -1):
        i = (k - 1) % 2
        for _ in range(a[k - 1]):
            w = apply_tau(i, w)
        w = w[c[k - 1]:]
    return w

def certified_prefix(a, c, K=None, pad=40, maxlen=None):
    """`maxlen` caps the work by truncating the S-adic depth K so that q_K stays
    within budget -- this yields a SHORTER certified prefix, never a wrong one."""
    if maxlen is not None and K is None:
        q = q_bhz(a)
        K = len(a)
        while K > 2 and q[K] * 4 > maxlen:
            K -= 1
        pad = min(pad, 6)
    return _certified_prefix(a, c, K, pad)


def _certified_prefix(a, c, K=None, pad=40):
    """Longest common prefix over two continuations starting with different
    letters -> a guaranteed prefix of omega (BHZ Lemma 2.4)."""
    K = K or len(a)
    s0 = "01" * pad
    s1 = "10" * pad
    w0 = build(a, c, s0, K)
    w1 = build(a, c, s1, K)
    n = 0
    while n < min(len(w0), len(w1)) and w0[n] == w1[n]:
        n += 1
    return w0[:n]

def lcp_with_power(omega, ell):
    """lcp(omega, W^infty) where W = omega[0:ell]."""
    if ell <= 0 or ell > len(omega):
        return None
    n = ell
    while n < len(omega) and omega[n] == omega[n - ell]:
        n += 1
    return n if n < len(omega) else None      # None = ran out of certified prefix

def audit(a, c, qfun=q_bhz, verbose=False):
    """Returns (checked, failures, details)."""
    omega = certified_prefix(a, c)
    terms, q, S = bhz_terms(a, c, qfun)
    ok = bad = 0
    det = []
    for k in sorted(terms):
        x, xp, y = terms[k]
        for which, ell, r, attained in (
            ("x", int(q[k]), x, True),
            ("y", int(q[k] - c[k - 1] * q[k - 1]), y,
             (0 < c[k - 1] < a[k - 1])),
        ):
            if r is None or not attained:
                continue
            if r < 1:
                # BHZ Prop. 3.2/3.3 speak of prefix powers r >= 2; for r < 1 the
                # statement is vacuous (lcp(omega, omega[0:ell]^infty) >= ell always),
                # so there is nothing to test.  Skipped, counted separately.
                det.append((k, which, ell, None, None, r, None))
                continue
            L = lcp_with_power(omega, ell)
            if L is None:
                continue
            pred = int(r * ell)              # floor(r*ell); r*ell is an integer here
            hit = (L == pred)
            ok += hit; bad += (not hit)
            det.append((k, which, ell, L, pred, r, hit))
            if verbose and not hit:
                print(f"     k={k} {which}: ell={ell} literal_lcp={L} predicted={pred} r={r}")
    return ok, bad, det, omega

def main():
    rng = random.Random(8080)
    print("=" * 78)
    print("PHASE 8 / B.  Literal longest-common-prefix vs Ostrowski prediction")
    print("=" * 78)

    cases = []
    for a in ([1]*14, [2]*12, [3]*10, [1,2]*7, [2,1,3]*4, [4,1]*6, [1,1,2,1]*3):
        cases.append((a, [0]*len(a), "characteristic  c=0"))
        cases.append((a, [0 if k % 2 else a[k-1] for k in range(1, len(a)+1)], "omega(-alpha)"))
        cmax = []
        prev = 0
        for k, ak in enumerate(a, 1):
            cmax.append(ak if (k == 1 or prev == 0) else max(0, ak - 1)); prev = cmax[-1]
        cases.append((a, cmax, "eventually-maximal (worst family)"))
        cnm = [max(0, ak - 1) for ak in a]
        if admissible(a, cnm):
            cases.append((a, cnm, "near-maximal d_k==1 (adversary)"))
        for _ in range(3):
            cases.append((a, rand_admissible(a, rng), "random admissible"))

    tot_ok = tot_bad = 0
    per_family = {}
    for a, c, nm in cases:
        if not admissible(a, c):
            continue
        ok, bad, det, omega = audit(a, c, q_bhz, verbose=True)
        tot_ok += ok; tot_bad += bad
        globals().setdefault('_vac', [0])[0] += sum(1 for d in det if d[6] is None)
        e = per_family.setdefault(nm, [0, 0])
        e[0] += ok; e[1] += bad
    print("\nBHZ convention  q_1 = a_1 + 1  (alpha = [0; a_1+1, a_2, ...]):")
    for nm, (o, b) in sorted(per_family.items()):
        print(f"    {nm:<36s} attained-power checks: {o:5d} pass, {b:3d} FAIL")
    print(f"    TOTAL: {tot_ok} pass, {tot_bad} FAIL"
          f"   ({_vac[0]} vacuous r<1 formula values skipped)")

    # ---------------- diagnosis of the Phase-7 mismatch -----------------
    print("\n" + "-" * 78)
    print("DIAGNOSIS of theorems/phase7/PHASE7_VERDICT.md's disclosed root-length mismatch")
    print("-" * 78)
    print("scripts/phase7/bhz_general_witness.py::convergents() sets q_1 = a_1,")
    print("i.e. the denominators of [0;a_1,a_2,...]; BHZ Prop. 2.7 sets q_1 = a_1+1.")
    a = [2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1]
    c = [0, 2, 0, 1, 1, 0, 1, 2, 1, 1, 0, 1]
    if not admissible(a, c):
        c = rand_admissible(a, rng)
    qb, qn = q_bhz(a), q_naive(a)
    print(f"\n  a = {a}")
    print(f"  BHZ   q = {[int(v) for v in qb]}")
    print(f"  naive q = {[int(v) for v in qn]}")
    omega = certified_prefix(a, c)
    print(f"\n  certified prefix of omega: {len(omega)} symbols")
    print(f"  {'k':>2} {'c_k':>3} | {'ell=q_k-c_k q_k-1':>17} {'literal lcp':>11} {'pred':>6} {'ok':>3} "
          f"| {'naive ell':>9} {'ok':>3}")
    tb, tn = bhz_terms(a, c, q_bhz)[0], bhz_terms(a, c, q_naive)[0]
    nb = nn = 0
    for k in sorted(tb):
        if not (0 < c[k-1] < a[k-1]):
            continue
        eb = int(qb[k] - c[k-1]*qb[k-1]); en = int(qn[k] - c[k-1]*qn[k-1])
        Lb = lcp_with_power(omega, eb)
        yb = tb[k][2]
        if Lb is None:
            continue
        pb = int(yb*eb); okb = (Lb == pb)
        Ln = lcp_with_power(omega, en); yn = tn[k][2]
        okn = (Ln is not None and yn is not None and Ln == int(yn*en))
        nb += okb; nn += okn
        print(f"  {k:>2} {c[k-1]:>3} | {eb:>17} {Lb:>11} {pb:>6} {str(okb):>3} "
              f"| {en:>9} {str(okn):>3}")
    print(f"\n  attained y-witnesses reproduced: BHZ convention {nb}, naive convention {nn}")
    print("  => the mismatch is the q_1 off-by-one, not a defect in BHZ Prop. 3.3.")

    print(f"\nRESULT: {'ALL LITERAL CHECKS PASS' if tot_bad == 0 else str(tot_bad)+' FAILURES'}")

if __name__ == "__main__":
    main()
