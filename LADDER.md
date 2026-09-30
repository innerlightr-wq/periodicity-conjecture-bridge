# LADDER.md — the exclusion-program milestones

```
Sturmian  p(n) = n+1
    ↓
counting classes  p(n) < 1.709511... n         (Dubickas 2009, transported)
    ↓
bounded-type CS Rote  p(n) = 2n                 (PROVED, Phase 6 — intercept 0 only)
    ↓
bounded-type CS Rote, EVERY intercept  p(n) = 2n (PROVED, Phase 8 — symbolic input: BHZ 2006 §5)
    ↓
unbounded-type CS Rote / next frontier
```

**Reading note.** This diagram is a **milestone map of an exclusion program**, not a chain of literal nested sets. `p(n)=n+1` (Sturmian) is not a subset of `p(n)<1.70951n`, and `p(n)<1.70951n` is not a subset of `p(n)=2n` — each rung is a **separately proved class** of aperiodic binary words for which `Φ(s)∉ℚ` has been established, reached by a *different* combination of technique (counting vs. repetition/height) and *different* combinatorial hypothesis (complexity growth vs. initial repetition structure). The arrows mark the order in which this research program proved each rung, not a containment relation.

## Rung-by-rung status

| Rung | Class | Method | Status | Where |
|---|---|---|---|---|
| 1 | Sturmian, `p(n)=n+1` | initial squares + balance (Theorem 10.1/10.2, source paper) | **PROVED** (source paper) | `reference/` |
| 2 | `p(n) < 1.70951...\,n`, not eventually periodic | counting (Dubickas 2009, transported) | **PROVED** (source paper, `Corollary 9.3`) | `reference/` |
| 3 | Quadratic CS Rote, `p(n)=2n`, every quadratic-irrational slope | repetition/height bridge + initial-critical-exponent bound (BHZ 2006) | **PROVED — precise subclass**, now superseded by rung 3′ | `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` |
| 3′ | Bounded-type CS Rote, `p(n)=2n`, **every** bounded-partial-quotient irrational slope (intercept-`0` representatives, both seeds, every shift) — an uncountable class, strictly containing rung 3's countable quadratic-irrational class | same bridge, chain reconstructed and re-verified without any periodicity hypothesis | **PROVED — precise subclass** (every bounded-type slope; other intercepts of the same slope still not covered, see `theorems/phase6/BOUNDED_TYPE_THEOREM.md`) | `theorems/phase6/BOUNDED_TYPE_THEOREM.md` |
| 3″ | Bounded-type CS Rote, `p(n)=2n`, **every** bounded-partial-quotient slope at **every intercept**, either mechanical convention, both seeds, every shift | same bridge; the general-intercept margin is **Berthé–Holton–Zamboni 2006 Prop. 5.1/5.2**, re-proved here with attained witnesses and growing root lengths | **PROVED** — supersedes rung 3′ | `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 2 |
| 4 | CS Rote on **unbounded**-partial-quotient slopes / next frontier | — | **OPEN, and now known to be genuinely hard**: BHZ Thm 1.1 gives slopes with an intercept where `ice = 2` exactly, so the odd-weight branch has zero margin | `theorems/phase8/PHASE8_NEXT_TARGET.md` |

## Attribution across rungs 3–3″

Rungs 3, 3′ and 3″ all run the same arithmetic machinery — the periodic-approximation/height
bridge, the exact XOR transfer, the density-`1/2` fact — over progressively weaker symbolic
hypotheses. The **symbolic** inputs are cited, not original to this repository: the
initial-critical-exponent formula is Berthé–Holton–Zamboni 2006 Cor. 3.5, and the
general-intercept margin that makes rung 3″ possible is **BHZ 2006 Prop. 5.1/5.2**. This
repository's contribution on these rungs is the arithmetic application and the attained-witness
bookkeeping, not the combinatorics on words. Phase 7 mistakenly recorded the rung-3″ symbolic
input as an open conjecture; see `theorems/phase7/PHASE7_CORRECTIONS.md`.

## Why rung 4 is left open

Rung 3″ closes the bounded-type case completely (every slope, every intercept). The one remaining
thread below the next complexity class is **unbounded** partial quotients, and it is not merely
untried: BHZ Theorem 1.1 characterises the slopes carrying an intercept with `ice(ω) = 2`
*exactly*, and every such slope has unbounded partial quotients. At such an intercept the
odd-weight branch has **zero** margin, so the current sufficient criterion cannot apply — a
genuine boundary of the method, not a gap in the bookkeeping.
`theorems/phase8/PHASE8_NEXT_TARGET.md` analyses what survives there. Per the research program's
own working discipline a genuinely new complexity class is not started while that thread is open —
candidates are recorded in `theorems/phase2/THEOREM_CONVERSION_VERDICT.md` and
`theorems/phase1/FULL_PERIODICITY_GAP.md`.

## Relationship to the EOC divergence programme (cross-program, 2026-09-29)

A falsification-first audit tested whether this ladder's mechanism hands off to the surviving
divergence sector of [`innerlightr-wq/eoc-divergence`](https://github.com/innerlightr-wq/eoc-divergence).
**It does not.** On an integer-realizable zero-confined orbit the periodic-approximation surplus
is bounded by `log₂ m₀` as an identity, so the criterion's hypothesis `limsup S = +∞` is
unsatisfiable there; and rungs 3/3′ are *vacuous* on that sector, because CS Rote's load-bearing
one-density `1/2` is incompatible with the sector's critical density `β ≈ 0.63093`. No rung above
is changed. The qualitative closure was already on record (this file's closing section, and EOC
Revision 7 Observation 5.9); the audit adds the exact identity, the quantified obstruction and
certified verification. Details: [`docs/EOC_HANDOFF_CLOSED.md`](docs/EOC_HANDOFF_CLOSED.md).

## Relationship to the full Lagarias Periodicity Conjecture

**Not claimed to be resolved, in whole or in part, by any rung above.** Every rung is a statement about a specific, structurally-defined *class* of aperiodic binary words reachable by a *repetition-based or counting-based* method. `theorems/phase1/FULL_PERIODICITY_GAP.md` (Q4) proves there exist aperiodic words (Thue–Morse) that **no repetition-based method can ever reach**, by construction — a structural ceiling on this entire program, independent of how many further rungs are added. Progress recorded here is progress on an increasingly broad *sub-class* of the Periodicity Conjecture's scope, not on the conjecture itself.
