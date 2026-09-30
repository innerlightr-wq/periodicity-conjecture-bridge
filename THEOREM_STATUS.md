# THEOREM_STATUS.md — consolidated status map

One line per load-bearing result, phase of origin, and status. Full statements and proofs are in `theorems/phaseN/`.

## Foundational (source paper, cited not re-derived)

| Result | Status | File |
|---|---|---|
| `Φ` is a 2-adic isometry (`v₂(Φ(a)−Φ(b))=lcp(a,b)`) | KNOWN (source paper, Prop. 2.2) | `reference/` |
| Periodic-value formula `Φ(W^∞)=c_W/(2^ℓ−3^k)` | KNOWN (source paper, Prop. 4.1) | `reference/` |
| Sturmian words have arbitrarily long initial squares | KNOWN (source paper, Thm 10.2, cites ADQZ 2001) | `reference/` |
| Sturmian, `p(n)=n+1` ⟹ `Φ∉ℚ` | KNOWN (source paper, Thm 10.1) | `reference/` |
| `p(n)<1.70951...n`, not eventually periodic ⟹ `Φ∉ℚ` | KNOWN (source paper, Cor. 9.3, Dubickas 2009 transported) | `reference/` |

## Phase 1 — abstraction and first non-Sturmian evidence

| Result | Status | File |
|---|---|---|
| Abstract periodic-approximation criterion (surplus `→+∞` ⟹ `Φ∉ℚ`), Sturmian-free | PROVED | `theorems/phase1/ABSTRACT_BRIDGE_THEOREM.md` |
| `c_W ≤ ℓ·3^⌈D⌉·max(2^ℓ,3^k)`, discrepancy-height bound | PROVED, exhaustively verified `ℓ≤16` | `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md` |
| Squares (`r=2`) suffice unconditionally, no discrepancy hypothesis | PROVED | `theorems/phase1/REPETITION_HEIGHT_CRITERION.md` |
| CS Rote sequences (3 tested slopes) certify | COMPUTATIONAL EVIDENCE | `theorems/phase1/ROTE_COMPUTATIONAL_AUDIT.md` |
| One non-Sturmian two-interval rotation coding certifies | COMPUTATIONAL EVIDENCE | `theorems/phase1/ROTATION_CODING_AUDIT.md` |

## Phase 2 — theorem conversion

| Result | Status | File |
|---|---|---|
| Abstract criterion, every subtlety (reducedness, cancellation, ceilings) resolved | PROVED | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| Rote–Sturmian transfer: depth preserved exactly, `L+1` | PROVED (was 3-example check in Phase 1) | `theorems/phase2/ROTE_TRANSFER_THEOREM.md` |
| Rote root discrepancy `D(V_n)=O(log ℓ_n)`, bounded-partial-quotient slopes | PROVED (reduction to classical 3-distance/Koksma bound) | `theorems/phase2/ROTE_ROOT_DISCREPANCY.md` |
| Weight-parity eventual periodicity (mechanism) | PROVED | `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` |
| `Φ(v)∉ℚ` for CS Rote sequences, 5 explicit quadratic-irrational slopes | **PROVED** | `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` |
| Non-Sturmian rotation coding: discrepancy proved generally; repetition-existence still open | PARTIALLY PROVED | `theorems/phase2/ROTATION_EXAMPLE_THEOREM.md` |

## Phase 3 — closing the weight-parity gap

| Result | Status | File |
|---|---|---|
| Finite 8-node automaton: exactly one bad (all-odd-weight) cycle exists, `(A,0)↔(C,1)` | PROVED (exhaustive search) | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Counterexample found: `γ=[0;1,1,1,\overline2]` has all-odd weight-parity forever | PROVED (explicit, verified) | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Odd-tail CF ⟹ bad cycle cannot sustain ⟹ infinitely many even-weight witnesses | PROVED | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| All-even-tail CF ⟹ odd-weight witnesses still certify (`r_u→≥2+√2>2log₂3`) | STRONGLY EVIDENCED (4 tails tested), **not proved for a fully general all-even tail** | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |
| Net: every tested quadratic irrational (9 slopes total, Phase 2+3) certifies; no genuine failure found | EMPIRICAL, consistent with a full theorem | `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md` |

## Phase 4 — closes the quadratic CS Rote rung, corrects a wrong working hypothesis

| Result | Status | File |
|---|---|---|
| Phase 3's "all-even tail" classification was incomplete — mixed-parity tails can also lock bad, given the right preperiod | CORRECTED (verified against the automaton directly) | `theorems/phase4/EVEN_TAIL_PROBLEM.md` |
| Silver-ratio extremality (`ice≥2+√2` for lock-sustaining tails) | **FALSE — COUNTEREXAMPLE found** (`\overline{6,2}` with preperiod `(1,4,1,5,1)`, `ice≈3.1547<2+√2`) | `theorems/phase4/SILVER_EXTREMALITY.md` |
| `2+√2` classified: numerical artifact / irrelevant after sharper analysis | AUDITED | `theorems/phase4/SILVER_CONSTANT_AUDIT.md` |
| **Real required threshold is `r_u>2`, not `r_u>2log₂3≈3.17`** — because the odd-weight route's doubled root `R=V\bar V` has density **exactly `1/2`**, always, unconditionally | PROVED (two-line structural fact) | `theorems/phase4/REQUIRED_EXPONENT.md` |
| `ice(u)>2+1/(A+1)` uniformly, any bounded-partial-quotient slope (max partial quotient `A`), via Berthé–Holton–Zamboni's exact formula | PROVED (cited formula + elementary bound, exactly verified) | `theorems/phase4/INITIAL_EXPONENT_FORMULA.md` |
| **`Φ(v)∉ℚ` for every complementary symmetric Rote sequence associated with every quadratic-irrational slope** (intercept-0 representative, both seeds, every shift) | **PROVED — precise subclass** (other intercepts of the same slope not covered) | `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` |
| Exhaustive stress test, 11 configurations (all-even + mixed lock-sustaining tails) | PASS, 11/11, exact surplus positive in every case | `theorems/phase4/COMPUTATIONAL_STRESS_TEST.md` |

## Phase 5 — fresh adversarial audit of Phase 4 (no theorem change; one justification repaired)

| Result | Status | File |
|---|---|---|
| BHZ identification `u=\omega(-\gamma)` | re-verified from BHZ's own `\S2.1` definitions, not secondary quotation; 2000 terms × 3 slopes, exact | `theorems/phase5/BHZ_PRIMARY_SOURCE_AUDIT.md` |
| Exact transfer theorem (`L_v=L+1`) | re-derived from scratch; 114,680-case independent exhaustive re-check, 0 failures | `theorems/phase5/TRANSFER_REDERIVATION.md` |
| Margin `1/(A+1)`, fixed, `k`-independent | re-derived independently | `theorems/phase5/UNIFORM_MARGIN_AUDIT.md` |
| Seed-independence justification | **repaired** — `c_W` is NOT complement-invariant (8/8 counterexamples found); true reason is `D(V\bar V)=D(\bar VV)` exactly (15/15 checked), since every script's `F_bound` depends on `R` only through `(\ell,k,D(R))` | `theorems/phase5/HOSTILE_REFEREE_REPORT.md` |
| Quadraticity vs. boundedness | recorded (not acted on): every ingredient checked needs only bounded partial quotients | `theorems/phase5/QUADRATICITY_DEPENDENCY.md` |
| Overall verdict | **THEOREM SURVIVES ADVERSARIAL AUDIT AFTER REPAIR** | `theorems/phase5/PHASE5_VERDICT.md` |

## Phase 6 — upgrades quadratic to bounded-type (theorem change)

| Result | Status | File |
|---|---|---|
| Chain reconstructed from BHZ's primary theorem against 4 genuinely non-eventually-periodic bounded-type slopes (Thue–Morse-coded, Fibonacci-word-coded, 2 random) | PASS — every arrow periodicity-free | `theorems/phase6/ARROW_BY_ARROW_RECONSTRUCTION.md` |
| Small-`k` boundary correction: `\text{term2}(k)>2+1/(A+1)` can be equality (never violation) at a rare small-`k` artifact | CORRECTED (found via adversarial non-periodic test; does not weaken the theorem) | `theorems/phase6/ARROW_BY_ARROW_RECONSTRUCTION.md` |
| **`Φ(v)∉ℚ` for every CS Rote sequence associated with every bounded-partial-quotient (not merely quadratic) irrational slope** (intercept-0, both seeds, every shift) | **PROVED — precise subclass** | `theorems/phase6/BOUNDED_TYPE_THEOREM.md` |


## Phase 7 — general-intercept obstruction mapped (**corrected by Phase 8**)

See [`theorems/phase7/PHASE7_CORRECTIONS.md`](theorems/phase7/PHASE7_CORRECTIONS.md). The Phase 7
files are preserved verbatim with correction banners; nothing was rewritten.

| Result | Status | File |
|---|---|---|
| Structured-intercept scans: 36/36 configurations clear the threshold; near-maximal digits identified as the empirical worst case, decay `~1/A²` | **CORRECT, and confirmed by Phase 8** (that family is exactly extremal, rate exactly `1/(Aβ_A)`) | `theorems/phase7/STRUCTURED_INTERCEPTS.md` |
| Flexible-margin boundary `ε_k = ω(log ℓ_k/ℓ_k)` | **CORRECT** (and not needed — Phase 8 lands in the constant-`ε` row) | `theorems/phase7/FLEXIBLE_MARGIN_BOUNDARY.md` |
| Intrinsic squares bypass the even branch but give **exactly zero** margin on the odd branch | **CORRECT**; superseded, not repaired | `theorems/phase7/INTRINSIC_SQUARE_ROUTE.md` |
| "The one remaining lemma" (general-intercept margin) classified `CONJECTURAL` | **SUPERSEDED — it is BHZ 2006 Prop. 5.1/5.2** | `theorems/phase7/PHASE7_CORRECTIONS.md` C1 |
| `ice(ω_ρ) = ind*(α)` off a countable "return" set; open cases countable; intercept `0` harder than generic | **REFUTED** (the exceptional set is uncountable; intercept `0` is among the easiest) | `theorems/phase7/PHASE7_CORRECTIONS.md` C2 |
| Convergent denominators with `q_1 = a_1` | **INDEXING ERROR** (BHZ Prop. 2.7: `q_1 = a_1+1`); limsups unaffected, root lengths wrong | `theorems/phase7/PHASE7_CORRECTIONS.md` C3 |
| Surplus decomposition `S_k ≥ A·E_k − …` | **DIMENSIONALLY INCOMPLETE** (leading term is `ℓ_k·E_k`) | `theorems/phase7/PHASE7_CORRECTIONS.md` C4 |
| `y(k)` attained for all admissible `(c_k)` | **OVERSTATED** (attained only when `0 < c_k < a_k`) | `theorems/phase7/PHASE7_CORRECTIONS.md` C5 |

## Phase 8 — closes the general-intercept case (theorem change)

The symbolic margin is **not new**: it is Berthé–Holton–Zamboni (2006), §5. Phase 8's own
contribution is the **arithmetic application and the attained-witness bridge** — identifying the
priority, supplying attained witnesses with explicit growing root lengths, correcting the
indexing and the surplus inequality, and closing the chain.

| Result | Status | File |
|---|---|---|
| `ice(ω) > 2` at every intercept of every bounded-type slope | **KNOWN** (BHZ 2006, Thm 1.1, corollary) | `theorems/phase8/PHASE8_TARGET_AUDIT.md` §3 |
| Uniform margin `ice(ω) ≥ 2 + 1/(2(A_b+1)²+1)`, every `ω ∈ X_γ` — i.e. the note's Conjecture 12.1 | **KNOWN** (BHZ 2006, **Prop. 5.1 + 5.2**) | `theorems/phase8/PHASE8_MARGIN_STATUS.md` T1 |
| Same bound at `1/(2(A_b+1)²)` **with an attained witness of exponent `≥ 2+δ` and root length `≥ q_{k-4}` for every `k ≥ 7`** | **PROVED** (Phase 8 Theorem 1; independent re-derivation) | `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` §3 |
| Keep-one closed form `ice = 2 + 1/(Aβ_A)`, `β_A = (A+√(A²+4))/2` | **PROVED** for eventually-constant BHZ digits; gives `δ*(γ) ≤ 1/(Aβ_A)` and rules out any `A`-free margin | `theorems/phase8/PHASE8_MARGIN_STATUS.md` T3 |
| Keep-one is **optimal** | **PROVED at restricted scope only** (eventually-constant BHZ digits, `A ≥ 2`; Fibonacci via BHZ Prop. 4.3). Otherwise **numerical evidence**, deliberately not promoted. Not used by Theorem 2. | `theorems/phase8/PHASE8_MARGIN_STATUS.md` T3b/T4 |
| Corrected surplus inequality, every length factor explicit: odd branch `S_k ≥ ℓ_k(r_u−2) + 1 − ⌈D(R_k)⌉log₂3 − log₂(2ℓ_k)` | **PROVED** | `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` §4 |
| Discrepancy step's missing hypothesis: `γ` bounded type ⟹ `γ/2` bounded type (the reduction is to the rotation by `γ/2`) | **GAP FOUND AND CLOSED** | `theorems/phase8/PHASE8_CHAIN_AUDIT.md` §3 |
| Supremum of prefix-power exponents vs. attained witness, kept apart | **RESOLVED** (BHZ's limsup form alone already suffices, at `δ/2`) | `theorems/phase8/PHASE8_CHAIN_AUDIT.md` §2 |
| **`Φ(v)∉ℚ` for both CS Rote lifts of *every* Sturmian word of *every* bounded-type slope — every intercept, both mechanical conventions, both seeds, every shift** | **PROVED** (Theorem 2) | `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` §5 |
| Independent end-to-end audit on literal mechanical words (no BHZ formula, certified brackets): 534 witnesses, transfer 534/534, `2^{L_v}>F(R)` 534/534, odd-branch density `1/2` 338/338 | **PASS** | `theorems/phase8/PHASE8_CHAIN_AUDIT.md` |

## Headline result of the repository

> For **every** complementary symmetric Rote sequence `v` whose associated Sturmian sequence is **any** Sturmian word — **any intercept, either mechanical convention** — of **any irrational slope with bounded partial quotients**, `Φ(v)∉ℚ`: **proved** (Phase 8, `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 2), for both seeds and every shift. This supersedes Phase 6's intercept-`0`-only result without weakening any other quantifier, which in turn superseded Phase 4's quadratic-irrational-only result.
>
> **Attribution.** The load-bearing symbolic input — a positive initial-critical-exponent margin uniform over all intercepts of a bounded-type slope — is **Berthé–Holton–Zamboni (2006), Propositions 5.1 and 5.2**, not a result of this repository. What this repository contributes is the **arithmetic application**: the periodic-approximation/height bridge, the exact XOR transfer, the density-`1/2` structural fact, and the attained-witness bookkeeping (explicit growing root lengths) that turns a `limsup` bound on `ice` into an unbounded surplus. Phase 7 recorded this symbolic input as an open conjecture; that was an error of literature search, corrected in `theorems/phase7/PHASE7_CORRECTIONS.md`.

## Cross-program scope limit — EOC divergence sector (audit, 2026-09-29)

No result above is changed. This records where the machinery above does **not** apply.

| Finding | Status | Where |
|---|---|---|
| On an integer-realizable zero-confined orbit the surplus is `S = log₂ h_eff − log₂ oddpart(m_n − m₀) ≤ log₂ m₀` — an identity, verified at 1 862 certified checkpoints | **PROVED** (exact form of an already-recorded qualitative fact) | `docs/EOC_HANDOFF_CLOSED.md` §3 |
| Therefore `limsup S = +∞` is unsatisfiable on that sector, and the periodic-approximation route cannot exclude EOC survivors | **PROVED** | `docs/EOC_HANDOFF_CLOSED.md` §4 |
| "EOC constraints ⟹ arbitrarily long initial squares" is **equivalent to** EOC's open problem (DE); the intermediate step is the conclusion restated | **CIRCULAR** | `docs/EOC_HANDOFF_CLOSED.md` §5 |
| `K ∩ {CS Rote} = ∅`: CS Rote one-density is exactly `1/2`, the sector needs `≥ β = 0.63093`; robust over shifts, seeds and corridor width | **PROVED**; rungs 3/3′ are **vacuous** on that sector | `docs/EOC_HANDOFF_CLOSED.md` §6 |
| The transported Dubickas rung has **zero margin** against an integer seed (Cor. 9.3's hypothesis is the exact negation of Prop. 9.2's conclusion) | **observed**, both are the source paper's own results | `docs/EOC_HANDOFF_CLOSED.md` §5 |

Novelty note: the qualitative route closure was already recorded (`LADDER.md` closing section;
EOC Revision 7 Observation 5.9). The audit supplies the exact identity, the quantified
obstruction and certified verification, not the original qualitative observation.

## Open, precisely stated

1. ~~CS Rote sequences at **other intercepts** of the same slope~~ — **CLOSED, Phase 8** (`theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 2).
2. Unbounded-partial-quotient slopes — open, and now known to be genuinely hard rather than merely untried: BHZ Thm 1.1 exhibits slopes carrying an intercept with `ice(ω) = 2` **exactly**, at which the odd-weight branch has zero margin. See `theorems/phase8/PHASE8_NEXT_TARGET.md`.
3. The rotation-coding repetition-existence gap (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`) — no analogue of Theorem 10.2 for mismatched two-interval codings is proved or cited anywhere.
4. The "next frontier" beyond `p(n)=2n` (`LADDER.md`) — deliberately not started.
