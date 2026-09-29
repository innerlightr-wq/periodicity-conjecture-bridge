# INTERCEPT_STATE_MODEL.md

## The admissibility rule itself is finite-state

`(c_k)$'s local constraint — "if `c_k=a_k` then `c_{k-1}=0`" — depends only on `(c_{k-1}\overset{?}{=}0)` (one bit) and `a_k` (bounded, `\le A`). This part is genuinely finite (state space `\{c_{k-1}=0\}\times\{1,\ldots,A\}`), directly analogous to `theorems/phase3`'s weight-parity automaton.

## But `x'(k),y(k)` are not finite-state in the raw sense

Both depend on `\sum_{j\le k}(a_j-c_j)q_{j-1}` normalized by `q_k` (or `q_k-c_kq_{k-1}`) — a **cumulative** quantity, not expressible from a bounded window of recent digits alone, because `q_{j-1}/q_k$ decays but never vanishes uniformly (older terms contribute exponentially less, but the normalization itself depends on the whole history multiplicatively).

## A genuine finite-*extension* description does exist

Track the state as `\big(c_{k-1}\overset{?}{=}0,\ z_k:=q_{k-1}/q_k\big)$, `z_k\in(0,1)` a **continuous** parameter evolving by the Möbius-type recursion `z_{k+1}=1/(a_{k+1}+z_k)` (standard CF recursion, `a_{k+1}$ from a bounded alphabet). This is **not finite** (the state space is a bounded but continuous interval, not a finite set) — but the *transition rule* is a finite family of Möbius maps (one per value of `a_{k+1}\in\{1,\ldots,A\}`, exactly as `theorems/phase4/SPECTRAL_BRIDGE.md`'s transfer-matrix picture), and the running sums `\sum(a_j-c_j)q_{j-1}/q_k` can be tracked *incrementally* via `S_{k+1}=(S_k+(a_{k+1}-c_{k+1}))\cdot z_{k+1}` (a linear update in the *normalized* coordinate, exact and finite-dimensional per step even though `z_k` ranges continuously).

## Verdict

**No finite-state (finite-alphabet) description of the exact `x'(k),y(k)` values exists** — the continuous `z_k$ (equivalently, the slope's own convergent-ratio dynamics) is essential and was not forced into a finite reduction. What *is* finite is the **transition rule** driving `z_k` and the admissibility bit — a finite iterated-function-system over a continuous state, the same structure underlying the classical three-distance theorem and the `\text{term2}` bound's own derivation. This is recorded as the honest answer (task explicitly permits: "do not force finiteness if continuous ratio data are essential").
