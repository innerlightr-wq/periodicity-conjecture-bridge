**TARGET AND DEPENDENCIES — IDENTITY RE-DERIVED, ATTAINMENT ROUTING CLOSED, ONE WEIGHT-LAW CORRECTION**

# PHASE9_TARGET_AND_DEPENDENCIES.md

Phase 9 works from `phase8-general-intercept` at HEAD **`3b321c0`** (clean; Revision 2 release
artifacts byte-identical — `note_rev2.pdf` `8daf1979…`, `correction_notice.pdf` `0c93457c…`,
`note.pdf` `b7054cee…`). Isolated branch `phase9-unbounded-type`; nothing pushed.

## 0. Symbols, fixed once

| symbol | definition |
|---|---|
| `γ` | irrational slope in `(0,1)`, `γ = [0; A_1, A_2, …]`. **No hypothesis on the `A_k`.** |
| `a_k` | BHZ digits: `a_1 = A_1 − 1`, `a_k = A_k` for `k ≥ 2` (BHZ Prop. 2.7) |
| `p_k, q_k` | `p_0=0, q_0=1`, `p_1=1, q_1=a_1+1`, `p_k = a_kp_{k-1}+p_{k-2}`, `q_k = a_kq_{k-1}+q_{k-2}` (`k≥2`); so `p_{-1}=1, q_{-1}=0` |
| `c_k` | Ostrowski digits of the intercept; admissible iff `0 ≤ c_k ≤ a_k`, `a_k ≥ 1` (`k≥2`), and `c_k = a_k ⇒ c_{k-1} = 0` |
| `d_k` | `:= a_k − c_k ∈ [0, a_k]` |
| `λ_k` | `:= q_{k-1}/q_k`, `λ_0 = 0` |
| `S_k, t_k` | `S_k := Σ_{j≤k} d_j q_{j-1}`, `t_k := S_k/q_k`, `t_0 = 0` |
| `m_k` | `:= t_{k-1} + d_k`; so `t_k = λ_k m_k` and `m_{k+1} = λ_k m_k + d_{k+1}` |
| `x'(k)` | `:= S_{k+1}/q_k = m_{k+1}` |
| `x(k)` | `:= 1_{a_{k+2}=c_{k+2}} + x'(k)` |
| `y(k)` | `:= 1 + S_k/(q_k − c_k q_{k-1}) = 1 + m_k/(λ_{k-1}+d_k)` |
| `ℓ_k` | `:= q_k − c_k q_{k-1} = d_k q_{k-1} + q_{k-2}` (the `y`-root length) |
| `E_k` | `:= y(k) − 2` |
| `ℓ(k,d), w(k,d)` | `:= d q_{k-1} + q_{k-2}` and `:= d p_{k-1} + p_{k-2}`, for an **effective digit** `d ∈ {1,…,a_k}` |
| `g(γ')` | `:= max(1, γ' log₂3) + γ'(1−γ') log₂3` — the **unconditional** even-branch threshold (§4) |

## 1. The unified witness family

`ℓ(k,d)` runs over the intermediate (semistandard) denominators between `q_{k-1}` and `q_k`, and
two of them are BHZ-guaranteed attained power roots:

| `d` | length | exponent | attained? |
|---|---|---|---|
| `a_k` | `q_k` | `x(k)` | **always** (BHZ Prop. 3.3, converse, first case) |
| `d_k` | `ℓ_k = q_k − c_kq_{k-1}` | `y(k)` | **iff `0 < c_k < a_k`** (second case) |
| other | `ℓ(k,d)` | measured literally | **no guarantee** |

## 2. The driver identity, re-derived

> **Identity.** For every `k ≥ 2`, every admissible `(c_k)`, and every irrational `γ`:
> ```
> ell_k = q_{k-1}(lam_{k-1} + d_k),     E_k = lam_{k-1}(m_{k-1} - 1)/(lam_{k-1} + d_k),
> so   ell_k * E_k  =  q_{k-1} lam_{k-1} (m_{k-1} - 1)  =  q_{k-2} (m_{k-1} - 1).
> ```

*Proof.* `q_k − c_kq_{k-1} = (q_k − a_kq_{k-1}) + d_kq_{k-1} = q_{k-2} + d_kq_{k-1}`, which needs
the recursion at index `k`, hence **`k ≥ 2`**; dividing by `q_{k-1}` gives the first display.
`S_k/q_{k-1} = S_{k-1}/q_{k-1} + d_k = t_{k-1} + d_k = m_k`, so `y(k) = 1 + m_k/(λ_{k-1}+d_k)`, and
`m_k − λ_{k-1} − d_k = t_{k-1} − λ_{k-1} = λ_{k-1}(m_{k-1}−1)`. ∎

**Valid index range: `k ≥ 2`.** At `k = 1` it fails (`q_1 − c_1q_0 = a_1+1−c_1 = d_1+1`, not `d_1`),
because `q_1 = a_1 + 1` is the boundary case of BHZ's normalisation. Phase 9 uses `k ≥ 3`
throughout.

**Sign.** `y(k) > 2 ⟺ m_{k-1} > 1`, and `m_{k-1} = t_{k-2} + d_{k-1} ≥ d_{k-1}`, so
**`d_{k-1} ≥ 1` already gives `y(k) ≥ 2`**.

**Verified:** 131 888 `(slope, admissible digit string, k)` instances, exact `Fraction`, no
exception (`scripts/phase9/phase9_witness_family.py`, A1).

## 3. The attainment routing — the identity is never applied to an unrealised length

`y(k)` is an attained power only when `0 < c_k < a_k`. The other cases route through
Corollary 3.5's observations, and in each the identity's `ℓ_k` is exactly the realised root length:

| routing | condition | attained witness | its root length | relation to `ℓ_k` |
|---|---|---|---|---|
| **R1** | `0 < c_k < a_k` | `y(k)` itself | `q_k − c_kq_{k-1}` | `= ℓ_k` |
| **R2** | `c_k = a_k` (so `d_k = 0`) | `x(k−2) = y(k)` | `q_{k-2}` | `ℓ_k = q_k − a_kq_{k-1} = q_{k-2}`, **equal** |
| **R3** | `c_k = 0`, `c_{k+1} < a_{k+1}` | `x(k) ≥ y(k)` | `q_k` | `ℓ_k = q_k`, **equal**, and the exponent is `≥` |
| **R4** | `c_k = 0`, `c_{k+1} = a_{k+1}` | `x(k−1) = y(k+1) > y(k)` | `q_{k-1}` | `= ℓ_{k+1}`, i.e. the identity **at index `k+1`** |

**Verified**, with the length equalities and the dominance inequalities asserted separately:
R1 41 397, R2 14 113, R3 61 137, R4 15 241 instances, no exception. So the Phase 8 identity is
safe to use as a statement about *realised* witnesses, including the branch where `y(k)` is
unavailable — which Phase 8 asserted but did not check.

## 4. The surplus, compared against **every** penalty — no `ℓ_kE_k → ∞` shortcut

Exact definitions (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`): for a root `R`,
`δ_R = 2^{|R|} − 3^{|R|_1}`, `c_R = Σ_{i<|R|,R_i=1} 3^{|R|_1−k_{i+1}(R)}2^i`, `F(R) = |δ_R| + c_R`,
and `S = lcp(v,R^∞) − log₂F(R)`; `limsup S = +∞ ⟹ Φ(v) ∉ ℚ`.

**Odd branch** (`|W|_1` odd, `R = VV̄`, `|R| = 2ℓ`, `γ_R = 1/2` exactly). `log₂|δ_R| = 2ℓ + O(1)` and
`log₂c_R ≤ log₂(2ℓ) + ⌈D(R)⌉log₂3 + 2ℓ`, so with `L_v = L_u + 1`:

```
S  =  ell*E + 1 - [ log2 F(R) - 2 ell ]   >=   ell_k E_k + 1 - ceil(D(R_k)) log2 3 - log2(2 ell_k).
```

Both penalties are explicit and **neither is negligible a priori**:

- `log₂(2ℓ_k)`: harmless — `ℓ_k ≈ q_{k-1}` and `q_{k-2}` is a *product* of partial quotients while
  `log₂q_{k-1}` is a *sum* of their logarithms.
- `⌈D(R_k)⌉log₂3`: **the binding one.** The unconditional combinatorial cap
  `D(R) ≤ γ_R(1−γ_R)·2ℓ = ℓ/2` gives a penalty `≈ 0.79ℓ`, which swamps `ℓ_kE_k` whenever
  `E_k < 0.79` — so at `ice = 2` the cap is useless and a genuine discrepancy estimate is
  required. That estimate is where a hypothesis on `γ` enters, via the Ostrowski/three-distance
  bound for the rotation by `γ/2` (`theorems/phase8/PHASE8_CHAIN_AUDIT.md` §3).

**Therefore: `ℓ_kE_k → ∞` is necessary, not sufficient.** Phase 9's sufficient growth condition
for the odd branch is

```
(H)   q_{k-2}(m_{k-1} - 1)  >  ceil(D(R_k)) log2 3 + log2(2 ell_k)     for infinitely many k,
```

and via the classical bound `D = O(Σ_{i≤j} b_i)` (`(b_i)` = partial quotients of `γ/2`,
`Q_j ≤ ℓ_k < Q_{j+1}`) a checkable sufficient form is `Σ_{i≤j} b_i = o(q_{k-2}(m_{k-1}−1))`.

**Even branch** (`|W|_1` even, root `V`, `|V| = ℓ`). With the same height bound and the
combinatorial cap,

```
S  >=  ell [ r - g(gamma_V) ] - log2 ell - log2 3,     g(gamma) = max(1, gamma log2 3) + gamma(1-gamma) log2 3.
```

`g` is continuous, `g(γ) < log₂3 = 1.58496` for every `γ < 1`, `g(1/2) = 1.39624`, `g(γ) → 1` as
`γ → 0`. **So the even branch needs only `r > g(γ_V)`, with no discrepancy hypothesis and no
hypothesis on the slope whatsoever.** Using `g(γ_V)` rather than the uniform `log₂3` is the
"sharper height estimate exploiting the actual root structure" Phase 9 was asked for; it matters
because real roots have `γ_V ≈ 0.15–0.5`, where `g ≈ 1.21–1.40`.

## 5. Dependency map

| step | source | hypothesis on `γ`? |
|---|---|---|
| attained roots, lengths `q_k` / `ℓ_k`, exponents `x(k)`, `y(k)` | BHZ Prop. 3.3 + Cor. 3.5 | none |
| root **weights** `p_k` / `d_kp_{k-1}+p_{k-2}` | BHZ Lemma 2.6 + cyclic invariance — **but only on attained roots**, see `PHASE9_FAILURE_SET_AUDIT.md` §1 | none |
| exact XOR transfer `L_v = L_u+1` | `theorems/phase2/ROTE_TRANSFER_THEOREM.md` | none |
| even branch, `r > g(γ_V)` | `theorems/phase1/REPETITION_HEIGHT_CRITERION.md` unconditional form + combinatorial cap | **none** |
| odd branch, `γ_R = 1/2` and `D(R) = o(ℓ)` | `theorems/phase4/REQUIRED_EXPONENT.md`, `theorems/phase5/ROTE_DISCREPANCY_AUDIT.md`, `PHASE8_CHAIN_AUDIT.md` §3 | **yes — this is the only place** |
| `limsup S = +∞ ⟹ Φ(v)∉ℚ` | `theorems/phase2/PHASE1_FREEZE.md` | none |
| both seeds | `D(V) = D(V̄)`; height depends on the root only through `(ℓ, weight, D)` | none |
| every shift | source paper Prop. 2.3: `Φ(σv) = T(Φ(v))`, and `T`, `T^{-1}` preserve `ℚ∩ℤ₂` | none |

**The entire dependence on bounded type sits in one cell: the odd branch's discrepancy estimate.**
That is why Phase 9's route is to avoid the odd branch rather than to improve `(H)`.
