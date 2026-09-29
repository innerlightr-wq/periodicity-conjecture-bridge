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

## Headline result of the repository

> For **every** complementary symmetric Rote sequence `v` whose associated Sturmian sequence is the intercept-`0` mechanical word of **any irrational slope with bounded partial quotients**, `Φ(v)∉ℚ` — **proved** (Phase 6, `theorems/phase6/BOUNDED_TYPE_THEOREM.md`). This supersedes Phase 4's quadratic-irrational-only result (a countable special case) without weakening any quantifier, and was reached only after Phase 5's independent hostile audit confirmed the underlying chain and Phase 6's adversarial non-periodic reconstruction confirmed no hidden periodicity dependence.

## Open, precisely stated

1. CS Rote sequences at **other intercepts** of the same slope (not a shift of the intercept-0 representative) — unchanged since Phase 4, re-confirmed still open in Phase 6.
2. Unbounded-partial-quotient slopes — genuinely out of reach of the discrepancy mechanism used.
3. The rotation-coding repetition-existence gap (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`) — no analogue of Theorem 10.2 for mismatched two-interval codings is proved or cited anywhere.
4. The "next frontier" beyond `p(n)=2n` (`LADDER.md`) — deliberately not started.
