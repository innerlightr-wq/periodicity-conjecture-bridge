# ABSTRACT_IRRATIONALITY_CRITERION.md

Pure arithmetic re-derivation, no Sturmian or Rote terminology. This restates `ABSTRACT_BRIDGE_THEOREM.md`'s content but works through every subtlety the task lists explicitly, as a standalone check rather than by reference.

## Setup

`s ∈ {0,1}ℕ` an aperiodic binary word (viewed via `Φ` as an element of `Z₂`). `(W_n)` a sequence of finite binary words with `ℓ_n=|W_n|→∞`, `k_n=|W_n|_1`. Assume `s ≠ W_n^∞` for every `n` (the only standing hypothesis on the pair `(s,W_n)`). Set `L_n = lcp(s,W_n^∞)`.

By Proposition 4.1 (general, no periodicity/Sturmian hypothesis on `W_n`):
```
Φ(W_n^∞) = c_{W_n} / (2^{ℓ_n} − 3^{k_n}),    δ_n := 2^{ℓ_n} − 3^{k_n}.
```

Suppose `Φ(s) = u/v ∈ Q`, written in **lowest terms**, `v ≥ 1`. Since `Φ(s) ∈ Z₂` and `Z₂ ∩ Q` consists exactly of rationals with odd denominator (in lowest terms), `v` is odd. Set `H = max(|u|,v)`.

## Checklist, item by item

**Zero denominators impossible.** `δ_n = 2^{ℓ_n}−3^{k_n} = 0` would require `2^{ℓ_n}=3^{k_n}`; by unique factorization this forces `ℓ_n=k_n=0` (both sides equal 1), excluded since `ℓ_n→∞`. **For every `n` under consideration, `δ_n ≠ 0`, hence `Φ(W_n^∞)` is a well-defined rational number.**

**`δ_n` is odd.** `2^{ℓ_n}` is even (`ℓ_n≥1`), `3^{k_n}` is odd; even minus odd is odd. **`δ_n` odd for every `n≥1` with `ℓ_n≥1`.**

**`M_n ≠ 0`.** Define `M_n := u δ_n − v c_{W_n} = v δ_n (Φ(s) − Φ(W_n^∞))`, the second equality by direct substitution of `Φ(s)=u/v` and `Φ(W_n^∞)=c_{W_n}/δ_n`, valid since `δ_n≠0`. `M_n=0 ⟺ Φ(s)=Φ(W_n^∞)`. `Φ:\{0,1\}ℕ → Z₂` is a bijection (the source paper's own Proposition 2.2/2.3 apparatus — injective and surjective onto `Z₂`), so `Φ(s)=Φ(W_n^∞) ⟺ s = W_n^∞`, excluded by hypothesis. **`M_n ≠ 0` for every `n`.**

**Possible cancellation — does it matter?** No. `M_n` is defined and bounded using `u,v,δ_n,c_{W_n}` **directly as integers**; the argument never forms or simplifies the fraction `c_{W_n}/δ_n`. Whether `gcd(c_{W_n},δ_n)>1` is irrelevant to both the valuation computation and the triangle-inequality bound below — cancellation would only matter if the argument passed through a reduced fraction, which it does not.

**Reduced versus unreduced periodic rational value — does it affect the valuation step?** No, and this is worth deriving explicitly since it is not obvious a priori. `v₂(M_n) = v₂(vδ_n) + v₂(Φ(s)−Φ(W_n^∞))` (valid since `vδ_n` is a nonzero **integer**, so `v₂` is additive across the product) `= 0 + v₂(Φ(s)−Φ(W_n^∞))` (as `v,δ_n` both odd) `= lcp(s,W_n^∞) = L_n`, the last equality being Proposition 2.2's isometry applied to the two 2-adic integers `Φ(s)` and `Φ(W_n^∞)` **as values**, not as fraction representations. The isometry identity `v₂(Φ(a)−Φ(b))=lcp(a,b)` depends only on `a,b∈\{0,1\}ℕ`, never on how `Φ(a)` or `Φ(b)` happen to be written as a fraction. **Reducedness of `c_{W_n}/δ_n` is therefore a complete non-issue for the valuation step.**

**A genuine (unpursued) refinement available via reduction.** Let `g_n=\gcd(c_{W_n},δ_n)`, `c_n'=c_{W_n}/g_n`, `δ_n'=δ_n/g_n` (so `c_n'/δ_n'` is `Φ(W_n^∞)` in lowest terms; `δ_n'` is still odd, dividing the odd `δ_n`). Repeating the argument with `M_n' := uδ_n'-vc_n'` gives the same valuation `v₂(M_n')=L_n` (identical proof) but a **tighter** archimedean bound, `|M_n'|≤H(|δ_n'|+c_n')≤H(|δ_n|+c_{W_n})`, since `g_n≥1`. **This means the crude bound `F(W)` used throughout is not always tight when `\gcd(c_W,δ_W)>1`; a sharper, reduction-aware height is available in principle.** Not pursued further here — `F(W)` is already sufficient for every theorem in this phase — but flagged as a legitimate strengthening for future work (relevant if a future target class needs the extra margin).

**2-adic lower bound.** `M_n` a nonzero integer, `v₂(M_n)=L_n` exactly ⟹ `2^{L_n} | M_n` and
```
|M_n| ≥ 2^{L_n}.                                                              (★)
```
Exact, no slack.

**Archimedean upper bound.** `|M_n| = |uδ_n − vc_{W_n}| ≤ |u||δ_n| + v\,c_{W_n} ≤ H(|δ_n|+c_{W_n})`. Define
```
F(W) := |2^{|W|}−3^{|W|_1}| + c_W        [note: |δ_n|, not max(2^ℓ,3^k) — see remark below]
```
so `|M_n| ≤ H·F(W_n)`. **(†)**

**Remark: two admissible packagings of `F`.** `|δ_n| ≤ max(2^{ℓ_n},3^{k_n})`, so `F(W):=|δ_W|+c_W` (used here, the *proof-native* form) is always `≤` the Phase 1 packaging `F(W):=\max(2^{|W|},3^{k(W)})+c_W`. Both are valid upper bounds satisfying (†); the `|δ_W|`-form is never worse and is strictly better whenever `2^ℓ` and `3^k` are close (i.e. `ℓ/k` near `\log_2 3`). This phase uses `F(W):=|δ_W|+c_W` as the canonical definition going forward, consistent with `SURPLUS_INVARIANT.md`'s Phase 1 remark that this was already identified as the "proof-native" choice.

**Combine.** `(★)` and `(†)`: `2^{L_n} ≤ H·F(W_n)`, i.e.
```
L_n − \log_2 F(W_n) ≤ \log_2 H,   for every n.                                (‡)
```

**Whether logarithms need ceilings.** They do not, as a matter of *proof* — `(‡)` is a real-number inequality, exact, no rounding anywhere. Ceilings enter **only** when producing a machine-checkable **integer** witness of `S_n>0` from exact big-integer arithmetic: the decisive computational test is the direct integer comparison `2^{L_n} \overset{?}{>} H\cdot F(W_n)` (no logarithm evaluated at all), and `\lceil\log_2 F(W_n)\rceil` is used only as a human-readable, conservative integer summary of the margin, never as part of the proof itself. **This is worth stating cleanly: the theorem's proof needs no ceiling; only the numerical verification scripts use one, for display purposes.**

**Whether only unbounded surplus is required.** Yes — confirmed by re-deriving Phase 1's sharpness remark from scratch here: suppose `\Phi(s)\in Q` with height `H`. Then `(‡)` gives `S_n := L_n - \log_2 F(W_n) \le \log_2 H` for **every** `n` — a single fixed bound, independent of `n`. So if **any** subsequence has `S_n\to\infty` (equivalently `\limsup_n S_n = +\infty`, since a bounded-above sequence with `\limsup=+\infty` is a contradiction in terms — the two are equivalent here), the fixed bound is violated. **`\limsup_n S_n=+\infty` is exactly the right and sharp hypothesis; convergence of the full sequence `S_n\to+\infty` is not required** (an oscillating `S_n`, e.g. alternating between `0` and `n`, still refutes rationality, since `\limsup=+\infty` still holds even though the sequence does not converge).

## The theorem (clean restatement)

> **THEOREM (abstract 2-adic periodic-approximation criterion).** Let `s\in\{0,1\}^{\mathbb N}` and `(W_n)_{n\ge1}` finite binary words with `s\ne W_n^\infty` for all `n`. Define `S_s(W):=\text{lcp}(s,W^\infty) - \log_2\!\big(|2^{|W|}-3^{|W|_1}|+c_W\big)`. If
> ```
> \limsup_{n\to\infty} S_s(W_n) = +\infty,
> ```
> then `\Phi(s)\notin\mathbb Q`.

**Status: PROVED**, with every item on the checklist resolved explicitly above and none found to weaken the theorem. This is the exact foundation §§5–7 build on, and it contains no Sturmian or Rote terminology.
