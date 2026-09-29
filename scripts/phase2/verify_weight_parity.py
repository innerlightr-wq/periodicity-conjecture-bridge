"""
Verifies ROTE_IRRATIONALITY_THEOREM.md's weight-parity claims:
  1. weight(u[0:q_k]) = p_k - [k odd], exactly, for the lower mechanical
     word of a quadratic-irrational slope (p_k,q_k its CF convergents).
  2. The resulting weight-parity sequence is eventually periodic, and its
     eventual cycle contains at least one 0 (even weight), for five
     explicit quadratic irrationals.

Exact integer arithmetic throughout (Fraction for the slope itself, plain
Python ints for convergents and weights -- all exact, no floating point in
any decision; floats appear only in a display line).
"""
from fractions import Fraction


def convergents(pq, n):
    a0 = pq[0]
    p = [1, a0]
    q = [0, 1]
    for i in range(1, n):
        ai = pq[i]
        p.append(ai * p[-1] + p[-2])
        q.append(ai * q[-1] + q[-2])
    return p[1:], q[1:]


def cf_convergent(pq, n):
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


def find_cycle(seq, min_periods_to_confirm=3):
    """
    Find the eventual period of a sequence by brute force. A candidate
    (start,period) is accepted only if seq[start:] -- the ENTIRE remaining
    tail, not just a short local window -- is exactly periodic with that
    period, and at least `min_periods_to_confirm` full periods are covered
    by the available data. (An earlier version of this function matched
    only a 3-symbol-long local window, which gave FALSE short "periods" --
    e.g. reporting period 1 inside a genuine period-6 pattern, because three
    consecutive equal symbols happen to occur inside the real cycle. Caught
    by the downstream assertion in main() failing unexpectedly; fixed here
    by requiring the period to explain the ENTIRE remaining tail.)
    """
    n = len(seq)
    for start in range(0, n):
        tail = seq[start:]
        m = len(tail)
        for period in range(1, m // min_periods_to_confirm + 1):
            if m < period * min_periods_to_confirm:
                continue
            root = tail[:period]
            reps = m // period
            if root * reps == tail[:period * reps]:
                return start, period, root
    return None, None, None


def analyze(name, a_tail, n_terms):
    pq = [0] + a_tail
    p, q = convergents(pq, len(pq))
    gamma = cf_convergent(pq, len(pq))
    n_needed = min(q[-1] + 5, n_terms)
    u = mechanical_word(gamma, n_needed)

    weights_exact = []
    predicted = []
    for k, qk in enumerate(q):
        if qk < 1 or qk > len(u):
            break
        w = sum(u[:qk])
        weights_exact.append(w)
        predicted.append(p[k] - (1 if k % 2 == 1 else 0))

    assert weights_exact == predicted, f"{name}: weight formula MISMATCH: {weights_exact} vs {predicted}"

    parity = [w % 2 for w in weights_exact]
    start, period, cycle = find_cycle(parity)
    contains_zero = (0 in cycle) if cycle else None

    print(f"=== {name}: gamma={float(gamma):.6f} ===")
    print(f"  weight formula weight(u[0:q_k]) = p_k - [k odd]: VERIFIED exactly ({len(weights_exact)} terms)")
    print(f"  parity sequence: {parity}")
    print(f"  eventual cycle (start={start}, period={period}): {cycle}")
    print(f"  contains 0 (even weight)? {contains_zero}")
    print()
    return contains_zero


def main():
    cases = [
        ("golden ratio [0;1,1,1,...]", [1] * 26, 200000),
        ("silver ratio [0;2,2,2,...]", [2] * 18, 200000),
        ("bronze ratio [0;3,3,3,...]", [3] * 14, 10000000),
        ("[0;1,3,1,3,...]", [1, 3] * 13, 3000000),
        ("[0;2,1,2,1,...]", [2, 1] * 13, 200000),
    ]
    results = {}
    for name, a_tail, n_terms in cases:
        results[name] = analyze(name, a_tail, n_terms)

    print("=== Summary ===")
    for name, has_zero in results.items():
        print(f"  {name}: contains 0 in eventual cycle = {has_zero}")
    assert all(results.values()), "Some slope's cycle did NOT contain a 0 -- theorem claim would be false!"
    print("\nALL FIVE SLOPES CONFIRMED: eventual weight-parity cycle contains 0.")


if __name__ == "__main__":
    main()
