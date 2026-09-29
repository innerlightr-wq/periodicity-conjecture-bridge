"""
Phase 3: exhaustive finite-automaton search for the weight-parity question
left open in Phase 2 (ROTE_IRRATIONALITY_THEOREM.md's "precise missing
lemma").

State: (p_{k-1} mod 2, p_k mod 2) in {A=(0,1), B=(1,1), C=(1,0), Z=(0,0)},
crossed with kappa=k mod 2 -- 8 nodes total. Transition on a_k parity:
  a_k even -> M0: A<->C swap, B and Z fixed.
  a_k odd  -> M1: A->B->C->A cycle, Z fixed.
kappa flips every step. weight_k = (2nd state coord) XOR kappa; "bad" means
weight_k = 1 (odd) -- the case Phase 2 needed to AVOID to get an easy
even-weight bridge witness.

This script exhaustively finds every cycle, among the 8 nodes, consisting
ENTIRELY of "bad" nodes -- i.e. every way weight-parity could fail to
contain a 0 forever.
"""


def step(state, a_parity):
    x, y = state
    if a_parity == 0:
        return (y, x)
    return (y, (x + y) % 2)


BASE_STATES = [(0, 1), (1, 1), (1, 0), (0, 0)]
NAMES = {(0, 1): "A", (1, 1): "B", (1, 0): "C", (0, 0): "Z"}


def weight(state, kappa):
    return state[1] ^ kappa


def label(node):
    s, k = node
    return f"{NAMES[s]},{k}"


def build_graph():
    nodes = [(s, k) for s in BASE_STATES for k in (0, 1)]
    edges = {}
    for s, k in nodes:
        t0 = (step(s, 0), k ^ 1)
        t1 = (step(s, 1), k ^ 1)
        edges[(s, k)] = (t0, t1)
    return nodes, edges


def find_bad_cycles(nodes, edges, max_len=8):
    bad = [n for n in nodes if weight(*n) == 1]
    bad_set = set(bad)
    found = set()
    for start in bad:
        stack = [(start, (start,))]
        while stack:
            cur, path = stack.pop()
            for tgt in edges[cur]:
                if tgt == start:
                    found.add(tuple(label(n) for n in path))
                elif tgt in bad_set and tgt not in path and len(path) < max_len:
                    stack.append((tgt, path + (tgt,)))
    return bad, found


def main():
    nodes, edges = build_graph()
    print("8 nodes and weight (1=bad/odd, 0=good/even):")
    for n in nodes:
        print(f"  {label(n)}: weight={weight(*n)}")
    print()
    print("Full transition table:")
    for n in nodes:
        t0, t1 = edges[n]
        print(f"  {label(n)} --a even--> {label(t0)}   --a odd--> {label(t1)}")
    print()
    bad, cycles = find_bad_cycles(nodes, edges)
    print("Bad (weight=1) nodes:", [label(n) for n in bad])
    print(f"Distinct bad-only cycles found (length<=8): {len(cycles)}")
    for c in sorted(cycles, key=len):
        print("  ", " -> ".join(c))
    print()
    print("CONCLUSION: the only bad-only cycle is (A,0)<->(C,1); sustaining it forever")
    print("requires a_k EVEN at every (A,0)-phase visit; (C,1)-phase visits are unconstrained.")
    print("An odd a_k at an (A,0)-phase visit always escapes to (B,1), a GOOD node.")


if __name__ == "__main__":
    main()
