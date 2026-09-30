**THE ARITHMETIC SIDE — EXPLICIT CONSTANTS, EXACT SURPLUS, EFFECTIVE HEIGHT FLOORS**

# EXACT_HEIGHT_AND_SURPLUS.md

> **CORRECTION (Phase 11B).** Two corrections. (i) The measured constants `|e_ℓ| ≤ 0.41`, `D(W) ≤ 2.02` are valid only on the computed range and are **not** used asymptotically; the asymptotic argument now runs on the proved bounds `|e_ℓ| ≤ C_D log₂ℓ + C_D'`, `D(W) ≤ 2C_D log₂ℓ + 2C_D'` alone. (ii) The closing appeal to "Baker's Theorem 3.1" and the form `S ≥ M − Cκ''log₂M − C₀` are **withdrawn**; the corrected continuation is `S ≥ M − (Cc₁/ln2)(log(M+2))^κ − C₀`. The five explicit height floors are **unaffected and Baker-free** — they are exact integer comparisons `2^L > F(W)`. See `theorems/phase11b/PHASE11B_VERDICT.md` and `theorems/phase11b/BAKER_SOURCE_AND_APPLICATION.md`. **Theorem 11 itself stands**; only this justification changed.


Verification: `scripts/phase11/exact_height_surplus.py`, `data/phase11/exact_height_surplus_output.txt`.

## 1. The periodic value and the height bound, reconstructed

For a finite word `W`, `ℓ := |W|`, `k := |W|_1`, `k_j(W) := |W[0:j]|_1`:

```
Phi(W^inf) = c_W / delta_W ,   delta_W := 2^ell - 3^k ,
c_W := sum_{i < ell, W_i = 1}  3^{k - k_{i+1}(W)} * 2^i         (foundation paper Prop. 4.1)
```

Height packaging (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`): `F(W) := |δ_W| + c_W`, and
for any hypothetical `Φ(s) = u/v` in lowest terms with `H := max(|u|,v)`,

```
2^{L(W)}  <=  H * F(W) ,     L(W) := lcp(s, W^inf) .                      (*)
```

By `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`, `c_W ≤ ℓ·3^{⌈D(W)⌉}·max(2^ℓ,3^k)`, and trivially
`|δ_W| ≤ max(2^ℓ,3^k)`, so `F(W) ≤ (1+ℓ3^{⌈D⌉})max(2^ℓ,3^k)` and

```
log2 F(W)  <=  log2(2 ell) + ceil(D(W)) log2 3 + ell + max(0, k log2 3 - ell) .
```

## 2. The critical-density simplification

With `e_ℓ := k − ℓβ` and the identity `β·log₂3 = 1` **exactly**, `k log₂3 − ℓ = log₂3 · e_ℓ`. Hence

> **(H)**  `S(W) := L − log₂F(W) ≥ (L − ℓ) − log₂3·max(0, e_ℓ) − ⌈D(W)⌉·log₂3 − log₂(2ℓ).`

This is the form the task asks for: the leading term is the **overshoot** `L − ℓ`, and the only
corrections are the finite-scale drift `e_ℓ` and the root discrepancy `D(W)`. Limiting density
contributes nothing.

Substituting Phase 10's Lemmas D and E (`|e_ℓ| ≤ C_D log₂ℓ + C_D'`, `D(W) ≤ 2C_D log₂ℓ + 2C_D'`,
both proved there for `[0,β)` and any bounded-type `α`, uniformly in `ρ`):

> **(H′)**  `S(W) ≥ (L − ℓ) − C·log₂ℓ − C₀`, with `C = 1 + 3·log₂3·C_D` and `C₀` explicit.

**[CORRECTED — the next two sentences are a consistency check on the computed range, not an ingredient of the asymptotic proof; see the Phase 11B banner above.]**
For this candidate the drift is tiny in the verified range: `|e_ℓ| ≤ 0.41` and `D(W) ≤ 2.02` for
`ℓ ≤ 6765`, so (H) reads `S ≥ (L−ℓ) − 1.59 − 3·1.59 − log₂(2ℓ)`, i.e. **`S ≥ (L−ℓ) − log₂ℓ − 7.35`**
on that range.

## 3. What suffices, stated without `≫`

Combining (H′) with `ROTATION_REPETITION_LEMMA.md` R5: along `ℓ(M)`,

```
S( s[0:ell(M)] )  >=  M  -  C * ( kappa'' log2 M + O(1) )  -  C_0   ->   +infinity .
```

Because `M` grows linearly in `M` while `C·κ''·log₂M` grows logarithmically, the right-hand side is
unbounded above. Equivalently, and this is the precise form of the repetition estimate that
suffices: **`(L−ℓ)/log₂ℓ` is unbounded along the subsequence `ℓ(M)`** — proved in R5, not assumed.

## 4. Exact evaluation at the R5 witnesses

Every quantity the obligation names, at `ℓ = ℓ(M)`; `S` is the **exact** surplus and the verdict
column is the **integer** comparison `2^L > F(W)`, with no estimate entering it.

```
 M   ell    k     e_ell    D(W)    L      L-ell   log2|delta_W|-ell  log2 c_W - ell
 4   377    238   0.1395   1.1326   846     469      -2.594209          6.661192
 8   610    385   0.1329   1.2049  1456     846      -2.669882          7.262688
16  1597   1008   0.4052   1.2098  2478     881      -0.834678          8.900252
32  2584   1630  -0.3225   1.9946  5062    2478      -1.745046          8.338274
64  6765   4268  -0.2398   2.0195 22773   16008      -2.110371          9.984893

 M   ell    L-ell   bound (H)     S exact       2^L > F(W)   height floor
 4   377     469      456.051      462.336      True         H >= 2^462.3
 8   610     846      832.367      838.736      True         H >= 2^838.7
16  1597     881      865.547      872.098      True         H >= 2^872.1
32  2584    2478     2462.495     2469.660      True         H >= 2^2469.7
64  6765   16008    15989.521    15998.015      True         H >= 2^15998.0
```

(H) is **asserted** at every row, not merely observed. Note `log₂|δ_W| − ℓ ∈ [−2.7, −0.8]`: at
critical density `2^ℓ` and `3^k` are genuinely close, so the `|δ_W|` term is *smaller* than `2^ℓ`
and the height is carried by `c_W` (`log₂c_W − ℓ ∈ [6.7, 10.0]`). Keeping numerator and denominator
separate matters here; the crude packaging `max(2^ℓ,3^k)` would have been lossy in the other
direction.

## 5. Effective height floors — the quantitative statement, kept separate

From (*) directly: for **any** rational `u/v = Φ(s)`, `H ≥ 2^{L} / F(W) = 2^{S}`. So the table gives,
unconditionally and with no asymptotics,

```
H >= 2^462,  2^838,  2^872,  2^2469,  2^15998
```

— five explicit floors, the largest a **4 816-digit** lower bound on the height of any rational that
could equal `Φ(s)`. These are certified by integer arithmetic. Because Baker's theorem (as corrected in Phase 11B: Mathematika **14** (1967), Thm 2) is
effective, the infinite family `S(ℓ(M)) ≥ M − (Cc₁/ln2)(log(M+2))^κ − C₀` is effective too, so the floors
continue explicitly for every `M`.

**This quantitative content is logically independent of the qualitative conclusion** and is stated
separately on purpose: T1 and T2 are contradiction arguments that bound no height
(`theorems/phase10/PRIOR_RESULT_COVERAGE.md` §2), whereas these floors are explicit numbers. The
method, however, is the foundation paper's own already-claimed "height floors / effective Liouville"
technique; what is new here is the class it is applied to.

## 6. A failed scale, inspected

`ℓ = 5` — the `M = 4` witness if only the `β`-threshold is imposed. `k = 3`, `L = 8`, `L − ℓ = 3`,
`|δ| = 0.0902`, `1/(147|δ|) = 0.075 < 1`, so R3 certifies nothing. The exact surplus is
`S = 2.608` — **positive**, but `L − ℓ = 3` is a constant, so the scale cannot contribute to an
asymptotic argument however the surplus happens to come out. (An earlier draft described this
surplus as negative. It is not; the witness is useless for a different reason, and the distinction
is the point of §3: a finite positive surplus is not an asymptotic proof.)
