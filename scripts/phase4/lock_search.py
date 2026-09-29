"""
Phase 4, corrects Phase 3's "all-even tail" classification. Searches whether
a MIXED-parity continued-fraction tail can, with the right preperiod, still
lock the weight-parity automaton into the bad (all-odd-weight) cycle
forever -- Phase 3 only tested all-even tails and did not check this.

Exact integer arithmetic throughout; no floating point in any decision.
"""


def convergents_p(pq, n):
    a0 = pq[0]
    p = [1, a0]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
    return p[1:]


def weight_seq(pq, n):
    p = convergents_p(pq, n)
    return [pk % 2 ^ (k % 2) for k, pk in enumerate(p)]


def search(tail, digits, max_prelen, tail_len=40, check_len=40):
    import itertools
    full_tail = tail * tail_len
    found = []
    for prelen in range(0, max_prelen + 1):
        for pre in itertools.product(digits, repeat=prelen):
            pq = [0] + list(pre) + full_tail
            n = min(len(pq), prelen + tail_len * len(tail))
            w = weight_seq(pq, n)
            if len(w) >= check_len and all(x == 1 for x in w[-check_len:]):
                found.append(pre)
    return found


if __name__ == "__main__":
    print("=== Searching for a preperiod that locks tail [2,1,2,1,...] (mixed parity) bad ===")
    locks = search([2, 1], digits=[1, 2, 3, 4], max_prelen=4)
    print(f"Found {len(locks)} locking preperiods (showing first 5):")
    for p in locks[:5]:
        print("  preperiod:", p)
    assert locks, "expected at least one locking preperiod for a mixed tail"
    print("\nCONFIRMED: a mixed-parity tail CAN sustain the bad weight-parity lock,")
    print("given the right preperiod -- Phase 3's 'all-even tail' framing was incomplete.")
