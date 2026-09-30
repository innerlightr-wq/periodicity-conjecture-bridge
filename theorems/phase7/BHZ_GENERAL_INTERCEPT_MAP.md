> **CORRECTED BY PHASE 8 — see [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md).**
> Items **C2** (the exceptional-orbit reduction in this file is **refuted**), **C3** (the
> convergent denominators are mis-indexed: BHZ sets `q_1 = a_1 + 1`) and **C5** (`y(k)` is an
> attained power only when `0 < c_k < a_k`). Retained verbatim as the historical record.

# BHZ_GENERAL_INTERCEPT_MAP.md

Read directly from Berthé–Holton–Zamboni (2006), primary source, general (not `\omega(-\alpha)`-specialized) sections.

## S-adic / Ostrowski representation

Every Sturmian sequence: `\omega=T^{c_1}\circ\tau_0^{a_1}\circ T^{c_2}\circ\tau_1^{a_2}\circ\cdots`, `\tau_0(0)=0,\tau_0(1)=01`, `\tau_1(0)=10,\tau_1(1)=1`. `(a_k)_{k\ge1}` = partial quotients of the slope. `(c_k)_{k\ge1}` = **Ostrowski digits of the intercept**.

**Admissibility condition (1)** (exact): `a_k\ge c_k\ge0` for all `k`, `a_k\ge1` for `k\ge2`, and **if `c_k=a_k` then `c_{k-1}=0`**. The characteristic sequence is `c_k\equiv0`.

## General formula (Corollary 3.5, exact quote)

```
x'(k) = [ sum_{j=1}^{k+1} (a_j-c_j) q_{j-1} ] / q_k
y(k)  = 1 + [ sum_{j=1}^{k} (a_j-c_j) q_{j-1} ] / (q_k - c_k*q_{k-1})
ice(omega) = limsup_k max(x'(k), y(k))
```
`q_j` the convergent denominators of `\alpha=[0;a_1,a_2,\ldots]`, `q_0=1$, `q_{-1}=0`. **This is fully general** — no periodicity, no restriction on `(c_k)` beyond admissibility.

## How initial powers are constructed (the achieving words)

BHZ's proof (§3, Proposition 3.3) constructs, for each `k`, an **explicit word** — a cyclic permutation of a specific substitution image `\tau_0^{a_1}\circ\tau_1^{a_2}\circ\cdots\circ\tau_{k-1}^{a_k-c_k}(i)` — that is a genuine prefix power of `\omega` achieving exactly `y(k)` (their words: "this is exactly the value of `r`"). **These are real, growing-length, actually-occurring initial powers, for any admissible `(c_k)`, not merely an abstract supremum.** Root lengths grow with `k` (each stage composes another morphism onto a nonempty word), confirmed general.

## Exceptional-orbit structure (Proposition 2.1, Lemma 2.2) — the key structural fact for this phase

- `\text{ice}(\omega)\le\text{ice}(T\omega)`, **with equality unless `T\omega` is left-special.**
- For Sturmian `X_\alpha`, the complexity `p(n)=n+1` has constant first difference `1`, so (Proposition 2.1(4)'s proof) **there is exactly one left-special sequence** — the characteristic sequence itself, confirming the source paper's own statement ("the characteristic sequence... is the unique left-special sequence").
- **Consequence, chained**: `\text{ice}(\omega)=\text{ice}(T\omega)` for every `\omega` **except** when `T\omega` equals the characteristic sequence — i.e. except when `\omega\in\{\omega(-\alpha),\omega(1-\alpha)\}` (its two shift preimages). Iterating: `\text{ice}(\omega)` is **constant along the entire forward orbit of `\omega`**, unless that orbit ever lands on `\omega(-\alpha)` or `\omega(1-\alpha)`.
- `ind^*(\alpha)=\max_{X_\alpha}\text{ice}` (Proposition 2.1(2), minimality), and (Proposition 2.1(4)/(5), Lemma 2.2) `\text{ice}(\omega)=ind^*(\alpha)$ **for almost every `\omega\in X_\alpha`** (every orbit except a finite/countable exceptional set tied to the characteristic sequence's own backward-preimage structure).
- **Translated to intercepts**: `\text{ice}(\omega_\rho)=ind^*(\alpha)$ for **every intercept `\rho`** except those in the countable set `\{j\alpha\bmod1:j\in\mathbb Z\}` — exactly the "return" intercepts `\rho=\{j\gamma\}` that the **source paper's own Sections 6–8 depth-law route** (Theorem 6.1, Corollary 7.2) already handles, by a *different* method, for the Sturmian word `u` itself (not yet for the Rote-transferred `v` — see `INTRINSIC_SQUARE_ROUTE.md`).

## `ind^*(\alpha)` for bounded type, re-derived

`ind^*(\alpha)=2+\limsup_k[a_k;a_{k-1},\ldots,a_1]` (source, quoted in BHZ's introduction, citing Vandeth [43]). Same elementary bound as `theorems/phase6`'s `\text{term2}` analysis: `[a_k;\text{rest}]\ge a_k\ge1`, and — the useful direction here — `[a_k;\text{rest}]<a_k+1\le A+1`, giving `ind^*(\alpha)<A+3`; the **lower** bound `ind^*(\alpha)\ge3+1/(A+1)$ (re-derived exactly as `theorems/phase4/INITIAL_EXPONENT_FORMULA.md`'s `\text{term2}` bound, one level up) — **strictly larger than the intercept-`0` margin `2+1/(A+1)$** used throughout Phases 4–6.

## Summary of what this means for Phase 7

For **generic** intercepts (all but the countable "return" set), the available margin is *larger* than at intercept `0`, not smaller. The genuinely open cases are the countable exceptional set — of which intercept `0` (`j=0`) is already fully proved (Phases 4–6); other members (`j\ne0`) are the actual open question, addressed in `INTRINSIC_SQUARE_ROUTE.md` and `OSTROWSKI_PATTERN_CLASSIFICATION.md`.
