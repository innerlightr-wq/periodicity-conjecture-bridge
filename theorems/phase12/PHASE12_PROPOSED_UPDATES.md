**PROPOSED — NOT APPLIED. Supersedes `theorems/phase9b/PROPOSED_STATUS_UPDATES.md` by absorbing it.**

# PHASE12_PROPOSED_UPDATES.md

> **WORDING CLARIFICATION (documentation pass).** Where this file describes **López & Stoll**,
> *The 3x+1 periodicity conjecture in ℝ*, arXiv:2101.12747 (2021), Theorem 1, the current-facing
> statement of this repository is the neutral one: *López–Stoll propose an upper-density exclusion. We
> do not rely on that result; the conclusions developed here follow from the independent arguments
> stated in this repository.* We have **neither established nor disproved** their theorem and take no
> position on it. The sharper language retained below is the **audit record** — it preserves a
> technical observation raised by a third party (`innerlightr-wq/eoc-divergence` issue #30, open at the
> time of writing) together with its source reference and its verification status, namely **not
> verified by us and not a result of this repository**. It is kept, not rewritten, because research
> history should not be edited after the fact; it should not be quoted as a claim. No conclusion in
> this repository depends on López–Stoll in either direction. Canonical wording:
> [`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](../../docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

> **SUPERSEDED BY [`theorems/phase13/PROPOSED_PUBLICATION_CORRECTIONS.md`](../phase13/PROPOSED_PUBLICATION_CORRECTIONS.md)**, which absorbs all eleven items below and adds four (T2 restated as a challenged claim relied on nowhere, the Ridout withdrawal, the polynomial-bound withdrawal, and the foundation paper's public DOI + self-citation label). Still **NOT APPLIED**. Retained as the historical record.

Exact replacement text for every outstanding correction, Phases 9B through 12, in one place. **No
status file, README, LADDER or manuscript has been edited; no PDF has been rebuilt; nothing has been
deposited.** Per the standing instruction, nothing is applied until the final theorem statements are
settled.

## 0. Inventory of outstanding corrections

| # | owed since | subject | vehicle |
|---|---|---|---|
| 1 | Phase 9B | CS Rote ladder is subsumed by Monks–Yazinski 2004 (density `1/2 < β`) | status files + note Rev 3 |
| 2 | Phase 9B | Thue–Morse scope claim in the note's abstract and §15 Open 6 is false | note Rev 3 |
| 3 | Phase 9B | the `g(γ)` threshold attribution for Thue–Morse is withdrawn | banner (applied) |
| 4 | Phase 10 | qualitative coverage vs. quantitative height floors must be separated; the floors are a new **instance** of the foundation paper's own method | status files |
| 5 | Phase 11B | the Baker citation: `c_m ≥ C₂m^{−κ}` withdrawn, replaced by `C e^{−(log B)^κ}` | banners (applied) + status files |
| 6 | Phase 11B | the no-wrap hypothesis `|δ| ≤ min(β,1−β)` was unstated | banners (applied) |
| 7 | Phase 11B | the measured constants `0.41`, `2.02` are not asymptotic input | banners (applied) |
| 8 | **Phase 12** | **T2 (López–Stoll 2021 Thm 1) must be downgraded from "preprint" to "preprint with a specific documented objection"**; the securely covered region is `liminf < β`, not `liminf ≠ β` | status files + note Rev 3 |
| 9 | **Phase 12** | "effective" must be split into *effective in principle* and *explicitly supplied* | status files |
| 10 | **Phase 12** | the hitting-time mechanism is the foundation paper's own open problem (1), not new in Phase 11 | status files |
| 11 | **Phase 12** | Phases 9–12 are absent from `THEOREM_STATUS.md` and `LADDER.md` entirely | status files |

## 1. `THEOREM_STATUS.md` — insert before "Headline result of the repository"

> ## Phase 9 — unbounded-type CS Rote, Thue–Morse
>
> | Result | Status | File |
> |---|---|---|
> | Even branch needs no slope hypothesis; `ℓ_k E_k = q_{k−2}(m_{k−1}−1)` | **PROVED** | `theorems/phase9/` |
> | `Φ(TM) ∉ ℚ` | **PROVED**, and **subsumed** — Thue–Morse has density `1/2 < β` | `theorems/phase9b/THUE_MORSE_INDEPENDENT_PROOF.md` |
> | The `g(γ)` threshold is *needed* for Thue–Morse | **WITHDRAWN** — the pre-existing criterion suffices at threshold `1` | `theorems/phase9b/PHASE9B_VERDICT.md` |
>
> ## Phase 10 — the density/complexity coverage map
>
> | Result | Status | File |
> |---|---|---|
> | Coverage is by **(density, complexity)**; every CS Rote rung sits at density `1/2` | **PROVED** | `theorems/phase10/DENSITY_COMPLEXITY_LADDER.md` |
> | The residual region is lower ones-density at or above `β` (see the T2 note below) at complexity `≥ 1.70951…n` | **ESTABLISHED** | `theorems/phase10/PRIOR_RESULT_COVERAGE.md` |
> | Target class: the repository's own rotation coding with interval length moved from `1/2` to `β` | **IDENTIFIED** | `theorems/phase10/` |
>
> ## Phase 11 / 11B / 12 — the critical-density rotation codings
>
> | Result | Status | File |
> |---|---|---|
> | `Φ(s) ∉ ℚ` for `α = (√5−1)/2`, `ρ = 1/7`, `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)` | **PROVED** (Theorem 11) | `theorems/phase11/PHASE11_VERDICT.md` |
> | R4's polynomial Baker bound `c_m ≥ C₂m^{−κ}` | **WITHDRAWN** — the source gives `C e^{−(log B)^κ}` (Baker III 1967, Thm 2) | `theorems/phase11b/BAKER_SOURCE_AND_APPLICATION.md` |
> | The repaired witness growth `log ℓ(M) = O((log(M+2))^κ)`, which suffices | **PROVED** | `theorems/phase11b/REPAIRED_WITNESS_GROWTH.md` |
> | The closed-form arc description needs `|δ| ≤ min(β,1−β)`; `R2` is unconditional | **GAP FOUND AND STATED** | `theorems/phase11b/THEOREM11_DEPENDENCY_AUDIT.md` |
> | Independent reconstruction of Theorem 11 from definitions, including all five height floors | **PASS** | `theorems/phase12/THEOREM11_INDEPENDENT_AUDIT.md` |
> | The Baker citation, checked against MR0220680 and an independent thesis | **CONFIRMED**; two fallback citations recorded | `theorems/phase12/THEOREM11_INDEPENDENT_AUDIT.md` §4 |
> | `A_m > β − 1/2 > 0` uniformly — nonvanishing with no case analysis | **PROVED** (supersedes Phase 11B's two-case argument) | `theorems/phase12/THEOREM11_INDEPENDENT_AUDIT.md` §5 |
> | **`Φ(s) ∉ ℚ` for every quadratic irrational `α ∈ (0,1)` and every rational `ρ`, `ρ = 0` included** | **PROVED** (Theorem 12) | `theorems/phase12/QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md` |
> | `ρ = 0` needs no finite shift and no separate argument — the signed relaxation plus the `δ>0` convergents | **PROVED** | same, §4 |
> | `ρ` irrational | **OPEN** — the arc at `0` has no effective rate | same, §5 |

## 2. `THEOREM_STATUS.md` — replace the Headline section

> ## Headline result of the repository
>
> > **Theorem 12.** For every quadratic irrational `α ∈ (0,1)`, every `ρ ∈ ℚ` (including `ρ = 0`), and
> > `β = ln2/ln3`, the word `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)` is aperiodic, has ones-density exactly `β` and
> > factor complexity `2n`, and satisfies **`Φ(s) ∉ ℚ`**.
> > (`theorems/phase12/QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md`; Theorem 11 is the case
> > `α = (√5−1)/2`, `ρ = 1/7`.)
>
> This supersedes the CS Rote chain as the repository's headline, on novelty grounds rather than
> mathematical ones: the CS Rote theorems of Phases 2/4/6/8/9 are all at ones-density exactly `1/2`
> and are therefore consequences of **Monks–Yazinski (2004) Thm 2.7(b)** whatever their complexity
> (Phase 9B). Their proofs stand; their novelty claims do not. Theorem 12 is at density exactly `β`,
> which no density result reaches.
>
> **Attribution.** Six published inputs carry Theorem 12: Bernstein–Lagarias/foundation-paper Props.
> 2.2 and 4.1; Lagrange and Perron on quadratic continued fractions; **Baker, Mathematika 14 (1967),
> Part III, Theorem 2**; Kuipers–Niederreiter Ch. 2 Thm 3.4; Rote (1994)/Berstel–Vuillon (2001);
> Gelfond–Schneider. And the **mechanism** — reading the agreement excess as a first entry time of the
> rotation orbit into an arc at the partition endpoint — is **the foundation paper's own §12 open
> problem (1)**, not new here. What is new here is its execution at two discontinuities, the split of
> the two arcs into an elementary bound at `0` and a Baker bound at `β`, the witness-size calculus,
> and the generalization to every quadratic slope and rational intercept. See
> `theorems/phase12/CLAIM_AND_DEPENDENCY_LEDGER.md`.
>
> **Effectivity, stated precisely.** The finite height floors (`H ≥ 2^462, …, 2^15998` for the named
> word) are exact integer facts and use no analytic input. The conclusion `S → ∞` is effective **in
> principle** — Baker's `C` and the Kuipers–Niederreiter constants are computable from their proofs —
> but **no numerical value is supplied for them here**. Earlier phases said "effective" without
> drawing this line.
>
> **Scope.** Nothing above bears on divergent orbits of positive integers, on the Collatz conjecture,
> or on the Periodicity Conjecture in general, which quantifies over all aperiodic parity vectors.
> Theorem 12's family is two-parameter and of measure zero in `{0,1}^ℕ`.

## 3. `THEOREM_STATUS.md` and `theorems/phase10/*` — the T2 downgrade (item 8)

Wherever T2 appears as "preprint", replace with:

> **López–Stoll**, arXiv:2101.12747 (2021), Thm 1 — **preprint, and specifically disputed.**
> `innerlightr-wq/eoc-divergence` issue #30 (open, uncontested) identifies the step that carries
> Theorem 1 — passing from "`Φ_ℝ(v)` is irrational" to "`Φ(v)` is aperiodic" through an alleged
> 2-adic expansion of a real irrational — and argues it does not follow, the real and 2-adic limits of
> one sequence of rationals being independent. The objection does not claim Theorem 1 is false.
> **Consequence: the securely covered density region is `liminf < β` (Monks–Yazinski 2004, refereed),
> not `liminf ≠ β`.** Density `> β` must be listed as not securely covered.

And in `theorems/phase10/PRIOR_RESULT_COVERAGE.md`, the sentence "only density exactly `β` is
uncovered" becomes "only density **at or above** `β` is securely uncovered; of that region, density
exactly `β` is the case T1 cannot reach even in principle." Theorem 12's standing is unchanged either
way.

## 4. `LADDER.md` — new rung and revised reading note

Replace the diagram's last line and add:

> ```
> bounded-type CS Rote, EVERY intercept  p(n) = 2n        (Phase 8; density 1/2, SUBSUMED)
>     |
> critical-density rotation codings  p(n) = 2n, density exactly beta   (Phase 12, Theorem 12)
>     |
> every s with p(L) <= 2L  (foundation paper problem (4)) -- OPEN
> ```
>
> **Reading the ladder by density, not by complexity (Phase 9B, refined Phase 12).** The known
> dichotomy for `Φ(v) ∉ ℚ` is by **lower ones-density**: below `β = ln2/ln3` by Monks–Yazinski (2004)
> Thm 2.7(b) [refereed]; above `β` **only** by López–Stoll (2021) Thm 1, a preprint whose load-bearing
> step is specifically disputed (§3 above). Rungs 1–3″ all sit at density `1/2` or `n+1`-complexity and
> are covered. Rung 4 is at density exactly `β`, where no density result applies. Each rung's
> *qualitative* conclusion is covered or not by that test; its *quantitative* content (effective height
> floors `H ≥ 2^{S}`) is never covered by T1/T2, which bound nothing — but producing such floors is the
> foundation paper's own claimed method, so they are new instances, not a new kind of result.

## 5. `README.md` — headline paragraph

> **Headline.** `Φ(s) ∉ ℚ` for every coding of a quadratic-irrational rotation by the interval
> `[0, ln2/ln3)` at any rational intercept — aperiodic, ones-density exactly the critical value
> `β = ln2/ln3`, factor complexity `2n`. This is strictly beyond the **counting** threshold
> (`1.70951…`) *and* beyond the **density** dichotomy that covers the repository's earlier
> complementary-symmetric Rote results, every one of which sits at density `1/2 < β` and is therefore
> a consequence of Monks–Yazinski (2004). Effective in principle; five explicit Baker-free height
> floors up to `2^15998` for the named word. It says nothing about integer Collatz orbits or about the
> Periodicity Conjecture in general.

## 6. `PRIOR_ART.md` — standing gate, final form

> **Standing gate (Phases 9B, 10, 12).** Before claiming novelty for any class:
> 1. Compute the lower ones-density. If `< β` the qualitative conclusion is already available from
>    Monks–Yazinski (2004) Thm 2.7(b), whatever the complexity. If `> β`, López–Stoll (2021) Thm 1
>    would cover it, **but that step is disputed** — treat the region as open and say so.
> 2. Compute `liminf p(L)/L`. If `< 1.70951…`, the counting route already covers it.
> 3. Ask **separately** whether the *quantitative* content is new, and check it against the foundation
>    paper's own effectivity claim (Cor. 6.2, Cor. 8.7) before calling it a contribution.
> 4. Search the **conclusion**, not only the mechanism. All three of the searches indexed above were
>    mechanism searches and missed step 1 entirely.
> 5. Check whether the mechanism is already proposed in the foundation paper's §12 open problems.

## 7. The deposited note — corrections owed, still **not** deposited

Revision 2 (`10.5281/zenodo.23045141`) now owes **four** corrections, not two:

1. the Thue–Morse scope claim (abstract, §15 Open 6) — false as stated;
2. the CS Rote novelty framing — it crosses the counting frontier only;
3. **the Baker citation** — any statement of the R4-style polynomial bound must become
   `C e^{−(log B)^κ}` with the Mathematika 14 (1967) Part III Theorem 2 citation;
4. **the T2 downgrade** wherever the note relies on density `> β` being covered.

None is an error in a proof; all four are citation or framing errors. A single Revision 3 is the right
vehicle. **No publication action has been taken and none should be until the author decides. Do not
rebuild a release until the Theorem 11/12 statements are settled.**

## 8. Files given correction notices rather than rewrites

Already applied (Phase 11B): banners on `theorems/phase11/{ROTATION_REPETITION_LEMMA,
PHASE11_VERDICT, EXACT_HEIGHT_AND_SURPLUS}.md`. Phase 12 adds a pointer line to
`theorems/phase11/PHASE11_VERDICT.md` and to `theorems/phase9b/PROPOSED_STATUS_UPDATES.md` (marking
it superseded by this file). **No historical text is deleted anywhere.**
