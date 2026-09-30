# THEOREM_STATUS.md — consolidated status map

One line per load-bearing result, with its provenance. Full statements and proofs are in
`theorems/phaseN/`. Four categories are kept apart throughout, and the table's "status" column says
which applies:

- **KNOWN** — a published result, cited not re-derived;
- **ALREADY IMPLIED** — proved here, but the conclusion follows from a published result; what this
  repository adds is an independent second proof and/or quantitative content;
- **PROVED HERE, NOT IMPLIED** — proved here, and no located published result reaches it;
- **CERTIFIED** — an exact finite computation, not an asymptotic statement;
- **OPEN** / **WITHDRAWN**.

**Novelty is formally unresolved throughout.** Absence of a hit in a literature pass is evidence, not
proof, of absence. Unrefereed preprints are labelled at every use, including the author's own.

## Headline

> **Critical-density rotation codings.** Let `α ∈ (0,1)` be a quadratic irrational, `β = ln2/ln3`,
> and `s_n = 1 ⟺ {nα+ρ} ∈ [u, u+β) (mod 1)`. If the offset `ρ−u` is **algebraic** — `ρ` and `u`
> themselves unrestricted — then `s` is aperiodic, has lower ones-density exactly `β` and factor
> complexity `2n`, and **`Φ(s) ∉ ℚ`**.
> (`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md`; manuscript Revision 4 Theorem 17.2 and Corollary 17.3 (Revision 3: 18.2 / 18.3).)

**Why this rung and not the earlier ones.** Every complementary-symmetric-Rote result of Phases 2–9
sits at ones-density exactly `1/2 < β` and is therefore **ALREADY IMPLIED** by Monks–Yazinski (2004)
Thm 2.7(b). Their proofs stand; their novelty claims do not. Lower ones-density exactly `β` is the one
place no density criterion reaches, and it is where the headline sits.

**Effectivity.** Explicit finite height floors up to `H ≥ 2^15998` are exact integer facts using no
analytic input. The asymptotic statement is effective and, since Phase 14, numerically written down
for the named example: `H ≥ 2^{f(M)}` with `f` explicit and `f(M) > 0` for `M ≥ 1.78·10^18`
(`theorems/phase14/EXPLICIT_HEIGHT_BOUND.md`). That threshold is beyond computation and is not a
computational claim.

**Scope.** Nothing here bears on divergent orbits of positive integers, on the Collatz conjecture, or
on the Periodicity Conjecture in general, which quantifies over an uncountable family of which these
classes are a measure-zero subset.

## Sources relied on

| Result | Status |
|---|---|
| `Φ` a 2-adic isometry, `Φ∘S = T∘Φ` | KNOWN — Bernstein–Lagarias (1996); foundation Prop. 2.2 |
| `Φ(W^∞) = c_W/(2^ℓ−3^k)` | KNOWN — foundation Prop. 4.1 (re-derived and checked mod `2^60` in Phase 12) |
| aperiodic, lower ones-density `< β` ⟹ `Φ(v) ∉ ℚ` | KNOWN — Monks–Yazinski (2004) Thm 2.7(b) [refereed] |
| `liminf p(L)/L < 1.70951…` ⟹ `Φ(s) ∉ ℚ` | KNOWN — Dubickas (2009) transported; foundation Cor. 9.3 |
| all Sturmian ⟹ `Φ(s) ∉ ℚ` | KNOWN — foundation Thm 10.1 / Cor. 10.5 |
| `\|β₁logα₁+β₂logα₂\| > Ce^{−(log B)^κ}`, algebraic coefficients | KNOWN — Baker, Mathematika 14 (1967), III, Thm 2; Part I Thm 1.1 for uniformity over degree |
| the same with an explicit constant | KNOWN — Waldschmidt, Thm 10.1 |
| `N D_N ≤ 3 + (1/log φ + K/log(K+1))log N` | KNOWN — Kuipers–Niederreiter, Ch. 2 Thm 3.4 |
| two-interval rotation coding has `p(n)=2n` iff endpoint `∉ ℤα+ℤ` | KNOWN — Rote (1994); Berstel–Vuillon (2001) |
| the hitting-time mechanism | KNOWN — **the foundation paper's own §12 problem (1)**, not original here |
| foundation paper | **preprint, not refereed, by the present author — a self-citation.** doi:10.5281/zenodo.23019799 |

## Proved in this repository

| Result | Status | File |
|---|---|---|
| Abstract criterion: `limsup S = +∞ ⟹ Φ(s) ∉ ℚ`, Sturmian-free, all fine print discharged | PROVED | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` |
| `c_W ≤ ℓ·3^{⌈D⌉}·max(2^ℓ,3^k)` | PROVED | `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md` |
| Discrepancy bound uniform in the intercept | PROVED | Phase 10 Lemma D |
| CS Rote, every bounded-type slope, every intercept, both seeds, every shift | **ALREADY IMPLIED** (density `1/2`); PROVED here as an independent second proof | `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` |
| `Φ(Thue–Morse) ∉ ℚ` | **ALREADY IMPLIED** (density `1/2`); PROVED here independently, and **without any square** | `theorems/phase9b/` |
| Coverage is by density, not complexity; the residual is density `≥ β` | ESTABLISHED | `theorems/phase10/` |
| Mismatch set = two arcs, under `\|δ\| ≤ min(β,1−β)` | PROVED (hypothesis was unstated before Phase 11B) | `theorems/phase11b/` |
| `L(ℓ) − ℓ = m*(ℓ)`, the first hitting time | PROVED; the *idea* is the foundation paper's | `theorems/phase11/` |
| `A_m > β − 1/2 > 0` always — non-vanishing with no case analysis | PROVED | `theorems/phase12/` |
| `‖mα+ρ‖ ≥ c_L m^{−D²}` for algebraic `ρ`, by **Liouville alone** | PROVED | `theorems/phase13/` |
| Exact `0`-boundary hits classified: `ρ ∈ ℤα+ℤ`, unique index, any value | PROVED | `theorems/phase13/` |
| **`Φ(s) ∉ ℚ`, quadratic slope, rational offset** | **PROVED HERE, NOT IMPLIED** | `theorems/phase12/QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md` |
| **`Φ(s) ∉ ℚ`, quadratic slope, algebraic offset; and `[u,u+β)` whenever `ρ−u` algebraic** | **PROVED HERE, NOT IMPLIED** | `theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md` |
| `C = 24.207846`, `C₀ = 35.869175` in `S ≥ (L−ℓ) − C log₂ℓ − C₀` | **PROVED, numerically explicit** | `theorems/phase14/EXPLICIT_DISCREPANCY_CONSTANTS.md` |
| `H ≥ 2^{f(M)}` with `f` explicit; `f(M) > 0` for `M ≥ 1.78·10^18` | **PROVED, numerically explicit** | `theorems/phase14/EXPLICIT_HEIGHT_BOUND.md`; manuscript §19, Thm 19.5 |

## Certified finite computations

| Result | Status |
|---|---|
| `H ≥ 2^462, 2^838, 2^872, 2^2469, 2^15998` for the named word | CERTIFIED — exact integer comparisons `2^L > F(W)·2^S`, no analytic input |
| `2^140 … 2^8069` over 10 `(α,ρ)` with `ρ ∈ ℚ`; `2^67 … 2^598` over 7 with `ρ` algebraic, `D = 2,4,6` | CERTIFIED |

## Withdrawn

| Claim | Status |
|---|---|
| `c_m ≥ C₂m^{−κ}` (a polynomial logarithmic-form bound) | **WITHDRAWN** — the source gives `Ce^{−(log B)^κ}`; a polynomial bound is Baker's own unproved conjecture `κ=1` |
| "Thue–Morse makes every repetition-based method structurally inapplicable" | **WITHDRAWN** — false; the substitution supplies approximants with no square |
| CS Rote as crossing a frontier | **WITHDRAWN** — it crosses the *counting* frontier only |
| "the subspace-theorem route is far too weak" | **WITHDRAWN** — the Ridout exponent exceeds the threshold at 7 of 20 convergents; infinitude is open |

## Open, precisely stated

1. **Transcendental offset `ρ−u`** — the only remaining obstruction on the offset axis. Both boundary
   bounds fail: Liouville needs algebraicity, and the `β`-distance stops being a logarithmic form in
   algebraic data.
2. **Uniformly numerical constants for the family** — `C`, `C₀` and `c₁` are uniform; `C_h` and `c_L`
   are not. Per-`(α,ρ)` they are a finite computation. Not claimed for the family.
3. **Transcendence** — is `m*(ℓ)/ℓ > 1+ε` for infinitely many convergents? If so Ridout upgrades
   irrationality to transcendence.
4. **Density `> β`** — treated as open here; see the acknowledgement below.
5. **All `s` with `p(L) ≤ 2L`** — the foundation paper's problem (4). Our classes are one
   two-parameter family inside it.
6. **CS Rote over unbounded-partial-quotient slopes** — *an unfinished second proof, not an open
   conclusion*: those words have density `1/2`, so Monks–Yazinski already covers them. What fails is
   this repository's own criterion, whose odd-weight branch has margin exactly `0` at an
   `ice(ω) = 2` intercept.

## Acknowledgement and dependency

López–Stoll's work on density and the 3x+1 conjugacy map helped guide this programme toward the critical density `β = ln2/ln3`. We acknowledge that influence. The results presented here are established through the independent arguments given in this repository and do not require their proposed upper-density exclusion.

We have neither established nor disproved their Theorem 1, and no argument here invokes it.
See [`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

## Published record

**Deposited:** Revision 3, doi:10.5281/zenodo.23068563 (concept 10.5281/zenodo.23045140), CC BY 4.0,
34 pp, byte-identical to `technical-note/note_rev3.pdf`.

**Prepared, not deposited:** Revision 4 — `technical-note/note_rev4.{tex,pdf}` (39 pp) with
`correction_notice_rev4.{tex,pdf}`, correcting Revision 3 in four places without altering any
mathematical statement. Proposed record text: `technical-note/ZENODO_DESCRIPTION_REV4.md`. Release
manifest: [`RELEASE_MANIFEST.md`](RELEASE_MANIFEST.md); reconciliation:
[`theorems/phase14/ZENODO_RELEASE_RECONCILIATION.md`](theorems/phase14/ZENODO_RELEASE_RECONCILIATION.md).
Record 10.5281/zenodo.23068326 duplicates Revision 2 byte for byte; cite Revision 2 as
10.5281/zenodo.23061396.

**For reviewers:** [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md).
