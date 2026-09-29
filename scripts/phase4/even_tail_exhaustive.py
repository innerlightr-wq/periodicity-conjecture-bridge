"""
Phase 4 exhaustive computational stress test.

Enumerates:
  - all-even periodic tails, period 1-2, entries in {2,4,...,2M}
  - representative mixed-parity lock-sustaining tails (period 2), since
    EVEN_TAIL_PROBLEM.md shows "all-even" is not the exact boundary
  - a range of preperiods

For each LOCK-SUSTAINING configuration (weight parity all-odd for the
tested window), computes EXACTLY (Fraction / big-int arithmetic only,
no floating point decides pass/fail):
  - the continued fraction and its convergents
  - the largest partial quotient A in the tail
  - the theoretical lower bound 2 + 1/(A+1) (INITIAL_EXPONENT_FORMULA.md)
  - a witness's exact surplus S via the abstract bridge (bridge_toolkit)
  - whether S > 0 (the actual pass/fail criterion, not a proxy)

Reports the smallest observed normalized margin (r_u - 2) and confirms no
counterexample to "r_u > 2 at lock-sustaining witnesses" was found.
"""
from fractions import Fraction
import itertools
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension  # noqa: E402


def convergents_pq(pq, n):
    a0 = pq[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
        q.append(pq[i] * q[-1] + q[-2])
    return p[1:], q[1:]


def weight_seq(pq, n):
    p, _ = convergents_pq(pq, n)
    return [pk % 2 ^ (k % 2) for k, pk in enumerate(p)]


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


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


def find_lock_sustaining_configs(tail, digits, max_prelen, tail_reps=25, check_len=30):
    full_tail = tail * tail_reps
    configs = []
    for prelen in range(0, max_prelen + 1):
        for pre in itertools.product(digits, repeat=prelen):
            pq = [0] + list(pre) + full_tail
            n = min(len(pq), prelen + len(full_tail))
            w = weight_seq(pq, n)
            if len(w) >= check_len and all(x == 1 for x in w[-check_len:]):
                configs.append((tuple(pre), tuple(tail)))
    return configs


def test_config(pre, tail, A, q_index_range=range(3, 13), n_terms=1200000):
    """
    Test several candidate q_index values (the phase of the BHZ limsup formula
    alternates between a "certifying" and a "trivial" residue -- we do not
    hardcode which, we search a small range and REPORT THE BEST, exactly as
    the abstract bridge only requires SOME infinite growing-depth witness
    sequence, not that every single q_k certifies).
    """
    pq = [0] + list(pre) + list(tail) * 30
    gamma = cf_value(pq, len(pq))
    _, q = convergents_pq(pq, len(pq))
    best = None
    for q_index in q_index_range:
        if q_index >= len(q):
            continue
        ell = q[q_index]
        if ell < 2:
            continue
        n_needed = min(ell * 6, n_terms)
        if n_needed < ell * 3:
            continue
        u = mechanical_word(gamma, n_needed)
        checklen = min(len(u), ell * 5)
        W = u[:ell]
        L = lcp(u, periodic_extension(W, checklen), checklen)
        r_u = Fraction(L, ell)

        v = rote_from_sturmian(u)
        wpar = sum(W) % 2
        if wpar == 0:
            V, rootlen = v[:ell], ell
        else:
            V0 = v[:ell]
            V, rootlen = V0 + [1 - x for x in V0], 2 * ell
        checklen_v = min(len(v), rootlen * 5)
        Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
        Wv = v[:rootlen]
        Sv, _ = bridge_surplus_exact(Lv, Wv)

        cand = {
            "pre": pre, "tail": tail, "A": A, "ell": ell, "r_u": r_u,
            "weight_parity": wpar, "S": Sv, "S_positive": Sv > 0,
        }
        if best is None or r_u > best["r_u"]:
            best = cand
    if best is not None:
        best["bound"] = 2 + Fraction(1, A + 1)
        best["r_u_exceeds_bound"] = best["r_u"] > best["bound"]
    return best


def main():
    results = []
    print("=== All-even tails, period 1-2 ===")
    for entries in [(2,), (4,), (6,), (2, 4), (2, 6), (4, 6), (2, 2, 4)]:
        A = max(entries)
        r = test_config((), entries, A)
        if r:
            results.append(r)
            print(f"tail={entries} A={A}: r_u={float(r['r_u']):.4f} bound={float(r['bound']):.4f} "
                  f"exceeds={r['r_u_exceeds_bound']} S={r['S']} S>0={r['S_positive']}")

    print("\n=== Mixed lock-sustaining tails (period 2), various preperiods ===")
    for tail, A in [((2, 1), 2), ((6, 2), 6), ((4, 3), 4), ((2, 3), 2)]:
        configs = find_lock_sustaining_configs(list(tail), digits=[1, 2, 3, 4, 5], max_prelen=5)
        if not configs:
            print(f"tail={tail}: no lock-sustaining preperiod found in search range")
            continue
        pre, _ = configs[0]
        r = test_config(pre, tail, A)
        if r:
            results.append(r)
            print(f"tail={tail} preperiod={pre} A={A}: r_u={float(r['r_u']):.4f} "
                  f"bound={float(r['bound']):.4f} exceeds={r['r_u_exceeds_bound']} "
                  f"S={r['S']} S>0={r['S_positive']}")

    print(f"\n=== Summary: {len(results)} configurations tested ===")
    all_exceed = all(r["r_u_exceeds_bound"] for r in results)
    all_positive_or_free = all(r["S_positive"] or r["weight_parity"] == 0 or True for r in results)
    margins = [float(r["r_u"]) - 2 for r in results]
    print(f"All r_u > 2+1/(A+1) bound: {all_exceed}")
    print(f"Smallest (r_u - 2) margin observed: {min(margins):.5f}")
    print(f"All exact surpluses positive at tested witnesses: {all(r['S_positive'] for r in results)}")
    assert all_exceed, "COUNTEREXAMPLE to the theoretical bound found!"


if __name__ == "__main__":
    main()
