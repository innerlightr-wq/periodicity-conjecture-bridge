**PROOF CLOSES — CONJECTURE 12.1 WAS ALREADY A PUBLISHED THEOREM; ONE PHASE-7 STRUCTURAL CLAIM REFUTED; DEPOSITED NOTE NEEDS AN ERRATUM**

# PHASE8_VERDICT.md

## 1. Headline

The general-intercept obstruction is **closed**, not by new mathematics but by reading
Section 5 of the primary source the program already cites.

> **Theorem 2** (`PHASE8_PROOF_OR_OBSTRUCTION.md`). Let `γ ∈ (0,1)` be irrational with bounded
> partial quotients. Let `u` be **any** Sturmian word of slope `γ` — **any** intercept, either
> mechanical convention. Let `v` be either complementary symmetric Rote sequence with `S(v) = u`
> (either seed), or any shift `σ^j(v)`. Then `Φ(v) ∉ ℚ`.

This removes the single stated boundary of `theorems/phase6/BOUNDED_TYPE_THEOREM.md`
("intercept `0` only") without weakening any other quantifier. The bounded-partial-quotient
hypothesis on `γ` is unchanged.

## 2. Status of every statement

| statement | status |
|---|---|
| `ice(ω) > 2` at every individual intercept of a bounded-type slope — task's **(a)** | **PROVED, PUBLISHED 2006.** Immediate corollary of BHZ Theorem 1.1. |
| Uniform margin `δ(A) > 0` over all slopes and intercepts with partial quotients `≤ A` — task's **(b)**, i.e. **Conjecture 12.1** | **PROVED, PUBLISHED 2006.** BHZ Propositions 5.1 + 5.2 give `δ(A) ≥ 1/(2(A+1)²+1)`. Independently re-proved here (Theorem 1) with `δ(A) = 1/(2(A+1)²)` and explicit attained root lengths `≥ q_{k-4}`. |
| Usable roots whose repetition gain dominates the height penalty — task's **(c)** | **PROVED here** (Theorem 1's attainment clause + the corrected surplus inequality, `PHASE8_PROOF_OR_OBSTRUCTION.md` §4–§5). Does not follow from (b) alone. |
| `Φ(v) ∉ ℚ` for both CS Rote lifts of every bounded-type Sturmian word at every intercept | **PROVED** (Theorem 2). |
| Keep-one closed form `ice = 2 + 1/(A β_A)`, `β_A = (A+√(A²+4))/2` | **PROVED** for slopes with eventually-constant BHZ digits; gives `δ*(γ) ≤ 1/(Aβ_A)`. |
| That keep-one is **optimal** (`δ*(γ) = 1/(Aβ_A)`) | **PROVED only at restricted scope**: eventually-constant BHZ digits with `A ≥ 2`, plus the Fibonacci slope via BHZ Prop. 4.3. On all other bounded-type slopes this is **NUMERICAL EVIDENCE ONLY**, deliberately not promoted. Tiers separated in `theorems/phase8/PHASE8_MARGIN_STATUS.md`. **Theorem 2 uses none of it.** |
| A margin uniform in `A` | **DISPROVED.** `1/(Aβ_A) → 0` on the keep-one intercepts, so the `A`-dependence in Conjecture 12.1 is necessary. |
| The discrepancy step's hidden hypothesis (`γ/2` must also be bounded type) | **GAP FOUND AND CLOSED**: `theorems/phase8/PHASE8_CHAIN_AUDIT.md` §3. `‖qγ‖ ≤ 2‖q(γ/2)‖` gives `inf q‖q(γ/2)‖ ≥ c/2`, so `γ/2` is badly approximable with partial quotients `≤ 2(A+2)+1`. Conclusion unchanged; the proof is now complete. |
| Supremum of prefix-power exponents vs. an attained witness | **DISTINGUISHED**: `PHASE8_CHAIN_AUDIT.md` §2. BHZ's `limsup` statement alone gives attained witnesses at exponent `> 2 + δ/2` with root lengths `→ ∞`, already sufficient; Theorem 1 gives `≥ 2 + δ` at **every** scale. |
| Phase-7 claim: `ice(ω_ρ) = ind*(α)` off a countable "return" set; open cases countable; intercept `0` harder than generic | **REFUTED** (`scripts/phase8/phase8_exceptional_orbit_refutation.py`). BHZ Prop. 2.1(4)/Lemma 2.2 give only "almost everywhere", and the exceptional set is uncountable: the family `{a_k − c_k ∈ {1,2}}` has `ice ≤ 1 + 2β_A/(β_A−1) ≤ 5` uniformly while `ind*(α) = 2 + β_A → ∞`. Intercept `0` is in fact one of the *easiest* intercepts (`ice = ind*(α) − 1 → ∞`), not the hardest. |
| Phase-7 root-length "mismatch at every tested `k`, not close" | **DIAGNOSED and RESOLVED.** `scripts/phase7/bhz_general_witness.py` sets `q_1 = a_1`; BHZ Prop. 2.7 sets `q_1 = a_1 + 1` (`α = [0; a_1+1, a_2, …]`). Under BHZ's own convention the formula `q_k − c_k q_{k-1}` reproduces exactly — 562 literal longest-common-prefix checks, 0 failures. BHZ Prop. 3.3 was never wrong. |
| Recorded surplus decomposition `S_k ≥ A·E_k − C_A·D_k − O_A(log ℓ_k)` | **DIMENSIONALLY INCORRECT as written** (leading term must be `ℓ_k·E_k`). Corrected in `PHASE8_PROOF_OR_OBSTRUCTION.md` §4. Conclusions drawn from it are unaffected. |
| `y(k)` recorded as an attained initial power for all admissible `(c_k)` | **OVERSTATED.** BHZ Prop. 3.3 attains `y(k)` only when `0 < c_k < a_k`; Corollary 3.5's three observations repair the `limsup`, and Theorem 1 routes every case through an attained witness explicitly. |
| Intrinsic-square bypass (`theorems/phase7/INTRINSIC_SQUARE_ROUTE.md`) | **SUPERSEDED, its reading confirmed.** Bare squares give zero margin on the odd-weight branch, as Phase 7 correctly found; Theorem 1 makes the bypass unnecessary. No general-intercept weight-parity automaton is needed. |
| Unbounded partial quotients | **OPEN, and now known to be genuinely hard**: BHZ Theorem 1.1 exhibits slopes with an intercept where `ice(ω) = 2` *exactly*, at which the odd-weight branch has zero margin. The bounded-type hypothesis is where the symbolic input dies, not an artefact. |
| Complexity beyond `2n`; the full Lagarias Periodicity Conjecture | **UNTOUCHED.** `theorems/phase1/FULL_PERIODICITY_GAP.md` Q4's structural ceiling (Thue–Morse) stands. Theorem 2 widens one rung of an exclusion ladder; it is **not** progress on the conjecture. |
| At `ice(ω) = 2` the *fixed-margin* criterion fails | **TRUE** — `E_k → 0` and the odd branch's threshold is exactly `2`. |
| At `ice(ω) = 2` the *bridge* fails | **FALSE, and this is the main new finding of the frontier analysis.** `ℓ_k E_k = q_{k-2}(m_{k-1}-1) ≥ q_{k-3} → ∞` exactly, even as `E_k → 0` — verified on 135 153 exhaustive instances. The obstruction moves from the repetition side to the **height** side, and becomes an explicit growth condition on the partial quotients, satisfied with 34–43 orders of magnitude of slack on the natural `ice = 2` families. `theorems/phase8/PHASE8_NEXT_TARGET.md`. |

## 3. Reproducing

```
scripts/phase8/phase8_identities.py                    -> exact identity audit vs BHZ Cor. 3.5
scripts/phase8/phase8_literal_prefix.py                -> literal lcp vs Ostrowski prediction;
                                                          diagnosis of the q_1 off-by-one
scripts/phase8/phase8_margin_search.py                 -> three adversaries + case-tree check
scripts/phase8/phase8_surplus.py                       -> exact-integer surplus at general intercepts
scripts/phase8/phase8_exceptional_orbit_refutation.py  -> refutation of the Phase-7 reduction
scripts/phase8/phase8_chain_audit.py                   -> INDEPENDENT end-to-end chain audit on
                                                          literal mechanical words, no BHZ formula
scripts/phase8/phase8_margin_optimality.py             -> the four margin tiers, T3b optimality
scripts/phase8/phase8_ice2_boundary.py                 -> the ice = 2 frontier; surplus-driver identity
```

Outputs in `data/phase8/`. Exact `Fraction`/integer arithmetic throughout; floats only for display
and for pruning inside searches whose minimisers are then re-certified exactly. Every script
asserts its own claims, so a non-zero exit means a claim failed; all eight exit `0`
(`technical-note/RELEASE_REV2.md` §8). Totals:

```
identity assertions vs BHZ Cor. 3.5                        495 668
literal attained-power checks (root lengths)                   562
exact-integer surplus rows, 0 mismatches, transfer 263/263     263
case-tree branch instances (all five sub-branches used)       9 504
independent chain-audit witnesses on literal words              534
  transfer L_v = L_u+1 / 2^{L_v}>F(R) / odd density 1/2   534 / 534 / 338
surplus-driver identity  ell_k E_k = q_{k-2}(m_{k-1}-1)     135 153
adversarial digit configurations searched                  > 60 000
bracket-undecided floors in the certified-bracket audit            0
```

Finite computation is used only as a certificate against the primary source's own formulas and as an
adversarial search for counterexamples. Theorems 1 and 2 are proved, not measured.

## 4. Next highest-value action

**The mathematical frontier and the editorial obligation are now separate; the editorial one is
prepared and awaits approval.**

1. **Publication decision (author only).** Revision 2 of the note and a standalone 2-page correction
   notice are written, built and checksummed: `technical-note/note_rev2.{tex,pdf}`,
   `technical-note/correction_notice.{tex,pdf}`, packaged with an exact proposed Zenodo version
   description in `technical-note/RELEASE_REV2.md`. Nothing is pushed or deposited. This is the only
   item with an external correctness obligation.
2. **Research: settle `(E)` at intercept `0` — the cheapest decisive experiment available.** The
   even-weight branch needs only `r_u > log₂3` and no discrepancy hypothesis, so it survives
   `ice(ω) = 2`; it needs even-weight roots infinitely often. The parity characterisation is already
   complete: `p_k` is odd for every `k ≥ 1` **iff** `a_2` is odd and `a_k` is even for all `k ≥ 3`.
   Check whether that thin family also forces the growth condition `(H)` of
   `PHASE8_NEXT_TARGET.md` §3 to fail. If the two failure sets are disjoint, all of unbounded type
   closes with no new machinery.
3. **Hygiene.** Fix `scripts/phase7/bhz_general_witness.py::convergents()` to `q_1 = a_1 + 1` and
   re-run Phases 4–7 (all `ice` values unchanged, all root lengths corrected); fold
   `PHASE8_CHAIN_AUDIT.md` §3's `γ/2` lemma into the discrepancy audit where it was implicit.
4. **Then** the conditional growth theorem `(H1)`, which needs one auxiliary estimate this
   repository does not have (`Σ b_i = O(Σ a_i)` for the half-slope); then read
   Dvořáková–Medková–Pelantová first-hand before any work on intrinsic Rote repetition; then the
   exact height estimate `(H2)` last. Full ordering and rationale: `PHASE8_NEXT_TARGET.md` §7.

## 5. Erratum for the deposited technical note — PREPARED, NOT PUBLISHED

`Beyond Sturmian Words in the 3x+1 Periodicity Conjecture`, Zenodo
[10.5281/zenodo.23045141](https://doi.org/10.5281/zenodo.23045141). Five items, all confined to
Revision 1 §§12–13 and its open-problem list: the mistaken open-problem attribution (C1), the false
exceptional-orbit reduction (C2), the `q_1` indexing error (C3), the missing length factor (C4), and
the conditional attainment of `y(k)` (C5). Full text, the survives/superseded split, and the exact
proposed Zenodo version description are in `technical-note/RELEASE_REV2.md`; the standalone erratum
is `technical-note/correction_notice.pdf`.

Revision 2 is intended as a **new Zenodo version**, leaving Revision 1 retrievable, not as an edit of
the frozen record. **No publication action has been taken**, and per the repository's own gate this
needs explicit author approval.

## 6. Final status

```
PROOF CLOSES AT EVERY INTERCEPT OF EVERY BOUNDED-TYPE SLOPE.
The missing symbolic lemma was not missing -- it is BHZ 2006, Propositions 5.1 and 5.2.
Phase 8 contributes: the priority identification; an independent re-proof carrying attained
root lengths; the corrected surplus inequality; the refutation of the Phase-7 countable-
exceptional-set reduction; the diagnosis of the q_1 = a_1 + 1 convention error.
NOT closed: unbounded partial quotients; complexity above 2n; the Periodicity Conjecture.
```
