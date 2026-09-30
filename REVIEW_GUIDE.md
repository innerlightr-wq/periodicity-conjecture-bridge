# REVIEW_GUIDE.md — a focused guide for number theorists and domain experts

This is the short path into the work for someone qualified to check it. It states the main theorem and
its assumptions, lists the four places where I most want an expert eye, and says what would invalidate
or narrow the result. It assumes no familiarity with the repository.

**Manuscript:** `technical-note/note_rev4.pdf`, deposited as Revision 4,
doi:[10.5281/zenodo.23070093](https://doi.org/10.5281/zenodo.23070093) — byte-identical to the file in
this repository. Section numbers below are Revision 4's.

**Standing caveats, stated once.** Nothing here has been refereed. The foundation paper it builds on
(doi:10.5281/zenodo.23019799) is also a preprint and is **by the same author** — a self-citation.
Novelty of the main result is **formally unresolved**. Nothing here proves the Collatz conjecture or
the 3x+1 Periodicity Conjecture in general.

## 1. The main theorem, exactly

Let `T : ℤ₂ → ℤ₂` be the `3x+1` map in the form `T(x) = x/2` for even `x`, `(3x+1)/2` for odd `x`, and
let `Φ` be the Bernstein–Lagarias conjugacy map sending a parity vector `v ∈ {0,1}^ℕ` to the 2-adic
integer whose `T`-itinerary has parity `v`. Put `β := ln2/ln3 = log₃2 = 0.6309297535…`.

> **Theorem** (Revision 4 Theorem 17.2 and Corollary 17.3; repository
> `theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md`).
> Let `α ∈ (0,1)` be a **quadratic irrational**. Let `u, ρ ∈ ℝ` with the offset `ρ − u`
> **algebraic** — `ρ` and `u` themselves unrestricted, so both may be transcendental. Define
> ```
> s_n = 1   <=>   { n*alpha + rho }  in  [u, u + beta)   (mod 1),    n = 0, 1, 2, ...
> ```
> Then `s` is aperiodic, has ones-density exactly `β`, has factor complexity `p_s(n) = 2n`, and
> **`Φ(s) ∉ ℚ`**.

**Assumptions, in full.**

| | assumption | where it is used |
|---|---|---|
| A1 | `α` quadratic irrational | *algebraic*: the `β`-boundary bound needs an algebraic coefficient. *Bounded type*: the `0`-boundary bound and the witness sizing. Quadratic gives both |
| A2 | `ρ − u` algebraic | both boundary bounds. This is the **only** arithmetic hypothesis on the intercept |
| A3 | interval length exactly `β` | the identity `β·log₂3 = 1`, which is what makes the height inequality collapse to `(L−ℓ) − O(log ℓ)` |

**What is not assumed.** No hypothesis on the intercept beyond A2; in particular `ρ = 0` and the case
`ρ ∈ ℤα+ℤ` (where the orbit hits a discontinuity exactly) are included, not excluded. No hypothesis
of bounded discrepancy. No periodicity of the continued fraction beyond what quadratic gives.

**Reduction to one case.** `1_{[u,u+β) mod 1}(x) = 1_{[0,β)}({x−u})` is an identity of arcs, valid also
when `u+β > 1` and the arc wraps. So WLOG `u = 0` and `ρ` algebraic (Revision 4 Corollary 17.3).

## 2. Dependency table

| id | input | source | status of source | used for |
|---|---|---|---|---|
| S1 | `v₂(Φ(a)−Φ(b)) = lcp(a,b)`; `Φ∘S = T∘Φ` | Bernstein–Lagarias, *Canad. J. Math.* **48** (1996) 1154–1169 | refereed | the valuation step |
| S2 | `Φ(W^∞) = c_W/(2^ℓ−3^k)` | foundation paper Prop. 4.1 | **preprint, self-citation** (re-derived and checked mod `2^60` here) | the approximants |
| S3 | quadratic ⟹ bounded partial quotients; `1/(q_{k+1}+q_k) < ‖q_kα‖ < 1/q_{k+1}` | Lagrange; Perron | classical | `0`-boundary, witness sizing |
| S4 | `\|b₁logα₁+b₂logα₂\| > Ce^{−(log B)^κ}`, **algebraic** `b_j` | Baker, *Mathematika* **14** (1967) 220–228, Thm 2; Part I (**13** (1966) 204–216) Thm 1.1 | refereed | the `β`-boundary |
| S5 | the same with an explicit constant | Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren **326** (2000), Thm 10.1 | refereed | the numerical constant |
| S6 | `N D_N ≤ 3 + (1/log φ + K/log(K+1))log N` | Kuipers–Niederreiter, Ch. 2 Thm 3.4, eq. (3.16) | refereed | drift and discrepancy |
| S7 | two-interval rotation coding has `p(n)=2n` iff endpoint `∉ ℤα+ℤ` | Rote, *J. Number Theory* **46** (1994) 196–213; Berstel–Vuillon | refereed / arXiv | the complexity value — **coverage claim only, never the proof** |
| S8 | Liouville's inequality | classical | the `0`-boundary at algebraic offsets |
| S9 | `log₃2` transcendental | Gelfond–Schneider | `β ∉ ℤα+ℤ`; the `β`-boundary is never hit |
| S10 | the **mechanism**: read the agreement excess as a first entry time of the rotation orbit into an arc at a partition endpoint | **foundation paper §12 open problem (1)** | **preprint, self-citation** | the shape of the whole argument. **Not original here** |
| — | Monks–Yazinski, *Discrete Math.* **275** (2004) 219–236, Thm 2.7(b) | refereed | used **only** to say which densities are already covered — not to prove anything |

**On results not used as premises.** The dependency table above lists everything the conclusions rest
on. Results that are relevant to the literature landscape but are not used as premises are discussed in
the manuscript; nothing in §3 below depends on any of them.

## 3. The four highest-priority checks

### (a) Waldschmidt's hypotheses and the height conversion

**Where.** Revision 4 §19.2, Remark 19.3 (the two height conventions) and Lemma 19.4; repository
`theorems/phase14/EXPLICIT_HEIGHT_BOUND.md` §1 and `theorems/phase13/EXPLICIT_CONSTANTS_STATUS.md` §2.

**What to check.** With `Λ_m = A_m log3 − log2`, `A_m = mα + ρ − j_m`:

1. that the hypotheses of Waldschmidt Thm 10.1 are met as stated — `n = 2`, `α₁ = 3`, `α₂ = 2`,
   `b₁ = A_m`, `b₂ = −1`, all non-zero algebraic; `D = [ℚ(A_m):ℚ]`; `log A_i ≥ h(α_i)` **and**
   `D log A_i ≥ e|ℓ_i|` **and** `A_i ≥ e`; `B ≥ (50nD log A)^{3n}`;
2. **the height conversion**, which is the single most likely place for an error. I use
   `h(1 : A_m : −1) ≤ ½log H(A_m) + 0.275`, from `h(a) = (1/d)log M(P)`,
   `M(P) ≤ ‖P‖₂ ≤ √(d+1)·H`, `h(−1) = 0` and `h(1:b₁:b₂) ≤ h(b₁)+h(b₂)`. Is the projective-height
   inequality being used correctly? Is `d = 2` the right degree throughout, including at `m = 0`?
3. that overestimating `B` is safe — I argue both hypotheses on `B` are lower bounds and the
   conclusion is monotone decreasing in `B`;
4. the arithmetic `c₁ = 100^6 · 2^4 · 1.493169 = 2.38907·10^13`.

**Also worth a sceptical look:** in Baker's Theorem 2 the hypothesis is that **either** the logarithms
**or** the coefficients be `ℚ`-independent. I use the first branch. The second branch *fails* at
`m = 0` when `ρ` is rational (`A_0 = 1/7 ∈ ℚ`), so the first branch is load-bearing — see Revision 4
§18 and `theorems/phase12/THEOREM11_INDEPENDENT_AUDIT.md` §4.

### (b) Discrepancy estimates, interval wrapping, and index conventions

**Where.** Revision 4 §19.1, Lemma 19.2 and Proposition 19.3; repository
`theorems/phase14/EXPLICIT_DISCREPANCY_CONSTANTS.md` §2.

**What to check.** Two adjustments carry Kuipers–Niederreiter's bound for `({nα})` to the drift of our
word, and each could be wrong:

1. **the factor 2 for the intercept.** `#{m<N : {mα+ρ} ∈ [0,β)}` counts `{mα}` in `[0,β) − ρ`, which
   mod 1 is one interval or two. I claim two intervals cost two applications of `D_N`, and that for
   `ρ = 1/7` the set `[−1/7, β−1/7)` genuinely wraps so the factor is incurred. Is `D_N`
   the right (extreme, not star) discrepancy for this, and is the constant 2 right rather than
   something smaller?
2. **`+1` for the index range.** KN count `n = 1,…,N`; the word is indexed `m = 0,…,N−1`.
3. that `D(W)` in the height lemma is deviation from the word's **own** density `k/ℓ`, not from `β`,
   and that `D(W) ≤ 2Δ(ℓ)` follows;
4. the log-base conversion `a·ln N = (a·ln2)·log₂N`. **I got this backwards on a first pass** and
   inflated `C_D` by `1/ln²2 ≈ 2.08`; the error is recorded rather than quietly fixed, and it is a
   good indicator of where to look.

### (c) Liouville separation and exact boundary hits

**Where.** Revision 4 §17, Lemma 17.1; repository
`theorems/phase13/ALGEBRAIC_INTERCEPT_THEOREM.md` §3.

**What to check.** With `θ_m = mα + ρ − j` (`j` nearest integer), `D = [ℚ(α,ρ):ℚ]`:

1. `deg θ_m ≤ D` and `H(θ_m) ≤ C_h m^D` — the conjugates are `O(m)`, so the elementary symmetric
   functions are `O(m^D)`. Is the denominator-clearing handled correctly?
2. the Liouville step `|θ| ≥ (1+H)^{−D}` for `θ ≠ 0` — I use `∏|roots| = |a₀/a_d| ≥ 1/H` and
   `|root| ≤ 1 + H/|a_d|`;
3. **the classification of exact hits**: `θ_m = 0 ⟺ ρ ∈ ℤα+ℤ`, and then the index is *unique* but may
   be **any** value (for `α = (√5−1)/2`, `ρ = 3−5α` it is `m = 5`);
4. that such a hit does **not** defeat the proof. Two independent treatments are given: the signed
   relaxation (for `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)` contains `0` in neither arc, so restrict to the
   `δ>0` convergents), and a reduction by finite shift using `Φ∘S = T∘Φ`. **Is the shift-invariance of
   rationality argued correctly in both directions?**
5. the unstated-then-stated hypothesis `|δ| ≤ min(β,1−β) = 0.3690702464` for the closed form of the
   mismatch set — it fails at `q₁ = 1` and the construction satisfies it with ~100× margin.

### (d) Coverage by prior results

**Where.** Revision 4 §15 (the density coordinate) and §20; repository
`theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md`, which places fourteen located results.

**What to check.**

1. that the results cited are stated with the hypotheses I ascribe to them — especially
   Monks–Yazinski Thm 2.7(b) (`liminf κ_n/n ≥ ln2/ln3` for a divergent rational orbit) and the
   transported Dubickas threshold `1/log₂(3/2) = 1.70951…`;
2. that lower ones-density of our word really is **exactly** `β` (Weyl; the limit exists) and factor
   complexity really is `2n`, so that neither a density nor a counting criterion applies;
3. **whether something I have not found already covers the family.** The `p`-adic low-complexity
   theorems (Adamczewski–Bugeaud; Bugeaud–Kekeç) constrain the **Hensel digit expansion** of a `p`-adic
   number, whereas our word is the **parity vector**; `Φ` is a 2-adic isometry conjugating the shift to
   `T` and is not digit-preserving. Is that distinction right, and is there a bridge I am missing?
4. the Hecke–Mahler line (Bugeaud–Laurent 2023; Luca–Ouaknine–Worrell 2025): I argue it fails twice
   over — archimedean, and its coefficient sequences are Beatty sequences `⌊kρ⌋`, whereas our
   `k_N = #{n<N : {nα+ρ} ∈ [0,β)}` is a Birkhoff sum over an interval of length `β ≠ α` with no
   floor-function closed form. Is that second point correct?

## 4. What would invalidate or narrow the theorem

Stated plainly, so that a reviewer knows what to aim at.

| finding | effect |
|---|---|
| Waldschmidt's or Baker's hypotheses not met as applied (check (a)) | **the theorem fails as proved.** The `β`-boundary has no other known lower bound |
| the height conversion wrong in the *unsafe* direction (i.e. my `B` too small) | **the theorem fails as proved**; a larger `B` would need re-deriving but the shape would survive |
| the discrepancy factor 2 or the `+1` wrong (check (b)) | the *constants* `C, C₀` change; the qualitative theorem survives, since only `O(log ℓ)` is needed |
| the Liouville height exponent wrong (check (c)) | the *constants* change; the theorem survives, since only `log ℓ(M) = o(M)` is needed |
| an exact boundary hit mishandled | **the theorem narrows** to offsets outside `ℤα+ℤ` |
| a prior result already covers the family (check (d)) | the theorem stands but is **not new**. This would be a genuinely useful finding and I would record it with thanks and full attribution |
| the mechanism attributed wrongly | attribution corrects; the mathematics stands |

The qualitative conclusion is robust to everything in the constants; it is **not** robust to a failure
in (a) or to a mishandled boundary hit. That is where the risk is concentrated.

## 5. Reproducing the computations

Python 3, standard library only — no numpy, sympy or mpmath. Every pass/fail decision is an exact
integer, exact rational, or exact algebraic-number comparison; floating point, where it appears, is
display only. Comparisons against the transcendental `β` use a certified 300-digit bracket that either
decides or raises.

```bash
cd scripts/phase12 && python3 independent_audit.py    # the theorem rebuilt from definitions; all 5 height floors
cd scripts/phase12 && python3 general_quadratic.py    # quadratic slope x rational offset, 50 end-to-end rows
cd scripts/phase13 && python3 algebraic_intercept.py  # ALGEBRAIC offset, field degrees 2, 4, 6
cd scripts/phase13 && python3 ridout_exponent.py      # the Ridout exponent -- a measurement, not a theorem
cd scripts/phase14 && python3 explicit_constants.py   # C, C_0, f(M), the certified threshold
```

Saved outputs are in the matching `data/phase*/` directories, so a reviewer can compare without
re-running. `scripts/phase13/numfield.py` implements exact arithmetic in a general number field
`ℚ(θ)`: an element is zero exactly when its coefficient vector is, and for a non-zero element the
characteristic polynomial supplies an a priori separation bound, so a high-precision evaluation decides
every sign with certainty.

**What the computations are and are not.** They are *supporting verification*: they check finitely many
instances of statements whose content is infinite, and they catch transcription and convention errors —
which they did, repeatedly, including the log-base error in (b) above and an unstated hypothesis in
(c). **They do not replace the arguments**, and no theorem here rests on a computation. Where a table
is the only evidence for something, the document says so and calls it a measurement, not a theorem —
`§21` of the manuscript is the clearest example.

## 6. Who is asking, and why

I work on this as an independent researcher. My professional experience is outside mathematics: in
electronics technology, in computer systems, and in an immunogenetics laboratory. I have not trained as
a number theorist and I do not present myself as one.

What that background contributes is a particular set of habits: look at how a system actually behaves
rather than how it is supposed to; find the interfaces where two components meet and check that each
side means the same thing by the values it passes; treat an assumption as unverified until something
independent confirms it; and build a test that fails loudly if the thing you believe is wrong. That is
why the conventions in checks (a) and (b) are written out rather than assumed, and why the verification
scripts exist.

**It is not mathematical certification, and it does not substitute for specialist review.** Checking
that an argument is internally consistent and that its computations are correct does not establish that
the argument is valid, that its citations support what they are asked to support, or that the result is
new. Those are judgements for specialists, and **they have not been made.**

So: please examine any part of this you find worth your time. I would rather learn that something is
wrong, already known, or achievable more simply than have it stand unexamined. A demonstration that a
result is already in the literature is a genuinely useful contribution and I will record it with
thanks and full attribution. You are also welcome to take any of it further independently, with
appropriate attribution, subject to the repository's existing licensing (Apache 2.0 for code and
analysis; `reference/` retains its own copyright).

Issues and pull requests on this repository are the best channel. Longer orientation:
[`docs/INVITATION_TO_DOMAIN_EXPERTS.md`](docs/INVITATION_TO_DOMAIN_EXPERTS.md); exact dependency
statement: [`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](docs/DEPENDENCE_ON_PRIOR_RESULTS.md).
