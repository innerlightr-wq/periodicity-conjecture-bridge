**`C = 24.207846`, `C₀ = 35.869175` — DERIVED FROM THE CITED THEOREM, READ FIRST-HAND**

# EXPLICIT_DISCREPANCY_CONSTANTS.md

Phase 14 / item 3, first half. Computation and verification:
`scripts/phase14/explicit_constants.py`, `data/phase14/explicit_constants_output.txt`.

## 1. The cited result, quoted from the source

**Kuipers & Niederreiter, *Uniform Distribution of Sequences*, Chapter 2, Theorem 3.4** — read
first-hand rather than quoted from the repository's earlier summaries. The book attributes it to
Niederreiter, improving earlier results of Ostrowski.

> Suppose the irrational `α = [a₀; a₁, a₂, …]` has bounded partial quotients, say `a_i ≤ K` for
> `i ≥ 1`. Then the discrepancy `D_N(ω)` of `ω = (nα)` satisfies `N D_N(ω) = O(log N)`. More exactly,
> ```
> N D_N(w)  <=  3 + ( 1/log(phi) + K/log(K+1) ) log N ,        (3.16)
> ```
> where `φ = (1+√5)/2`.

Conventions, checked against the chapter: `log` is the natural logarithm; `D_N` is the **extreme**
discrepancy (supremum over subintervals), not the star discrepancy; `ω = (nα)` runs `n = 1,…,N`.

**For our slope `α = (√5−1)/2` every partial quotient is `1`, so `K = 1` and**

```
c_K := 1/ln(phi) + 1/ln 2 = 2.078087 + 1.442695 = 3.520782 ,
N D_N({n alpha})  <=  3 + 3.520782 * ln N .
```

*Corroboration of the reading* (not a proof — the proof is the citation). Computing `D_N` directly
from `D_N = max_i(i/N − x_(i)) + max_i(x_(i) − (i−1)/N)` on the sorted orbit:

```
N        N*D_N      3 + c_K ln N    slack
10       1.8197     11.1069          9.29
1000     2.6497     27.3207         24.67
20000    4.8162     37.8680         33.05
60000    4.4974     41.7360         37.24
```

The inequality holds throughout with large margin, as one expects of a bound valid for every bounded
type.

## 2. From the cited theorem to the drift of our word

We need `Δ(N) := max_{1≤i≤N} |k_i − iβ|`, where `k_i = #{m<i : {mα+ρ} ∈ [0,β)}`. Two adjustments
separate this from (3.16), each stated rather than waved through.

**(i) The intercept costs a factor 2, and it is actually incurred.** `A([0,β); N)` for the shifted
sequence counts `{mα}` in `[0,β) − ρ`, which modulo 1 is one interval or two. Two intervals cost two
applications of `D_N`. For `ρ = 1/7` the set `[0,β) − 1/7 = [−1/7, β−1/7)` **does** wrap, so the
factor is used, not assumed away.

**(ii) The index range costs 1.** Kuipers–Niederreiter count `n = 1,…,N`; we count `m = 0,…,N−1`.
The symmetric difference is a single point, contributing at most `1` to any count.

Hence

> **`Δ(N) ≤ 2(3 + c_K ln N) + 1 = 7 + 7.041564 ln N = C_D·log₂N + C_D'`**
> with **`C_D = 2c_K·ln2 = 4.880840`** and **`C_D' = 7`**.

(The conversion is `ln N = ln2 · log₂N`, so the coefficient is *multiplied* by `ln2`. An earlier draft
of this derivation divided instead, inflating `C_D` by `1/ln²2 ≈ 2.08`; the error was caught by the
verification table below, which is why the table is here.)

*Verification against the actual word*, exact counts with the certified `β`-bracket:

```
N        max|k_i - i beta|   C_D log2 N + 7    slack
10       0.5237              23.2138           22.69
1000     1.3084              55.6414           54.33
10000    1.7963              71.8552           70.06
60000    2.0025              84.4720           82.47
```

## 3. The surplus inequality, with numbers

From `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`, `c_W ≤ ℓ·3^{⌈D(W)⌉}·max(2^ℓ,3^k)`, and
`F(W) = |2^ℓ−3^k| + c_W ≤ (1 + ℓ3^{⌈D(W)⌉})max(2^ℓ,3^k)`, so

```
log2 F(W)  <=  1 + log2(ell) + ceil(D(W)) log2(3) + max(ell, k log2 3).
```

Because **`β·log₂3 = 1` exactly**, writing `e_ℓ := k − ℓβ` gives
`k log₂3 = ℓ + e_ℓ log₂3`, hence `max(ℓ, k log₂3) = ℓ + log₂3·max(0,e_ℓ)` and

```
S(W) >= (L - ell) - log2(3) max(0, e_ell) - ceil(D(W)) log2(3) - log2(ell) - 1.
```

`D(W)` in that theorem is deviation from the word's **own** density `k/ℓ`, not from `β`. Since
`k_i − i·k/ℓ = (k_i − iβ) − (i/ℓ)e_ℓ`, we get `D(W) ≤ Δ(ℓ) + |e_ℓ| ≤ 2Δ(ℓ)`, while
`|e_ℓ| ≤ Δ(ℓ)`. Substituting and using `⌈x⌉ ≤ x+1`:

> **`S(W) ≥ (L − ℓ) − C·log₂ℓ − C₀`** with
> ```
> C   = 3 C_D log2(3) + 1                  = 24.207846
> C_0 = 3 C_D' log2(3) + log2(3) + 1       = 35.869175
> ```

*Verification against exactly computed surpluses* (`S = L − log₂F(W)`, `F` from exact big integers):

```
ell     k      L        S exact     (L-ell) - C log2 ell - C_0    holds
233     147    469       230.269       9.756                        yes
377     238    846       462.336     225.950                        yes
610     385    1456      838.736     586.144                        yes
987     623    2443     1447.868    1179.338                        yes
```

Twelve convergents tested, no failures. The bound is loose by a factor of roughly 1.2–2 at these
lengths, as expected of a worst-case discrepancy estimate.

## 4. Where each constant comes from

| constant | value | source |
|---|---|---|
| `c_K` | `3.520782` | KN Ch. 2 Thm 3.4 (3.16), at `K = 1` |
| factor `2` | — | the intercept shift; a wrapped interval is two intervals |
| `+1` | — | index range `m=0..N−1` versus `n=1..N` |
| `C_D` | `4.880840` | `2c_K ln2` |
| `C_D'` | `7` | `2·3 + 1` |
| `log₂3` | `1.5849625` | — |
| `C` | `24.207846` | `3C_D log₂3 + 1` |
| `C₀` | `35.869175` | `3C_D' log₂3 + log₂3 + 1` |

Nothing here is measured. The verification tables are checks on the derivation, and the paper trail
is the citation plus eight lines of arithmetic.

## 5. Dependence on the slope

Only `c_K` sees the slope, through the largest partial quotient `A`:

```
A     c_A = 1/ln(phi) + A/ln(A+1)    C_D = 2 c_A ln2    C = 3 C_D log2 3 + 1
1     3.520782                       4.880840           24.207846
2     3.898565                       5.404559           26.698071
3     4.242129                       5.880840           28.962733
5     4.868640                       6.749368           33.092487
10    6.248411                       8.662137           42.187486
```

**`C₀ = 35.869175` is universal** — independent of `α` and of `ρ` — and **`C` depends on `α` only
through `A`**, so both are numerical for the whole bounded-type family, not just for the named
example. That is not true of the constants on the analytic side; see `EXPLICIT_HEIGHT_BOUND.md` §5.
