# FALSIFICATION_REPORT.md

Six candidate claims, actively attacked.

## C1. "Any aperiodic word with infinitely many initial squares has irrational Φ-value."

**Task's prior**: "Likely false without height control." **Finding: TRUE, and proved** (`REPETITION_HEIGHT_CRITERION.md`, unconditional-squares theorem). The task's expectation was reasonable *a priori* but wrong: height control is not an extra hypothesis that can fail — it is **automatically present** for every word, because discrepancy is combinatorially capped at `γ(1−γ)ℓ≤ℓ/4` (exhaustively verified, `scripts/worst_case_discrepancy_check.py`) and `2 − sup_γ[max(1,γlog₂3)+γ(1−γ)log₂3] = 2−log₂3 > 0` holds uniformly. This is the single most important corrected expectation in this audit — reported plainly, including the fact that the initial intuition (mine and the task's) was wrong until checked.

## C2. "Bounded discrepancy alone implies irrational Φ-value."

**FALSE, as stated** — confirmed by `BRIDGE_CONTROLS.md` Control 4: a *single* non-repeated prefix agreement (`r=1`, i.e. depth `~ℓ` with no repetition at all) gives margin `≤0` regardless of how small the discrepancy is (even `D=0` exactly, the mechanical-word case). Discrepancy control bounds the *height* of the approximant; it says nothing about whether the *depth* of agreement is large enough to beat that height. **Repetition (or an equivalent depth-forcing mechanism) is independently necessary.**

## C3. "Linear factor complexity implies irrational Φ-value."

**Established, but only below the counting threshold — not "linear complexity" unconditionally.** Corollary 9.3 gives exactly `liminf_L p_s(L)/L < 1/log₂(3/2)=1.70951...`; a word with `p_s(L) ~ 1.8L` (still linear, `O(L)`) is **not** covered by counting, and this audit's repetition bridge does not automatically cover it either (linear complexity says nothing about initial powers). **Partially false as a blanket claim**: "linear complexity" alone, without the specific constant `<1.70951...`, is insufficient; confirmed not established beyond that threshold, consistent with the task's framing.

## C4. "Every Rote word satisfies the bridge."

**Still unknown as a general theorem — but no longer unexamined.** `ROTE_LITERATURE_AUDIT.md` found the literature's own "critical exponent" results for CS Rote sequences (minimum `2+1/√2≈2.707` over the whole class, Dvořáková–Medková–Pelantová 2020; repetition threshold `5/2`, Ollinger–Shallit 2024) do **not** directly answer the question, since both concern powers occurring *anywhere*, not *initial* powers specifically. This audit derived an original transfer lemma (exact, computationally verified) relating initial powers of a CS Rote sequence to those of its associated Sturmian sequence via the confirmed `S(v)=u` construction, and `ROTE_COMPUTATIONAL_AUDIT.md` used it to find **genuine, exact, growing-depth positive-surplus certificates for three tested Sturmian slopes** (golden ratio, silver ratio, a mixed-CF slope) — real evidence the bridge reaches at least these instances, **not** a proof for the whole class. **Verdict: FALSE as a universal claim (not established), TRUE for the three tested instances (evidence, not proof).**

## C5. "Every primitive morphic word satisfies the bridge."

**Unknown, and likely too broad, exactly as the task suspects.** `FULL_PERIODICITY_GAP.md` Q3/Q4: morphic words include both linear-complexity examples (already covered by C3's threshold, when the constant is small enough) and words that may lack any useful initial power at all (structurally, no different from Thue–Morse in principle). No blanket claim is asserted; scoped further only in `MORPHIC_BRIDGE_AUDIT.md`, kept deliberately bounded per the task's own instruction.

## C6. "Positive bridge surplus is necessary for irrationality."

**FALSE, confirmed.** The bridge is a **sufficient**, not necessary, criterion for this specific method. Direct counterexample: `Φ(1cγ)` for `γ<β` is irrational by the *density* argument of Monks–Yazinski (quoted in the source paper, `CURRENT_BRIDGE.md`'s Credit discussion) — a completely different mechanism, with no reference to any specific periodic approximant's surplus. More generally, `Corollary 9.3`'s counting route proves irrationality for a wide class with **no** periodic approximant or surplus computation anywhere in its proof — so the *existence* of an irrational `Φ(s)` with **bounded** surplus against every choice of `W_n` (i.e. `sup_W S_s(W) < ∞`, yet `Φ(s)∉Q` by a different argument) is not merely conceivable but is the generic situation for words reached only by counting. **Necessity would require proving the converse of the abstract bridge theorem, which is not attempted and not expected to be true.**

## Summary

| Claim | Verdict |
|---|---|
| C1 | **TRUE** (the one genuine surprise — corrects the task's own prior) |
| C2 | **FALSE** (repetition independently necessary) |
| C3 | **Partially false** (only below the explicit counting threshold) |
| C4 | **False universally; TRUE for 3 tested instances** (real computational evidence, not a class-wide proof) |
| C5 | **Unknown**, likely too broad |
| C6 | **FALSE** (sufficiency only, by explicit counterexample mechanism) |
