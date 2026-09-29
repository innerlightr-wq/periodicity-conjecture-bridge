"""
Verifies ROTE_TRANSFER_THEOREM.md's exact claim: if u agrees with W^inf to
depth L (lcp(u,W^inf)=L), and v is the induced CS-Rote-style sequence
(v_0=0, v_{n+1}=v_n XOR u_n), then v agrees with V^inf (weight(W) even) or
R^inf=(V Vbar)^inf (weight(W) odd) to depth EXACTLY L+1 -- no more, no less.

Exact integer/boolean arithmetic throughout; no floating point anywhere.
"""


def lcp(a, b):
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def check(W, periods=3, extra_periods_for_target=6):
    ell = len(W)
    s = sum(W)
    Winf = W * (periods + extra_periods_for_target)
    L = periods * ell
    assert L < len(Winf)
    u = Winf[:L] + [1 - Winf[L]]  # force the first mismatch exactly at position L
    assert lcp(u, Winf) == L

    v = [0]
    for b in u:
        v.append(v[-1] ^ b)
    v = v[: len(u) + 1]

    if s % 2 == 0:
        V = v[:ell]
        target = V * (len(v) // ell + 3)
    else:
        V = v[:ell]
        Vbar = [1 - x for x in V]
        R = V + Vbar
        target = R * (len(v) // (2 * ell) + 3)

    Lv = lcp(v, target)
    return L, Lv, Lv - L


def main():
    cases = [
        [0, 1, 1, 0],
        [0, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1],
        [0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1],
        [1, 0],
        [0] * 6 + [1] * 3,   # weight 3, odd, ell=9
        [1] * 8,             # all ones, ell=8 even, weight 8 even
        [1] * 7,             # all ones, ell=7 odd, weight 7 odd
    ]
    all_ok = True
    for W in cases:
        for periods in [1, 2, 3, 5]:
            L, Lv, diff = check(W, periods=periods)
            ok = diff == 1
            all_ok &= ok
            print(f"W={W} weight={sum(W)%2} periods={periods}: L={L} Lv={Lv} diff={diff} {'OK' if ok else 'FAIL'}")
    print()
    print("ALL PASS (diff == 1 in every case)" if all_ok else "FAILURES FOUND")


if __name__ == "__main__":
    main()
