**PROPOSED — NOT APPLIED. Hold until the theorem statements are settled and the author approves.**

# PROPOSED_STATUS_UPDATES.md

Exact replacement text. **No file below has been edited**, and no PDF has been rebuilt.

## 1. `LADDER.md` — replace the rung table's framing

Add immediately after the rung table:

> **Reading the ladder by density, not by complexity (Phase 9B).** The complexity axis of this
> diagram is the wrong coordinate. The known dichotomy for `Φ(v) ∉ ℚ` is by **lower ones-density**:
> below `β = ln2/ln3 = 0.63093` by Monks–Yazinski (2004) Thm 2.7(b) [refereed], above `β` by
> López–Stoll (2021) Thm 1 [preprint]. **Every rung above sits at ones-density `1/2`**, hence is a
> corollary of the 2004 result, whatever its complexity. What the rungs supply is an independent
> second proof by a different mechanism, not a new class. The one uncovered density is exactly `β`,
> which no rung above approaches. See `theorems/phase9b/`.

## 2. `THEOREM_STATUS.md` — add at the head of the Headline section

> **Novelty status (Phase 9B).** Every CS Rote result below (Phases 2, 4, 6, 8, 9) proves
> `Φ(v) ∉ ℚ` for words of ones-density exactly `1/2`, and is therefore a consequence of
> Monks–Yazinski (2004) Theorem 2.7(b). The proofs stand; the novelty claims do not. The
> repository's contribution on these rungs is an independent second proof by a 2-adic
> depth-versus-height mechanism, plus the exact structural results about that mechanism.

And change the Phase 9 rows' status from `PROVED` to `PROVED (subsumed — see theorems/phase9b/)`.

## 3. `README.md` — replace the "Headline result" framing

> ~~"strictly beyond the Dubickas counting threshold"~~ → "strictly beyond the Dubickas **counting**
> threshold, though not beyond the **density** dichotomy of Monks–Yazinski (2004): every
> complementary symmetric Rote sequence has ones-density exactly `1/2 < β`, so its irrationality was
> already available. What is proved here is an independent second proof by a different mechanism."

## 4. `PRIOR_ART.md` — add a standing gate

> **Standing gate (Phase 9B).** Before claiming novelty for any class, check the conclusion against
> the density dichotomy (`< β`: Monks–Yazinski 2004 Thm 2.7(b); `> β`: López–Stoll 2021 Thm 1). All
> three searches recorded here targeted the *mechanism* and missed this. A class is only new if it
> sits at lower ones-density exactly `β`.

## 5. `theorems/phase1/FULL_PERIODICITY_GAP.md` Q4 — the scope statement

Apply `CORRECTION_ADDENDUM.md` C4 verbatim.

## 6. `theorems/phase9/PHASE9_VERDICT.md` — banner

Prepend, in the repository's established banner style (original text preserved below it):

> **CORRECTED BY PHASE 9B — see [`theorems/phase9b/PHASE9B_VERDICT.md`](../phase9b/PHASE9B_VERDICT.md).**
> §1's attribution of Corollary 4.1 to the `g(γ)` threshold is **withdrawn** (the pre-existing
> criterion suffices at threshold `1`), and Corollaries 4.1/4.2 and Theorem 3 are **subsumed** by
> Monks–Yazinski (2004) Thm 2.7(b). The proofs stand; the novelty claims do not. Retained verbatim
> as the historical record.

## 7. Revision 2 of the deposited note — **two** corrections now owed

Revision 2 (`10.5281/zenodo.23045141`) needs:

- **(i)** the Thue–Morse scope correction (`CORRECTION_ADDENDUM.md` C4): its abstract and §15 Open 6
  state that Thue–Morse makes every repetition-based method structurally inapplicable. False.
- **(ii)** the novelty framing of the CS Rote ladder (`C3`): the note presents the bounded-type CS
  Rote theorem as crossing a frontier. It crosses the *counting* frontier only; the conclusion was
  already available from the density dichotomy. The note's own §8 already says this for the
  Sturmian family — the same sentence applies to CS Rote, and should be stated.

Neither is a mathematical error in the note's proofs. Both are attribution/framing errors. A third
Zenodo version is the right vehicle. **No publication action has been taken and none should be until
the author decides.**
