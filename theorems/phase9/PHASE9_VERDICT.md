**TWO NEW THEOREMS, ONE STANDING CLAIM REFUTED, ONE EXPLICIT FAMILY DEFEATING THE CRITERION**

# PHASE9_VERDICT.md

Branch `phase9-unbounded-type`, cut from `phase8-general-intercept` at HEAD `3b321c0`.
Nothing pushed; Revision 2 release artifacts untouched and byte-identical.

## 1. Strongest proved extensions

> **THEOREM 3 (unbounded-type CS Rote bridge, parity form).** Let `γ ∈ (0,1)` be irrational, **with
> no hypothesis whatever on its partial quotients**. Let `u` be any Sturmian word of slope `γ` (any
> intercept, either mechanical convention), with BHZ digits `(a_k)`, admissible Ostrowski digits
> `(c_k)`, `d_k := a_k − c_k`. If infinitely many `k ≥ 3` satisfy
> `0 < c_k < a_k`, `d_{k−1} ≥ 1`, and `d_k p_{k−1} + p_{k−2}` **even**,
> then `Φ(v) ∉ ℚ` for either CS Rote lift `v` (either seed) and every shift `σ^j(v)`.

Proof in `PHASE9_PROOF_OR_COUNTEREXAMPLE.md` §1. **Why it escapes bounded type:** the even-weight
branch needs only `r > g(γ_V)` where
`g(γ) = max(1, γ log₂3) + γ(1−γ) log₂3 ≤ log₂3 < 2`, and that bound uses only the *combinatorial*
discrepancy cap, valid for every binary word. The odd branch's discrepancy estimate — the sole
carrier of the bounded-type hypothesis in Phase 8 — is never invoked.
Corollary 3.1: every slope with `a_2` odd and `a_k` even for `k ≥ 3`, at BHZ's keep-one intercept,
qualifies at **every** `k ≥ 3`, with partial quotients growing arbitrarily fast. Corollary 3.2: the
covered class contains uncountably many unbounded-type slopes. Verified end-to-end (36 exact
evaluations, including `sup a_k` up to 40 320).

> **THEOREM 4 (sharpened repetition–height criterion).** Let `s` be aperiodic. Suppose there are
> prefixes `W_n` of `s`, `ℓ_n = |W_n| → ∞`, `γ_n = |W_n|_1/ℓ_n`, `r_n = lcp(s, W_n^∞)/ℓ_n`, with
> `r_n ≥ g(γ_n) + ε` for some fixed `ε > 0`. Then `Φ(s) ∉ ℚ`.

This replaces the uniform threshold `log₂3` of `theorems/phase1/REPETITION_HEIGHT_CRITERION.md` by
the `γ`-dependent `g(γ)`, which is strictly smaller for every `γ < 1` (`g(1/2) = 1.39624`,
`g(1/5) = 1.25359`, `g → 1` as `γ → 0`). **Consequence: initial squares are not needed.**

> **COROLLARY 4.1.** `Φ(Thue–Morse) ∉ ℚ.`

Proof: `t = μ^∞(0)`, `μ(0)=01`, `μ(1)=10`. `W_0 := t[0{:}24]` has `lcp(t, W_0^∞) = 40`, i.e. prefix
power exactly `5/3`, and `|W_0|_1 = 12` (density exactly `1/2`) — verified two independent ways.
`μ` is 2-uniform, `μ(t) = t`, and `μ(0), μ(1)` differ in their first letter, so
`lcp(μ(x),μ(y)) = 2 lcp(x,y)` exactly; hence `W_m := μ^m(W_0) = t[0{:}24·2^m]` has
`lcp(t, W_m^∞) = 40·2^m`, prefix power `5/3` and density `1/2` for **every** `m`. The `±1`
Thue–Morse partial sums lie in `{−1,0,1}`, so `D(W_m) = 1/2` uniformly. Since
`5/3 − g(1/2) = 0.270426 > 0`, Theorem 4 applies. Checked with exact integers: `2^{lcp} > F(W_m)`
for `m = 0..8`, exact surplus `14.73, 30.67, 62.68, …, 4094.68`, growing with `S/|W| → 2/3`.

> **COROLLARY 4.2 (automatic sequences).** Let `σ` be a `k`-uniform substitution on `{0,1}` with
> aperiodic fixed point `t = σ^∞(0)`. Since `lcp(σ(x),σ(y)) = k·lcp(x,y) + lcp(σ(0),σ(1))` for
> `x ≠ y`, the prefix powers of `W_m := σ^m(W_0)` are non-decreasing in `m` with limit
> `r_∞ = (L_0 + cst/(k−1))/|W_0|`, `cst := lcp(σ(0),σ(1))`; the densities converge to the frequency
> `γ*` of `1` in `t`; and for a primitive uniform substitution the prefix discrepancy is
> `O(|W|^θ)`, `θ = log|λ_2|/log k < 1`, hence `o(|W|)`. So Theorem 4 applies whenever
> `r_∞ > g(γ*)`.
>
> **Swept exhaustively for `k = 2, 3`: all 21 aperiodic fixed points are reached**, each with
> positive **exact integer** surplus (`2^{lcp} > F(W)`), including Thue–Morse (`r_∞ = 5/3`) and the
> period-doubling word (`r_∞ = 2`). The two substitutions with `r_∞ = 1` have *eventually periodic*
> fixed points, which the Periodicity Conjecture excludes, so they are not failures.

Status: the `k = 2,3` sweep is a **certified finite check** of the exact surplus plus the quoted
standard sublinear-discrepancy fact for primitive uniform substitutions, which is cited, not proved
here. The Thue–Morse case is fully proved, because there `D(W_m) = 1/2` exactly.

## 2. The standing scope claim is **refuted**

`theorems/phase1/FULL_PERIODICITY_GAP.md` Q4 — repeated in `LADDER.md`, `THEOREM_STATUS.md`, and
**Revision 2 of the deposited note** (§15 Open 6 and the abstract) — asserts that Thue–Morse has no
initial square and is therefore beyond "every purely repetition-based method … by construction".
The observation is correct; the inference is not. The criterion's threshold is `g(γ) < log₂3 < 2`,
and at density `1/2` an exponent of `5/3` clears it with margin `0.27`. **Thue–Morse is reached.**

What survives: a word whose initial prefix powers satisfy `r_n → 1` fast enough *is* out of reach,
since `g(γ) > 1` for every `γ > 0`. So a structural ceiling for this method exists, but it must be
stated as a *quantitative* condition on `limsup ℓ_n(r_n − g(γ_n))`, and **no explicit aperiodic word
is currently known to this record to satisfy it.** Exhibiting one is now an open problem in its own
right. This requires an erratum; see §5.

## 3. The explicit family that defeats the current criterion

`PHASE9_FAILURE_SET_AUDIT.md` §5. Take `a = [3, 1, 2·2^{2^1}, 2·2^{2^2}, …]` (all digits even from
`k = 3`, tower-fast) with `c_k = a_k − 2` (so `d_k = 2`, even). Then every `p_k` is odd, so the
`x`-root weight `p_k` is odd; and the `y`-root weight `≡ d_k + 1 ≡ 1` is odd too — **no guaranteed
even-weight root exists at any scale**, structurally. The even branch is unavailable, the odd branch
is forced, and the growth condition breaks:

```
 k   ell_k    driver ell_k E_k    sum b_i   penalty est   driver/penalty
 4      93              11          15         30.77          0.357
 5    2870              60          32         62.72          0.957
```

| level | verdict |
|---|---|
| **(a)** sufficient growth condition `(H)` | **FAILS** from `k = 4` |
| **(b)** estimated surplus bound | **FAILS**, same estimate |
| **(c)** exact integer surplus at selected witnesses | **HOLDS wherever computable**: `k=3` (`ℓ=44`, `S=15.33`), `k=4` (`ℓ=93`, `S=10.34`), `2^{L_v}>F` both. Beyond `k=5`, `q_k > 10^{150}`: **not determined** |
| **(d)** every available witness family | **NOT DETERMINED** |

The `k = 4` row is decisive: `(a)` and `(b)` already fail there and `(c)` still holds, because the
three-distance bound gives `Σb_i = 15` (penalty `30.8`) while the actual `D(R) = 2` gives penalty
`≈ 10.7` against a driver of `11`. **The obstruction is in the estimate of `D(R)`, not in the
arithmetic.** This family is not a counterexample to `Φ(v) ∉ ℚ`.

## 4. Smallest remaining lemma

> **(L1)** For every Sturmian word `u` and all large `k`, the prefix of length `q_{k−1} + q_{k−2}`
> has prefix power `≥ 2/(1 + λ_{k−1})`, i.e. `lcp ≥ 2q_{k−1}`.

With (L1) the hostile family closes unconditionally: on an all-odd-numerator slope that root has
even weight `p_{k−1}+p_{k−2}`, and `2/(1+λ_{k−1}) > g(γ)` holds at one of any two consecutive
scales (if `λ_{k−1}` is near `1/2` then `a_{k−1} = 2` and `a_{k−2}` is large, forcing `λ_{k−2}`
small). (L1) is **proved for the characteristic word** from `s_k = s_{k−1}^{a_k}s_{k−2}`; the gap is
the general intercept, where the prefix of that length is not `s_{k−1}s_{k−2}`. Currently a
certified finite check: 27 hostile slope/intercept pairs, 144 exact even-branch surplus evaluations,
all positive.

## 5. Evidence classification, and what is owed

| status | items |
|---|---|
| **PROVED** | Theorem 3 + Corollaries 3.1, 3.2; Theorem 4; Corollary 4.1 (`Φ(TM) ∉ ℚ`); the `lcp(σx,σy) = k·lcp(x,y) + cst` lemma of Corollary 4.2; the driver identity `ℓ_kE_k = q_{k−2}(m_{k−1}−1)` for `k ≥ 2`; the attainment routing R1–R4; weight laws (W-y), (W-x); the numerator-parity characterisation (finite and asymptotic forms); `μ`-invariance of the Thue–Morse witness family |
| **CERTIFIED FINITE CHECK** | Corollary 4.2's sweep (21/21 aperiodic fixed points, `k = 2,3`, exact surplus positive) — modulo the quoted sublinear-discrepancy fact; 131 888 identity/routing instances; 4 984 weight-law comparisons; 144 exact even-branch surpluses on the hostile family; 36 Theorem-3 end-to-end evaluations; `2^{lcp} > F` for Thue–Morse, `m = 0..8`; exact surplus `(c)` on the double-failure family at `k = 3,4` |
| **NUMERICAL EVIDENCE** | that the `d=1` intermediate root always clears `g(γ)` (i.e. (L1)); that weight-law deviations stop at small `k` |
| **DISPROVED** | disjointness of the two obstructions (parity permits arbitrarily large even partial quotients); the universal exactness of `w(k,d) = dp_{k−1}+p_{k−2}`; the Thue–Morse structural-ceiling inference |
| **NOT DETERMINED** | `(c)` and `(d)` on the double-failure family beyond `k = 5`; whether any explicit aperiodic word defeats Theorem 4; **novelty of Corollary 4.1** — a targeted literature search found nothing on Thue–Morse and `Φ`, which establishes nothing either way and must be checked properly before any claim of priority |

**Erratum owed on Revision 2** (`10.5281/zenodo.23045141`, Revision 2): its abstract and §15 Open 6
state that Thue–Morse makes every repetition-based method structurally inapplicable. That is
refuted by Corollary 4.1. Also worth correcting there: the even-branch threshold is `g(γ)`, not the
uniform `log₂3`. **No publication action taken**; this needs author approval, exactly as Revision 2
did.

## 6. Next highest-value action

1. **Check the literature on Corollary 4.1 first-hand** before anything else. If `Φ(TM) ∉ ℚ` is new
   it is the most publishable item this programme has produced, and it is independent of the whole
   Sturmian/Rote apparatus — Theorem 4 needs only one prefix-power family with bounded discrepancy.
2. **Extend the automatic sweep** (Corollary 4.2 already does `k = 2,3` exhaustively, 21/21). Do
   `k = 4,5`, non-binary alphabets projected to `{0,1}` (Rudin–Shapiro, paperfolding), and then
   non-uniform primitive substitutions, where `lcp(σx,σy)` is no longer a clean multiple. Also
   supply the sublinear-discrepancy fact with a reference or a proof, since Corollary 4.2 quotes it.
3. **Prove (L1)** for general intercepts, closing the hostile family.
4. **Only then** the exact height estimate for the double-failure regime.
5. Restate the method's ceiling quantitatively in `FULL_PERIODICITY_GAP.md`, `LADDER.md` and
   `THEOREM_STATUS.md`, and try to exhibit an aperiodic word that genuinely defeats Theorem 4.

## 7. Reproducibility

```
scripts/phase9/phase9_witness_family.py      identity, routing, weights, parity
scripts/phase9/phase9_intermediate_roots.py  literal prefix powers, all intermediate roots
scripts/phase9/phase9_even_branch.py         g(gamma), adversarial search, exact even surplus
scripts/phase9/phase9_weight_stress.py       the weight formula is NOT universally exact
scripts/phase9/phase9_weight_law.py          the exact weight law (W-y)/(W-x)/(W-int)
scripts/phase9/phase9_failure_set.py         coverage, failure set, intermediate rescue
scripts/phase9/phase9_double_failure.py      odd-branch cover, (H), the double-failure family
scripts/phase9/phase9_theorem3_verify.py     Theorem 3 end to end
scripts/phase9/phase9_thue_morse.py          Corollary 4.1, exact integers
```

Outputs in `data/phase9/`. Exact `Fraction`/big-integer arithmetic; `F(W)` always evaluated
exactly, never bounded. Every script asserts its own claims — a non-zero exit means a claim failed.
