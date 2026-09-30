# periodicity-conjecture-bridge

Research program on the 3x+1 Periodicity Conjecture using periodic approximation, 2-adic rigidity, symbolic repetition, and arithmetic height to exclude increasingly broad classes of aperiodic parity words.

> ### Specialists welcome
>
> I am an independent researcher whose professional background is outside mathematics, and **nothing
> in this repository has been refereed.** If you work in number theory, symbolic dynamics,
> combinatorics on words, Diophantine approximation, or `p`-adic dynamics, I would be glad of your
> eyes on it — to correct, strengthen, or extend any part of it, or to tell me it is already known.
>
> **→ [An invitation to number theorists and domain experts](docs/INVITATION_TO_DOMAIN_EXPERTS.md)**,
> with a concrete list of review and extension targets.
>
> See also **[what these conclusions depend on](docs/DEPENDENCE_ON_PRIOR_RESULTS.md)** — the external
> results relied on, their refereeing status, and the ones deliberately not relied on.

## Technical Note

The programme is consolidated in a citable technical note:

**Elias De Jesús (2026), _Beyond Sturmian Words in the 3x+1 Periodicity Conjecture: A
Periodic-Approximation and Arithmetic-Height Bridge_.** Zenodo, concept DOI
`10.5281/zenodo.23045140`, CC BY 4.0. **Preprint; not refereed.**

- **Deposited:** Revision 3, DOI **[10.5281/zenodo.23068563](https://doi.org/10.5281/zenodo.23068563)**,
  34 pp, byte-identical to `technical-note/note_rev3.pdf`.
- **Prepared, not deposited:** Revision 4, `technical-note/note_rev4.pdf` (39 pp) with a standalone
  correction notice. It corrects Revision 3 in four places — the deposit statement, "draft" labelling,
  the framing of one open problem, and the addition of explicit constants — **without altering any
  mathematical statement**. See [`RELEASE_MANIFEST.md`](RELEASE_MANIFEST.md) and
  [`theorems/phase14/ZENODO_RELEASE_RECONCILIATION.md`](theorems/phase14/ZENODO_RELEASE_RECONCILIATION.md).
- Record `10.5281/zenodo.23068326` duplicates Revision 2 byte for byte; cite Revision 2 as
  `10.5281/zenodo.23061396`.

The foundation paper this programme builds on is **doi:10.5281/zenodo.23019799** — also a preprint,
also not refereed, and **by the same author**: a self-citation, treated with the same caution as any
other preprint.

## Headline result

> Let `α ∈ (0,1)` be a quadratic irrational, `β = ln2/ln3`, and
> `s_n = 1 ⟺ {nα+ρ} ∈ [u, u+β) (mod 1)`. If the offset `ρ−u` is **algebraic** — `ρ` and `u` themselves
> unrestricted, so both may be transcendental — then `s` is aperiodic, has lower ones-density exactly
> `β` and factor complexity `2n`, and **`Φ(s) ∉ ℚ`**.

`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md`; manuscript Revision 4 Theorem 17.2 and
Corollary 17.3. **New readers: start with [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md).**

**Why this and not the earlier headline.** Through Phase 8 this README claimed a
complementary-symmetric-Rote theorem as the headline. That theorem is true, but its *conclusion* was
already available: CS Rote sequences have ones-density exactly `1/2`, and Monks–Yazinski (2004)
Theorem 2.7(b) excludes every aperiodic word of lower ones-density below `β`, whatever its complexity.
It crosses the **counting** frontier, not the density one. What this repository contributes there is
an independent second proof and effective height bounds. Lower ones-density exactly `β` is the one
place no density criterion reaches, and that is where the headline above sits.

**What is proved, checked, and open** — kept apart deliberately:

| | |
|---|---|
| **already implied by prior results** | every CS Rote rung, and Thue–Morse (all at density `1/2 < β`) |
| **independent effective proofs + quantitative refinements** | the same rungs, plus explicit height floors a density argument cannot give |
| **proved here and not implied** | the critical-density family above |
| **certified finite computations** | `H ≥ 2^462, …, 2^15998` for the named word — exact integer comparisons, no analytic input |
| **explicit constants** | `S ≥ (L−ℓ) − 24.207846·log₂ℓ − 35.869175`, and `H ≥ 2^{f(M)}` with `f` written down, positive for `M ≥ 1.78·10^18` — beyond computation, and not a computational claim |
| **unresolved novelty** | formal. No literature pass located a covering result; absence of a hit is not proof of absence |
| **open extensions** | transcendental offset; density `> β`; all `s` with `p(L) ≤ 2L`; transcendence |

**Scope.** Nothing here bears on divergent orbits of positive integers, on the Collatz conjecture, or
on the Periodicity Conjecture in general.

## Acknowledgement and dependency

López–Stoll's work on density and the 3x+1 conjugacy map helped guide this programme toward the critical density `β = ln2/ln3`. We acknowledge that influence. The results presented here are established through the independent arguments given in this repository and do not require their proposed upper-density exclusion.

We have neither established nor disproved their Theorem 1, and no argument here invokes it. See
[`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

## The ladder

See [`LADDER.md`](LADDER.md). The programme is organised on **two** coordinates — lower ones-density
and factor complexity — and the exclusion results in the literature read the density one. The live
frontier is density exactly `β` at complexity `2n`.

## Cross-program scope limit

**EOC handoff audit (2026-09-29): the periodic-approximation surplus route is bounded on
integer-realizable zero-confined orbits, so this mechanism does not currently yield divergence
exclusion.** On such an orbit the surplus equals `log₂ h_eff − log₂ oddpart(m_n − m₀)` and is
capped by `log₂ m₀`, making the criterion's `limsup S = +∞` hypothesis unsatisfiable; and the
headline bounded-type CS Rote class is vacuous there, since its load-bearing one-density `1/2`
is incompatible with the sector's critical density `β ≈ 0.63093`. No theorem in this repository
is affected. The qualitative closure was already on record in both programmes; the audit adds
the exact identity, the quantified obstruction and certified verification. See
[`docs/EOC_HANDOFF_CLOSED.md`](docs/EOC_HANDOFF_CLOSED.md), and the companion note
[`notes/PERIODICITY_HANDOFF_ROUTE_CLOSED.md`](https://github.com/innerlightr-wq/eoc-divergence/blob/main/notes/PERIODICITY_HANDOFF_ROUTE_CLOSED.md)
in [`innerlightr-wq/eoc-divergence`](https://github.com/innerlightr-wq/eoc-divergence), whose
[`notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md`](https://github.com/innerlightr-wq/eoc-divergence/blob/main/notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md)
indexes all three closed pointwise routes. **This repository should not be cited as a path to
the Collatz conjecture under the presently proved EOC constraints** — see
[`docs/EOC_HANDOFF_CLOSED.md`](docs/EOC_HANDOFF_CLOSED.md) §7b.

## Repository structure

```
LICENSE                Apache License 2.0 (covers this repo's code and analysis)
NOTICE                 scope of the license; the source paper keeps its own copyright
README.md              this file
LADDER.md              the exclusion-program milestone diagram, with per-rung status
THEOREM_STATUS.md       consolidated status map, every result across all phases
PRIOR_ART.md            index into the two adversarial prior-art searches
docs/                   INVITATION_TO_DOMAIN_EXPERTS.md   invitation for specialist review
                        DEPENDENCE_ON_PRIOR_RESULTS.md    what the conclusions rest on
                        EOC_HANDOFF_CLOSED.md             cross-program scope limit (EOC audit)
CITATION.cff            citation metadata

theorems/phase{1..8}/   the complementary-symmetric-Rote chain (proved; conclusion
                        already implied by Monks-Yazinski -- see THEOREM_STATUS.md)
theorems/phase9b/       Thue-Morse, independently proved and subsumed
theorems/phase10/       the (density, complexity) coverage map
theorems/phase11{,b}/   the named critical-density word; the Baker repair
theorems/phase12/       quadratic slope, rational offset
theorems/phase13/       quadratic slope, ALGEBRAIC offset; prior-result coverage
theorems/phase14/       Zenodo reconciliation; explicit discrepancy and height constants

scripts/phase{1..14}/   exact-arithmetic verification scripts, one directory per phase
data/phase{1..14}/      saved script outputs, for the record

reference/               the foundation paper this program audits and builds on
                         (separately copyrighted — see NOTICE)
```

## Running the verification scripts

Every script uses exact integer/`Fraction` arithmetic for every pass/fail decision — floating point, where it appears, is display-only and never decides a result. No external dependencies beyond the Python standard library.

```bash
cd scripts/phase1 && python3 bridge_toolkit.py        # sanity self-check
cd scripts/phase2 && python3 verify_rote_transfer.py   # exact transfer theorem, 44 cases
cd scripts/phase3 && python3 automaton_search.py        # exhaustive weight-parity automaton
cd scripts/phase3 && python3 counterexample_and_recovery.py  # the found counterexample + its resolution
cd scripts/phase4 && python3 verify_phase4.py            # consolidated Phase 4 verification (13 checks)
cd scripts/phase5 && python3 independent_transfer_check.py   # 114,680-case independent transfer re-check
cd scripts/phase6 && python3 full_pipeline_nonperiodic.py    # full chain on 4 non-periodic bounded-type slopes
cd scripts/phase12 && python3 independent_audit.py       # Theorem rebuilt from definitions, all 5 height floors
cd scripts/phase12 && python3 general_quadratic.py       # quadratic slope x rational offset, 50 end-to-end rows
cd scripts/phase13 && python3 algebraic_intercept.py     # ALGEBRAIC offset, field degrees 2, 4, 6
cd scripts/phase13 && python3 ridout_exponent.py         # the Ridout exponent (a measurement, not a theorem)
cd scripts/phase14 && python3 explicit_constants.py      # C, C_0, f(M) and the certified threshold
```

Phase 13 adds exact arithmetic in a general number field `ℚ(θ)`: an element is zero exactly when its
coefficient vector is, and for a non-zero element the characteristic polynomial gives an a priori
separation bound, so a high-precision evaluation decides every sign with certainty. Comparisons
against the transcendental `β` use a certified 300-digit bracket that either decides or raises.

## Discipline notes

- Falsification-first throughout: every phase actively attacks its own prior claims before extending them. Real bugs and wrong working hypotheses were found and fixed in-session — a reciprocal continued-fraction bug (Phase 1), a false-positive cycle detector (Phase 2/3), an over-conservative threshold promoted from too few examples that Phase 4 actively stress-tested, broke, and replaced with the correct general bound, a false justification for seed-independence caught and repaired by Phase 5's hostile referee pass, and a small-`k` boundary equality caught by Phase 6's non-periodic adversarial controls — all disclosed in `THEOREM_STATUS.md` and the relevant phase files, not silently corrected.
- No claim here asserts progress on the full Lagarias Periodicity Conjecture. An earlier version of
  this note claimed a *structural* reason why no repetition-based method could ever reach it, arguing
  from the Thue–Morse word's lack of a square prefix. **That claim was false and is withdrawn**: the
  method needs approximants whose 2-adic agreement outruns their height, not a square, and the
  Thue–Morse substitution supplies them. What remains true is weaker — the classes reached so far are
  parametrised families of measure zero, and no mechanism here is known to reach an arbitrary
  aperiodic word.
- This repository is an audit and proof record. The technical note drafted from it lives in
  `technical-note/`; the repository is the source of truth and the note follows it, never the reverse.
- Unrefereed preprints are labelled as such at every use, **including my own**; a foundation result of
  mine is additionally labelled a self-citation. No preprint is treated as settled.
- Specialist review has **not** taken place. See
  [`docs/INVITATION_TO_DOMAIN_EXPERTS.md`](docs/INVITATION_TO_DOMAIN_EXPERTS.md).

## License

Apache License 2.0 for this repository's code and written analysis. The foundation paper under `reference/` retains its own separate copyright — see `NOTICE`.
