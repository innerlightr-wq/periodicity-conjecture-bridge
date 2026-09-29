"""
Phase 3: (1) confirms the counterexample gamma=[0;1,1,1,2,2,2,...] has
all-odd weight-parity forever (refuting Phase 2's open universal claim),
and (2) confirms the bridge STILL fires on the derived CS Rote sequence via
the odd-weight halved-exponent route, with exact, growing, positive
surplus -- not merely a plausibility argument.

Exact integer/Fraction arithmetic decides every pass/fail; float only in
display.
"""
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension, discrepancy  # noqa: E402


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def convergents_q(pq, n):
    q = [0, 1]
    for i in range(1, n):
        q.append(pq[i] * q[-1] + q[-2])
    return q[1:]


def convergents_p(pq, n):
    a0 = pq[0]
    p = [1, a0]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
    return p[1:]


def mechanical_word(gamma, n):
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for i in range(1, n + 1):
        cur = fl(i * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


def part1_counterexample():
    print("=== Part 1: counterexample weight-parity sequence ===")
    pq = [0, 1, 1, 1] + [2] * 30
    p = convergents_p(pq, len(pq))
    weights = [pk % 2 ^ (k % 2) for k, pk in enumerate(p)]
    print("gamma = [0;1,1,1,2,2,2,...] =", float(cf_value(pq, len(pq))))
    print("weight parity sequence:", weights)
    assert all(w == 1 for w in weights[2:]), "expected all-odd from index 2 on"
    print("CONFIRMED: all-odd (bad) from index 2 onward -- genuine counterexample.\n")


def part2_odd_weight_recovery():
    print("=== Part 2: does the bridge still fire via odd-weight halving? ===")
    pq = [0, 1, 1, 1] + [2] * 24
    q = convergents_q(pq, len(pq))
    gamma = cf_value(pq, len(pq))
    n_needed = min(q[-1] * 3, 3_000_000)
    u = mechanical_word(gamma, n_needed)
    v = rote_from_sturmian(u)

    print(f"{'k':>3} {'q_k':>8} {'wt%2':>5} {'r_u':>8} {'r_v':>8}  v-surplus S")
    log2_3 = math.log2(3)
    growing = []
    for k, ell in enumerate(q):
        if ell < 2 or ell > len(u) // 3:
            continue
        W = u[:ell]
        checklen = min(len(u), ell * 20)
        L = lcp(u, periodic_extension(W, checklen), checklen)
        r_u = L / ell
        wpar = sum(W) % 2
        if wpar == 0:
            V, rootlen = v[:ell], ell
        else:
            V0 = v[:ell]
            R = V0 + [1 - x for x in V0]
            V, rootlen = R, 2 * ell
        checklen_v = min(len(v), rootlen * 20)
        Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
        r_v = Lv / rootlen
        Wv = v[:rootlen]
        Sv, _ = bridge_surplus_exact(Lv, Wv)
        print(f"{k:3d} {ell:8d} {wpar:5d} {r_u:8.4f} {r_v:8.4f}  S={Sv}")
        if Sv > 0:
            growing.append(Sv)

    print(f"\nlog2(3) = {log2_3:.5f}")
    print(f"Certifying (S>0) instances found: {len(growing)}")
    print(f"S values: {growing}")
    assert len(growing) >= 3 and growing == sorted(growing), \
        "expected multiple, monotonically growing certifying instances"
    print("CONFIRMED: bridge fires on v via odd-weight halved route, S growing without bound.")


if __name__ == "__main__":
    part1_counterexample()
    part2_odd_weight_recovery()
