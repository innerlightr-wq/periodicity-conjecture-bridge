# PRIOR_ART_EVEN_TAIL.md

## What was searched

Initial critical exponent formulas (Berthé–Holton–Zamboni — found and used directly, `INITIAL_EXPONENT_FORMULA.md`); Damanik–Lenz critical exponent / powers-in-Sturmian-words results; silver-ratio Sturmian extremality; even continued-fraction partial quotients and repetition; Ostrowski numeration and initial powers; CS-Rote recurrence functions (Dvořáková–Medková–Pelantová 2020, already found in Phase 1); complementary-word density and irrationality criteria.

## Findings, per source

**Berthé–Holton–Zamboni (2006).** The primary source for `INITIAL_EXPONENT_FORMULA.md` — read directly, formula used and verified, properly attributed. Does not contain the `\text{term2}>2+1/(A+1)` uniform bound as a stated corollary; that specific inequality (an elementary consequence of their formula, `a_{2k-1}\ge1` plus a crude reversed-CF bound) is this phase's own derivation from their result, not a rediscovery of a stated theorem.

**Damanik–Lenz (2003), *Powers in Sturmian Sequences*.** Confirms (via search summary) the *critical exponent* (not initial critical exponent) is finite iff partial quotients are bounded, and gives the general critical-exponent formula. Not directly used here (this phase needs the *initial* critical exponent specifically, BHZ's quantity, not Damanik–Lenz's).

**Silver-ratio Sturmian extremality.** No source found claiming or discussing silver ratio as extremal for any repetition/initial-power quantity among even-tailed or lock-sustaining slopes. This appears to have been this project's own (Phase 3's) unproven extrapolation, now shown false (`SILVER_EXTREMALITY.md`).

**Even continued-fraction partial quotients and repetition.** No source found specifically addressing "even partial quotients" as a distinguished class for any repetition or complexity property. Not a recognized special case in the literature surveyed.

**Complementary-word density.** No source found using the elementary fact that `V\bar V` (a word concatenated with its own bitwise complement) has density exactly `1/2` as part of an irrationality or repetition threshold argument. This is a two-line structural observation (`\ell V$'s ones plus `\ell-`(that many)` from `\bar V` always sums to exactly `\ell` out of `2\ell`), not a deep result, and is very plausibly folklore in the combinatorics-on-words community even if not found in this search — reported as a negative search result, not a claim of novelty, consistent with this project's standing discipline (`theorems/phase1/PRIOR_ART_BRIDGE.md`, `theorems/phase2/THEOREM_PRIOR_ART.md`).

## Overall verdict

No prior-art hit for the specific chain used in `FINAL_PROOF_CHAIN.md`. Every individual classical ingredient (BHZ's formula, Theorem 10.2, the three-distance discrepancy bound) is properly cited; the specific combination — and in particular the density-`1/2` observation that collapses the required threshold from `2\log_23` down to `2` — is not found elsewhere and is treated as original to this project, with the usual caveat that absence of a hit is evidence, not proof, of absence.
