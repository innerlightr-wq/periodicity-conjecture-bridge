"""
Part 8: computational test of the bridge on complementary symmetric (CS) Rote
sequences, built via the EXACT construction confirmed from the literature
(Rote 1994; Dvorakova-Medkova-Pelantova 2020, arXiv:2003.06916):

    u = S(v)  <=>  u_i = v_i XOR v_{i+1}  for all i.

v is a CS Rote sequence iff u = S(v) is Sturmian. Equivalently, given a
Sturmian u and a seed bit v_0, the unique v with S(v)=u is the mod-2 partial
sum ("integral") of u:  v_{n} = v_0 XOR (u_0 XOR u_1 XOR ... XOR u_{n-1}).

ORIGINAL LEMMA (derived in this audit, not taken from the literature --
the literature's own "critical exponent" (cr) machinery is about exponents
of factors occurring ANYWHERE in the sequence, not specifically INITIAL
powers, so it does not directly answer what the bridge needs):

  If u has an initial power u[0:r*ell] = W^r (root W, |W|=ell, weight s =
  sum(W)), then v inherits an initial power as follows:
    - if s is EVEN: v[0:r*ell] = V^r for some V, |V|=ell  (SAME exponent r,
      same root length -- the parity sum returns to v_0 every period).
    - if s is ODD:  v[0:r*ell] = (V V-bar)^floor(r/2) [+ V if r odd], i.e.
      v has an initial power of root length 2*ell and exponent r/2 (the
      parity sum flips sign every period, so v alternates V, V-bar, V, ...).

  So: v's inherited initial exponent is r (even-weight root) or r/2
  (odd-weight root) -- i.e. AT WORST HALVED. For the bridge (needs exponent
  > log2(3) ~ 1.585) to transfer in the worst case, u itself needs initial
  exponent > 2*log2(3) ~ 3.170, not just > log2(3).

This script verifies the lemma computationally (exact integer arithmetic,
no floating point in the periodicity check itself) and then empirically
searches, for several concrete Sturmian slopes, whether u actually possesses
initial powers exceeding 3.170 with UNBOUNDED root length (not just a single
finite instance) -- which is what is actually required for the transferred
bridge to reach v via this route.
"""
import sys
sys.path.insert(0, ".")
from fractions import Fraction
from bridge_toolkit import initial_power_search, discrepancy, bridge_surplus_exact, c_W


def cf_convergent(partial_quotients, n_terms):
    """
    Exact rational convergent of [a0; a1, a2, ...] truncated to n_terms,
    via bottom-up folding: x <- a_i + 1/x, tracked as num/den (x=num/den).
    (A previous version of this function returned den/num -- the RECIPROCAL
    of the intended value -- by mistake; caught by a downstream sanity check
    when it produced density k>ell, an impossible value for a binary
    mechanical word, since the "silver ratio" slope came out as 2.414...
    instead of 0.414....)
    """
    num, den = 1, 0
    for a in reversed(partial_quotients[:n_terms]):
        num, den = a * num + den, num
    return Fraction(num, den)


def mechanical_word(gamma, n_terms):
    """s_n = floor((n+1)*gamma) - floor(n*gamma), n=0..n_terms-1, exact Fraction floor."""
    def fl(x):
        return x.numerator // x.denominator
    s = []
    prev = 0
    for n in range(1, n_terms + 1):
        cur = fl(n * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def rote_from_sturmian(u, v0=0):
    """v_0 = v0, v_{n+1} = v_n XOR u_n. Returns v of length len(u)+1."""
    v = [v0]
    for bit in u:
        v.append(v[-1] ^ bit)
    return v


def verify_transfer_lemma_on_examples():
    print("=== Verifying the even/odd-weight initial-power transfer lemma ===")
    # Build a short periodic u with an even-weight root and an odd-weight root,
    # check v's induced structure directly, exact.
    for W, label in [([0, 1, 1, 0], "weight 2 (even)"), ([0, 1, 1], "weight 2 (even), len3"),
                      ([0, 1, 0, 1, 1], "weight 3 (odd)")]:
        ell = len(W)
        s = sum(W)
        r = 5
        u = (W * r)[: r * ell]
        v = rote_from_sturmian(u, v0=0)
        if s % 2 == 0:
            V = v[:ell]
            ok = v[: r * ell] == (V * r)[: r * ell]
            print(f"  W={W} ({label}): predicted v period {ell}, exponent {r} -> match={ok}")
        else:
            V2 = v[: 2 * ell]
            achieved = r * ell // (2 * ell)
            ok = v[: achieved * 2 * ell] == (V2 * achieved)[: achieved * 2 * ell]
            print(f"  W={W} ({label}): predicted v period {2*ell}, exponent {r/2} "
                  f"(root V,Vbar) -> match={ok}")
    print()


def all_initial_powers(s, max_check_len, max_root):
    """Every primitive-root initial power (r>=1, i.e. L>=ell) up to max_root, no r-filter."""
    from bridge_toolkit import lcp, periodic_extension
    results = []
    for ell in range(1, max_root + 1):
        W = s[:ell]
        primitive = True
        for d in range(1, ell):
            if ell % d == 0 and all(W[i] == W[i % d] for i in range(ell)):
                primitive = False
                break
        if not primitive:
            continue
        ext = periodic_extension(W, max_check_len)
        L = lcp(s, ext, max_check_len)
        if L < ell:
            continue
        results.append({"ell": ell, "k": sum(W), "L": L, "r": Fraction(L, ell), "W": W})
    results.sort(key=lambda d: -d["ell"])
    return results


def scan_slope(name, gamma, n_terms=6000, max_root=1200):
    """
    THE decisive test is the exact surplus S = L - ceil(log2(F(W))) for each
    candidate initial power, NOT any fixed r-threshold (r>log2(3) alone is
    NOT unconditionally sufficient -- only asymptotically, and only once the
    discrepancy-rate term is accounted for; REPETITION_HEIGHT_CRITERION.md's
    only UNCONDITIONAL guarantee is at r>=2). Report every candidate's exact
    S, and flag which ones genuinely certify (S>0).
    """
    print(f"=== Slope {name}: gamma = {float(gamma):.8f} ===")
    u = mechanical_word(gamma, n_terms)
    v = rote_from_sturmian(u, v0=0)[:-1]

    check_len = min(n_terms, 2 * max_root)
    u_powers = all_initial_powers(u, check_len, max_root)
    v_powers = all_initial_powers(v, check_len, max_root)

    def summarize(label, powers):
        certifying = []
        for p in powers:
            S, F = bridge_surplus_exact(p["L"], p["W"])
            p["S"] = S
            if S > 0:
                certifying.append(p)
        print(f"  {label}: {len(powers)} initial powers total (r>=1); "
              f"{len(certifying)} have POSITIVE exact surplus (S>0, genuine unconditional certification).")
        if certifying:
            deepest = max(certifying, key=lambda d: d["ell"])
            print(f"    deepest certifying root: ell={deepest['ell']} r={float(deepest['r']):.4f} "
                  f"S={deepest['S']} (integer lower bound on log2-margin)")
        elif powers:
            best = max(powers, key=lambda d: d["r"])
            print(f"    best r found (non-certifying): ell={best['ell']} r={float(best['r']):.4f} S={best['S']}")
        return certifying

    uc = summarize("u (Sturmian)", u_powers)
    vc = summarize("v (CS Rote)", v_powers)
    print(f"  -> {'BRIDGE FIRES on v' if vc else 'bridge does not fire on v'} at this slope, up to root {max_root}.")
    print()
    return u_powers, v_powers


def main():
    verify_transfer_lemma_on_examples()

    prec = 60
    golden = cf_convergent([0] + [1] * prec, prec + 1)                 # [0;1,1,1,...]
    silver = cf_convergent([0] + [2] * prec, prec + 1)                 # [0;2,2,2,...]
    mixed = cf_convergent([0] + [1, 2, 1, 3, 1, 4, 1, 5] * (prec // 8 + 1), prec + 1)  # growing-ish

    scan_slope("golden ratio conjugate [0;1,1,1,...]", golden)
    scan_slope("silver ratio [0;2,2,2,...]", silver)
    scan_slope("mixed bounded-but-larger CF [0;1,2,1,3,1,4,...]", mixed)


if __name__ == "__main__":
    main()
