# SURPLUS_INVARIANT.md

## Which definition falls directly out of the proof

`ABSTRACT_BRIDGE_THEOREM.md` Step 3 gives, with no slack beyond `|δ|≤max(2^ℓ,3^k)` (itself only used to package the bound cleanly, not intrinsic to the proof), the *exact* quantity the comparison produces:
```
S_s(W) := lcp(s, W^∞) − log₂( |2^{ℓ} − 3^{k}| + c_W ),    ℓ=|W|, k=#ones(W).
```
This is the task's proposed definition, confirmed to be the **proof-native** one — using `|δ|=|2^ℓ−3^k|` exactly (not the cruder `max(2^ℓ,3^k)` packaging used elsewhere in this audit for convenience) gives a **tighter, strictly better** surplus whenever `2^ℓ ≈ 3^k` is anomalously close (i.e. `ℓ/k` near `log₂3`), since then `|δ| ≪ max(2^ℓ,3^k)`. The two differ by at most an `O(1)` additive term in `log₂` in general, but the exact-`δ` form is the one the theorem's proof actually manufactures and should be treated as canonical; `F(W)=max(2^ℓ,3^k)+c_W` (used elsewhere in this audit) is a convenient, slightly weaker upper-bound packaging of the same idea.

**Normalized version**: `σ(s;W) = S_s(W)/ℓ`.

## Properties

**Shift-sensitivity.** `S_s(W)` depends on `s` through `lcp(s,W^∞)` directly, not through any shift-invariant summary — replacing `s` by `σ(s)` (the shift) while keeping `W` fixed generally changes the longest-common-prefix length in an uncontrolled way. **`S_s(W)` is shift-sensitive.** This is expected and correct: `s` and `σ(s)` genuinely have `Φ`-values related by `Φ(σs)=T(Φ(s))` (Proposition 2.3), and `T` is a bijection, so irrationality of one is equivalent to irrationality of the other (Corollary 7.2's argument) — but the *specific numeric* approximation quality by a *specific* `W^∞` need not be shift-invariant, only the qualitative conclusion.

**Cyclic-conjugacy stability of `W`.** `δ_W = 2^ℓ−3^k` depends only on `(ℓ,k)`, hence is **exactly invariant** under cyclic conjugation of `W`. `c_W` itself is **not** exactly invariant (different starting phase gives a different one-position pattern relative to position `0`), but its *order of magnitude* is stable: Lemma 10.4 is stated, and holds with the *same* constant, uniformly over **every** cyclic permutation of a given standard word — and more generally `DISCREPANCY_HEIGHT_THEOREM.md`'s bound depends on `W` only through `(ℓ,k,D(W))`, and discrepancy is essentially conjugation-stable (cyclically permuting a word changes the discrepancy profile by at most an additive `O(1)`, since the prefix-count function only gets cyclically re-indexed). **`S_s(W)` is exactly cyclic-conjugacy-*insensitive* in its `δ`-term and stable up to `O(1)` in its `c_W`-term.**

## Does a rational Φ-value force `S` bounded above? — Yes, exactly, this is the whole theorem

`ABSTRACT_BRIDGE_THEOREM.md` Step 4, restated in this notation: if `Φ(s)=u/v∈Q`, height `H`, then for **every** `W` with `s≠W^∞`,
```
S_s(W) ≤ log₂H.
```
**This is not a new observation — it is a restatement of the abstract bridge theorem itself**, confirming `S_s(W)` is exactly the right invariant: rationality forces a *uniform, W-independent* upper bound on it, and `limsup_W S_s(W)=+∞` (over any admissible sequence of `W`'s) is therefore precisely the right, and provably sufficient, certificate for irrationality.

## The strongest clean theorem

> **Theorem.** `Φ(s) ∈ Q ⟹ sup{S_s(W) : W$ finite, $s≠W^∞} < ∞`. Equivalently (contrapositive): `sup_W S_s(W) = +∞ ⟹ Φ(s) ∉ Q`.

This is identical in content to `ABSTRACT_BRIDGE_THEOREM.md`'s main theorem, now phrased as a single clean invariant rather than a sequence-indexed statement — the two are interchangeable, and `S_s(W)` earns the name "invariant" in the sense that it is *the* quantity whose boundedness is equivalent (in the sufficient direction) to rationality, not a merely convenient proxy.

## Status

Neither `S_s(W)` nor `σ(s;W)` is introduced here as new terminology for the final mathematical record (per the task's standing instruction) — both are used only as bookkeeping labels within this audit, pending whatever the eventual paper's own notation settles on.
