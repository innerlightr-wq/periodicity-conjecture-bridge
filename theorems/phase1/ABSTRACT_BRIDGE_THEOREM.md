# ABSTRACT_BRIDGE_THEOREM.md

## Setup, restated precisely

Let `s ∈ {0,1}ℕ`. Suppose `Φ(s) = u/v ∈ Q ∩ Z₂` in lowest terms, `v ≥ 1` odd (automatic, since `Φ(s) ∈ Z₂`), `H = max(|u|,v)`. Let `(W_n)` be finite words, `ℓ_n = |W_n|`, `k_n` = number of ones in `W_n`, and suppose `s ≠ W_n^∞` as infinite words for every `n` under consideration. Put `L_n = lcp(s, W_n^∞)`, `δ_n = 2^{ℓ_n} − 3^{k_n}`, `c_n = c_{W_n}` (Proposition 4.1's constant).

## Derivation (not assumed — derived from the integer comparison alone)

**Step 1 (nonvanishing).** `Φ(W_n^∞) = c_n/δ_n` (Proposition 4.1; `δ_n ≠ 0` since `2^{ℓ_n} = 3^{k_n}` is impossible for `k_n ≥ 1` by unique factorization, and `δ_n = 2^{ℓ_n} > 0` if `k_n = 0`). Define `M_n = uδ_n − vc_n ∈ Z`. If `M_n = 0` then `Φ(s) = u/v = c_n/δ_n = Φ(W_n^∞)`, and `Φ` is a bijection on `{0,1}ℕ`, so `s = W_n^∞`, contradicting the standing hypothesis. **Hence `M_n ≠ 0`.**

**Step 2 (2-adic lower bound — uses only Proposition 2.2, nothing else).** `δ_n` is odd whenever `ℓ_n ≥ 1` (`2^{ℓ_n}` even, `3^{k_n}` odd, difference odd), and `v` is odd. So
```
v₂(M_n) = v₂(vδ_n · (Φ(s) − Φ(W_n^∞))) = v₂(Φ(s) − Φ(W_n^∞)) = lcp(s, W_n^∞) = L_n,
```
the middle equality being Proposition 2.2 applied to `v = s`, `v' = W_n^∞` **verbatim, with no hypothesis on `s` or `W_n` beyond both being elements of `{0,1}ℕ`.** Since `M_n` is a nonzero integer of 2-adic valuation exactly `L_n`,
```
2^{L_n} | M_n  and |M_n| ≥ 2^{L_n}.                                                    (★)
```
This is **exact**, not an inequality with slack — the isometry gives equality of valuations, and `(★)` follows from `M_n ≠ 0`.

**Step 3 (archimedean upper bound — general, no discrepancy assumption yet).**
```
|M_n| ≤ |u||δ_n| + v·c_n ≤ H(|δ_n| + c_n) ≤ H(max(2^{ℓ_n}, 3^{k_n}) + c_n),
```
using `|δ_n| = |2^{ℓ_n} − 3^{k_n}| ≤ max(2^{ℓ_n}, 3^{k_n})` (true for any two non-negative reals: `|a−b| = max(a,b)−min(a,b) ≤ max(a,b)`). **Define**
```
F(W) := max(2^{|W|}, 3^{k(W)}) + c_W,
```
a quantity depending only on `W` (its length, its number of ones, and the combinatorial constant `c_W` of Proposition 4.1 — no discrepancy, balance, or repetition hypothesis has been used to define it). Then
```
|M_n| ≤ H · F(W_n).                                                                      (†)
```
**This `F` is exactly what the task calls for**: it is the *crudest fully general* bound obtainable from Steps 1–3 alone, valid for *every* finite word `W_n`, with *no* extra hypothesis. Pinning down explicit closed-form estimates of `c_W` (and hence of `F(W)`) in terms of a discrepancy parameter is a **separate** question, deferred to `DISCREPANCY_HEIGHT_THEOREM.md` — conflating the two would smuggle an unstated hypothesis into this theorem, exactly what the task instructs against.

**Step 4 (combine).** `(★)` and `(†)` give `2^{L_n} ≤ H·F(W_n)`, i.e.
```
L_n − log₂ F(W_n) ≤ log₂ H,   for every n.                                              (‡)
```

## The theorem

Define the **surplus** `S_n = S_s(W_n) := L_n − log₂ F(W_n) = lcp(s,W_n^∞) − log₂F(W_n)`.

> **Theorem (abstract periodic-approximation bridge).** Let `s ∈ {0,1}ℕ` and `(W_n)` finite words with `s ≠ W_n^∞` for all `n`. If
> ```
> limsup_n S_s(W_n) = +∞,
> ```
> then `Φ(s) ∉ Q`.

**Proof.** Suppose `Φ(s) = u/v ∈ Q`, height `H`. By `(‡)`, `S_n ≤ log₂H` for *every* `n`, i.e. `S_n` is bounded above by the constant `log₂H` — contradicting `limsup_n S_n = +∞`. ∎

**This is `PROVED`** — a direct, unconditional consequence of Propositions 2.2 and 4.1 alone (Classification A and B in `CURRENT_BRIDGE.md`), with **no** discrepancy, balance, repetition-exponent, or continued-fraction hypothesis anywhere in the proof. Those enter only in *constructing* sequences `(W_n)` for which the hypothesis `limsup S_n = +∞` can actually be *verified* — that is the content of Parts 4–5 (`DISCREPANCY_HEIGHT_THEOREM.md`, `REPETITION_HEIGHT_CRITERION.md`), not of this theorem itself.

## Sharpness of the criterion — `limsup`, not `→ +∞`

The task's proposed formulation asked whether `L_n − log₂F(W_n) → +∞` (a genuine limit) is the right sufficient criterion. **It is not the sharpest correct statement — `limsup = +∞` is strictly weaker and is exactly what the proof uses.** The proof only needs, for *each* candidate height `H`, *some* `n` with `S_n > log₂H`; a sequence with `S_n` oscillating (e.g. `S_n = n` for even `n`, `S_n = 0` for odd `n`) still has `limsup = +∞` and the theorem applies, even though `S_n → +∞` fails (the sequence does not converge). **This matches, and explains, why the paper's own Theorem 10.1 only asserts "such `ℓ` are unbounded"** (Theorem 10.2 gives infinitely many square half-lengths, not a monotonically-behaving sequence) — the paper already implicitly uses the sharp `limsup` form, not a full-limit form, and this audit's derivation confirms that is exactly the correct level of generality, not an accidental weakening.

## No hidden logarithmic/polynomial correction terms

The task asked whether logarithmic or polynomial error terms alter the criterion. **They do not, because none are hidden**: `(‡)` is an *exact* inequality for every single `n`, not an asymptotic statement with an implicit `O(·)`. Every correction term that could matter (the `log₂F(W_n)` itself, which typically has a `ℓ_n`-linear leading part plus lower-order terms once `F` is pinned down explicitly in Part 4) is already accounted for *inside* `S_n`'s own definition. The criterion `limsup S_n = +∞` is therefore already in its sharpest, fully-corrected form; no further asymptotic slack needs to be added or can be safely removed.

## Classification

**PROVED.** Sufficient, general, and sharp *as a sufficiency criterion for this specific method* (see `BRIDGE_CONTROLS.md` and `FALSIFICATION_REPORT.md` for why it is not, and should not be expected to be, necessary). Terminology `S_s(W)` is used here only as a bookkeeping label for this audit, per the task's instruction not to canonize new terminology before the criterion survives further scrutiny (Parts 3–4 below).
