# periodicity-conjecture-bridge

Research program on the 3x+1 Periodicity Conjecture using periodic approximation, 2-adic rigidity, symbolic repetition, and arithmetic height to exclude increasingly broad classes of aperiodic parity words.

## The ladder

```
Sturmian  p(n) = n+1
    ↓
counting classes  p(n) < 1.709511... n
    ↓
CS Rote  p(n) = 2n
    ↓
[next frontier]
```

This is a **milestone map of an exclusion program**, not a chain of nested sets — see `LADDER.md` for the precise reading and per-rung status.

## Headline result

For every complementary symmetric Rote sequence `v` (factor complexity exactly `2n`, strictly beyond the Dubickas counting threshold) whose associated Sturmian sequence has a quadratic-irrational slope with at least one **odd** partial quotient in its continued-fraction tail, `Φ(v) ∉ ℚ` — **proved**. The same conclusion holds, tested and unrefuted, for every all-even-tail slope checked, resting on one classical critical-exponent bound not yet re-derived in full generality. See `THEOREM_STATUS.md` for the complete, honest status map — nothing here is overclaimed past what is actually proved.

## Repository structure

```
LICENSE                Apache License 2.0 (covers this repo's code and analysis)
NOTICE                 scope of the license; the source paper keeps its own copyright
README.md              this file
LADDER.md              the exclusion-program milestone diagram, with per-rung status
THEOREM_STATUS.md       consolidated status map, every result across all phases
PRIOR_ART.md            index into the two adversarial prior-art searches
CITATION.cff            citation metadata

theorems/phase1/        Phase 1: abstraction of the source paper's bridge technique,
                         first computational evidence beyond Sturmian words
theorems/phase2/         Phase 2: theorem-conversion — proofs replacing computational
                         evidence wherever possible
theorems/phase3/         Phase 3: closes Phase 2's precise open lemma (weight-parity),
                         finds and resolves a genuine counterexample

scripts/phase{1,2,3}/    exact-arithmetic verification scripts, one directory per phase,
                         each runnable standalone (`python3 <script>.py` from its own
                         directory — no cross-phase import dependencies)
data/phase{1,2,3}/       saved script outputs, for the record

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
```

## Discipline notes

- Falsification-first throughout: every phase actively attacks its own prior claims before extending them. Two real bugs were found and fixed in-session (a reciprocal continued-fraction bug in Phase 1, a false-positive cycle detector in Phase 2/3) — both disclosed in `THEOREM_STATUS.md` and the relevant phase files, not silently corrected.
- No claim in this repository asserts progress on the full Lagarias Periodicity Conjecture. See `LADDER.md`'s closing section for the precise, structural reason no repetition-based method — however far this ladder is extended — can ever close the conjecture alone.
- This repository is an audit and proof record, not a manuscript. No paper is drafted here.

## License

Apache License 2.0 for this repository's code and written analysis. The foundation paper under `reference/` retains its own separate copyright — see `NOTICE`.
