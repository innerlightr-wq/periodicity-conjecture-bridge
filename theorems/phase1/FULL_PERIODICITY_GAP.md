# FULL_PERIODICITY_GAP.md

Discipline note: the Periodicity Conjecture quantifies over **all** aperiodic `s ∈ {0,1}ℕ`, an uncountable family. Everything below is scoped explicitly; no claim here should be read as progress on the conjecture in general.

## 1. Does every uniformly recurrent word have sufficiently deep periodic approximants?

**No, not via the initial-squares route specifically.** Uniform recurrence guarantees every factor recurs with bounded gaps, but says nothing about *initial* squares/powers — a uniformly recurrent word can fail to begin in any square at all (indeed can avoid squares everywhere, cf. square-free uniformly recurrent words, e.g. over a larger alphabet, or aperiodic binary words with bounded repetition — the existence of binary uniformly recurrent words with small critical exponent, though not exactly `0`, is classical). The bridge as derived here needs an *initial* repetition of exponent `>log₂3`, which is strictly more than uniform recurrence alone supplies.

## 2. Does every linear-complexity word (`p_s(L) ≤ cL+O(1)`)?

**Already fully covered — by the *other*, independent route.** `Corollary 9.3` (the transported Dubickas counting bound, `CURRENT_BRIDGE.md` Classification, no repetition/discrepancy machinery at all) covers **every** word with `liminf_L p_s(L)/L < 1/log₂(3/2) = 1.70951...`, unconditionally. The repetition/height bridge audited here is not needed for this class at all, and — per `Remark 9.5`, confirmed in this audit — the two methods' margins coincide numerically (`2−log₂3` on one side, the counting threshold's complement on the other) without either being a special case of the other.

## 3. Does every morphic word?

**Unknown in general; not established by anything in this audit.** Primitive morphic words can have complexity ranging from linear (many classical examples, covered by Q2) to super-linear; whether they generically possess initial powers of exponent `>log₂3` is a case-by-case combinatorics-on-words question, briefly scoped (not solved) in `MORPHIC_BRIDGE_AUDIT.md`.

## 4. Can an aperiodic word deliberately avoid the required repetitions?

**Yes, provably — this is exactly Control 2** (`BRIDGE_CONTROLS.md`): the Thue–Morse word has no square at all below half-length 2048 (verified in the paper's own Appendix A), hence certainly no *initial* square of unbounded length is guaranteed by any general principle for an arbitrary aperiodic word. More strongly, there exist aperiodic binary words with critical exponent arbitrarily close to `1` (the infimum over binary sequences, by the Thue–Morse-adjacent theory of repetition thresholds — the binary repetition threshold is `2`, attained, but words can have *initial* critical exponent much smaller even when *somewhere* they repeat more). **An adversarially constructed aperiodic word can have no useful initial power at all**, making this bridge (in either its Sturmian-specific or generalized form) inapplicable to it by construction — this is not a gap in the *method*, it is a structural limitation of what "periodic approximation via initial powers" can ever reach, on any word, by design.

## 5. Can a rational Φ-value itself force repetition or low discrepancy? — the closing-the-circle question

**Not established by this audit, and not obviously true.** This is the deepest of the five questions, and the task is right to flag it as the one that could combine the two proof strategies into something reaching *every* aperiodic word. Speculatively: if `Φ(s)=u/v∈Q`, then `s`'s prefixes are **the parity words of the orbit of a fixed rational** (Lemma 9.1's `a_t/b`), which live in a bounded-height family (`|a_t|+b ≤ (3/2)^t(|a_0|+b)`) — this *does* force a kind of "arithmetic rigidity" (exactly what powers Section 9's counting bound), but **rigidity of the orbit's height is not the same as repetition or low discrepancy of the parity word itself**, and no argument in the source paper, nor derived in this audit, shows the latter follows from the former. **This remains fully open**; asserting otherwise would be exactly the kind of unproved progress-claim the task explicitly forbids.

## What would still be missing even given a complete answer to Section 12, Open Problem (4)

Even a full resolution of "does every `s` with `p_s(L) ≤ 2L` satisfy the bridge" (the paper's own stated next target) would leave:
- Every morphic/substitutive word not already linear-complexity (Q3, genuinely open).
- Every word that is aperiodic, non-linear-complexity, *and* avoids long initial powers by construction (Q4) — a bridge based on initial repetition can **never**, by its own logic, reach such a word; a fundamentally different method (not a generalization of this one) would be needed.
- The general Periodicity Conjecture itself, which is a statement about an uncountable family with no combinatorial structure assumed at all — **no version of the initial-power bridge, however generalized, can settle this alone**, since Q4 exhibits words permanently outside its reach.

## Honest verdict

The strongest defensible relationship to the full Periodicity Conjecture, after this audit, is: **the initial-power/height bridge (in its now-generalized, unconditional-at-`r=2` form) is a genuinely broader tool than the paper's own Sturmian-specific application, reaching any class with sufficiently long initial powers of exponent `>log₂3`, with no further combinatorial hypothesis — but it is fundamentally a repetition-based method, and the Periodicity Conjecture contains words (Q4) that no repetition-based method can reach by construction.** Progress on this bridge is progress on a genuinely large but *structurally bounded* sub-class of aperiodic words, not on the conjecture itself. Question 5 is the only currently-visible route to closing that structural gap, and it is unresolved.
