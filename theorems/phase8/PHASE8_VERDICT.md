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
| `δ*(A) = Θ(A^{-2})`, extremal family `d_k ≡ 1` (BHZ's "keep one"), closed form `2 + 1/(A β_A)` | **PROVED** (closed form) **+ COMPUTATIONALLY CONFIRMED** as the global minimum (exhaustive periodic scan to `A = 10`; exhaustive branch-and-bound over *all* admissible digit strings for `A ≤ 3`; greedy adversary on non-eventually-periodic slopes to `A = 6`). |
| A margin uniform in `A` | **DISPROVED.** `1/(Aβ_A) → 0`; the `A`-dependence in Conjecture 12.1 is necessary. |
| Phase-7 claim: `ice(ω_ρ) = ind*(α)` off a countable "return" set; open cases countable; intercept `0` harder than generic | **REFUTED** (`scripts/phase8/phase8_exceptional_orbit_refutation.py`). BHZ Prop. 2.1(4)/Lemma 2.2 give only "almost everywhere", and the exceptional set is uncountable: the family `{a_k − c_k ∈ {1,2}}` has `ice ≤ 1 + 2β_A/(β_A−1) ≤ 5` uniformly while `ind*(α) = 2 + β_A → ∞`. Intercept `0` is in fact one of the *easiest* intercepts (`ice = ind*(α) − 1 → ∞`), not the hardest. |
| Phase-7 root-length "mismatch at every tested `k`, not close" | **DIAGNOSED and RESOLVED.** `scripts/phase7/bhz_general_witness.py` sets `q_1 = a_1`; BHZ Prop. 2.7 sets `q_1 = a_1 + 1` (`α = [0; a_1+1, a_2, …]`). Under BHZ's own convention the formula `q_k − c_k q_{k-1}` reproduces exactly — 562 literal longest-common-prefix checks, 0 failures. BHZ Prop. 3.3 was never wrong. |
| Recorded surplus decomposition `S_k ≥ A·E_k − C_A·D_k − O_A(log ℓ_k)` | **DIMENSIONALLY INCORRECT as written** (leading term must be `ℓ_k·E_k`). Corrected in `PHASE8_PROOF_OR_OBSTRUCTION.md` §4. Conclusions drawn from it are unaffected. |
| `y(k)` recorded as an attained initial power for all admissible `(c_k)` | **OVERSTATED.** BHZ Prop. 3.3 attains `y(k)` only when `0 < c_k < a_k`; Corollary 3.5's three observations repair the `limsup`, and Theorem 1 routes every case through an attained witness explicitly. |
| Intrinsic-square bypass (`theorems/phase7/INTRINSIC_SQUARE_ROUTE.md`) | **SUPERSEDED, its reading confirmed.** Bare squares give zero margin on the odd-weight branch, as Phase 7 correctly found; Theorem 1 makes the bypass unnecessary. No general-intercept weight-parity automaton is needed. |
| Unbounded partial quotients | **OPEN, and now known to be genuinely hard**: BHZ Theorem 1.1 exhibits slopes with an intercept where `ice(ω) = 2` *exactly*, at which the odd-weight branch has zero margin. The bounded-type hypothesis is where the symbolic input dies, not an artefact. |
| Complexity beyond `2n`; the full Lagarias Periodicity Conjecture | **UNTOUCHED.** `theorems/phase1/FULL_PERIODICITY_GAP.md` Q4's structural ceiling (Thue–Morse) stands. Theorem 2 widens one rung of an exclusion ladder; it is **not** progress on the conjecture. |

## 3. Reproducing

```
scripts/phase8/phase8_identities.py                    -> exact identity audit vs BHZ Cor. 3.5
scripts/phase8/phase8_literal_prefix.py                -> literal lcp vs Ostrowski prediction;
                                                          diagnosis of the q_1 off-by-one
scripts/phase8/phase8_margin_search.py                 -> three adversaries + case-tree check
scripts/phase8/phase8_surplus.py                       -> exact-integer surplus at general intercepts
scripts/phase8/phase8_exceptional_orbit_refutation.py  -> refutation of the Phase-7 reduction
```

Outputs in `data/phase8/`. Exact `Fraction`/integer arithmetic throughout; floats only for
display and for pruning inside searches whose minimisers are then re-certified exactly. Totals:
495 668 identity assertions, 562 literal attained-power checks, 263 exact-integer surplus rows
(0 mismatches, transfer `L_v = L_u + 1` confirmed 263/263), 9 504 case-tree branch instances,
and adversarial scans over > 60 000 admissible digit configurations — no failure anywhere.

Finite computation is used only as a certificate against the primary source's own formulas and
as an adversarial search for counterexamples. Theorems 1 and 2 are proved, not measured.

## 4. Next highest-value action

**Write the erratum for the deposited note, then re-verify Phase 4–7's numerics under the
correct `q_1` convention.** In order:

1. **Erratum to Zenodo `10.5281/zenodo.23045141`** (§5 below). This is the only item with an
   external correctness obligation: a deposited paper states as an open conjecture something
   published in 2006 in a paper it cites.
2. **Fix `scripts/phase7/bhz_general_witness.py::convergents()`** to `q_1 = a_1 + 1` and re-run
   Phases 4–7. Expected: all `ice` values unchanged (limsups are insensitive to the shift), all
   root lengths corrected, and `scripts/phase7/verify_phase7.py`'s disclosed mismatch cleared.
3. **Promote Theorem 2** into `THEOREM_STATUS.md`, `LADDER.md` and `README.md`, superseding
   `theorems/phase6/BOUNDED_TYPE_THEOREM.md`'s intercept-`0` boundary, and retract the two
   Phase-7 structural claims listed in §2.
4. **Then, and only then**, the genuinely open frontier: the odd-weight branch at slopes with
   unbounded partial quotients. The concrete question is whether a general-intercept
   weight-parity criterion can force the **even** branch (which needs only `r_u > log_2 3` and so
   survives `ice(ω) = 2` with margin `2 − log_2 3`) infinitely often. This is exactly the
   automaton `theorems/phase7/INTRINSIC_SQUARE_ROUTE.md` flagged as unattempted, and it is now
   the load-bearing question rather than a bypass. Prior art to check first: the parity of
   `k_i(W)` for general-intercept mechanical words is classical Ostrowski-digit arithmetic, so a
   literature search should precede any new derivation.

## 5. Erratum required for the deposited technical note

`Beyond Sturmian Words in the 3x+1 Periodicity Conjecture`, Zenodo
[10.5281/zenodo.23045141](https://doi.org/10.5281/zenodo.23045141):

- **§12, Conjecture 12.1** is not a conjecture. It is Berthé–Holton–Zamboni (2006),
  Propositions 5.1 and 5.2 — Section 5 of reference [27]/[28]'s own paper. The correct statement
  is: for every `ω ∈ X_α` with `α` of bounded type, `ice(ω) ≥ 2 + 1/(2(A+1)²+1)`. The sentences
  "This is classified conjectural in the repository record… It is not claimed proved here or
  anywhere in the underlying record" and "until then, that extension remains open" must be
  withdrawn, and Theorem 10.1 stated at every intercept.
- **§13** the displayed surplus decomposition `S_k ≥ A·E_k − C_A·D_k − O_A(log ℓ_k)` is
  dimensionally incorrect; the leading term is `ℓ_k·E_k`. (The note's own flexible condition
  `E_k ≫ log ℓ_k/ℓ_k` is consistent with `ℓ_k·E_k`, so this is a transcription slip, not a
  different claim.)
- **§12** the quoted Phase-7 verdict rests on the exceptional-orbit reduction refuted in §2
  above; the quotation should be dropped rather than repeated.

Nothing else in the note is affected: Theorem 10.1's intercept-`0` case, the `term2(k) > 2 + 1/(A+1)`
analysis, the density-`1/2` transfer fact and the counting-threshold material all stand as
written. **No publication action has been taken.** Per the repository's own gate this needs
explicit author approval; a new Zenodo version (not an edit of the frozen record) is the right
vehicle.

## 6. Final status

```
PROOF CLOSES AT EVERY INTERCEPT OF EVERY BOUNDED-TYPE SLOPE.
The missing symbolic lemma was not missing -- it is BHZ 2006, Propositions 5.1 and 5.2.
Phase 8 contributes: the priority identification; an independent re-proof carrying attained
root lengths; the corrected surplus inequality; the refutation of the Phase-7 countable-
exceptional-set reduction; the diagnosis of the q_1 = a_1 + 1 convention error.
NOT closed: unbounded partial quotients; complexity above 2n; the Periodicity Conjecture.
```
