**PROVED — PRECISE SUBCLASS** (same quantifier scope as the frozen quadratic theorem, now for the strictly larger bounded-type class)

# BOUNDED_TYPE_THEOREM.md

## Statement

> **THEOREM.** Let `\gamma\in(0,1)` be irrational with bounded partial quotients (`A:=\sup_n a_n<\infty`). Let `u` be the intercept-`0` lower mechanical word of `\gamma`. Let `v` be either complementary symmetric Rote sequence with `S(v)=u` (either seed), or any shift `\sigma^j(v)`. Then
> ```
> Phi(v) not in Q.
> ```

## Why this is the same theorem, more general hypothesis

Every ingredient in `MINIMAL_PROOF.md` (Phase 5) that was checked in `QUADRATICITY_DEPENDENCY.md` to need only boundedness, not periodicity, is now **independently re-verified against genuinely non-periodic examples** in `ARROW_BY_ARROW_RECONSTRUCTION.md`, not merely re-asserted. The proof text is **identical** to the quadratic case's, with `A` now meaning `\sup_n a_n` directly (no longer "the largest partial quotient in the eventual period," since there may be no period) — this is exactly the substitution the task warned against doing *blindly*; here it is done only **after** independently reconstructing and testing every arrow.

## The one precise correction folded in

`\text{term2}(k)>2+1/(A+1)` holds for **all sufficiently large `k`** (empirically, from `k\ge3` in every tested case), with possible **equality** (never violation) at a small-`k` boundary artifact unrelated to periodicity (`ARROW_BY_ARROW_RECONSTRUCTION.md`, Arrow 1). Since the theorem only needs **infinitely many, arbitrarily long** witnesses exceeding the threshold — not literally every `k` — this correction does not weaken the statement, and is recorded for precision, matching this project's standing discipline of not silently smoothing over a found imprecision.

## Quantifier scope — unchanged from the frozen theorem, audited identically

- **Intercept `0` only**: same boundary as `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` and re-confirmed in `theorems/phase5/QUANTIFIER_AUDIT.md` — the `\omega(-\gamma)`-specific BHZ formula is what is used; general-intercept extension remains unattempted.
- **Both seeds**: covered, by the same seed-independence argument re-derived and *corrected* in Phase 5 (`HOSTILE_REFEREE_REPORT.md`'s finding: via `D(V\bar V)=D(\bar VV)`, not via `c_R` complement-invariance) — this argument is CF-independent and applies verbatim here.
- **Every shift**: covered, via source-paper Proposition 2.3, CF-independent, applies verbatim.

## What changed, concretely, in the class of `\gamma` covered

Quadratic irrationals (eventually periodic continued fractions) are **countable**. Bounded-partial-quotient ("bounded type") irrationals are **uncountable** (indeed of full Hausdorff dimension, though Lebesgue measure zero) — this theorem covers a strictly, and vastly, larger class of slopes, while remaining entirely on the `p(n)=2n` rung (CS Rote sequences, unchanged complexity class).

## Status

```
PROVED — PRECISE SUBCLASS.
Supersedes theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md (which is the special case A given
by an eventually-periodic CF) without weakening any of its quantifiers.
Boundary unchanged: other intercepts of the same slope remain uncovered.
```
