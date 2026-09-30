**PROPOSED — NOT APPLIED. Supersedes and absorbs `theorems/phase12/PHASE12_PROPOSED_UPDATES.md`.**

# PROPOSED_PUBLICATION_CORRECTIONS.md

Every outstanding correction, Phases 9B → 13, in one reviewable place, with exact replacement text.
**Nothing has been applied: no status file, README, LADDER or manuscript edited; no PDF rebuilt; no
Zenodo action taken; no deposited artifact overwritten.** Historical files keep their text and carry
pointers.

> **Standing wording rule (added with the documentation pass).** In current-facing documentation and
> in the replacement text below, results by other authors that this repository does not use are
> described in dependency-and-acknowledgement language, not adversarial language. The canonical form
> is:
>
> > López–Stoll's work on density and the 3x+1 conjugacy map helped guide this programme toward the
> > critical density `β = ln2/ln3`. We acknowledge that influence. The results presented here are
> > established through the independent arguments given in this repository and do not require their
> > proposed upper-density exclusion.
>
> Technical concerns remain recorded in the audit files with their source references and verification
> status; they are not repeated as claims. See `docs/DEPENDENCE_ON_PRIOR_RESULTS.md`.

## 0. Inventory — fifteen items

| # | owed since | subject | vehicle |
|---|---|---|---|
| 1 | 9B | CS Rote ladder subsumed by Monks–Yazinski 2004 (density `1/2 < β`) | status + note Rev 3 |
| 2 | 9B | Thue–Morse scope claim in the note's abstract and §15 Open 6 is false | note Rev 3 |
| 3 | 9B | the `g(γ)` threshold attribution for Thue–Morse withdrawn | banner (applied) |
| 4 | 10 | qualitative coverage vs. quantitative height floors must be separated; the floors are a new **instance** of the foundation paper's own method | status |
| 5 | 11B | Baker citation: `c_m ≥ C₂m^{−κ}` withdrawn → `C e^{−(log B)^κ}` | banner (applied) + status |
| 6 | 11B | the no-wrap hypothesis `|δ| ≤ min(β,1−β)` was unstated | banner (applied) |
| 7 | 11B | the measured constants `0.41`, `2.02` are not asymptotic input | banner (applied) |
| 8 | 12 | T2 (López–Stoll) restated as a result **not relied on**, with the coverage claim rephrased against what is independently available | status + note Rev 3 |
| 9 | 12 | "effective" split into *in principle* / *explicitly supplied* | status |
| 10 | 12 | the hitting-time mechanism is the foundation paper's own §12 problem (1) | status + note Rev 3 |
| 11 | 12 | Phases 9–13 absent from `THEOREM_STATUS.md` and `LADDER.md` | status |
| 12 | **13** | **T2 wording made neutral** (see §7): a proposed result we do not rely on, neither established nor disproved by us | status + note Rev 3 |
| 13 | **13** | **Phase 12's one-line dismissal of the Ridout route is withdrawn** (the exponent exceeds the threshold at 7 of 20 convergents) | status |
| 14 | **13** | **Phase 12's polynomial-bound hope is withdrawn** (it is Baker's own unproved conjecture `κ=1`) | status |
| 15 | **13** | **the foundation paper must be cited by its public DOI**, and as a **self-citation to an unrefereed preprint** | status + README + note Rev 3 |

## 1. Citation form for the foundation paper — to be used everywhere

> De Jesús, Elias. *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic
> Integer*. Zenodo, 28 September 2026. Version DOI **10.5281/zenodo.23019799**, concept DOI
> **10.5281/zenodo.22920055**. CC BY 4.0. Preprint, **not refereed**; **by the present author**.

The local `reference/` copy is byte-identical to the deposited file (md5
`54732e14b939c39f74c118097a069f30`) — see `PUBLIC_FOUNDATION_VERSION_CHECK.md`. Earlier versions of
the record remain restricted and must not be cited.

## 2. `THEOREM_STATUS.md` — new sections (Phases 9–13)

Insert before "Headline result of the repository" the Phase 9/10/11/11B/12 table of
`theorems/phase12/PHASE12_PROPOSED_UPDATES.md` §1 **verbatim**, then append:

> ## Phase 13 — algebraic intercepts, consolidation, explicit constants
>
> | Result | Status | File |
> |---|---|---|
> | The public foundation paper is byte-identical to the local reference copy | **VERIFIED** | `theorems/phase13/PUBLIC_FOUNDATION_VERSION_CHECK.md` |
> | `‖mα+ρ‖ ≥ c_L m^{−D²}` for algebraic `ρ`, by **Liouville alone** — no transcendence input | **PROVED** | `theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md` §3 |
> | Exact `0`-boundary hits: `ρ ∈ ℤα+ℤ`, unique index `m₀`, any value; two independent treatments | **PROVED** | same, §3(d) |
> | **`Φ(s) ∉ ℚ` for every quadratic irrational `α ∈ (0,1)` and every real algebraic `ρ`** | **PROVED** (Theorem 13) | same, §1 |
> | The same for `[u,u+β)` whenever `ρ−u` is algebraic — `ρ` and `u` may both be transcendental | **PROVED** (Cor. 13.1) | same, §10 |
> | `ρ−u` transcendental | **OPEN** — now the only obstruction on the intercept axis | same, §11 |
> | An **explicit** algebraic-coefficient estimate: `c₁ ≈ 2.39·10^13` at `D=2` | **LOCATED AND APPLIED** (Waldschmidt Thm 10.1) | `theorems/phase13/EXPLICIT_CONSTANTS_STATUS.md` |
> | A **polynomial** logarithmic-form bound at fixed degree | **WITHDRAWN** — it is Baker's own unproved conjecture `κ = 1` | same, §5 |
> | The Ridout/transcendence route | **REOPENED** — the exponent exceeds `2` at 7 of 20 convergents; infinitude open | `theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md` §5 |

## 3. `THEOREM_STATUS.md` — Headline section, replacement

> ## Headline result of the repository
>
> > **Theorem 13.** For every quadratic irrational `α ∈ (0,1)`, every real algebraic `ρ`, and
> > `β = ln2/ln3`, the word `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)` is aperiodic, has ones-density exactly `β`
> > and factor complexity `2n`, and satisfies **`Φ(s) ∉ ℚ`**. More generally the interval may be
> > `[u,u+β)` whenever `ρ−u` is algebraic, with `ρ` and `u` themselves unrestricted.
> > (`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md`.)
>
> This supersedes the CS Rote chain as the headline on **novelty** grounds, not mathematical ones: the
> CS Rote theorems of Phases 2/4/6/8/9 all sit at ones-density exactly `1/2` and are consequences of
> **Monks–Yazinski (2004) Thm 2.7(b)** whatever their complexity. Their proofs stand; their novelty
> claims do not.
>
> **Attribution.** Ten published inputs carry Theorem 13: Bernstein–Lagarias (1996); the foundation
> paper's Props. 2.2 and 4.1; Lagrange and Perron on quadratic continued fractions; Liouville's
> inequality; **Baker, Mathematika 14 (1967), Part I Thm 1.1 / Part III Thm 2**; **Waldschmidt Thm
> 10.1**; Kuipers–Niederreiter Ch. 2 Thm 3.4; Rote (1994) and Berstel–Vuillon (2001);
> Gelfond–Schneider. And the **mechanism** — reading the agreement excess as a first entry time of the
> rotation orbit into an arc at the partition endpoint — is **the foundation paper's own §12 open
> problem (1)**, not new here. What is new is its execution at two discontinuities, the split into an
> elementary bound at `0` and a logarithmic-form bound at `β`, the witness-size calculus, the `ρ = 0`
> and exact-hit treatments, and the generalisation in both parameters.
>
> **Effectivity, stated precisely.** The finite height floors (`H ≥ 2^462 … 2^15998` for the named
> word) are exact integer facts and use no analytic input. The asymptotic conclusion `S → ∞` is
> effective, and since Phase 13 its **analytic** constant is numerically supplied
> (`c₁ ≈ 2.39·10^13`); its **arithmetic** constants `C, C₀` are not. The explicit bound first bites at
> `M ≈ 10^17`, so it adds rigour and no usable numbers.
>
> **Scope.** Nothing above bears on divergent orbits of positive integers, on the Collatz conjecture,
> or on the Periodicity Conjecture in general. Theorem 13's family is two-parameter and of measure
> zero in `{0,1}^ℕ`.

## 4. `LADDER.md` — rung and reading note

> ```
> bounded-type CS Rote, EVERY intercept   p(n)=2n           (Phase 8; density 1/2, SUBSUMED)
>     |
> critical-density rotation codings, rational intercept       (Phase 12, Theorem 12)
>     |
> critical-density rotation codings, ALGEBRAIC intercept,     (Phase 13, Theorem 13)
> and any interval [u,u+beta) with rho-u algebraic
>     |
> rho - u transcendental  --  OPEN, the intercept-axis boundary
>     |
> every s with p(L) <= 2L  (foundation problem (4))  --  OPEN
> ```
>
> **Reading the ladder by density, not by complexity (9B, refined 12, refined 13).** The relevant
> coordinate is lower ones-density. Below `β = ln2/ln3` the conclusion is already available from
> Monks–Yazinski (2004) Thm 2.7(b), refereed. Above `β`, López–Stoll (2021) Thm 1 propose an
> upper-density exclusion. **López–Stoll's work on density and the 3x+1 conjugacy map helped guide
> this programme toward the critical density `β`; we acknowledge that influence. The results
> presented here are established through the independent arguments given in this repository and do not
> require their proposed upper-density exclusion.** Stated against what is independently available,
> the covered region is `liminf < β` and the residual is `liminf ≥ β`.
> Rungs 1–3″ sit at density `1/2` or at complexity `n+1` and are covered. The critical-density rungs
> sit at `= β`, where no density result applies. Each rung's *qualitative* conclusion is decided by
> that test; its *quantitative* content (height floors) is never covered by T1/T2, which bound
> nothing — but producing such floors is the foundation paper's own claimed method, so they are new
> instances, not a new kind of result.

## 5. `README.md` — headline paragraph

> **Headline.** `Φ(s) ∉ ℚ` for every coding of a quadratic-irrational rotation by an interval of
> length `ln2/ln3` whose left endpoint differs from the intercept by an algebraic number — aperiodic,
> ones-density exactly the critical value `β = ln2/ln3`, factor complexity `2n`. This is beyond the
> **counting** threshold (`1.70951…`) and beyond the **density** dichotomy that covers this
> repository's earlier complementary-symmetric Rote results, every one of which sits at density
> `1/2 < β` and is therefore a consequence of Monks–Yazinski (2004). Effective, with the analytic
> constant numerically supplied since Phase 13; five explicit Baker-free height floors up to `2^15998`
> for the named word. It says nothing about integer Collatz orbits or about the Periodicity Conjecture
> in general. The foundation reference is the author's own unrefereed preprint,
> doi:10.5281/zenodo.23019799.

## 6. `PRIOR_ART.md` — standing gate, final form

> **Standing gate (9B, 10, 12, 13).** Before claiming novelty for any class:
> 1. Compute the lower ones-density. If `< β`, Monks–Yazinski (2004) Thm 2.7(b) already gives the
>    qualitative conclusion, whatever the complexity. If `> β`, López–Stoll (2021) Thm 1 propose an
>    exclusion covering it; since this repository does not rely on that result, state the coverage
>    claim against what is independently available and say plainly which of the two situations you are
>    describing.
> 2. Compute `liminf p(L)/L`. If `< 1.70951…`, counting already covers it.
> 3. Ask **separately** whether the *quantitative* content is new, and check it against the foundation
>    paper's own effectivity claim (Cor. 6.2, Cor. 8.7).
> 4. Search the **conclusion**, not the mechanism. Also search the **stronger** conclusions
>    (transcendence, irrationality measure) — Phase 13 found that the Ridout threshold is not out of
>    reach, which a mechanism search would never surface.
> 5. Check whether the mechanism is already proposed in the foundation paper's §12 open problems.
> 6. Distinguish the **parity vector** from the **2-adic digit string**. The `p`-adic
>    low-complexity literature (Adamczewski–Bugeaud; Bugeaud–Kekeç) constrains the digit string of
>    `D(s) = Σ s_i 2^i`, not `Φ(s)`. They are different numbers.

## 7. `theorems/phase10/PRIOR_RESULT_COVERAGE.md` and every T2 mention — neutral wording

Replace "preprint" with:

> **preprint; a proposed result this repository does not rely on, by authors whose earlier work this
> programme is indebted to.** López–Stoll's work on density and the 3x+1 conjugacy map helped guide
> this programme toward the critical density `β = ln2/ln3`. We acknowledge that influence. The results
> presented here are established through the independent arguments given in this repository and do not
> require their proposed upper-density exclusion. We have **neither established nor disproved** it and
> take no position on it. Stated against what is independently available, the covered density region
> is `liminf < β` (Monks–Yazinski 2004, refereed); the classes treated here sit at exactly `β` and are
> outside that range either way, so **no conclusion changes in either case.**

A technical observation about one step of that paper, raised by a third party
(`innerlightr-wq/eoc-divergence` issue #30, open at the time of writing), is retained in the audit
record with its source reference and verification status — see
`theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md` §1 and
`theorems/phase12/CRITICAL_ROTATION_PRIOR_RESULTS.md` §3. **It has not been verified by us, it is not
a result of this repository, and it must not be presented as one.** The canonical current-facing
wording is `docs/DEPENDENCE_ON_PRIOR_RESULTS.md`.

## 8. The deposited note — **five** corrections owed

`Beyond Sturmian Words in the 3x+1 Periodicity Conjecture`, Revision 2
(`10.5281/zenodo.23045141`) owes:

1. the **Thue–Morse scope claim** (abstract, §15 Open 6) — false as stated;
2. the **CS Rote novelty framing** — it crosses the counting frontier only;
3. the **Baker citation** — any polynomial-bound statement becomes `C e^{−(log B)^κ}`, cited to
   Mathematika **14** (1967), Part III, Theorem 2;
4. **the T2 wording** wherever the note treats density `> β` as covered — restate it as a proposed
   result the note does not rely on, and phrase the coverage claim against what is independently
   available;
5. **the foundation citation** — now by version DOI `10.5281/zenodo.23019799`, and labelled a
   self-citation to an unrefereed preprint.

None is an error in a proof; all five are citation or framing errors. A single **Revision 3** is the
right vehicle, and it should also add Theorems 12 and 13.

> **No publication action has been taken and none should be. Do not rebuild a release, do not upload,
> and do not overwrite any deposited artifact, until the Theorem 11/12/13 statements are settled.**

Release artifacts are unchanged and verified this phase: `technical-note/note_rev2.pdf`
`8daf1979…`, `technical-note/correction_notice.pdf` `0c93457c…`, `technical-note/note.pdf`
`b7054cee…`, and both `~/Downloads` copies.

## 9. Files given pointers rather than rewrites

Applied in Phase 11B and 12: banners on `theorems/phase11/{ROTATION_REPETITION_LEMMA,
PHASE11_VERDICT, EXACT_HEIGHT_AND_SURPLUS}.md`, `theorems/phase10/PRIOR_RESULT_COVERAGE.md`, and the
supersede marker on `theorems/phase9b/PROPOSED_STATUS_UPDATES.md`. Phase 13 adds pointers to
`theorems/phase12/{PHASE12_VERDICT,PHASE12_PROPOSED_UPDATES,CRITICAL_ROTATION_PRIOR_RESULTS}.md`.
**No historical text is deleted anywhere.**
