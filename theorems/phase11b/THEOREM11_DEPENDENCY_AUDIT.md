**DEPENDENCY AUDIT — TWO UNSTATED HYPOTHESES FOUND, BOTH SATISFIED; MEASURED CONSTANTS REPLACED**

# THEOREM11_DEPENDENCY_AUDIT.md

Independent audit of every link in Theorem 11. `scripts/phase11b/geometry_audit.py`,
`data/phase11b/geometry_audit_output.txt`.

## 1. Ledger

| link | Phase 11 status | after this audit |
|---|---|---|
| aperiodicity, density `= β` | proved | **unchanged** |
| `p(n) = 2n` | cited (Rote 1994) + verified `n ≤ 20` | **unchanged** |
| R1 first-mismatch identity | proved, verified | **confirmed**, by three independent routes |
| R2 two-ball relaxation | proved | **confirmed, and shown unconditional** (survives arc wrap) |
| R3 arc at `0` | proved | **unchanged** |
| R4 arc at `β` | **polynomial** Baker bound | **WITHDRAWN and replaced** — stretched exponential |
| R5 witness size `ℓ(M) = O(M^κ)` | proved from R4 | **replaced** — `log ℓ(M) = O((log(M+2))^κ)` |
| closed-form arc description | stated without hypothesis | **hypothesis found and stated**: `|δ| ≤ min(β,1−β)` |
| drift / discrepancy constants | **measured** `0.41`, `2.02` | **replaced by proved asymptotic bounds** |
| exact surplus certificates | certified integers | **unchanged, and shown Baker-free** |

## 2. The arc description needs a no-wrap hypothesis — found here

The case analysis giving

```
delta > 0 :  M(delta) = [beta-delta, beta) u [1-delta, 1)
delta < 0 :  M(delta) = [0, |delta|)       u [beta, beta+|delta|)
```

silently assumes the arcs do not wrap past `0`/`1`, i.e.

> **`|δ| ≤ min(β, 1−β) = 0.3690702464…`**

Checking the closed form against the definition `χ(x) ≠ χ({x+δ})` over 14 shifts × 3000 orbit
points: **0 disagreements wherever the hypothesis holds, 39 disagreements where it fails** — and it
fails at exactly one tested shift, `q = 1`, where `|δ| = 0.3819660113 > 0.3690702464`. The closed
form is therefore exactly right under its hypothesis and exactly wrong without it.

The construction uses `|δ| < 1/(147M) ≤ 1/294 = 0.0034`, so the hypothesis holds with a factor of
about `108` to spare. Phase 11 never stated it.

**R2 is unconditional.** If an arc crosses `1`, its overspill lands next to `0`, and `B(0,·)` is the
two-sided ball at `0 ≡ 1`; so `M(δ) ⊆ B(0,|δ|) ∪ B(β,|δ|)` holds regardless. Verified over 42 000
tests **including** `q = 1`: 0 containment violations. Since the proof routes through R2, the
no-wrap issue never reaches the conclusion — but it had to be checked, not assumed.

## 3. Translation sign, endpoints, and the identity

**Sign.** `{x + ℓα} = {x + δ}` with `δ := ℓα − round(ℓα)`, since adding an integer does not change
the fractional part. Both signs of `δ` occur (consecutive convergents alternate) and both are
handled; the case analysis is written out for each.

**Endpoints.** The half-open side of each arc matches the half-open side of the partition `[0,β)`.
An endpoint slip would move `m*` by one. The four-interval case analysis is given explicitly in
`data/phase11b/geometry_audit_output.txt` (a), for each sign.

**The identity.** `L(ℓ) − ℓ = m*(ℓ)` verified by **three** independent computations — the literal
longest common prefix of the certified word, the `χ(x) ≠ χ({x+δ})` definition, and the closed-form
arc description — agreeing at every convergent denominator `5 ≤ q ≤ 2584`.

## 4. `m = 0`, explicitly

The orbit point at `m = 0` is `{ρ} = 1/7`. Its distances to the two discontinuities are

```
|| 1/7 - 0 ||    = 1/7          = 0.1428571429
|| 1/7 - beta || = c_0          = 0.4880726107
```

The construction has `|δ| < 1/(147M) ≤ 1/294 = 0.0034 < 1/7` and `|δ| < C_M ≤ c_0`. So `m = 0` lies
in **neither** arc. It is not a special case, but it does require the minimum defining `C_M` to
start at `m = 0` — which it does, and which matters because `c_0 = 0.488` is not the smallest `c_m`.

## 5. Drift and discrepancy from proved bounds, not measured constants

Phase 11 substituted the **measured** values `|e_ℓ| ≤ 0.41`, `D(W) ≤ 2.02`, valid only on the
computed range. Replaced by:

By Phase 10 Lemma D (shifting the orbit equals shifting the interval; the **extreme** discrepancy
bounds every interval at once) together with Kuipers–Niederreiter, *Uniform Distribution of
Sequences*, Ch. 2 Thm 3.4,

```
N * D_N  <=  c_1' * sum_{i <= k+1} a_i  +  c_2'      ( q_k <= N < q_{k+1} ),
```

and for `α = (√5−1)/2` every `a_i = 1`, so `Σ_{i≤k+1} a_i = k+1 ≤ log_φ N + 2`. Hence with
`C_D := c_1'/log₂φ`:

```
| e_ell |  = | k_ell - ell*beta |  <=  C_D log2(ell) + C_D' ,
  D(W)     <=  max_i |k_i - i*beta| + |e_ell|  <=  2 C_D log2(ell) + 2 C_D' .
```

Substituting into (H):

```
S >= (L-ell) - log2(3)*[ (C_D log2 ell + C_D') + (2 C_D log2 ell + 2 C_D' + 1) ] - log2(2 ell)
   = (L - ell)  -  C log2(ell)  -  C_0 ,
   C   := 1 + 3 C_D log2(3) ,      C_0 := 1 + log2(3) (3 C_D' + 1) ,
```

both **absolute constants for this `α`**, independent of `ℓ`. The measured numbers are demoted to a
consistency check: `|e_ℓ|/log₂ℓ` stays below `1` for every convergent `ℓ ≤ 60 000`.

## 6. What remains Baker-free

The finite height certificates `H ≥ 2^{S}` at the computed witnesses are exact integer facts
(`2^L > F(W)` compared as integers) and use **no** analytic input. Baker enters only in showing
that the witness family continues for every `M` — i.e. only in the asymptotic conclusion.
