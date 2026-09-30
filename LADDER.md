# LADDER.md — the exclusion-program milestones

The programme is organised along two coordinates, and it matters which one a given result reads.

```
                         lower ones-density
                  < beta            = beta            > beta
              +----------------+----------------+----------------+
  p(n)=n+1 |  covered (T1) |  foundation |  foundation |
 | |  Thm 10.1 |  Thm 10.1 |
              +----------------+----------------+----------------+
  p(n)=2n |  covered (T1) |  PHASE 11-13 |   open |
 |  + our 2nd |  Thm 16.5/17.2 | |
 |  proof (CS Rote)|  <- the frontier| |
              +----------------+----------------+----------------+
  higher |  covered (T1) |   open |   open |
              +----------------+----------------+----------------+
```

**Read the ladder by density, not by complexity.** The complexity axis is the one the *counting*
route operates on; the exclusion results in the literature read the **density** axis. Below
`β = ln2/ln3` the conclusion is available from Monks–Yazinski (2004) Thm 2.7(b) [refereed] whatever
the complexity. That single fact reclassifies most of this repository's earlier rungs.

## Rung-by-rung status

| Rung | Class | What it is | Where |
|---|---|---|---|
| 1 | Sturmian, `p(n)=n+1` | **KNOWN** — foundation paper Thm 10.1 (every slope, every intercept) | `reference/` |
| 2 | `liminf p(L)/L < 1.70951…` | **KNOWN** — Dubickas (2009) transported, foundation Cor. 9.3 | `reference/` |
| 3 | CS Rote, quadratic slopes | **PROVED here**, and **subsumed**: density exactly `1/2 < β`, so rung 1′ below covers the conclusion | `theorems/phase4/` |
| 3′ | CS Rote, every bounded-type slope, every intercept | **PROVED here** (Phase 8), and **subsumed** for the same reason. Contributes an independent second proof and effective height floors | `theorems/phase8/` |
| 1′ | **any** aperiodic word of lower ones-density `< β` | **KNOWN** — Monks–Yazinski (2004) Thm 2.7(b). This is what subsumes rungs 3 and 3′ | — |
| **4** | **critical density: `p(n)=2n`, lower ones-density exactly `β`** | **PROVED here (Phases 11–13)** — quadratic rotation, rational then algebraic offset. **No density or counting result reaches this class** | `theorems/phase13/` |
| 5 | lower ones-density `> β` | **open**, and treated as open here | — |
| 6 | every `s` with `p(L) ≤ 2L` | **open** — the foundation paper's own problem (4) | `reference/` |

## Coverage, stated against what is independently available

The densities reached by refereed work are those **below** `β`: Monks–Yazinski (2004) Thm 2.7(b). The
region **at or above** `β` is treated here as open, and the classes of rung 4 sit at exactly `β`, so
they lie outside the covered range. See
[`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

## Two things Open 4 of the technical note runs together

The note's "Open 4 — unbounded partial quotients" concerns CS Rote sequences over slopes with
unbounded partial quotients. Two statements must be kept apart:

- **the conclusion is not open.** CS Rote sequences have ones-density exactly `1/2` whatever the
  slope — a structural fact about the doubled root, independent of the partial quotients — so rung 1′
  already gives `Φ(v) ∉ ℚ` for all of them;
- **this repository's own bridge is unfinished there.** BHZ Thm 1.1 characterises the slopes carrying
  an intercept with `ice(ω) = 2` exactly, all of unbounded partial quotients, and there the
  odd-weight branch has margin exactly `0`.

So Open 4 asks for *an independent second proof of an available conclusion*, not for a new exclusion.
It is a methodological question. The live frontier is rung 4, and beyond it rungs 5 and 6.

## Relationship to the full Lagarias Periodicity Conjecture

**Not claimed to be resolved, in whole or in part.** Every rung is a statement about a
structurally-defined class. Rung 4's classes form a two-parameter family, of measure zero in
`{0,1}^ℕ`. Nothing here bears on divergent orbits of positive integers or on the Collatz conjecture.

## Cross-program scope limit

See [`docs/EOC_HANDOFF_CLOSED.md`](docs/EOC_HANDOFF_CLOSED.md): on integer-realizable zero-confined
orbits the surplus is bounded, so this mechanism does not yield divergence exclusion, and the CS Rote
classes are vacuous there (density `1/2` versus the sector's critical density `β`).
