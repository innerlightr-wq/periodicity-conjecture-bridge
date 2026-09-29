# TRANSFER_EFFICIENCY.md

## The reframing

Phase 2/3 organized the theory around **weight parity** (even `\Rightarrow` full-strength transfer; odd `\Rightarrow` halved). This phase's finding (`REQUIRED_EXPONENT.md`) shows parity is not the fundamental quantity — it is one mechanism controlling a more basic pair: the **transfer factor** `\tau\in\{1,\tfrac12\}` (root length multiplier `1/\tau$, i.e. `\ell` or `2\ell`) and the **transferred density** `\gamma_v` it forces.

> **Fundamental criterion.** The bridge closes at a witness whenever
> ```
> \tau \cdot r_u > \max(1, \gamma_v \log_2 3),
> ```
> where `(\tau,\gamma_v) = (1,\gamma_V)` [even weight] or `(\tfrac12, \tfrac12)` [odd weight] — **the odd-weight case's `\gamma_v` is not a free or worst-case quantity, it is forced to exactly `\tfrac12` by the `R=V\bar V` construction itself**, which is the single fact `REQUIRED_EXPONENT.md` isolates.

## Consequence: parity is a mechanism, not the organizing principle

The historical parity analysis (`theorems/phase2/ROTE_TRANSFER_THEOREM.md`, `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`) is **not erased** — it correctly identifies *which* of the two `(\tau,\gamma_v)` pairs applies at a given witness, and remains the mechanism by which `\tau` is determined. What this phase corrects is the *next* step: previously, the odd-weight case's required threshold was computed using the *generic, worst-case* `\max(1,\gamma\log_23)<\log_23` bound (as if `\gamma_v` were unconstrained), rather than using the *actual, forced* value `\gamma_v=\tfrac12`, whose threshold is the strictly smaller `1`. Once this is corrected, **both branches reduce to the same single requirement, `r_u>2`** (`REQUIRED_EXPONENT.md`):
- `\tau=1`: need `r_u>\log_23\approx1.585`; `r_u>2` overshoots by margin `\approx0.415`.
- `\tau=\tfrac12`: need `r_u>2\cdot1=2` exactly; `r_u>2+1/(A+1)` overshoots by margin `1/(A+1)`.

## Restated theory

> The bridge closes at any standard-word witness with `r_u>2` (a single, transfer-factor-independent threshold), **regardless of which weight-parity case applies** — parity only determines which `(\tau,\gamma_v)` pair is in effect, and in both cases the resulting required `r_u` threshold turns out to be `\le2`, so `r_u>2` (which Theorem 10.2 plus `INITIAL_EXPONENT_FORMULA.md` together guarantee unconditionally, with an explicit `A`-dependent margin) suffices for either mechanism.

This is the shortest correct statement of the theory and is the one used in `QUADRATIC_CS_ROTE_THEOREM.md` and `FINAL_PROOF_CHAIN.md`.
