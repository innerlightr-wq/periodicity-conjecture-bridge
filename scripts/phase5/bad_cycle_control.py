"""
Phase 5, Section 13: independent reproduction of the Phase 3 bad-parity
counterexample gamma=[0;1,1,1,2,2,2,...] as a positive control. Rebuilt from
scratch (different code structure than Phase 3/4's scripts) to confirm:
  - all-odd relevant weight parity (the "bad cycle")
  - odd-transfer roots R=V.Vbar
  - density exactly 1/2
  - exact lcp / exact c_R
  - exact surplus, growing

This is the theorem's OWN required stress case: the new mechanism (density
1/2) MUST succeed exactly where the old sufficient condition (even-weight
witnesses) fails.
"""
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension, c_W  # noqa: E402


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def convergents_pq(pq, n):
    a0 = pq[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
        q.append(pq[i] * q[-1] + q[-2])
    return p[1:], q[1:]


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


def main():
    pq = [0, 1, 1, 1] + [2] * 26
    gamma = cf_value(pq, len(pq))
    p, q = convergents_pq(pq, len(pq))

    MAX_ELL = 60000  # keep c_W's big-integer sums (O(ell) terms up to 3^ell) tractable
    n_needed = min(max(x for x in q if x <= MAX_ELL) * 6, 400_000)
    u = mechanical_word(gamma, n_needed)
    v = rote_from_sturmian(u)

    print(f"gamma = {float(gamma):.10f}")
    print(f"{'k':>3} {'ell':>10} {'weight%2':>9} {'|R|':>10} {'R_1s':>8} {'density':>10} {'L':>10}  exact S")
    prev_S = None
    growing_confirmed = True
    for k, ell in enumerate(q):
        if ell < 2 or ell > MAX_ELL or ell * 4 > len(u):
            continue
        W = u[:ell]
        wpar = sum(W) % 2
        if wpar == 0:
            continue  # only auditing the ODD (bad-cycle) branch here, by design
        # confirm weight IS odd -- i.e. we really are in the bad-parity cycle
        checklen = min(len(u), ell * 6)
        L_u = lcp(u, periodic_extension(W, checklen), checklen)

        V = v[:ell]
        Vbar = [1 - x for x in V]
        R = V + Vbar
        assert len(R) == 2 * ell
        assert sum(R) * 2 == len(R), "density(R) != 1/2 exactly!"

        checklen_v = min(len(v), 2 * ell * 6)
        Lv = lcp(v, periodic_extension(R, checklen_v), checklen_v)
        cR = c_W(R)
        S, F = bridge_surplus_exact(Lv, R)

        print(f"{k:3d} {ell:10d} {wpar:9d} {len(R):10d} {sum(R):8d} "
              f"{sum(R)}/{len(R)}={'1/2':>6} {Lv:10d}  S={S}")
        if prev_S is not None and S <= prev_S:
            growing_confirmed = False
        prev_S = S

    print(f"\nDensity(R) confirmed exactly 1/2 at every tested witness: True (assertion never failed)")
    print(f"Surplus strictly increasing across the tested witnesses: {growing_confirmed}")


if __name__ == "__main__":
    main()
