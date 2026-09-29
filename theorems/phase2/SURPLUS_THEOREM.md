# SURPLUS_THEOREM.md

## 1. Is `S_s(W)` exactly the quantity the proof produces?

**Yes, in its `|δ_W|`-form.** `ABSTRACT_IRRATIONALITY_CRITERION.md` derives `(‡)`: `L - \log_2(|δ_W|+c_W) \le \log_2 H` directly from the two bounds `(★)`,`(†)` with no slack beyond the single triangle inequality `|u\delta_W - vc_W|\le|u||\delta_W|+vc_W`. `S_s(W) := \text{lcp}(s,W^\infty) - \log_2(|δ_W|+c_W)` is therefore the proof-native quantity, not a convenient after-the-fact packaging.

## 2. Is a simpler equivalent height preferable?

The Phase 1 packaging `F(W)=\max(2^{|W|},3^{k})+c_W` is simpler to state and estimate (no absolute value of a difference of two huge numbers to track) and is used throughout Phase 1's asymptotic theorems (`DISCREPANCY_HEIGHT_THEOREM.md`, `REPETITION_HEIGHT_CRITERION.md`) precisely because `|\delta_W|\le\max(2^\ell,3^k)` makes it a valid — if slightly lossy — substitute. **Recommendation for this phase: use `|\delta_W|+c_W` (this phase's `ABSTRACT_IRRATIONALITY_CRITERION.md` canonical form) whenever an exact numeric margin is computed, and the cruder `\max(2^\ell,3^k)+c_W` whenever only the asymptotic (`\Theta(\ell)`-level) behavior matters** — both give the same qualifying/non-qualifying verdict in every asymptotic theorem in this phase, since they differ by at most a factor of `2` in `F` (hence an additive `O(1)` in `\log_2F`), which never changes a strict `\Theta(\ell)`-level inequality's sign for large `\ell`.

## 3–4. Effect of reducing `c_W/\delta_W` to lowest terms

Derived in full in `ABSTRACT_IRRATIONALITY_CRITERION.md`: reduction is **valid** (the same valuation argument goes through verbatim with `c_W',\delta_W'=c_W/g,\delta_W/g`) and **strictly improves** the bound whenever `g=\gcd(c_W,\delta_W)>1`, since `|\delta_W'|+c_W' = (|\delta_W|+c_W)/g \le |\delta_W|+c_W`. **The unreduced height is not "more natural" merely because it appears directly in `M_n` — it appears there because `M_n` is built from `u,v` and the *specific* fraction `c_W/\delta_W` as computed by Proposition 4.1's formula, and there is no obstruction to first reducing that fraction before forming `M_n`.** This is a real, unused strengthening — not pursued in this phase (every target theorem below closes without it) but recorded as available headroom for a harder future target (e.g. Target A, or a multiplier `q\ge5` class where every bit of margin matters, `MULTIPLIER_DIAGNOSTIC.md`).

## 5. Effect of cyclic rotation of `W`

Let `W' = \sigma^j(W)` (cyclic shift by `j`). `\delta_{W'}=\delta_W` **exactly** (depends only on `(\ell,k)`, both invariant under cyclic rotation). `c_{W'}` generally differs from `c_W$, bounded via the same discrepancy-height machinery applied to `W'` (whose discrepancy differs from `W`'s by at most an additive `O(1)`, since prefix-count functions are cyclic re-indexings of one another) — so `F(W')=\Theta(F(W))` (same exponential order, `\log_2 F(W')=\log_2F(W)+O(1)`). **But `L' := \text{lcp}(s,W'^\infty)` is not controlled by `L=\text{lcp}(s,W^\infty)` at all** — `W'^\infty` is a genuinely different infinite periodic sequence (a shift of `W^\infty`), and `s` may agree with it to a wildly different depth, in either direction. **Conclusion: `S_s(W)` is height-stable but depth-sensitive under cyclic rotation** — exactly the Phase 1 `SURPLUS_INVARIANT.md` finding, now derived from the proof mechanics directly rather than asserted.

## 6–7. Effect of `W \to W^m`, and whether powers can manufacture fake surplus

**Key identity:** `(W^m)^\infty = W^\infty` as infinite sequences, for every `m\ge1` — replacing the root by a power does not change the infinite periodic extension being compared against `s`. Hence `L_{W^m} := \text{lcp}(s,(W^m)^\infty) = \text{lcp}(s,W^\infty) = L_W`, **exactly unchanged**. Meanwhile `|W^m|=m\ell\to\infty$ and (from the general asymptotic form `\log_2F(W)\approx\max(\ell,k\log_2 3)`, which scales linearly in the word) `\log_2 F(W^m) \approx m\cdot\log_2F(W) + O(\log m) \to +\infty` as `m\to\infty`. So
```
S_s(W^m) = L_W - \log_2F(W^m) \xrightarrow{m\to\infty} -\infty,
```
**strictly decreasing surplus, not increasing it.** **No fake surplus can be manufactured by taking powers — the opposite happens.**

> **Corollary (primitivity is free — and necessary — for an optimal witness).** For a fixed target infinite periodic extension `W^\infty`, the surplus `S_s(W)` is maximized by using the **primitive root** of the period (the shortest `W` with that periodic extension), never a proper power of it. This is exactly why Phase 1's `initial_power_search`/`all_initial_powers` scripts filter for primitivity — not a computational convenience, but a provable optimality requirement.

## 8. The dual (necessity-direction) theorem

> **THEOREM (uniform surplus bound under rationality).** If `\Phi(s)=u/v\in\mathbb Q` (lowest terms, height `H=\max(|u|,v)`), then for **every** finite word `W` with `s\ne W^\infty`,
> ```
> S_s(W) \le \log_2 H.
> ```

**Proof.** This is exactly `(‡)` from `ABSTRACT_IRRATIONALITY_CRITERION.md`, restated as a standalone claim: the derivation there used no property of `W` beyond `s\ne W^\infty`, so it holds for every such `W`, with the **same** constant `\log_2H` — i.e. the bound is uniform over the (infinite) set of all admissible witnesses, not merely along a chosen sequence `(W_n)`. `\blacksquare`

**Status: PROVED.** This is the exact contrapositive-equivalent of the main criterion (`\sup_W S_s(W)<\infty` whenever `\Phi(s)\in\mathbb Q`), confirming `S_s(W)` is the right invariant in both directions of the *sufficiency* argument. **The converse — that `\sup_W S_s(W)<\infty` implies `\Phi(s)\in\mathbb Q`, i.e. that bounded surplus against every possible witness forces rationality — remains open, exactly as flagged in Phase 1's `SURPLUS_INVARIANT.md` and `FULL_PERIODICITY_GAP.md` Q5, and is not addressed in this phase either** (the counting route already proves it false as stated: words with no useful periodic witness at all can still be irrational, so `\sup_W S_s(W)` could be `-\infty`-flavored/undefined-in-any-useful-sense for such `s`, without `\Phi(s)` being rational — the converse would need careful restatement even to be a well-posed question, and is out of scope for the theorem-conversion goal of this phase).
