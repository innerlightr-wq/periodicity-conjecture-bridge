**THE NAMED WORD — PROPERTIES PROVED, COVERAGE AUDITED**

# EXPLICIT_CRITICAL_WORD.md

## 1. The word

> ```
> alpha = (sqrt5 - 1)/2 ,   rho = 1/7 ,   beta = ln2/ln3 = log_3 2 ,
> s_n = 1   <=>   { n*alpha + rho }  in  [0, beta) .
> ```

`s[0:40] = 1010110110101101101011010110110101101111`.

**Consistency with Phase 10's hypotheses**, checked before any work: Phase 10 requires `α` a
quadratic irrational and `ρ ∉ ℤα + ℤ`. Here `α` satisfies `α² + α − 1 = 0` ✓, and `1/7 = mα + n`
would force `α ∈ ℚ` ✓. The slope and intercept are **not** substituted anywhere below.

**Arithmetic discipline.** All `α`-arithmetic is *exact* in `ℚ(√5)` (`scripts/phase11/exact_word.py`):
numbers are `a + b√5` with `a,b ∈ ℚ`, sign is decided by comparing `a²` with `5b²`, and `floor` is
exact. Only comparisons against the transcendental `β` use a bracket (300 decimal digits); each such
comparison is either decided or raises `Undecided`. No symbol of `s` is guessed.

## 2. Aperiodicity — PROVED

If `s` had period `p ≥ 1` then for every `n`, `{nα+ρ}` and `{(n+p)α+ρ}` would lie on the same side of
the partition, i.e. the arc `[0,β)` would be invariant under rotation by `pα ≢ 0 (mod 1)`. A proper
arc of the circle is not invariant under a non-trivial rotation. ∎

## 3. Lower ones-density exactly `β` — PROVED

`k_N(s) = #{m < N : {mα+ρ} ∈ [0,β)}`, and `α` is irrational, so by Weyl equidistribution
`k_N/N → β`. The limit exists, hence `liminf = limsup = β`. ∎

This is the whole point: both T1 (Monks–Yazinski 2004 Thm 2.7(b), needs `liminf < β`) and T2
(arXiv:2101.12747 (2021) Thm 1, needs lower density `> β`) are **strict**, so neither applies.

## 4. Factor complexity — and the role of `β ∉ ℤα + ℤ`

`β = log₃2` is transcendental (Gelfond–Schneider: `3^β = 2` is algebraic, so `β` cannot be algebraic
irrational; and `β ∈ ℚ` would give `3^p = 2^q`). `α` is algebraic, so `ℤα + ℤ` consists of algebraic
numbers and **`β ∉ ℤα + ℤ`**. For a coding of an irrational rotation by a two-interval partition,
the endpoint condition is exactly the Sturmian/non-Sturmian dichotomy:

```
beta  in  Z*alpha + Z   ->   p(n) = n + 1   (Sturmian)
beta not in Z*alpha + Z ->   p(n) = 2n
```

(Rote, *J. Number Th.* **46** (1994) 196–213; Berstel–Vuillon, *Coding rotations on intervals*,
arXiv:math/0106217.) **Verified exactly here** at `n = 6, 12, 20`: `p = 12, 24, 40`. The value `2n`
for all `n` is cited, not re-proved.

**`β ∉ ℤα+ℤ` and `ρ ∉ ℤα+ℤ` are different conditions doing different jobs**, and conflating them
would be an error:

| condition | what it controls | what fails without it |
|---|---|---|
| `β ∉ ℤα + ℤ` | the **partition endpoint** relative to the rotation module — hence the complexity | `s` would be Sturmian (`p(n)=n+1`), covered by T4 |
| `ρ ∉ ℤα + ℤ` | the **orbit's starting phase** relative to the discontinuity at `0` | the orbit would hit `0` exactly; at `ρ = 0`, `L − ℓ = 0` and the witness is empty |

Additionally, and separately again, the **rationality** of `ρ = 1/7` is what makes the quantitative
bound of `ROTATION_REPETITION_LEMMA.md` R3 available. A merely irrational `ρ ∉ ℤα+ℤ` would give
aperiodicity and a non-degenerate orbit but **no** effective bound on the approach to `0`. The
theorem proved here is for `ρ = 1/7`, and that is not cosmetic.

## 5. Coverage audit

| exclusion | hypothesis | applies to `s`? |
|---|---|---|
| **T1** Monks–Yazinski 2004 Thm 2.7(b) [refereed] | aperiodic, `liminf k_n/n < β` | **No** — density is `= β` |
| **T2** arXiv:2101.12747 (2021) Thm 1 [preprint] | aperiodic, lower density `> β` | **No** — density is `= β` |
| **T3** Dubickas transported (foundation Cor. 9.3) | `liminf p(L)/L < 1/log₂(3/2) = 1.70951129…` | **No** — `liminf p(L)/L = 2` |
| **T4** foundation Thm 10.1 (all Sturmian) | `s` a mechanical word, `p(n) = n+1` | **No** — `p(20) = 40 ≠ 21` |

**Novelty status: unresolved, and deliberately stated as such.** Phase 10's literature audit located
no result covering lower ones-density exactly `β` at complexity `2n`, and the coverage above is by
*implication* from the hypotheses, not by absence of a paper naming the class. Absence of a hit is
not proof of absence. What *is* established is that the four exclusions above do not reach `s`.

A final guard demanded by the task: `s` is not a disguised covered word. It is not a finite
modification or shift of a Sturmian word (complexity is shift- and finite-modification-invariant
asymptotically, and `2n ≠ n+1`), and it is not related to a density-`1/2` word by any transformation
T1/T2 can see, since those read only the density.
