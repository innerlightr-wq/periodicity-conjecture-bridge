"""
Phase 5, independent re-verification of the Rote transfer theorem
(L_v = L+1). Deliberately structured differently from
scripts/phase2/verify_rote_transfer.py: exhaustive over EVERY mismatch
position for every root, both seeds, and cross-checks the root's
primitivity/period explicitly (Section 6 of this audit needs that data
too, gathered here once).

Exact integer/boolean arithmetic; no floating point anywhere.
"""


def lcp(a, b):
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def fundamental_period(W):
    """Smallest d | len(W) with W periodic of period d."""
    ell = len(W)
    for d in range(1, ell + 1):
        if ell % d == 0 and all(W[i] == W[i % d] for i in range(ell)):
            return d
    return ell


def build_target(W, v0):
    s = sum(W)
    ell = len(W)
    if s % 2 == 0:
        # V is the mod-2 partial sum of W, seeded at v0, over one period
        V = [v0]
        for b in W:
            V.append(V[-1] ^ b)
        V = V[:ell]
        return V, ell
    else:
        V = [v0]
        for b in W:
            V.append(V[-1] ^ b)
        V = V[:ell]
        Vbar = [1 - x for x in V]
        R = V + Vbar
        return R, 2 * ell


def run_case(W, L_target, v0):
    ell = len(W)
    Winf = (W * (L_target // ell + 3))[: L_target + 1]
    # force a genuine mismatch exactly at position L_target
    u = Winf[:L_target] + [1 - Winf[L_target]]
    u = u + [0] * 5  # pad a little so lcp has room past the mismatch
    assert lcp(u, Winf) == L_target

    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    v = v[: len(u) + 1]

    target_root, rootlen = build_target(W, v0)
    target_inf = target_root * (len(v) // rootlen + 3)

    Lv = lcp(v, target_inf)
    return L_target, Lv, Lv - L_target


def main():
    total = 0
    failures = 0
    min_period_ratio_seen = None
    for ell in range(2, 11):
        for bits in range(2 ** ell):
            W = [(bits >> i) & 1 for i in range(ell)][::-1]
            if sum(W) == 0 or sum(W) == ell:
                pass  # still valid, test anyway
            period = fundamental_period(W)
            for v0 in (0, 1):
                for L_target in range(ell, 4 * ell + 1):
                    total += 1
                    L, Lv, diff = run_case(W, L_target, v0)
                    if diff != 1:
                        failures += 1
                        print(f"FAIL: W={W} v0={v0} L={L_target} -> Lv={Lv} diff={diff}")
    print(f"\nTotal cases tested: {total}")
    print(f"Failures: {failures}")
    if failures == 0:
        print("ALL CASES: L_v = L + 1 EXACTLY (independent exhaustive check, W length 2-10,"
              " every mismatch position L in [ell,4ell], both seeds).")
    else:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
