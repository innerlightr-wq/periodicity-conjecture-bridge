**CHAIN AUDIT — THEOREM 2 SURVIVES; ONE HYPOTHESIS WAS MISSING FROM THE DISCREPANCY STEP AND IS NOW SUPPLIED**

# PHASE8_CHAIN_AUDIT.md

Independent audit of every link in Theorem 2 (`PHASE8_PROOF_OR_OBSTRUCTION.md` §5), run
adversarially against the chain rather than along it.

## 0. Method

The audit deliberately avoids the derivation it is auditing. `scripts/phase8/phase8_chain_audit.py`
uses **no BHZ formula and no Ostrowski digit machinery at all**: it builds the mechanical word
literally from certified rational brackets and then tests the *conclusion* — attained initial
powers, the XOR transfer, the exact integer height, the surplus — on the literal word. So a
sign error, an index shift or a wrong convention anywhere in the Ostrowski bookkeeping cannot
hide inside it.

Irrational slopes and intercepts are certified brackets. Every `floor`/`ceil` is either decided
by the bracket or raises `UndecidedError`; none is guessed. Bracket widths are `10^-17` to
`10^-41` against `N = 30 000` floors, i.e. `10^12` times tighter than needed.

## 1. Link-by-link verdict

| # | link | source | verdict |
|---|---|---|---|
| 1 | `ice(ω) ≥ 2 + δ(A_b)` for every `ω ∈ X_γ` | BHZ Prop. 5.1 + 5.2 | **HOLDS.** Priority confirmed; see §2 for the supremum-vs-attained issue. |
| 2 | attained witnesses `W_k^{r_k}`, `r_k ≥ 2 + δ`, `ell_k → ∞` | Phase 8 Thm 1 | **HOLDS**, and this is the step BHZ's *statement* does not give (§2). |
| 3 | root lengths `q_k`, `q_k − c_k q_{k-1}`, correctly indexed | BHZ Prop. 3.3 + F1 | **HOLDS** under `q_1 = a_1 + 1`; 562 literal checks (Phase 8 §B). |
| 4 | exact XOR transfer `L_v = L_u + 1` | `theorems/phase2/ROTE_TRANSFER_THEOREM.md` | **HOLDS.** 534/534 in this audit, on literal words, both conventions, both seeds. |
| 5 | odd branch density `γ_R = 1/2` exactly | `theorems/phase4/REQUIRED_EXPONENT.md` | **HOLDS.** 338/338 odd-branch witnesses, exactly `1/2`. |
| 6 | `D(R_k) = o(ell_k)` uniformly in the intercept | `theorems/phase5/ROTE_DISCREPANCY_AUDIT.md` | **HOLDS, but one hypothesis was missing** — see §3. |
| 7 | surplus `S_k → +∞` | Phase 8 §4 | **HOLDS.** 534/534 with `2^{L_v} > F(R)` as exact integers; `S/ell` bounded below. |
| 8 | `limsup S = +∞ ⟹ Φ(v) ∉ ℚ` | `theorems/phase2/PHASE1_FREEZE.md` | **HOLDS**, no symbolic hypothesis. |
| 9 | both mechanical conventions | §4 | **HOLDS.** |
| 10 | both seeds | §5 | **HOLDS.** |
| 11 | every shift `σ^j(v)` | §6 | **HOLDS**, and the justification is now one line instead of an appeal. |

## 2. Supremum of exponents versus an attained witness

This distinction is load-bearing and was not made explicitly before.

`ice(ω)` is defined (BHZ §2.2) as `limsup_n p_n` where `p_n` is the prefix power of `ω[0,n)` in
`ω`. Each `p_n = L_n/n` with `L_n = lcp(ω, ω[0,n)^∞)` **is** attained. But `ice(ω) ≥ 2 + δ` is a
statement about a `limsup`, so by itself it yields, for each `ε > 0`, infinitely many `n` with
`p_n > 2 + δ − ε` — **not** infinitely many `n` with `p_n ≥ 2 + δ`.

Consequences, kept apart:

- **From BHZ Prop. 5.1/5.2 as stated** (a `limsup` bound): take `ε = δ/2`. There are infinitely
  many `n` with an attained initial power of exponent `> 2 + δ/2`, and those `n → ∞`, so the root
  lengths grow automatically. **This is already sufficient for Theorem 2**, at half the margin.
  Nothing else is needed.
- **From Phase 8 Theorem 1** (and from BHZ's *proof* of Prop. 5.1, once the `y(k)`-attainment
  gap of audit finding F3 is repaired): for **every** `k ≥ 7` there is an attained witness of
  exponent `≥ 2 + δ(A_b)` with root length `≥ q_{k-4}`. This is a per-scale statement, strictly
  stronger than the `limsup` bound, and it is what makes the surplus bound uniform in `k` rather
  than only along an unspecified subsequence.

So Theorem 2 does not depend on the stronger form — but the stronger form is what Phase 8 proves,
and it is the honest description of what the repository now has.

## 3. The one real gap found: the discrepancy step is about `γ/2`, not `γ`

`theorems/phase5/ROTE_DISCREPANCY_AUDIT.md` reduces `|k_ell(V) − ell/2|` to the discrepancy of the
orbit `{i·(γ/2)}` against `[1/2,1)`, correctly: for the intercept-`ρ` lower mechanical word,
`k_i(u) = ⌊iγ+ρ⌋ − ⌊ρ⌋`, and `k_i mod 2 = 1` iff `{(iγ+ρ)/2} ∈ [1/2,1)`, so the relevant rotation
is by **`γ/2`** with starting phase `ρ/2`. It then applies `N·D*_N(β) = O(Σ_{i≤k} a_i)` and
concludes that "constants depend on the slope only through the partial-quotient bound `A`".

That last step needs a hypothesis the audit never states: **the partial quotients of `γ/2` must
also be bounded.** Bounded type is not preserved by arbitrary operations, so this cannot be
assumed. It is true, and cheap:

> **Lemma.** If `γ` has bounded partial quotients then so does `γ/2`, with a bound depending only
> on `A = sup_k A_k`.
>
> *Proof.* Bounded type is equivalent to `inf_{q≥1} q‖qγ‖ =: c > 0`, and `c ≥ 1/(A+2)`. For any
> `q ≥ 1`, `‖qγ‖ = ‖2·q(γ/2)‖ ≤ 2‖q(γ/2)‖`, hence `q‖q(γ/2)‖ ≥ q‖qγ‖/2 ≥ c/2 > 0`. So `γ/2` is
> badly approximable with constant `≥ c/2 ≥ 1/(2(A+2))`, and its partial quotients are bounded by
> `⌊2(A+2)⌋ + 1`. ∎

Checked numerically (`data/phase8/chain_audit_output.txt`): `sup` partial quotient of `γ/2` is
`4, 4, 6, 8, 10` for `γ = [0;\overline{A}]`, `A = 1..5`, and `2, 5, 3` for three mixed-digit
slopes — in every case well inside `2(A+2)+1`.

**Severity: low.** The conclusion `D(R_k) = O_{A}(\log ell_k)` is unchanged, only its proof is now
complete. Theorem 2 needs only `D = o(ell)`, and the audit measures `D(R)/\log_2 ell ∈ [0.30, 0.61]`
and `D(R)/ell → 0` across 534 witnesses with `ell` from 8 to 10 946 — two orders of magnitude of
slack. The lemma should be folded into `ROTE_DISCREPANCY_AUDIT.md`'s successor rather than left
implicit.

## 4. Both mechanical conventions

Two independent confirmations.

**Structural.** BHZ §2.1 define a Sturmian sequence of slope `α` as the itinerary of a point of
`[-α, 1-α]` under `R_α` (half-open `[·,·)`) **or** under `R̃_α` (half-open `(·,·]`); `X_α` is the
set of all of them, and BHZ §2.4's correspondence with `K_α` is a bijection onto `X_α`. The two
interval exchanges are exactly the lower and the upper mechanical families. So BHZ Prop. 5.1/5.2
("every `ω ∈ X_α`") and Theorem 1 quantify over both conventions with nothing to add. The source
paper's own Theorem 10.1 is likewise stated for "either mechanical word".

**Literal.** The audit builds both `u_i = ⌊(i+1)γ+ρ⌋ − ⌊iγ+ρ⌋` and
`u'_i = ⌈(i+1)γ+ρ⌉ − ⌈iγ+ρ⌉` from the same certified brackets and runs the whole chain on each.
Every link passes for both, at every intercept tested. The two conventions genuinely differ
where it matters (e.g. at `γ = [0;\overline1]`, `ρ = 0`: the lower word's witnesses run
`ell ∈ [13, 10946]` with `min r_u = 2.538`, the upper word's run `ell ∈ [8, 6765]` with
`min r_u = 2.500`) — so this is not a vacuous duplicate.

## 5. Both seeds

`v` is determined by `u` and the seed `v_0 ∈ {0,1}`; the two choices give `v` and `v̄`, and
`S(v̄) = S(v) = u`, so these are exactly the two CS Rote lifts. The audit runs the full chain at
both seeds for every case. `theorems/phase5/HOSTILE_REFEREE_REPORT.md`'s repaired justification
is the operative one: `c_W` is *not* complement-invariant, but every height bound used depends on
the root only through `(ell, k, D)`, and `D(V V̄) = D(V̄ V)`. Confirmed: the surplus differs
slightly between seeds (e.g. `min S = 13.9` versus `14.7` at one intercept) but is positive and
growing for both, in all 534 rows.

## 6. Shifts

Now a one-line consequence rather than an appeal. Source paper **Proposition 2.3**:
`Φ(σv) = T(Φ(v))`, with `T` the `3x+1` map on `ℤ₂`. `T` maps `ℚ ∩ ℤ₂` into itself
(`x/2` or `(3x+1)/2`), and so does `T^{-1}` (`2y` or `(2y−1)/3`). Hence

```
Phi(v) in Q  <=>  Phi(sigma^j v) in Q     for every j >= 0,
```

so `Φ(v) ∉ ℚ` transfers to every shift with no combinatorial input at all. This replaces
`theorems/phase6/BOUNDED_TYPE_THEOREM.md`'s citation of "source-paper Proposition 2.3,
CF-independent" with the actual argument.

## 7. Aggregate figures

```
4 slopes (gamma = [0;1bar], [0;2bar], [0;3bar], and a non-eventually-periodic slope with
  digits in {1,2} coded by the Fibonacci word)
x 3-4 intercepts each (rho = 0; rho = 1/2 rational; rho = {gamma} return; rho = keep-one)
x 2 mechanical conventions x 2 seeds
= 534 attained witnesses, ell from 8 to 10946

transfer L_v = L_u + 1 exactly              534 / 534
2^{L_v} > F(R) as exact integers            534 / 534
odd-branch density gamma_R = 1/2 exactly    338 / 338
witness exponent r_u >= 2 + delta(A_b)      534 / 534   (assertion, not observation)
D(R)/ell                                    0.200 at ell~8  ->  0.0004 at ell~8192
D(R)/log2(ell)                              in [0.302, 0.602] throughout
min S/ell                                   >= 0.0749 in every bucket
bracket-undecided floors                    0
```

## 8. Caveats on the audit itself

- The `ρ = keep-one` row coincides with `ρ = {γ}` when `A = 1`, because the keep-one digits
  `c_k = a_k − 1` are all `0` there; keep-one *is* the characteristic sequence at `A = 1`. The
  label is retained for uniformity but should not be read as a separate intercept at `A = 1`.
- Finite computation cannot certify a `limsup`. Every figure above is a lower-bound certificate
  against an asserted inequality, never evidence for one. Theorem 1 and Theorem 2 are proved in
  `PHASE8_PROOF_OR_OBSTRUCTION.md`; this file is an attempt to break them, which failed.
