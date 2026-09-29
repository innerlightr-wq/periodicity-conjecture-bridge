# LADDER.md — the exclusion-program milestones

```
Sturmian  p(n) = n+1
    ↓
counting classes  p(n) < 1.709511... n         (Dubickas 2009, transported)
    ↓
CS Rote  p(n) = 2n
    ↓
[next frontier]
```

**Reading note.** This diagram is a **milestone map of an exclusion program**, not a chain of literal nested sets. `p(n)=n+1` (Sturmian) is not a subset of `p(n)<1.70951n`, and `p(n)<1.70951n` is not a subset of `p(n)=2n` — each rung is a **separately proved class** of aperiodic binary words for which `Φ(s)∉ℚ` has been established, reached by a *different* combination of technique (counting vs. repetition/height) and *different* combinatorial hypothesis (complexity growth vs. initial repetition structure). The arrows mark the order in which this research program proved each rung, not a containment relation.

## Rung-by-rung status

| Rung | Class | Method | Status | Where |
|---|---|---|---|---|
| 1 | Sturmian, `p(n)=n+1` | initial squares + balance (Theorem 10.1/10.2, source paper) | **PROVED** (source paper) | `reference/` |
| 2 | `p(n) < 1.70951...\,n`, not eventually periodic | counting (Dubickas 2009, transported) | **PROVED** (source paper, `Corollary 9.3`) | `reference/` |
| 3 | CS Rote, `p(n)=2n`, five explicit quadratic-irrational associated slopes | repetition/height bridge, generalized | **PROVED** | `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` |
| 3′ | CS Rote, **every** quadratic-irrational slope | repetition/height bridge + weight-parity dichotomy | **PROVED for odd-tail slopes; strongly evidenced (not fully closed) for all-even-tail slopes** | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| 4 | next frontier | — | **OPEN, deliberately not pursued yet** | — |

## Why rung 4 is intentionally left open

Per the research program's own working discipline: the quadratic-irrational CS Rote rung (3/3′) is not yet fully closed (one classical-but-not-fully-reproved bound remains, `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`'s branch (b)), and the program does not advance to a new complexity class while a lower rung has an open thread. The candidates already scouted for a future rung 4 — Rote sequences beyond quadratic-irrational slopes, general two-interval rotation codings, and general morphic words — are recorded in `theorems/phase2/THEOREM_CONVERSION_VERDICT.md` and `theorems/phase1/FULL_PERIODICITY_GAP.md`, not attacked here.

## Relationship to the full Lagarias Periodicity Conjecture

**Not claimed to be resolved, in whole or in part, by any rung above.** Every rung is a statement about a specific, structurally-defined *class* of aperiodic binary words reachable by a *repetition-based or counting-based* method. `theorems/phase1/FULL_PERIODICITY_GAP.md` (Q4) proves there exist aperiodic words (Thue–Morse) that **no repetition-based method can ever reach**, by construction — a structural ceiling on this entire program, independent of how many further rungs are added. Progress recorded here is progress on an increasingly broad *sub-class* of the Periodicity Conjecture's scope, not on the conjecture itself.
