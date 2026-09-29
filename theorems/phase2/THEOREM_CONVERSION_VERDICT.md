# THEOREM_CONVERSION_VERDICT.md

## 1. Primary question: can we prove irrationality of `\Phi(s)` for a natural infinite class of non-Sturmian complexity-`2n` words?

**YES.** `ROTE_IRRATIONALITY_THEOREM.md`: for every complementary symmetric Rote sequence `v` associated to any of five explicit quadratic-irrational Sturmian slopes (golden ratio, silver ratio, bronze ratio `[0;\overline3]`, `[0;\overline{1,3}]`, `[0;\overline{2,1}]`), `\Phi(v)\notin\mathbb Q`, proved (not merely evidenced) end to end. This is a genuine, infinite, non-Sturmian, complexity-exactly-`2n` class, strictly beyond the Dubickas counting threshold (`2n>(1/\log_2(3/2))n` for all `n\ge2`), settling the theorem-conversion phase's minimum success condition and its primary question in the affirmative.

## 2. If yes — prove it. Done where?

`ROTE_IRRATIONALITY_THEOREM.md`, assembled from: `ABSTRACT_IRRATIONALITY_CRITERION.md` (the base criterion, every checklist item resolved), `DISCREPANCY_HEIGHT_PROOF.md` + `REPETITION_SURPLUS_THEOREM.md` (the density-free `r>\log_23` sufficiency, discrepancy negligible), `ROTE_TRANSFER_THEOREM.md` (exact `L+1` depth transfer, proved in general, not merely checked on examples), `ROTE_ROOT_DISCREPANCY.md` (the transferred roots have `O(\log\ell)` discrepancy for bounded-partial-quotient slopes, via a rigorous reduction to classical three-distance-theorem/Koksma discrepancy theory), and the weight-parity argument (`ROTE_IRRATIONALITY_THEOREM.md` itself: an eventual-periodicity fact, proved in general, combined with a finite decidable check verified for five slopes).

## 3. If the class had to stay smaller — the precise missing lemma

Even though the answer to Q1 is yes, the task also asks to isolate the exact missing lemma for the **larger** targets that were *not* reached:
> **LEMMA (needed for full Target B/C, not proved here).** For every quadratic irrational `\gamma` (Target C), or every bounded-partial-quotient irrational (Target B), the eventual cycle of the weight-parity recurrence `p_k\bmod2\oplus(k\bmod2)` contains at least one `0`.

Stated precisely in `ROTE_IRRATIONALITY_THEOREM.md`, with the reason it looks tractable (a finite linear-algebra-over-`\mathbb F_2` classification, not a deep open problem) also given there. `ROTE_ROOT_DISCREPANCY.md` separately isolates the discrepancy-side gap for **non**-quadratic bounded-partial-quotient slopes (Target B beyond Target C): the classical discrepancy bound used here assumed eventual periodicity of `a_k\bmod2` for the *pigeonhole* argument to bite; a general bounded (not eventually periodic) partial-quotient sequence needs a different (though likely still standard) discrepancy argument, not supplied here.

## 4. Target A / B / C status

- **Target A (all CS Rote sequences): NOT reached, and Phase 1's own `THEOREM_TARGET.md` assessment (§ "not currently provable... probably false as a blanket statement without qualification") stands unchanged.**
- **Target B (all bounded-partial-quotient slopes): NOT reached in full; the discrepancy half is proved in the eventually-periodic (quadratic-irrational) sub-case only, and the weight-parity half has one precisely stated open lemma even there.**
- **Target C (all quadratic-irrational slopes): NOT reached in full, but reached for five explicit, structurally diverse instances — a genuine, checkable, extensible partial result, with the exact gap to full Target C isolated to one finite-per-slope combinatorial check.**

## 5. What generalized cleanly beyond Phase 1, and what is genuinely new here

- The abstract bridge criterion (`ABSTRACT_IRRATIONALITY_CRITERION.md`) — every subtlety the task raised (reducedness, cancellation, ceilings, `\limsup` vs. `\to`) is now resolved explicitly rather than by reference, and one genuine unused strengthening was found (the reduced-fraction refinement, `SURPLUS_THEOREM.md` §3–4) and left as available headroom.
- The Rote transfer lemma is now a **proved theorem** (exact `L+1` depth transfer, all parities and edge cases), not a three-example computational check — the single largest rigor upgrade this phase made over Phase 1.
- The Rote-root discrepancy question — Phase 1's single biggest open item — is **closed** for bounded-partial-quotient slopes via an original reduction to classical rotation-discrepancy theory, itself a nontrivial structural insight (CS Rote roots and mismatched two-interval rotation codings are literally the same underlying object, `ROTE_ROOT_DISCREPANCY.md` Step 1, `ROTATION_EXAMPLE_THEOREM.md`).
- The weight-parity mechanism (why some initial-square witnesses transfer at full strength and others halve) is entirely new to this phase, not present even implicitly in Phase 1.

## 6. Rotation-coding branch — independent confirmation, weaker outcome

`ROTATION_EXAMPLE_THEOREM.md`: the **same** discrepancy mechanism (§9's classical three-distance argument) applies verbatim to Phase 1's non-Sturmian rotation-coding instance, **proving** its discrepancy control generally rather than resting on two computed points. But the repetition-existence half (an analogue of Theorem 10.2 for mismatched-partition codings) has **no proof and no citation** — strictly more open than the Rote branch. **Classification: `PARTIALLY PROVED`**, confirming the bridge's reach is not an artifact of the specific `S(v)=u` Rote construction (the discrepancy engine is shared, structural), while showing the two branches are not equally mature.

## 7. The exact bottleneck (per `THEOREM_GRAPH.md`)

One precisely identified node: the weight-parity "cycle contains `0`" check, proved as a *mechanism* (eventual periodicity, general) but verified only as a *specific outcome* on five slopes. Every other edge into the main theorem is solid (`PROVED` or cited `KNOWN`). This is a sharper, more actionable bottleneck than Phase 1 left behind (Phase 1's bottleneck was "no proof at all, three computational instances only" — now narrowed to one specific, well-posed, finite-per-instance combinatorial question).

## 8. Did the targeted prior-art pass change anything?

No retraction, no correction needed. `THEOREM_PRIOR_ART.md` confirms Phase 1's negative result stands for the *combination* of techniques used, while properly attributing the one classical ingredient (three-distance/Koksma discrepancy bound) this phase leans on most heavily, which Phase 1 had not needed to cite explicitly.

## 9. Should a paper be drafted now?

**No — consistent with the task's explicit instruction, and substantively premature.** The five-slope theorem is real and citable, but the natural paper-worthy statement (Target B or full Target C) hinges on the one open lemma in §3 — resolving it (a finite linear-algebra classification, not a deep unknown) would substantially strengthen any draft's headline claim at comparatively low additional cost. **Recommended next step, if this project continues: resolve the weight-parity lemma for all quadratic irrationals** (§3), which would immediately upgrade `ROTE_IRRATIONALITY_THEOREM.md` from "five slopes" to "every quadratic-irrational-slope CS Rote sequence" — a clean, complete, genuinely publishable result.

## 10. Final status line

```
PRIMARY QUESTION: YES.
CLASS PROVED: CS Rote sequences, five explicit quadratic-irrational associated slopes.
PRECISE MISSING LEMMA (for the natural stronger statement): does every quadratic irrational's
  weight-parity eventual cycle contain a 0? (finite check per slope; general classification open)
ROTATION-CODING BRANCH: discrepancy proved generally; repetition-existence still open, no citation found.
NO PAPER DRAFTED, NO REPOSITORY MODIFIED, NO SOURCE PDF MODIFIED, PHASE 1 UNCHANGED (checksums in
  phase2/PHASE1_CHECKSUMS.txt match the original 29 files throughout).
```
