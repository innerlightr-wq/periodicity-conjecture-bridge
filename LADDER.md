# LADDER.md — the exclusion-program milestones

```
Sturmian  p(n) = n+1
    ↓
counting classes  p(n) < 1.709511... n         (Dubickas 2009, transported)
    ↓
quadratic CS Rote  p(n) = 2n                    (PROVED, Phase 4 — precise subclass, see below)
    ↓
general CS Rote / next frontier
```

**Reading note.** This diagram is a **milestone map of an exclusion program**, not a chain of literal nested sets. `p(n)=n+1` (Sturmian) is not a subset of `p(n)<1.70951n`, and `p(n)<1.70951n` is not a subset of `p(n)=2n` — each rung is a **separately proved class** of aperiodic binary words for which `Φ(s)∉ℚ` has been established, reached by a *different* combination of technique (counting vs. repetition/height) and *different* combinatorial hypothesis (complexity growth vs. initial repetition structure). The arrows mark the order in which this research program proved each rung, not a containment relation.

## Rung-by-rung status

| Rung | Class | Method | Status | Where |
|---|---|---|---|---|
| 1 | Sturmian, `p(n)=n+1` | initial squares + balance (Theorem 10.1/10.2, source paper) | **PROVED** (source paper) | `reference/` |
| 2 | `p(n) < 1.70951...\,n`, not eventually periodic | counting (Dubickas 2009, transported) | **PROVED** (source paper, `Corollary 9.3`) | `reference/` |
| 3 | Quadratic CS Rote, `p(n)=2n`, **every** quadratic-irrational slope (intercept-`0` representatives, both seeds, every shift) | repetition/height bridge + initial-critical-exponent bound (BHZ 2006) | **PROVED — precise subclass** (every quadratic irrational; other intercepts of the same slope not covered, see `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`) | `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` |
| 4 | general CS Rote (non-quadratic-irrational slopes) / next frontier | — | **OPEN, deliberately not pursued yet** | — |

## Why rung 4 is intentionally left open

Rung 3 is now closed for every quadratic-irrational slope (Phase 4), but two threads remain open before advancing further: (a) the "other intercepts of the same slope" gap noted in `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`, and (b) extending beyond quadratic irrationals to general bounded-partial-quotient slopes (Target B, `theorems/phase2/THEOREM_TARGET.md`). Per the research program's own working discipline, rung 4 (a genuinely new complexity class, or Rote sequences beyond quadratic-irrational slopes, or general two-interval rotation codings, or general morphic words) is not pursued while these threads are open — candidates are recorded in `theorems/phase2/THEOREM_CONVERSION_VERDICT.md` and `theorems/phase1/FULL_PERIODICITY_GAP.md`.

## Relationship to the full Lagarias Periodicity Conjecture

**Not claimed to be resolved, in whole or in part, by any rung above.** Every rung is a statement about a specific, structurally-defined *class* of aperiodic binary words reachable by a *repetition-based or counting-based* method. `theorems/phase1/FULL_PERIODICITY_GAP.md` (Q4) proves there exist aperiodic words (Thue–Morse) that **no repetition-based method can ever reach**, by construction — a structural ceiling on this entire program, independent of how many further rungs are added. Progress recorded here is progress on an increasingly broad *sub-class* of the Periodicity Conjecture's scope, not on the conjecture itself.
