**PROVED — A SUBSTANTIAL UNBOUNDED-TYPE THEOREM, WITH NO HYPOTHESIS ON THE PARTIAL QUOTIENTS**

# PHASE9_PROOF_OR_COUNTEREXAMPLE.md

## 0. What is proved, in one line

The even-weight transfer branch needs **no hypothesis on the slope at all** — not bounded type, not
a growth condition, not even a discrepancy estimate. So whenever the parity of an attained witness
root comes out even infinitely often, `Φ(v) ∉ ℚ` follows for arbitrary irrational slope and
arbitrary intercept. That is Theorem 3.

## 1. Theorem 3, with all quantifiers

> **THEOREM 3 (unbounded-type CS Rote bridge, parity form).**
> Let `γ ∈ (0,1)` be irrational, with **no hypothesis whatever on its partial quotients**. Let `u`
> be **any** Sturmian word of slope `γ` — any intercept `ρ`, either the upper or the lower
> mechanical convention — with BHZ digits `(a_k)` and admissible Ostrowski digits `(c_k)`,
> `d_k := a_k − c_k`. Suppose there exist infinitely many `k ≥ 3` with
>
> ```
> (i)   0 < c_k < a_k ,
> (ii)  d_{k-1} >= 1 ,
> (iii) d_k p_{k-1} + p_{k-2}  is EVEN .
> ```
>
> Let `v` be either complementary symmetric Rote sequence with `S(v) = u` (either seed), or any
> shift `σ^j(v)`. Then
> ```
> Phi(v) not in Q .
> ```

**Proof.** Fix `k` satisfying (i)–(iii).

*Witness.* By BHZ Prop. 3.3 (second case, whose standing hypothesis is exactly (i)), `u` begins in
`W^{y(k)}` where `W` is a cyclic permutation of `τ_0^{a_1}∘⋯∘τ_{k-1}^{a_k−c_k}(i)` and
`ℓ_k := |W| = q_k − c_kq_{k-1} = d_kq_{k-1} + q_{k-2} ≥ q_{k-2}`, so `ℓ_k → ∞` along the chosen
`k`'s. By BHZ Lemma 2.6 the weight of that word is `p_k − c_kp_{k-1} = d_kp_{k-1} + p_{k-2}`, and
cyclic permutation preserves weight, so `|W|_1 = d_kp_{k-1} + p_{k-2}`, which is **even** by (iii).
(This is weight law (W-y) of `PHASE9_FAILURE_SET_AUDIT.md` §1; exact in 952/952 checks.)

*Exponent.* By (ii), `m_{k-1} = t_{k-2} + d_{k-1} ≥ 1`, so by the identity of
`PHASE9_TARGET_AND_DEPENDENCIES.md` §2, `y(k) − 2 = λ_{k-1}(m_{k-1}−1)/(λ_{k-1}+d_k) ≥ 0`, i.e.
**`y(k) ≥ 2`**.

*Transfer.* `|W|_1` is even, so over one period of `W` the recursion `v_{n+1} = v_n ⊕ u_n` returns
to its starting value: `v` is periodic with period `ℓ_k` on the agreement range, at root
`V := v[0:ℓ_k]`, and `lcp(v, V^∞) = lcp(u, W^∞) + 1 = y(k)ℓ_k + 1` exactly
(`theorems/phase2/ROTE_TRANSFER_THEOREM.md`, proved intercept-agnostic there). **This is the even
branch: no doubling, so no exponent halving.**

*Height.* Put `γ_V := |V|_1/ℓ_k ∈ [0,1]`. By `theorems/phase2/DISCREPANCY_HEIGHT_PROOF.md`,
`log₂F(V) ≤ log₂ℓ_k + ⌈D(V)⌉log₂3 + max(ℓ_k, |V|_1 log₂3)`, and by the combinatorial cap of
`theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`, `D(V) ≤ γ_V(1−γ_V)ℓ_k` **for any word**. Hence

```
S_k := lcp(v,V^inf) - log2 F(V)  >=  ell_k [ y(k) - g(gamma_V) ] - log2 ell_k - log2 3,
g(gamma) := max(1, gamma log2 3) + gamma(1-gamma) log2 3 .
```

Since `sup_{γ∈[0,1]} g(γ) = log₂3 < 2 ≤ y(k)`,

```
S_k  >=  ell_k (2 - log2 3) - log2 ell_k - log2 3  ->  +infinity,
```

because `ℓ_k → ∞` and `2 − log₂3 = 0.41504… > 0`. **No hypothesis on `γ` was used anywhere in this
step** — the cap is a combinatorial fact about arbitrary binary words, and `2 − log₂3 > 0` is the
single numerical fact doing the work.

*Conclusion.* `limsup_k S_k = +∞`, so `Φ(v) ∉ ℚ` by
`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` / `PHASE1_FREEZE.md`.

*Both seeds.* The other seed gives `v̄`, hence root `V̄`; `|V̄| = |V|`, `D(V̄) = D(V)`, and the height
bound depends on the root only through `(ℓ, weight, D)` — with `max(ℓ, w log₂3)` and
`γ(1−γ)` both symmetric under `γ ↦ 1−γ`. So the same bound applies.
*Every shift.* Source paper Prop. 2.3 gives `Φ(σv) = T(Φ(v))` with `T` the `3x+1` map on `ℤ₂`; `T`
and `T^{-1}` both map `ℚ∩ℤ₂` into itself, so `Φ(v)∉ℚ ⟺ Φ(σ^jv)∉ℚ` for every `j ≥ 0`. ∎

### 1.1 Restating (iii) usefully

With `P_{k-1} := (p_{k-2}, p_{k-1}) mod 2 ∈ {(0,1),(1,0),(1,1)}`, condition (iii) reads
`p_{k-1}d_k ≡ p_{k-2} (mod 2)`, i.e.

```
P_{k-1} = (0,1)  ->  (iii) <=> d_k EVEN
P_{k-1} = (1,1)  ->  (iii) <=> d_k ODD
P_{k-1} = (1,0)  ->  (iii) never holds
```

> **COROLLARY 3.1 (all-even-tail slopes at keep-one).** If `a_2` is odd and `a_k` is even for all
> `k ≥ 3` — so every `p_k` is odd and `P_{k-1} ≡ (1,1)` — and the intercept is BHZ's "keep one"
> `c_k = a_k − 1` (so `d_k = 1`, odd, and `0 < c_k < a_k` since `a_k` is even, and `d_{k-1} = 1 ≥ 1`),
> then **all three hypotheses hold at every `k ≥ 3`** and `Φ(v) ∉ ℚ`. The partial quotients may
> grow arbitrarily fast.

> **COROLLARY 3.2 (unbounded type is reached).** The class covered by Theorem 3 contains
> uncountably many slopes of **unbounded** partial quotients. For instance, for any sequence
> `(e_k)` of positive integers, `a = (3, 1, 2e_3, 2e_4, …)` at the keep-one intercept satisfies
> Corollary 3.1; choosing `e_k` freely gives uncountably many such slopes, with `sup_k a_k = ∞`
> whenever `e_k → ∞`.

Theorem 3 is therefore a genuine extension of Phase 8's Theorem 2 in the slope direction, at the
cost of a parity hypothesis on the intercept. The two are incomparable: Theorem 2 needs bounded type
but no parity condition; Theorem 3 needs no growth condition but a parity condition.

### 1.2 The `x`-root analogue

> **THEOREM 3′.** Same setting. If there are infinitely many `k` with `x(k) > g(γ_{V_k})` and `p_k`
> even (equivalently `P_k = (1,0)`), then `Φ(v) ∉ ℚ`.

Same proof with the `x`-witness of BHZ Prop. 3.3 (first case), root length `q_k`, weight `p_k` —
using weight law (W-x), whose hypothesis `x(k) ≥ 1` is implied by `x(k) > g ≥ 1`. Note the exponent
hypothesis is `> g(γ_V)`, not `≥ 2`: the even branch does not need squares.

## 2. What is **not** proved

1. **Theorem 3's hypothesis can fail.** `PHASE9_FAILURE_SET_AUDIT.md` §4 exhibits two families
   (`a_k = 2^k` and `a_k = k!`, both at keep-one) where no guaranteed root has even weight at any
   scale, because `P_{k-1}` never visits `(1,1)`. Both are covered by the **odd** branch instead,
   with positive exact integer surplus — so they are not gaps in the conclusion, only in Theorem 3's
   reach.
2. **The intermediate-root rescue is a certified finite check, not a theorem.** On the hostile
   all-odd-numerator family the `d = 1` intermediate root has even weight and prefix power
   `≈ 1.69–1.82 > g(γ) ≈ 1.21–1.40`, giving positive exact surplus in 144/144 evaluations across 27
   slope/intercept pairs. But intermediate roots carry **no** BHZ attainment guarantee, and weight
   law (W-int) is not exact, so this is evidence, not proof. **The smallest remaining lemma is
   precisely:**

   > **(L1)** For every Sturmian word `u` and all large `k`, the prefix of length `q_{k-1} + q_{k-2}`
   > satisfies `lcp(u, ·^∞) ≥ 2q_{k-1}`, i.e. prefix power `≥ 2/(1 + λ_{k-1})`.

   For the characteristic word this is provable from the standard-word recursion
   `s_{k} = s_{k-1}^{a_k}s_{k-2}`: the root is `s_{k-1}s_{k-2}`, agreement runs through `s_{k-1}`,
   then `q_{k-2}` more because `s_{k-2}` is a prefix of `s_{k-1}`, then `(a_{k-1}−1)q_{k-2} + q_{k-3}
   = q_{k-1} − q_{k-2}` more because `s_{k-1} = s_{k-2}^{a_{k-1}}s_{k-3}` — total `2q_{k-1}`. For a
   **general intercept** the prefix of that length is not `s_{k-1}s_{k-2}` and the argument does not
   transfer; that is the gap. Note `2/(1+λ_{k-1}) > g(γ)` needs `λ_{k-1} < 2/g − 1`, which holds at
   one of any two consecutive scales (if `λ_{k-1}` is near `1/2` then `a_{k-1} = 2` and `a_{k-2}` is
   large, forcing `λ_{k-2}` small), so (L1) plus that two-scale argument would upgrade the finite
   check to a theorem.
3. **The odd branch beyond `(H)`.** `PHASE9_FAILURE_SET_AUDIT.md` §5 exhibits a family where the
   growth condition `(H)` and the estimated surplus bound both fail, while the **exact** surplus
   holds wherever it is computable. Closing that gap needs an exact (not worst-case) evaluation of
   `log₂c_R`, which is untouched.
4. **No counterexample to `Φ(v) ∉ ℚ` was found anywhere**, at any slope, any intercept, any branch.

## 3. Numerator height versus denominator height — kept separate

`F(R) = |2^{|R|} − 3^{|R|_1}| + c_R`. The two summands behave differently and improving one does not
control the other:

- **denominator part** `|δ_R| = |2^{|R|} − 3^{|R|_1}|`. On the odd branch `γ_R = 1/2` exactly, so
  `|δ_R| = 2^{2ℓ}(1 − (3/4)^ℓ)` and `log₂|δ_R| = 2ℓ − O((3/4)^ℓ)`: completely controlled, with no
  discrepancy input. A Baker-type improvement here would buy nothing, since the term is already
  `2ℓ + o(1)`.
- **numerator part** `c_R = Σ_{i<|R|,R_i=1} 3^{|R|_1−k_{i+1}(R)}2^i`. Writing `e_i := i/2 − k_{i+1}(R)`,
  the `i`-th term has `log₂ = ℓ log₂3 + i(1 − ½log₂3) + e_i log₂3`, maximised near `i = 2ℓ` where it
  equals `2ℓ + e_i log₂3 + O(1)`. **So `c_R` is where the whole discrepancy dependence lives**, and
  it is governed by the deviations `e_i` for `i` near the *end* of `R`, not by the global
  discrepancy. That is the precise object route (H2) would have to estimate; the `⌈D(R)⌉log₂3`
  bound replaces `max_i e_i` by a sup over all prefixes, and Phase 9 measured it to be 2–3 orders
  of magnitude pessimistic (`D(V) = 3–5` against a cap of `960–5600`).

Since `|δ_R|` and `c_R` are comparable in size (`both ≈ 2^{2ℓ}`), no bound on one alone controls
`F(R)`; the sum must be handled together, which is why `F(R)` is evaluated exactly in every Phase 9
surplus test rather than bounded.

## 4. Reproducibility

```
scripts/phase9/phase9_witness_family.py      -> identity, attainment routing, weights, parity
scripts/phase9/phase9_intermediate_roots.py  -> literal prefix powers of all intermediate roots
scripts/phase9/phase9_even_branch.py         -> g(gamma), adversarial search, exact even surplus
scripts/phase9/phase9_weight_stress.py       -> the weight formula is NOT universally exact
scripts/phase9/phase9_weight_law.py          -> the exact weight law (W-y)/(W-x)/(W-int)
scripts/phase9/phase9_failure_set.py         -> coverage, failure set, intermediate rescue
scripts/phase9/phase9_double_failure.py      -> odd-branch cover, (H), the double-failure family
```

Outputs in `data/phase9/`. Exact `Fraction`/big-integer arithmetic throughout; `F(R)` is always
computed exactly. Every script asserts its own claims, so a non-zero exit means a claim failed.
