**THEOREM 13: EVERY QUADRATIC SLOPE, EVERY ALGEBRAIC INTERCEPT — AND THE ANALYTIC CONSTANT IS NOW A NUMBER**

# PHASE13_VERDICT.md

> **WORDING CLARIFICATION (documentation pass).** Where this file describes **López & Stoll**,
> *The 3x+1 periodicity conjecture in ℝ*, arXiv:2101.12747 (2021), Theorem 1, the current-facing
> statement of this repository is the following:
>
> > López–Stoll's work on density and the 3x+1 conjugacy map helped guide this programme toward the
> > critical density `β = ln2/ln3`. We acknowledge that influence. The results presented here are
> > established through the independent arguments given in this repository and do not require their
> > proposed upper-density exclusion.
>
> We have **neither established nor disproved** their theorem and take no position on it. The sharper language retained below is the **audit record** — it preserves a
> technical observation raised by a third party (`innerlightr-wq/eoc-divergence` issue #30, open at the
> time of writing) together with its source reference and its verification status, namely **not
> verified by us and not a result of this repository**. It is kept, not rewritten, because research
> history should not be edited after the fact; it should not be quoted as a claim. No conclusion in
> this repository depends on López–Stoll in either direction. Canonical wording:
> [`docs/DEPENDENCE_ON_PRIOR_RESULTS.md`](../../docs/DEPENDENCE_ON_PRIOR_RESULTS.md).

Isolated worktree `/home/elias/scratch/phase13-bridge`, branch `phase13-algebraic-intercept`, cut from
`phase12-audit-generalize` at HEAD `e21aab9` (expected and actual agree; tree clean). Nothing pushed,
nothing published, no PDF rebuilt, no deposited artifact touched. `note_rev2.pdf` `8daf1979…`,
`correction_notice.pdf` `0c93457c…`, `note.pdf` `b7054cee…` and both `~/Downloads` copies verified
byte-identical.

## 1. The public foundation paper — verified, and identical to what we had

Version DOI **10.5281/zenodo.23019799**, concept DOI `10.5281/zenodo.22920055`, CC BY 4.0, 22 pages,
`Sturmian_v2_revision_draft3.pdf`, 467 315 bytes, md5 `54732e14b939c39f74c118097a069f30`. The local
`reference/` copy carries **exactly that md5**, so there are **no differences to record** — every
theorem number cited in Phases 1–12 was already cited from these bytes. Of the four versions on the
concept record, only the latest is open; the three earlier ones remain restricted. All labels used by
this programme (Props. 2.2/4.1, Cor. 6.2, Thm 8.5, Cor. 8.7, Cor. 9.3/9.4, Thms 10.1–10.3, Cor. 10.5,
§12 problems 1–4) were located. **It is the author's own unrefereed preprint, and every use of it is
now flagged as a self-citation.** Details: `PUBLIC_FOUNDATION_VERSION_CHECK.md`.

## 2. Item 1 — consolidation

`CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md` gives the full chain with ten published source results
`S1–S10`, five adaptations `A1–A5`, fifteen mechanism results `M1–M15`, and four separations kept
strictly apart: qualitative conclusions (§6), quantitative height bounds (§7), finite certificates
(§8), and **effectively computable versus numerically supplied** (§9). The last table is the one that
changed most:

| constant | supplied before Phase 13 | supplied now |
|---|---|---|
| finite certificates `H ≥ 2^462 … 2^15998` | yes, exactly | yes |
| `K = (A+2)q²` (arc at `0`) | yes | yes |
| `c_L, D` (arc at `0`, algebraic `ρ`) | — | **yes** (Liouville) |
| `c₁` (arc at `β`) | **no** | **yes — `≈ 2.39·10^13` at `D = 2`** |
| `C, C₀` (drift / discrepancy) | no | **still no** |

**López–Stoll is treated as instructed**: a challenged preprint claim pending verification, neither
disproved nor securely established, **relied on nowhere**. The consequence is stated once and
propagated: the securely covered density region is `liminf < β`, and the residual is `liminf ≥ β`.

## 3. Item 2 — prior coverage: **(d) not located in the searched literature**

Fourteen results placed with exact hypotheses (`FAMILY_THEOREM_PRIOR_COVERAGE.md`). Two findings
matter more than the classification.

**(a) A Phase 12 dismissal is withdrawn.** Phase 12 wrote off the subspace-theorem route with "our
witnesses give `L/ℓ → 1`, far too weak". Measured properly against **Ridout's threshold** (Bugeaud–Kekeç
Thm 1.3: `0 < |ξ − x_n/y_n|_p < |x_n,y_n|^{−2−ε}` for infinitely many ⟹ transcendence), the exponent
`E(ℓ) = L(ℓ)/log₂H_red(ℓ)` **exceeds `2` at 7 of the 20 convergents tested, with a maximum of
`3.361`**. The route is not out of reach; what is missing is infinitude with a fixed `ε`, i.e.
`m*(ℓ)/ℓ > 1+ε` infinitely often (measured: `>1` at 8 of 20, median `0.904`). **Open; nothing claimed.**
Phase 12's measurement was taken on the constructed family, where `E → 1` by design — which was the
error.

**(b) The Hecke–Mahler line does not reach it, for two independent reasons.** Luca–Ouaknine–Worrell
(Bull. LMS 57 (2025) 1360–1368) and Bugeaud–Laurent (Acta Arith. 209 (2023) 59–90) are archimedean,
and their coefficient sequences are Beatty sequences `⌊kρ⌋`. Our `k_N = #\{n<N:\{nα+ρ\}∈[0,β)\}` is a
Birkhoff sum over an interval of length `β ≠ α` — a generalised-Beatty count with no floor-function
closed form. So even the archimedean analogue of our object is not a Hecke–Mahler value. The
foundation paper's §11 ("Why the 2-adic place") and problem (3) say the same thing from the other side.

Also recorded: the `p`-adic low-complexity theorems constrain the 2-adic **digit string** of
`D(s) = Σ s_i 2^i`, not `Φ(s)`; these are different numbers, and `Φ` is an isometry conjugating the
shift to `T`, not digit-preserving.

## 4. Item 3 — the algebraic-intercept extension: **PROVED**

> **THEOREM 13.** `α ∈ (0,1)` a quadratic irrational, `ρ` **any real algebraic number** (mod 1),
> `β = ln2/ln3`, `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`. Then `s` is aperiodic, has ones-density exactly `β`,
> has `p_s(n) = 2n`, and **`Φ(s) ∉ ℚ`**.

Verified over 7 cases with field degrees `D = 2, 4, 6`, including two with an exact `0`-boundary hit:
34 end-to-end rows with `L−ℓ ≥ M`, 0 failures anywhere.

**The `0`-boundary, as asked.** Write the distance as `|θ_m|`, `θ_m = mα+ρ−j`. Then
`deg θ_m ≤ D := [ℚ(α,ρ):ℚ]` and `H(θ_m) ≤ C_h m^D` (the conjugates are `O(m)`, so the symmetric
functions are `O(m^D)`). **Liouville's inequality** `|θ| ≥ (1+H)^{−D}` then gives

> `‖mα+ρ‖ ≥ c_L(α,ρ)·m^{−D²}` — a **polynomial** bound with **no transcendence input whatever**.

This is what replaces the rational-`ρ` trick `‖x‖ ≥ ‖qx‖/q`, and it is why the extension is cheap.
Exact hits are classified exactly: `θ_m = 0 ⟺ ρ ∈ ℤα+ℤ`, and then the index `m₀` is **unique** — but
may be **any** value, not `0` (`ρ = 3−5α` gives `m₀ = 5`, tested).

**The `β`-boundary, as asked.** `c_m = |A_m log3 − log2|/log3` with `A_m = mα+ρ−j_m`. Non-vanishing is
uniform and needs no case analysis: `j_m` is the nearest integer to `mα+ρ−β`, so `|A_m−β| ≤ 1/2`, and
`β > 1/2`, whence **`A_m > β − 1/2 = 0.13093 > 0`** for every `m`, every `α`, every `ρ` — small indices
and exact-hit indices included. `deg A_m ≤ D`, `H(A_m) = O(m^D)`, so the dependence on `ρ` enters
exactly through the field degree and the height constant. The `β`-boundary is **never hit** (it would
make `β` algebraic). For `D > 2` the citation is taken as **Baker Part I, Theorem 1.1**, which quantifies
over "degree at most `d`" with a **single** constant — the cleaner form when `deg A_m` varies with `m`.

**An exact `0`-boundary hit does not defeat the proof**, and was not discarded. Two independent
treatments: the **signed relaxation** (`M(δ) = [β−δ,β) ∪ [1−δ,1)` for `δ > 0` contains `0` in neither
arc, so restrict to the `δ>0` convergents — insensitive to `m₀`), and a **reduction by finite shift**
(`ρ = j₀−m₀α` gives `{nα+ρ} = {(n−m₀)α}`, so the word is the `ρ=0` coding read from index `−m₀`, and
rationality of `Φ` is shift-invariant in both directions since `T` and both its branches preserve
rationality). Verified: `s_n = t_{n−5}` for `5 ≤ n < 600`.

**The uniform minimum-distance bound, witness growth, unbounded surplus.**
`t(M) ≥ min(c_L M^{−D²}, exp(−c₁(log(M+2))^κ)) = exp(−O((log(M+2))^κ))`; hence
`log ℓ(M) = O((log(M+2))^κ)` and `ℓ(M) → ∞`, using `q_{k+1} ≤ (A+1)q_k` (available because `α` is
quadratic); hence `L(ℓ(M))−ℓ(M) ≥ M`; hence `S ≥ M − O((log M)^κ) − C₀ → +∞`, and the abstract
criterion gives `Φ(s) ∉ ℚ`. The discrepancy input is **uniform in `ρ`** and so needed no change at all.

## 5. Item 4 — the strongest justified statement, and the translated-interval equivalence

Aperiodicity, density `β`, complexity `2n`, attained witnesses and arithmetic surplus were all verified
**for the actual coding** in every case, including both exact-hit cases
(`ALGEBRAIC_INTERCEPT_THEOREM.md` §8, and §9 for the certificates `2^67 … 2^598`).

**The equivalence, checked explicitly.** `1_{[u,u+β) mod 1}(x) = 1_{[0,β)}(\{x−u\})` is an identity of
arcs, valid **including when `u+β > 1` and the arc wraps** (verified at 7 values of `u` × 400 orbit
points, 0 mismatches). Therefore:

> **Corollary 13.1.** `α ∈ (0,1)` quadratic irrational, `u, ρ ∈ ℝ` with `ρ−u` **algebraic**. If
> `s_n = 1 ⟺ {nα+ρ} ∈ [u,u+β) (mod 1)`, then `Φ(s) ∉ ℚ`.

This is **strictly more general** than Theorem 13: `ρ` and `u` may **both be transcendental** provided
their difference is algebraic — e.g. `ρ = π`, `u = π − 1/7`. What the theorem constrains is the
**offset between the intercept and the interval's left endpoint**, never the intercept alone. Stating
it that way is the correct form, and it makes the remaining boundary precise: `ρ−u` transcendental.

## 6. Item 5 — explicit constants: **located, applicable, and evaluated**

> **Waldschmidt, Theorem 10.1** (*Linear independence of logarithms of algebraic numbers*; book:
> *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren 326, Springer 2000):
> `|Λ| > exp{−(50m)^{3m}D^{m+2}(log B)² log A₁⋯log A_m}` for **algebraic** `β_j`, all hypotheses
> verified in `EXPLICIT_CONSTANTS_STATUS.md` §2.

For our form (`m = 2`, `α₁ = 3`, `α₂ = 2`, `β₁ = A_m`, `β₂ = −1`): `c₁ = 2.39·10^13` at `D = 2`, rising
to `1.42·10^15` at `D = 6`. The exponent on `log B` is **exactly 2** — sharper than Baker III Theorem
2's `κ > 2` — and Waldschmidt's theorem assumes **no** linear-independence condition on the
coefficients, which removes the one place where `m = 0` fell outside a branch of Baker's disjunction.

Three cautions honoured:

- **No integer-coefficient theorem was substituted, and none can be.** Clearing denominators gives
  integer coefficients but turns the first logarithm into `α·log 3 = log(3^α)`, and `3^α` is
  **transcendental** by Gelfond–Schneider. Laurent–Mignotte–Nesterenko and Baker–Wüstholz require
  algebraic arguments, so **no valid reduction exists**.
- **Fixed degree does not yield a polynomial bound.** Phase 12's hope is **withdrawn**: a polynomial
  bound is exactly `κ = 1`, which MR0220680 records as **Baker's own conjecture**, unproved. Phase
  12's orienting example (Waldschmidt 1978 Thm 3.6, polynomial at `N=2`) concerns `|log α − ξ|` — an
  *inhomogeneous form in one logarithm* — and does not transfer.
- **Kept separate from the qualitative proof.** Theorem 13 does not use §6 at all; the
  stretched-exponential estimate already suffices.

**What it costs:** the explicit surplus first turns positive at `M ≈ 2.7·10^17`, at a witness length
`≈ 10^{8·10^16}`. So this buys **rigour, not numbers**. The five finite certificates remain the only
numerically useful floors, and they are Baker-free.

## 7. Limitations, and remaining gaps

1. **`ρ − u` transcendental** — the only remaining obstruction on the intercept axis. Both bounds
   fail: Liouville needs algebraicity, and `‖mα+ρ−β‖` stops being a logarithmic form in algebraic data.
2. **`C, C₀` not numerically supplied** — the Kuipers–Niederreiter constants. This is the last item
   between Theorem 13 and a fully numerical `H ≥ 2^{f(M)}` at every `M`.
3. **Transcendence of `Φ(s)`** — open, and closer than Phase 12 thought (§3(a)).
4. **An irrationality measure** — foundation problem (2), untouched: our witnesses bound only the
   approximants, not every rational.
5. **Foundation problem (4)** (all `s` with `p_s(L) ≤ 2L`) — untouched; Theorem 13 is a two-parameter
   family inside it.
6. **`α` transcendental** — impossible by this route. **`α` algebraic of degree `≥ 3` with bounded
   partial quotients** — covered verbatim, but vacuous as far as anyone knows.
7. **Novelty** — formally unresolved, as since Phase 10. What is *proved* is that fourteen located
   results do not reach the family.

## 8. Next highest-value action

> **Evaluate `C` and `C₀`. It is bookkeeping, it needs no new theorem, and it is the last step to a
> fully numerical theorem.**

Specialise `N·D_N ≤ c₁'Σ_{i≤k+1}a_i + c₂'` (Kuipers–Niederreiter Ch. 2 Thm 3.4) to the interval
`[0,β)` and to `α` of bounded type, extract numerical `c₁', c₂'`, and propagate through
`C = 1 + 3C_D log₂3`, `C₀ = 1 + log₂3(3C_D'+1)`. Combined with `c₁` from §6 this yields an explicit
`H ≥ 2^{f(M)}` at every `M` — the first fully numerical statement in the programme beyond the finite
certificates, and the axis on which this work has an uncontested contribution.

**Second, and mathematically more interesting:** decide whether `m*(ℓ)/ℓ > 1+ε` infinitely often. If
yes, Ridout upgrades Theorem 13 from irrationality to **transcendence**, answering the foundation
paper's problem (3) for these words. The measured data (7/20 convergents above the threshold, max
`3.361`) say the question is live, not that the answer is yes. The obstruction is that `m*(ℓ)` is a
hitting time for two arcs of length `‖ℓα‖`, and controlling it from **below** along a subsequence needs
the opposite of what the current construction arranges — a genuinely different argument, not a
refinement of this one.

**Not recommended next:** attacking transcendental `ρ−u`. The missing ingredient is an effective
irrationality measure for `ρ−u` relative to `α`, which for a general transcendental number does not
exist. Gap 1 is a boundary, not a gap in effort.
