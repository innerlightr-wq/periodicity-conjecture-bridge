# THEOREM_PRIOR_ART.md

Adversarial search against the **now-precise** phase-2 theorem (CS Rote irrationality via weight-parity + transfer + three-distance discrepancy control), not the broad keyword search Phase 1's `PRIOR_ART_BRIDGE.md` already did.

## Comparison 1

**OUR RESULT:** `\Phi(v)\notin\mathbb Q` for CS Rote `v` associated to a quadratic-irrational slope with weight-parity cycle containing `0` (`ROTE_IRRATIONALITY_THEOREM.md`).
**KNOWN RESULT:** Ferenczi–Mauduit (1997)/Adamczewski–Bugeaud (2005–2010): transcendence/irrationality of numbers whose digit expansion is Sturmian or "stammering" (contains precociously-recurring blocks), via Roth's theorem / Schmidt Subspace Theorem.
**SOURCE:** Cited in Phase 1's `PRIOR_ART_BRIDGE.md`; re-confirmed here (search: "Adamczewski Bugeaud p-adic stammering sequences Mahler transcendence").
**SAME HYPOTHESES?** No — their criterion is about digit expansions (base-`b` or continued-fraction) of the number itself; ours is about the parity-vector/2-adic conjugacy image `\Phi(v)` of a combinatorial word, a structurally different object.
**SAME CONCLUSION?** Similar flavor (repetition `\Rightarrow` irrationality/transcendence) but for different mathematical objects.
**ARCHIMEDEAN OR p-ADIC?** Their classical results: archimedean (real digit/CF expansions). Their more recent extension (Adamczewski, "Real and p-adic expansions involving symmetric patterns") does cross into p-adic territory, but via the **same** Roth/Schmidt Subspace machinery, not an elementary valuation-vs-height comparison.
**SPECIALIZATION / COROLLARY / DISTINCT?** **Distinct.** No indication either result is a special case of the other; different proof engines (Schmidt Subspace Theorem vs. elementary 2-adic integer comparison), different objects.

## Comparison 2

**OUR RESULT:** `D(V_n)=O(\log\ell_n)` for the discrepancy of a mismatched two-interval rotation coding under a bounded-partial-quotient rotation (`ROTE_ROOT_DISCREPANCY.md` Step 2, `ROTATION_EXAMPLE_THEOREM.md`).
**KNOWN RESULT:** Classical discrepancy theory of irrational rotations — the `N\cdot D_N^*(\beta)=O(\sum_{i\le k}a_i)` bound, and its consequences via Koksma's inequality for bounded-variation functions (including interval indicators).
**SOURCE:** Standard in uniform distribution theory (Kuipers–Niederreiter, *Uniform Distribution of Sequences*); directly corroborated by this search's "three-distance theorem discrepancy bounded partial quotients" query, which surfaced Alessandri–Berthé, *Three distance theorems and combinatorics on words* — a direct, on-target reference connecting three-distance-theorem discrepancy bounds to combinatorics-on-words applications of exactly this style.
**SAME HYPOTHESES?** Yes, essentially — bounded partial quotients, any fixed interval.
**SAME CONCLUSION?** Yes.
**ARCHIMEDEAN OR p-ADIC?** Archimedean (real-line rotation discrepancy) — used here only as an **input** to the 2-adic bridge, not itself a 2-adic result.
**SPECIALIZATION / COROLLARY / DISTINCT?** **This phase's discrepancy bound is a direct application (not a new discovery) of this classical fact** — explicitly acknowledged as cited, not original, in `ROTE_ROOT_DISCREPANCY.md`. What **is** original to this phase is the *reduction* of the CS Rote root's discrepancy question to this classical setup (§9's Step 1), and its combination with the 2-adic valuation bridge (a genuinely different, non-archimedean setting) to produce an irrationality conclusion — the classical fact itself is not claimed as new.

## Comparison 3

**OUR RESULT:** the weight-parity eventual-periodicity argument for standard-word witnesses (`ROTE_IRRATIONALITY_THEOREM.md`).
**KNOWN RESULT:** none found matching this specific construction (a linear recurrence mod 2 on continued-fraction convergent numerators, applied to determine parity of Rote-transfer witnesses).
**SOURCE:** Search "Rote sequence arithmetic value transcendence irrationality 2-adic" — no hit. The general fact that CF convergent numerators/denominators satisfy linear recurrences, and hence are eventually periodic mod any fixed integer, is folklore-classical (a direct pigeonhole argument on any linear recurrence modulo a fixed base — analogous to the well-known Pisano-period phenomenon for Fibonacci numbers mod `m`), but its specific application to CS Rote weight-parity was not found anywhere and appears to be original to this phase.
**SAME HYPOTHESES / CONCLUSION?** N/A — no matching result found.
**ARCHIMEDEAN OR p-ADIC?** N/A.
**SPECIALIZATION / COROLLARY / DISTINCT?** **Distinct**, reported as a negative search result (absence of a hit, not proof of absence — the same caveat Phase 1 applied to its own prior-art search).

## Comparison 4: contemporaneous adjacent work, re-checked

**OUR RESULT:** irrationality via a 2-adic depth-vs-height elementary comparison, for a combinatorics-on-words-defined sequence class.
**KNOWN RESULT:** Stephan (2026), *Transcendence criteria for the minimal word of the rational base 3/2*, arXiv:2609.19007 — already identified in Phase 1's `PRIOR_ART_BRIDGE.md` as the closest contemporaneous adjacent paper, using a complexity-threshold (counting) criterion, not a repetition/height one.
**SOURCE:** Re-confirmed, no update — still the closest adjacent work, still methodologically on the counting side, not the repetition/height side this phase's theorem uses.
**SPECIALIZATION / COROLLARY / DISTINCT?** **Distinct**, as established in Phase 1; nothing in this phase's more precise theorem changes that assessment.

## Overall verdict

**No prior-art hit for the specific theorem proved in `ROTE_IRRATIONALITY_THEOREM.md`.** Every individual *ingredient* is either classical and properly attributed (three-distance/Koksma discrepancy bound, Comparison 2) or a direct citation to Phase 1's own already-audited source material (Theorem 10.2/ADQZ 2001, the CS Rote–Sturmian correspondence of Rote 1994/Dvořáková–Medková–Pelantová 2020). The specific **combination** — weight-parity transfer analysis plus three-distance discrepancy control plus the abstract 2-adic bridge, applied to prove irrationality for an explicit infinite class of complexity-`2n` words — is not claimed to be found elsewhere, reported honestly as a negative search result, not a proof of novelty.
