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

## Where the programme currently stands

The ladder diagram, "Headline result", and repository-structure listing below describe the programme
**through Phase 6**, and are accurate for that range. Phases 7–13 are recorded in
the `theorems/`, `scripts/` and `data/` directories for phases `7`, `8`, `9`, `9b`, `10`, `10b`, `11`,
`11b`, `12` and `13`; the consolidated current chain is
[`theorems/phase13/CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md`](theorems/phase13/CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md),
and the strongest statement proved so far is in
[`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md`](theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md).

The rewrite of this README, `LADDER.md` and `THEOREM_STATUS.md` to cover Phases 7–13 is **drafted but
deliberately not applied**, pending my own review of the final theorem statements and of several
outstanding citation corrections; the exact replacement text is in
[`theorems/phase13/PROPOSED_PUBLICATION_CORRECTIONS.md`](theorems/phase13/PROPOSED_PUBLICATION_CORRECTIONS.md).
Until that is settled, treat the sections below as the Phase 1–6 record and the phase directories as
the current one. **Novelty remains formally unresolved throughout**, and no statement here should be
read as a claim on the full Periodicity Conjecture or on the Collatz conjecture.

## Technical Note

The current research program is consolidated in a peer-citable technical note:

**Elias De Jesús (2026), _Beyond Sturmian Words in the 3x+1 Periodicity Conjecture: A Periodic-Approximation and Arithmetic-Height Bridge_.** Zenodo. DOI: **[10.5281/zenodo.23045141](https://doi.org/10.5281/zenodo.23045141)**

This is a technical research note, not a claim to have solved the full Periodicity Conjecture. It consolidates the periodic-approximation / arithmetic-height bridge developed across Phases 1–7, through the bounded-type complementary-symmetric-Rote result (`theorems/phase6/BOUNDED_TYPE_THEOREM.md`). The full 3x+1 Periodicity Conjecture remains open, and complementary symmetric Rote sequences at arbitrary intercepts remain an open frontier (`theorems/phase7/`). See `technical-note/` for the manuscript source, preservation record, and statement-by-statement source-of-truth classification.

## The ladder

```
Sturmian  p(n) = n+1
    ↓
counting classes  p(n) < 1.709511... n
    ↓
bounded-type CS Rote  p(n) = 2n     (PROVED, Phase 6)
    ↓
general CS Rote / next frontier
```

This is a **milestone map of an exclusion program**, not a chain of nested sets — see `LADDER.md` for the precise reading and per-rung status.

## Headline result

For **every** complementary symmetric Rote sequence `v` (factor complexity exactly `2n`, strictly beyond the Dubickas counting threshold) whose associated Sturmian sequence is the intercept-`0` mechanical word of **any irrational slope with bounded partial quotients** (any seed, any shift of `v`), `Φ(v) ∉ ℚ` — **proved** (`theorems/phase6/BOUNDED_TYPE_THEOREM.md`). The proof rests on one clean structural fact discovered in Phase 4: the odd-weight transfer route's doubled root always has density exactly `1/2`, which drops the required Sturmian repetition exponent from an earlier, over-conservative `2\log_23\approx3.17` down to the true requirement, `2` — comfortably supplied, with an explicit margin, by a classical initial-critical-exponent bound (Berthé–Holton–Zamboni 2006). Phase 5 audited this chain end to end and found it survives (with one justification repaired); Phase 6 then reconstructed the same chain against genuinely non-periodic bounded-type slopes and found it needs only boundedness of partial quotients, not eventual periodicity — upgrading the theorem from a countable class (quadratic irrationals) to an uncountable one (bounded-type irrationals). One precise gap remains throughout (CS Rote sequences at *other* intercepts of the same slope) — see `THEOREM_STATUS.md` for the complete, honest status map. Nothing here is overclaimed past what is actually proved.

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

theorems/phase1/        Phase 1: abstraction of the source paper's bridge technique,
                         first computational evidence beyond Sturmian words
theorems/phase2/         Phase 2: theorem-conversion — proofs replacing computational
                         evidence wherever possible
theorems/phase3/         Phase 3: closes Phase 2's precise open lemma (weight-parity),
                         finds and resolves a genuine counterexample
theorems/phase4/         Phase 4: corrects Phase 3's threshold, proves the quadratic
                         CS Rote theorem in full generality via a structural density fact
theorems/phase5/         Phase 5: fresh adversarial audit of Phase 4, independently
                         re-derived end to end; theorem survives, one justification repaired
theorems/phase6/         Phase 6: reconstructs the audited chain against non-periodic
                         bounded-type slopes, upgrading quadratic -> bounded-partial-quotient

scripts/phase{1..6}/     exact-arithmetic verification scripts, one directory per phase,
                         each runnable standalone (`python3 <script>.py` from its own
                         directory — no cross-phase import dependencies)
data/phase{1..6}/        saved script outputs, for the record

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
```

## Discipline notes

- Falsification-first throughout: every phase actively attacks its own prior claims before extending them. Real bugs and wrong working hypotheses were found and fixed in-session — a reciprocal continued-fraction bug (Phase 1), a false-positive cycle detector (Phase 2/3), an over-conservative threshold promoted from too few examples that Phase 4 actively stress-tested, broke, and replaced with the correct general bound, a false justification for seed-independence caught and repaired by Phase 5's hostile referee pass, and a small-`k` boundary equality caught by Phase 6's non-periodic adversarial controls — all disclosed in `THEOREM_STATUS.md` and the relevant phase files, not silently corrected.
- No claim in this repository asserts progress on the full Lagarias Periodicity Conjecture. See `LADDER.md`'s closing section for the precise, structural reason no repetition-based method — however far this ladder is extended — can ever close the conjecture alone.
- This repository is an audit and proof record, not a manuscript. No paper is drafted here.
- Unrefereed preprints are labelled as such at every use, **including my own**; a foundation result of
  mine is additionally labelled a self-citation. No preprint is treated as settled.
- Specialist review has **not** taken place. See
  [`docs/INVITATION_TO_DOMAIN_EXPERTS.md`](docs/INVITATION_TO_DOMAIN_EXPERTS.md).

## License

Apache License 2.0 for this repository's code and written analysis. The foundation paper under `reference/` retains its own separate copyright — see `NOTICE`.
