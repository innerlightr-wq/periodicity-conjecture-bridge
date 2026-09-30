**SCOPE OF "ALL 21 APERIODIC FIXED POINTS" — NARROWER THAN IT SOUNDS, AND SUBSUMED ANYWAY**

# SUBSTITUTION_SWEEP_SCOPE.md

Audit of Phase 9 Corollary 4.2 (`scripts/phase9/phase9_automatic_sweep.py`).

## 1. What was actually enumerated

| constraint | value |
|---|---|
| alphabet | `{0,1}` only |
| substitution lengths | `k = 2` and `k = 3` only |
| prolongable seed | `σ(0)` must begin with `0`, so the fixed point is `σ^∞(0)` and begins with `0` |
| excluded | `σ(0) = σ(1)` (not a substitution on two letters in any useful sense) |
| aperiodicity filter | finite test: no preperiod `< 64` with period `< 400` on a prefix of length `≥ 4096` |
| fixed-point length used | `2^16` (`k=2`) / `3^10` (`k=3`) |

Counts: `k = 2` gives `σ(0) ∈ {00, 01}`; `σ(0) = 00` yields the periodic `000…`, and `(01,11)`
yields the eventually periodic `0111…`, leaving **2**. `k = 3` gives `4 × 8 − 4 = 28` candidates, of
which **19** survive the filter. **2 + 19 = 21.**

## 2. What "all 21" does **not** mean

- **Not all uniform substitutions.** `k ≥ 4` untested; the count grows as `2^k·(2^k − 1)/…` and
  nothing here extrapolates.
- **Not all binary substitutions.** Non-uniform ones (Fibonacci, `0→01, 1→0`) are excluded outright:
  the propagation lemma `lcp(σx,σy) = k·lcp(x,y) + cst` uses `k`-uniformity essentially.
- **Not all automatic sequences.** A `k`-automatic sequence is a letter-to-letter *projection* of a
  fixed point of a `k`-uniform substitution on a possibly larger alphabet. Rudin–Shapiro and the
  regular paperfolding word are of that kind and are **not** in the sweep; nothing here covers them.
- **Not all morphic words.** Strictly larger again.
- **Not closed under `0↔1` exchange.** Only `σ(0)`-prolongable substitutions were taken. The
  complementary fixed points (beginning with `1`) are different words with density `1 − γ`, and were
  not enumerated. No identification or de-duplication up to exchange, mirror or conjugacy was applied,
  so "21" counts *substitution pairs*, not equivalence classes of words.
- **Aperiodicity is not proved.** It is a finite test with a hard-coded preperiod and period bound.
  Two earlier candidates were reclassified as eventually periodic precisely because the first version
  of that filter was too weak. Any member could in principle still be eventually periodic with a
  longer preperiod or period.

## 3. Certified finite check versus proof, per ingredient

| ingredient | status |
|---|---|
| `lcp(σ(x),σ(y)) = k·lcp(x,y) + lcp(σ(0),σ(1))` for `x ≠ y` | **PROVED** (uniformity + first differing letter) |
| `r_m` non-decreasing with limit `r_∞ = (L_0 + cst/(k−1))/|W_0|` | **PROVED**, given the base case |
| the base case `(|W_0|, L_0)` for each substitution | **certified finite check** (literal `lcp`) |
| density `γ_m → γ*`, the letter frequency | **standard** (Perron–Frobenius for primitive `σ`); **primitivity was not checked per row** |
| `D(W_m) = o(|W_m|)` | **quoted, not proved here**: the `O(|W|^θ)`, `θ = log|λ₂|/log k < 1` bound for primitive uniform substitutions. No reference was supplied and no row was verified. **This is the weakest link in Corollary 4.2.** |
| `2^{lcp} > F(W)` at one finite `m` per row | **certified finite check**, exact integers |
| aperiodicity | **finite test only** |

So Corollary 4.2 is, honestly stated: *for each of 21 explicitly listed substitutions, a certified
finite computation plus a proved propagation lemma plus an unverified quoted discrepancy bound.* It
is not a theorem about automatic sequences, and it was over-stated in `PHASE9_VERDICT.md` §6 item 2
as licensing a sweep of "the whole `k`-automatic family".

## 4. And it is subsumed regardless

`THUE_MORSE_LITERATURE_AUDIT.md` §4: for a `k`-uniform substitution the letter frequencies are the
normalised left Perron eigenvector for the integer eigenvalue `k`, hence **rational**, hence `≠ β`
(irrational). Classification of all 21 by which half of the known dichotomy applies
(`data/phase9b/tm_subsumption_check_output.txt`):

```
15 of 21   density < beta   -> Monks-Yazinski 2004 Thm 2.7(b)   [refereed]
 4 of 21   density > beta   -> Lopez-Stoll 2021 Thm 1           [preprint]
 0 of 21   density = beta
```

Sample: `σ = (001,000)` density `1/4`; `(010,001)` density `1/3`; `(001,011)` density `1/2`;
`(011,101)` and `(011,110)` density `2/3`; `(001,111)` and `(010,111)` density `≈ 0.98266`.

So the sweep establishes nothing that was not already available — and for the four members above `β`
the only available prior source is an **unrefereed preprint**, which is the one place where the
sweep still has marginal value as an independent confirmation.

## 5. What would make a sweep worth doing

Only a class placed at, or straddling, density `β`. Uniform substitutions cannot do it (rational
frequencies). A non-uniform primitive substitution can have irrational frequencies — the Fibonacci
word has density `1/φ² = 0.38197` (still `< β`), but a substitution whose Perron frequency equals
`β` would need `β` to be an algebraic unit of the right degree, and `β = log₃2` is transcendental
(Gelfond–Schneider). **So no primitive substitutive word has density exactly `β`**, and no
substitution sweep can ever reach the one uncovered density. That is a structural reason to stop
this line, not merely a budget one.
