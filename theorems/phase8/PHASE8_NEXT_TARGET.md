**NEXT TARGET — `ice = 2` DOES NOT KILL THE METHOD; THE OBSTRUCTION MOVES FROM REPETITION TO HEIGHT**

# PHASE8_NEXT_TARGET.md

Analysis of the frontier Theorem 2 leaves open: irrational slopes with **unbounded** partial
quotients, where BHZ Theorem 1.1 produces an intercept with `ice(ω) = 2` exactly.
`scripts/phase8/phase8_ice2_boundary.py`, `data/phase8/ice2_boundary_output.txt`.

## 1. Where exactly the boundary is

> **BHZ Theorem 1.1.** `X_α` contains a sequence with `ice(ω) = 2` **iff** for each pair `(s,t)`
> of positive integers with `s > 1` there are only finitely many `k` with `(a_k,a_{k+1}) = (s,t)`
> or `(a_k,a_{k+1},a_{k+2}) = (1,1,t)`.

Every such `α` has unbounded partial quotients (BHZ deduce this themselves), and the set of such
`α` has Lebesgue measure zero. Explicit families: `a_k = k`, `a_k = k²`, `a_k = 2^k` — all verified
to satisfy the condition, with BHZ's §5.3 minimiser giving `ice = 2.0011`, `2.0000069`,
`2.00000012` at the tested depths.

At such an intercept the two branches behave completely differently, and the difference is the
whole story:

| branch | required exponent | at `r_u = 2` | discrepancy hypothesis needed |
|---|---|---|---|
| even weight | `r_u > max(1, γ_V log₂3)` | margin `≥ 2 − log₂3 = 0.41504` | **none** (combinatorial cap suffices: `sup_γ[max(1,γlog₂3)+γ(1−γ)log₂3] = log₂3 < 2`, verified) |
| odd weight | `r_u > 2` | margin **exactly 0** | `D(R) = o(ℓ)` |

So the *fixed-margin* criterion dies on the odd branch, and only there.

## 2. The key finding: an exact identity says the odd branch survives anyway

The surplus is driven not by the excess `E_k := r_k − 2` but by `ℓ_k·E_k`. Those two are not
interchangeable, and Phase 7's `FLEXIBLE_MARGIN_BOUNDARY.md` was right to separate them. Phase 8
computes the product exactly.

> **Identity.** For every `k`, every admissible `(c_k)`, and every irrational slope — bounded type
> or not — the `y`-witness satisfies
>
> ```
> ell_k = q_{k-1}(lam_{k-1} + d_k),      E_k = y(k) - 2 = lam_{k-1}(m_{k-1} - 1)/(lam_{k-1} + d_k),
> ```
> so the root length and the denominator cancel exactly:
> ```
>            ell_k * E_k  =  q_{k-2} * ( m_{k-1} - 1 ) .
> ```
> On a keep-one tail (`d_{k-1} = 1`) this is `q_{k-2} lam_{k-2} m_{k-2} = q_{k-3} m_{k-2} ≥ q_{k-3}`.

*Proof.* Immediate from `PHASE8_PROOF_OR_OBSTRUCTION.md` Lemma 1. **Verified exhaustively**: 135 153
`(slope, admissible digit string, k)` instances across 5 slopes, exact arithmetic, no exception.

**Consequence.** `ℓ_k E_k ≥ q_{k-3} → ∞` whenever `d_{k-1} ≥ 1` and `d_{k-2} ≥ 1` — *even though
`E_k → 0`*. The repetition side of the criterion therefore does **not** fail at `ice = 2`. The
excess vanishes, but it vanishes exactly slowly enough that the product still diverges, because it
vanishes like `q_{k-3}/ℓ_k` and `ℓ_k` is what multiplies it.

Measured at the `ice = 2` slopes (`data/phase8/ice2_boundary_output.txt`):

```
slope          k    ell_k       ell_k*E_k    q_{k-3}     log2(2 ell_k)  sum a_i   (ell_k E_k)/log2(2 ell_k)
a_k = k       36    4.0e+40     3.4e+37      3.3e+37     135.9          666       2.5e+35
a_k = k^2     26    5.6e+50     1.6e+45      1.6e+45     169.6          6201      9.2e+42
a_k = 2^k     18    1.9e+46     2.2e+36      2.2e+36     154.8          524286    1.5e+34
```

The driver beats the logarithmic penalty by 34 to 43 orders of magnitude, and beats `Σ_{i≤k} a_i`
— the classical bound on the discrepancy penalty — by 30 or more.

## 3. So what is actually still missing: the height term

With the corrected surplus inequality, the odd branch needs

```
q_{k-3} * m_{k-2}   >>   ceil(D(R_k)) * log_2 3  +  log_2(2 ell_k)      for infinitely many k.
```

- The `log₂(2ℓ_k)` term is harmless: `log₂ℓ_k ≈ log₂ q_{k-1}`, and `q_{k-3}` is a product of
  partial quotients while `log₂ q_{k-1}` is a sum of their logarithms.
- The `D(R_k)` term is the real one. The **unconditional** combinatorial cap is useless here:
  `D(R) ≤ γ_R(1−γ_R)·2ℓ = ℓ/2`, so the penalty would be `≈ 0.79ℓ`, which swamps `ℓ_kE_k` as soon as
  `E_k < 0.79`. The bound that is actually needed is the Ostrowski/three-distance one,
  `D = O(Σ_{i≤j} b_i)` where `(b_i)` are the partial quotients of **`γ/2`** (`PHASE8_CHAIN_AUDIT.md`
  §3) and `q_j ≤ ℓ < q_{j+1}`. That is exactly where bounded type was being used.

So the frontier condition is a **growth condition on the partial quotients**, not a repetition
condition:

```
(H)   sum_{i <= k-1} b_i  =  o( q_{k-3} )      along infinitely many k,
      where (b_i) are the partial quotients of gamma/2.
```

`(H)` holds with enormous slack for polynomially and exponentially growing `a_k` (the table above).
It can fail only if some partial quotient is astronomically large relative to an earlier
convergent denominator — e.g. `a_k ≈ 2^{q_{k-1}}`, where `Σ_{i≤k-1} b_i ≳ a_{k-1} ≫ q_{k-3}`. Two
sub-questions, in order of tractability:

- **(H1)** Make `(H)` precise and prove the corresponding conditional theorem. This would extend
  Theorem 2 from "bounded partial quotients" to "partial quotients not growing faster than `(H)`
  permits" — a strictly and substantially larger class, containing every polynomially and
  exponentially growing continued fraction, hence uncountably many slopes of unbounded type.
  Needs one auxiliary estimate this repository does not have: a quantitative transfer
  `Σ b_i = O(Σ a_i)` from `γ` to `γ/2`. That is standard for `GL₂(ℚ)`-equivalent numbers but is
  **not verified here** — `PHASE8_CHAIN_AUDIT.md` §3 proves only the qualitative
  bounded-⟹-bounded form.
- **(H2)** Replace the discrepancy route by an exact height estimate. `c_R` is an explicit integer
  sum, `c_R = Σ_{i<|R|, R_i=1} 3^{k_R − k_{i+1}(R)} 2^i`; the discrepancy bound is only a
  convenient upper estimate of it. An exact or near-exact evaluation of `log₂ c_R` for a
  rotation-coded root — rather than a worst-case bound — would remove `(H)` entirely. This is the
  "exact height estimate" route, and it is the only one of the three that could close the *whole*
  unbounded-type case rather than a growth-restricted sub-case.

## 4. The even-weight route, and exactly how thin its failure set is

The even branch needs no margin and no discrepancy hypothesis, so it closes everything **if** it is
available infinitely often. Stated exactly:

> **(E)** For every Sturmian word `u` — any slope, any intercept — are there infinitely many
> initial powers `W^r` of `u` with `r ≥ 2` and `|W|_1` **even**?

If `(E)` holds, `Φ(v) ∉ ℚ` for both CS Rote lifts of **every** Sturmian word, with no hypothesis on
`γ` at all, and the `p(n) = 2n` rung closes completely.

`(E)` is elementary arithmetic, not new combinatorics. By BHZ Prop. 3.3 every initial power of
exponent `≥ 2` has root a cyclic permutation of a standard word, and by BHZ Lemma 2.6 the weights
are

```
x-witness root:  weight p_k                     (length q_k)
y-witness root:  weight p_k - c_k p_{k-1}        (length q_k - c_k q_{k-1})
```

with `p_k` the convergent **numerators**. So `(E)` is a parity question about `p_k` and
`p_k − c_k p_{k-1}`.

**How thin is the failure set?** `p_{k+1} = a_{k+1}p_k + p_{k-1}` with `p_0 = 0`, `p_1 = 1`, so
`p_2 = a_2`, and once `(p_{k-1},p_k) ≡ (1,1)` the next is odd iff `a_{k+1}` is even. Hence

```
p_k odd for every k >= 1   <=>   a_2 odd  and  a_k even for all k >= 3.
```

(Verified: `a = (3,1,2,2,2,…)` gives all `p_k` odd; an all-even digit string fails at once because
`p_2 = a_2`.) This is exactly the single "bad cycle" the Phase 3 automaton found, and it recovers
Phase 3's explicit counterexample from the parity side. So at intercept `0` the even branch **can**
be unavailable at every scale — but only on that thin family. At a general intercept the extra
term `c_k p_{k-1}` flips the parity whenever `c_k` is odd and `p_{k-1}` is odd, so general
intercepts have strictly **more** even-weight opportunities than intercept `0` — though the
intercept is given, not chosen, so this is not something a proof can help itself to.

**The honest worst case.** Nothing prevents a slope from being in the `(E)`-failure family *and*
the `(H)`-failure regime simultaneously (`a_k` even and astronomically fast-growing is perfectly
consistent). On such a slope, at such an intercept, neither route applies. That is a statement
about the current method, **not** an impossibility proof — see §6.

## 5. Intrinsic Rote repetition — literature first, and it does not answer this

The third route: does `v` itself carry initial powers not inherited from `u`? If `v` has
arbitrarily long initial squares of its own, the unconditional squares theorem
(`theorems/phase1/REPETITION_HEIGHT_CRITERION.md`) applies to `v` **directly**, with `r_v = 2 >
log₂3`, no transfer, no weight parity, no discrepancy hypothesis, and no hypothesis on `γ`.

There is primary literature this repository has never consulted:

- Ľubomíra Dvořáková, Kateřina Medková, Edita Pelantová, *Complementary symmetric Rote sequences:
  the critical exponent and the recurrence function*, Discrete Mathematics & Theoretical Computer
  Science **22** (2020); [arXiv:2003.06916](https://arxiv.org/abs/2003.06916).

Read at abstract level only, and recorded as such: it determines the **critical exponent** of CS
Rote sequences — powers occurring *anywhere* — via a formula in the continued-fraction expansion of
the associated standard Sturmian sequence, built on return words to bispecial factors. It does
**not** treat initial or prefix powers, and does not mention `ice`. So it does **not** answer route
(b) as stated. Two things it does supply, and one warning:

- the right machinery (return words to bispecial factors, and an explicit CF-indexed formula) for
  anyone attempting an *initial*-power analogue;
- a classification of CS Rote sequences with critical exponent `≤ 3`;
- **the warning**: they show uncountably many CS Rote sequences have critical exponent *below* the
  Fibonacci sequence's. Low global repetition bounds initial repetition from above, so route (b)
  cannot be assumed generous. It must be checked, not hoped for.

**This paper should be read first-hand before any new derivation on route (b).** It is the single
clearest instance in this programme of the lesson Phase 8 already learned once: the result may
already exist.

## 6. Failure of the criterion versus impossibility of the method

Kept strictly apart, as the task requires:

| level | statement | status |
|---|---|---|
| **L1** | the *fixed-margin* criterion (`E_k ≥ δ > 0`) fails at `ice = 2` | **TRUE, and provable** — `E_k → 0` by definition of `ice = 2`, and the odd branch's threshold is exactly `2` |
| **L2** | the *flexible* criterion (`ℓ_kE_k ≫ penalty`) fails at `ice = 2` | **FALSE** — the identity of §2 gives `ℓ_kE_k ≥ q_{k-3} → ∞`; measured slack of 34–43 orders of magnitude at the natural `ice = 2` families. L1 does not imply L2, and conflating them would be the single easiest mistake to make here. |
| **L3** | the *bridge* fails at `ice = 2` | **NOT SHOWN, and unlikely in general.** What can fail is condition `(H)`, a growth condition on the partial quotients, together with `(E)`, a parity condition. Both failure sets are thin and explicitly describable. |
| **L4** | no extension of the method can reach unbounded type | **NOT SHOWN, and not expected.** Three independent routes remain open (`H1`, `H2`, `(E)`, plus intrinsic Rote repetition), and `H2` in particular would dissolve the obstruction rather than route around it. |
| **L5** | no repetition-based method can reach *every* aperiodic word | **TRUE** — but for a different and already-recorded reason: `theorems/phase1/FULL_PERIODICITY_GAP.md` Q4 (Thue–Morse has no useful initial power at all). This is the real ceiling, and it is nowhere near the `ice = 2` boundary. |

## 7. Recommended order of attack

1. **(E) at intercept `0` first**, since the parity characterisation `a_2` odd and `a_k` even for
   `k ≥ 3` is already complete: check whether that family also forces `(H)` to fail, or whether the
   two failure sets are disjoint. If disjoint, `(E) ∨ (H)` already closes all of unbounded type,
   and the theorem follows with no new machinery at all. **This is the cheapest decisive experiment
   available and should be done before anything else.**
2. **(H1)**, the conditional growth theorem, plus the missing `Σ b_i = O(Σ a_i)` transfer estimate
   for `γ/2`. Self-contained, and yields a large new class immediately.
3. **Read Dvořáková–Medková–Pelantová first-hand** (§5) before any work on intrinsic Rote
   repetition.
4. **(H2)**, the exact height estimate, last: highest value, highest cost, and the only route that
   could remove the growth condition rather than restrict to it.
