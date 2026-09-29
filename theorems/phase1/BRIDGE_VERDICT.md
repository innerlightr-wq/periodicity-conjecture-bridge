# BRIDGE_VERDICT.md

Main deliverable. Falsification-first audit of whether the periodic-approximation/Liouville bridge in "The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-Adic Integer" (De Jesús, Sept. 2026) generalizes to larger rungs of the Lagarias Periodicity Conjecture. Answers below reference the supporting `.md` files in this directory; nothing here asserts progress on the Periodicity Conjecture itself beyond what is explicitly scoped.

## 1. Can the proof be abstracted cleanly, independent of Sturmian-specific structure?

**Yes, cleanly and completely.** `ABSTRACT_BRIDGE_THEOREM.md`: from Propositions 2.2 and 4.1 alone (both fully general, no Sturmian hypothesis), the bridge reduces to one clean theorem: for aperiodic `s`, `Φ(s)=u/v`, height `H`, `limsup_n [lcp(s,W_n^∞) − log₂F(W_n)] = +∞ ⟹ Φ(s)∉Q`, `F(W)=max(2^ℓ,3^k)+c_W`. Sturmian structure is used only to *supply witnesses* `W_n` satisfying the hypothesis, never in the theorem itself.

## 2. What is the minimal, actually-proved sufficient criterion?

**`limsup_n S_s(W_n) = +∞`** (surplus, `SURPLUS_INVARIANT.md`), sharper than the task's proposed "surplus → +∞" (only `limsup`, not full convergence, is needed). Concretely and unconditionally: **arbitrarily long initial squares (`r=2`) alone suffice, for any word, at any density** (`REPETITION_HEIGHT_CRITERION.md`) — no balance, no bounded discrepancy hypothesis, because discrepancy is combinatorially capped (`D(W)≤γ(1-γ)ℓ≤ℓ/4`, exhaustively verified) below the level that could ever defeat `r=2`.

## 3. Is the controlling quantity "repetition depth minus height," and can this be made precise?

**Yes** — `S_s(W) = lcp(s,W^∞) − log₂F(W)`, exactly the depth-minus-height quantity, proven (not merely conjectured) to be the right invariant: `Φ(s)∈Q ⟹ sup_W S_s(W)<∞` (the necessary direction, `SURPLUS_INVARIANT.md`), and the converse-sufficient direction is the main theorem. The **converse** (bounded surplus `⟹` rational) is explicitly **not** established (`FULL_PERIODICITY_GAP.md` Q5) — the invariant is sufficient-side complete, necessity-side open.

## 4. What discrepancy condition suffices for height control?

**Sublinear discrepancy** (`D(W_n)=o(ℓ_n)`) suffices (`DISCREPANCY_HEIGHT_THEOREM.md`) — strictly weaker than "balanced" (`D<1`, the paper's own Sturmian-specific fact). More precisely, **no discrepancy condition is needed at all** once repetition exponent exceeds `2` (see Q2): the general bound `c_W≤ℓ·3^⌈D⌉·max(2^ℓ,3^k)` combined with the proven ceiling `D≤γ(1-γ)ℓ` makes height control automatic.

## 5. Are initial squares sufficient under bounded discrepancy, without balance?

**Yes, and more**: sufficient under **no discrepancy hypothesis whatsoever** (`REPETITION_HEIGHT_CRITERION.md`'s unconditional-squares theorem — the single most significant correction of this audit's own prior expectations, `FALSIFICATION_REPORT.md` C1).

## 6. Does the bridge reach any class beyond the Dubickas counting threshold (`p_s(L)/L<1.70951...`)?

**Yes, in both directions, independently.** The repetition/height route and the counting route are **not** nested — `FULL_PERIODICITY_GAP.md` Q2, `Remark 9.5`: the repetition route reaches any word with arbitrarily long initial squares regardless of complexity growth rate (can exceed the counting threshold), while the counting route reaches words with no initial squares at all (e.g. some morphic words), provided complexity stays below `1.70951...`. Neither contains the other.

## 7. Does the bridge reach Rote words?

**Not proved for the class; proved (exact, computational) for three tested instances.** `ROTE_LITERATURE_AUDIT.md`+`ROTE_COMPUTATIONAL_AUDIT.md`: the literature's own critical-exponent results for CS Rote sequences (minimum `2+1/√2≈2.707` over the whole class) concern powers occurring *anywhere*, not initial powers, so don't directly settle this. An original transfer lemma (parity-dependent, exact, verified) plus direct exact-surplus computation on CS Rote sequences derived from three Sturmian slopes (golden ratio, silver ratio, a mixed-CF slope) found genuine, growing-depth, positive-surplus certificates in every case tested. **No natural subclass has been proved to satisfy the bridge universally**; the computational evidence is real but not a theorem.

## 8. Does the bridge reach non-Sturmian rotation codings?

**Confirmed for one concrete instance, not a general class.** `ROTATION_CODING_AUDIT.md`: a two-interval coding of the golden-ratio rotation with a deliberately mismatched partition (`δ=1/3≠γ,1-γ`) was confirmed genuinely non-Sturmian (complexity exactly `2n`), and found to have exact, unconditionally-certifying initial squares (`r>2`, positive surplus). One witness, not a theorem over all `(γ,δ,ρ)`.

## 9. Does the bridge reach any morphic class beyond counting?

**Not established; deliberately not pursued beyond Thue–Morse as a control.** `MORPHIC_BRIDGE_AUDIT.md`, `FULL_PERIODICITY_GAP.md` Q3: morphic words range from linear-complexity (already covered by counting) to structurally square-avoiding (Thue–Morse, no square below half-length 2048) — no blanket claim possible, and none asserted.

## 10. What is the first genuinely new rung, beyond Sturmian, that this audit establishes?

**Rung C, populated for the first time**: CS Rote sequences (3 tested slopes) and one non-Sturmian two-interval rotation coding, both computationally confirmed to admit unconditionally-certifying initial squares. This is the first non-empty content beyond Sturmian words at any rung, and directly answers (with evidence) the source paper's own Section 12, Open Problem (4).

## 11. What exact lemma or theorem is missing to promote Rung C to Rung B (a full class-wide guarantee)?

A **general existence theorem**: "every CS Rote sequence (resp. every two-interval rotation coding with mismatched partition) has arbitrarily long initial powers of exponent `>2`" — analogous to the Sturmian case's Theorem 10.2 (ADQZ 2001). No such theorem was found in the literature search, and none is proved here; this is the single concrete open problem this audit identifies as the natural next step (see Q15).

## 12. Is the missing ingredient repetition, discrepancy, height, arithmetic, or literature knowledge?

**Purely combinatorial repetition** — specifically, a guarantee on *initial* powers (not the literature's "critical exponent," which is about powers occurring anywhere). Height and discrepancy are no longer bottlenecks (Q4/Q5); the arithmetic packaging (`F(W)`, surplus) is complete and general (Q1–Q3). The gap is entirely: does the relevant word class have a *provable*, general, arbitrarily-deep initial-square guarantee? This is squarely a combinatorics-on-words existence question, not an arithmetic or height-control question.

## 13. Does any generalization collapse to a known theorem?

**No direct collapse found.** `PRIOR_ART_BRIDGE.md`: the closest body of work (Adamczewski–Bugeaud combinatorial transcendence, Schmidt Subspace Theorem) proves irrationality/transcendence via a structurally analogous but mechanistically different (archimedean, Roth/Schmidt-based) route. The counting route (`Corollary 9.3`) sits in an actively-worked area (a contemporaneous September 2026 paper, Stephan, on a related `3/2`-multiplier system, uses the same complexity-threshold idea for a different map) — not novel in kind. The repetition/height 2-adic elementary route found no direct match — reported as a negative search result, not a claim of originality.

## 14. What is the strongest defensible relationship to the full Periodicity Conjecture?

**A genuinely broader but structurally bounded tool.** The generalized bridge (unconditional at `r=2`, no discrepancy hypothesis) reaches any class with arbitrarily long initial powers of exponent `>log₂3` (uniformly) — strictly larger than "Sturmian," now confirmed to include specific Rote and rotation-coding instances. But it is fundamentally repetition-based, and **provably cannot reach every aperiodic word**: adversarially constructed aperiodic words can avoid useful initial powers entirely (Thue–Morse; `FULL_PERIODICITY_GAP.md` Q4), a structural limitation of *any* repetition-based method, not a gap in this one. The only visible route past this limitation — whether rationality of `Φ(s)` itself forces some repetition/discrepancy structure (`FULL_PERIODICITY_GAP.md` Q5, the "closing the circle" question) — is open and not obviously true. **Progress on this bridge is progress on a large but structurally bounded sub-class of aperiodic words, not on the Periodicity Conjecture in general.**

## 15. What should the next paper or project be?

Two concrete, well-scoped candidates, in order of tractability:
1. **A general initial-power existence theorem for CS Rote sequences** (or a clearly-delineated subclass, e.g. bounded-partial-quotient associated Sturmian slopes), proved analytically using the transfer lemma derived here (`ROTE_COMPUTATIONAL_AUDIT.md`) plus the known Sturmian initial-power machinery (Berthé et al.'s `ice` formula) — this would promote Rung C to Rung B for a real, citable class, the single most promising and immediately tractable next step identified by this audit.
2. **The "closing the circle" question** (`FULL_PERIODICITY_GAP.md` Q5): does `Φ(s)∈Q` force repetition or low discrepancy in `s`? This is deeper, not obviously true, but is the only currently-visible route that could unify the repetition and counting methods into something reaching every aperiodic word — flagged as the highest-value long-term direction, not a near-term paper.

**No new paper should be drafted from this audit's findings without further verification** — per the task's explicit instruction, this document and its supporting files are an audit, not a draft.
