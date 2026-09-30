**THE DEPOSIT IS THE LOCAL FILE; `C` AND `C₀` ARE NOW NUMBERS; FOUR CORRECTIONS ARE OWED**

# PHASE14_VERDICT.md

Isolated worktree `/home/elias/scratch/phase14-bridge`, branch `phase14-release-reconciliation`, cut
from `docs-framing-and-invitation`. **Ancestry verified**: HEAD was `5d04064` (the Revision 3 draft),
one commit ahead of the expected `ec035dd`, and `ec035dd`, `46b0d0a` (Phase 13), `e21aab9` and
`c1bbff4` are all ancestors. Tree clean. Nothing pushed, nothing published, no deposited artifact
overwritten.

## 1. What is actually published

The correct record is **`10.5281/zenodo.23068563`** — not `…23068326`, which §2 explains.

> The deposited file is **byte-identical** to `technical-note/note_rev3.pdf`:
> md5 `4e37bf96f28414bc51eb6f90e6b87e9e`, 471 520 bytes, 34 pages, CC BY 4.0, concept DOI
> `10.5281/zenodo.23045140`.

Checked against the downloaded file, not from memory, **every correction outstanding at the start of
Phase 13 is already in it**: the quadratic-rotation theorem (Thm 17.5), the **algebraic-offset
theorem** (Thm 18.2, Cor. 18.3), the repaired Baker argument with the polynomial bound withdrawn
(§19, §1 D6), the **acknowledgement** (§1 D3, §16, Acknowledgments), the Thue–Morse
withdrawal (D1), the CS Rote novelty correction (D2), the foundation paper by public DOI and labelled
a self-citation (D4), the theorem-numbering clarification (D5), and "has not been refereed". **None
of these was redone.**

## 2. Four versions exist where three were intended

| record | file | md5 | is |
|---|---|---|---|
| 23045141 | `…3x1_Periodicity_Conjecture.pdf` | `9b80c77c…` | Revision 1 |
| 23061396 | `…Revision_2.pdf` | `b61d76f6…` | Revision 2 |
| **23068326** | `…Latest_Built.pdf` | `b61d76f6…` | **Revision 2 again — a byte duplicate** |
| 23068563 | `…Revision_3_DRAFT.pdf` | `4e37bf96…` | Revision 3 |

Every local PDF matches its deposit exactly. Record 23068326 carries Revision 2's bytes under a
filename suggesting the newest build; it is the DOI the earlier Phase 14 brief had. It should never be
cited. Also: `correction_notice.pdf`, Revision 2's erratum, appears on no version.

## 3. Corrections still owed — four, all arising since the deposit

| | what | severity |
|---|---|---|
| **C1** | **The record description is Revision 1's.** It still advertises "intercept-zero complementary symmetric Rote representatives", superseded two revisions ago, and mentions none of the critical-density work. The file is right; the page describing it is wrong | **high** |
| **C2** | The PDF's provenance section says "Revision 3 is a draft and has not been deposited." It has been | medium |
| **C3** | The citable filename contains `DRAFT` | medium |
| **C4** | **"Open 4 — Unbounded partial quotients. THE LIVE FRONTIER"** conflates an unfinished proof with an open conclusion | **high** |

Exact replacement text for all four is in `ZENODO_RELEASE_RECONCILIATION.md` §6. **Nothing applied.**

### C4, because it is the one that matters mathematically

CS Rote sequences have ones-density exactly `1/2` **whatever the slope's partial quotients** — that is
a structural fact about the doubled root, not a consequence of bounded type. Since `1/2 < β`,
Monks–Yazinski (2004) Thm 2.7(b) already gives `Φ(v) ∉ ℚ` for **every** CS Rote sequence over **every**
irrational slope. So Open 4:

- is **not** an open irrationality question — the conclusion is available;
- **is** an unfinished independent second proof: at an intercept with `ice(ω) = 2` exactly (BHZ Thm
  1.1 characterises those slopes, all of unbounded partial quotients) this repository's own criterion
  has margin exactly `0`.

Calling it "the live frontier" repeats, for the unbounded-type case, exactly the framing error that
D2 corrects one page earlier for the bounded-type case. D2 was not propagated to Open 4. The live
frontier is density exactly `β`.

## 4. Consolidated documentation

`README.md`, `LADDER.md` and `THEOREM_STATUS.md` rewritten from the audited results. The obsolete
Phase 1–6 headline is gone. `LADDER.md` is now a **two-coordinate** map (density × complexity) rather
than a complexity chain, because the density axis is the one the literature reads. Five categories
are kept apart in all three files: already implied by prior results; independent effective proofs and
quantitative refinements; the critical-density family theorem; unresolved novelty; open extensions.
Process language is gone — including `PHASE13_VERDICT.md`'s "treated as instructed", now an
acknowledgement. The acknowledgement paragraph appears verbatim in all three.

Two stale README discipline notes were also caught and fixed: one still asserted the **withdrawn**
Thue–Morse structural claim, and one said no paper is drafted here.

## 5. Explicit constants — the named example closes

**The discrepancy side.** Kuipers–Niederreiter Ch. 2 Thm 3.4 read first-hand: for `a_i ≤ K`,
`N D_N ≤ 3 + (1/log φ + K/log(K+1))log N`. At `K = 1`, `c_K = 3.520782`. Two adjustments, each stated:
the intercept costs a factor 2 (and for `ρ = 1/7` the shifted interval genuinely wraps, so it is
incurred), the index range costs 1. Hence `Δ(N) ≤ 4.880840·log₂N + 7`, and

> **`S(W) ≥ (L − ℓ) − C·log₂ℓ − C₀` with `C = 24.207846`, `C₀ = 35.869175`.**

Verified against exactly computed surpluses at twelve convergents, no failures. *An error in my own
derivation was caught by that table*: I converted `ln N → log₂N` in the wrong direction, inflating
`C_D` by `1/ln²2 ≈ 2.08`. It is recorded in `EXPLICIT_DISCREPANCY_CONSTANTS.md` §2 rather than
silently fixed.

**The analytic side, audited.** Waldschmidt Thm 10.1's hypotheses re-checked. One real looseness
found: Phase 13 wrote `log B = log H(A_m) + 2` without distinguishing the **Weil** height in the
hypothesis from the **classical** height being bounded. The correct conversion is
`h(1:A_m:−1) ≤ (log H(A_m))/2 + 0.275`. Phase 13's choice was *larger*, hence admissible — both
hypotheses on `B` are lower bounds and the conclusion decreases in `B` — but wasteful by about a
factor 4 in the exponent. Also, `H(A_m) ≤ 2601m²` is now **proved** (the measured maximum is `55`; the
measured value is not substituted for the proof). `c₁ = 2.38907·10^13` confirmed.

**The result.**

> `f(M) := M − C·[1 + max((c₁(log B_M)² + 1)/ln2, log₂(147M))] − C₀`, and for every integer `M ≥ 2`
> the constructed witness gives **`H ≥ 2^{f(M)}`**.
> **`f(M) > 0` for every `M ≥ M₀ = 1.78337·10^18`**, with monotonicity proved
> (`f′(M) > 0` once `M > 2Cc₁log B_M/ln2 = 7.7·10^16 < M₀`) and grid-checked.

Starting-index restrictions stated in full: `M ≥ 2`; `ℓ(M) = q_k` with `k ≥ 2` (the no-wrap hypothesis
fails at `q₁`); `H(A_m) ≤ 2601m²` for `m ≥ 1`; `m = 0` handled by `c₀ = 0.4880726107`, no theorem.

**Four heights, kept apart**: the approximants' own heights (`≈2^ℓ`, actual rationals, prove nothing
alone); the hypothetical `u/v` with `H` fixed *before* `M`; the practical certificates
(`2^462 … 2^15998`, exact integer comparisons, the only numerically useful floors); and `f(M)`, which
is beyond computation and whose value is that it is *written down*, not that it is small.

## 6. Parameter dependence — and what is not claimed

| constant | depends on | uniform? |
|---|---|---|
| `C₀ = 35.869175` | nothing | **yes, absolutely** |
| `C` | the largest partial quotient `A` only | **yes, given `A`** |
| `c₁` | `D = [ℚ(α,ρ):ℚ]` only | **yes, given `D`** |
| `C_h` (in `H(A_m) ≤ C_h m^D`), `c_L` | the actual `α, ρ` | **no** |

> **`f(M)` is therefore not uniformly numerical over the family, and that is not claimed.** A `ρ` of
> large height pushes `C_h` up without bound at fixed `(A,D)`. For any single explicit `(α,ρ)` both
> missing constants are a finite computation, so `f(M)` is numerical case by case — which is what was
> done for `α=(√5−1)/2`, `ρ=1/7`, and all that is asserted.

## 7. The strongest verified statement

> Let `α ∈ (0,1)` be a quadratic irrational, `β = ln2/ln3`, and `s_n = 1 ⟺ {nα+ρ} ∈ [u,u+β) (mod 1)`.
> If `ρ−u` is **algebraic** — `ρ` and `u` themselves unrestricted — then `s` is aperiodic, has lower
> ones-density exactly `β` and factor complexity `2n`, and **`Φ(s) ∉ ℚ`**.
>
> For `α=(√5−1)/2`, `ρ=1/7`, `u=0`: `H ≥ 2^{462}, 2^{838}, 2^{872}, 2^{2469}, 2^{15998}` are exact
> integer certificates, and `H ≥ 2^{f(M)}` holds for every `M ≥ 2` with `f` explicit and positive
> beyond `M₀ ≈ 1.78·10^18`.

Carried by: Bernstein–Lagarias (1996); the foundation paper's Props. 2.2, 4.1 and its §12 problem (1),
which is the **mechanism** and is not original here; Lagrange–Perron; Liouville; Baker (1966 I, 1967
III); Waldschmidt Thm 10.1; Kuipers–Niederreiter Ch. 2 Thm 3.4; Rote (1994) and Berstel–Vuillon
(2001); Gelfond–Schneider. **Novelty remains formally unresolved.**

## 8. Ready for specialist review

The four items most likely to repay a number theorist's attention, in order:

1. **`EXPLICIT_HEIGHT_BOUND.md` §1** — the Waldschmidt hypothesis check, especially the Weil-versus-
   classical height conversion and whether `h(1:b₁:b₂) ≤ h(b₁)+h(b₂)` is being used correctly.
2. **`EXPLICIT_DISCREPANCY_CONSTANTS.md` §2** — the two adjustments (factor 2 for the intercept, `+1`
   for the index range) that carry KN's theorem to our drift.
3. **`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md` §3** — the Liouville bound and the
   classification of exact boundary hits.
4. **`theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md`** — whether the fourteen located results are
   stated with the hypotheses ascribed to them, and whether anything else already covers the family.

See `docs/INVITATION_TO_DOMAIN_EXPERTS.md`.

## 9. Not advanced

No new generalization was attempted, per the instruction to finish consolidating first. The open
items — transcendental offset, density `> β`, all `s` with `p(L) ≤ 2L`, transcendence via Ridout —
are recorded in `THEOREM_STATUS.md` and untouched.
