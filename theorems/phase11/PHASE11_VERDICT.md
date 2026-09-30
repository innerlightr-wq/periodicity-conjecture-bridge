**SUCCESS — A COMPLETE THEOREM FOR THE NAMED WORD, MODULO ONE CITED EFFECTIVE THEOREM**

# PHASE11_VERDICT.md

Isolated branch `phase11-explicit-word`, cut from `phase10-critical-density` at HEAD `d91e56e`
(expected and actual agree). Nothing pushed, nothing published, no release rebuilt;
`note_rev2.pdf` `8daf1979…`, `correction_notice.pdf` `0c93457c…` and both `~/Downloads` copies
byte-identical. The pending Revision-2 corrections remain pending and unapplied.

## The theorem

> **THEOREM 11.** Let `α = (√5−1)/2`, `ρ = 1/7`, `β = ln2/ln3`, and let `s ∈ {0,1}^ℕ` be
> `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`. Then
> ```
> Phi(s)  not in  Q .
> ```
> Moreover the proof is **effective**: for every `M ≥ 2` there is an explicit `ℓ(M)` with
> `S(s[0:ℓ(M)]) ≥ M − C·κ''·log₂M − C₀`, and consequently any rational `u/v = Φ(s)` would satisfy
> `H = max(|u|,v) ≥ 2^{S(s[0:ℓ(M)])}` for every `M`.

**Status of the ingredients.**

| ingredient | status |
|---|---|
| aperiodicity; density exactly `β` | **PROVED** (`EXPLICIT_CRITICAL_WORD.md` §2–3) |
| `p(n) = 2n`, via `β ∉ ℤα+ℤ` (`β` transcendental, `α` algebraic) | **CITED** (Rote 1994; Berstel–Vuillon 2001) + verified at `n ≤ 20` |
| R1 first-mismatch characterisation `L(ℓ) − ℓ = m*(ℓ)` | **PROVED**, verified at every convergent `q ≤ 3000` |
| R2 two-ball relaxation | **PROVED** |
| R3 `t₀ > 1/(147‖ℓα‖)` | **PROVED**, using `‖qα‖ > 1/(3q)` and the **rationality** of `ρ = 1/7` |
| R4 `c_m ≥ C₂m^{−κ}` | **CITED, EFFECTIVE** — Baker, *Transcendental Number Theory*, Thm 3.1 (algebraic coefficients). Sole external analytic input |
| R5 construction, `L(ℓ(M)) − ℓ(M) ≥ M`, `log₂ℓ(M) = O(log M)` | **PROVED**, verified `M ≤ 256` |
| height bound (H)/(H′) with explicit constants | **PROVED**; Phase 10 Lemmas D, E supply the drift and discrepancy |
| exact surplus at the witnesses | **CERTIFIED** by integer comparison `2^L > F(W)` |

So Theorem 11 is proved outright **conditional on nothing but cited standard results** — Baker's
theorem and the `2n` complexity statement. That is a genuine closure, not a reduction to a new
conjecture.

## Answers to the five required points

**(a) What remains valid from Phases 1–9B.** Unchanged from `theorems/phase10/PHASE10_VERDICT.md`:
every proof and record; the mechanism results (criterion, height/repetition bounds, transfer
identity, `g(γ)` refinement, driver identity, attainment routing, weight law); the four corrections
to the record; and the quantitative **(Q)** content, which T1/T2 do not supply.

**(b) Which conclusions were already known.** Every qualitative irrationality claim in Phases 2–9 —
CS Rote at every stage, Thue–Morse, the 21 substitution fixed points, the interval-`1/3` coding —
all at densities `≠ β`, all covered by T1 (refereed) or T2 (preprint). Unchanged.

**(c) The word, and why the exclusions miss it.** `s` above. T1 needs `liminf < β`, T2 needs
`> β`; `s` has density exactly `β`. T3 needs `liminf p(L)/L < 1.70951129…`; `s` has `2`. T4 is the
complexity-`(n+1)` line; `s` has `p(20) = 40`. **Novelty remains formally unresolved** — no prior
result was located covering density exactly `β` at complexity `2n`, but absence of a hit is not
proof of absence, and this is recorded as such rather than as a novelty claim.

**(d) The smallest remaining proof obligation.** *None, for this word.* Phase 10's open lemma (L2)
— "infinitely many `ℓ` with `(L−ℓ)/log₂ℓ` large" — is now **proved** for this `(α,ρ)`, in the
sharper form that `(L−ℓ)/log₂ℓ` is unbounded along the explicit subsequence `ℓ(M)`. What remains is
not a gap in Theorem 11 but the question of scope: see (e).

**(e) Next highest-value action.** Extend the scope, in this order:

1. **Other rational `ρ`.** R3 used only `‖mα+ρ‖ ≥ ‖qmα‖/q` for `ρ = 1/q`; the argument goes through
   verbatim for any rational `ρ = p/q ∉ ℤα+ℤ`, with `147` replaced by `3q²`. This is nearly free and
   would upgrade the theorem from one word to a countable family.
2. **Other quadratic `α`.** R3 needs only `‖qα‖ > c/q`, true for every quadratic irrational with an
   explicit `c`; R4 is unchanged. Also nearly free.
3. **Irrational `ρ`.** *Not* free: R3 collapses, because a merely irrational `ρ ∉ ℤα+ℤ` gives no
   effective approach rate to `0`. This is the real boundary of the present method and the first
   genuinely open extension.
4. Only then, general slopes of unbounded type, where Lemmas D and E themselves weaken.

**Do not** generalise the statement to "every intercept" or "every slope" on the strength of
Theorem 11 — items 1–2 are routine but unwritten, and item 3 is open.

## Discipline notes

- **Quantitative and qualitative kept apart.** The height floors of `EXACT_HEIGHT_AND_SURPLUS.md` §5
  (`H ≥ 2^{462}, 2^{838}, 2^{872}, 2^{2469}, 2^{15998}` — the last a 4 816-digit bound) are stated
  separately from the irrationality conclusion, and the method is credited to the foundation paper's
  own already-claimed effective technique.
- **A recorded bug.** The first draft of R5 imposed only the `β`-threshold; at `M = 4` that yields
  `ℓ = 5`, `m* = 3 < 4`. Kept on the record in `ROTATION_REPETITION_LEMMA.md` R5.
- **A recorded misdescription.** An earlier line called the `ℓ = 5` surplus negative; it is `+2.608`.
  The witness is useless because `L − ℓ = 3` is constant, not because the surplus fails. Corrected
  in place with the correction noted.
- **Finite positive surplus is not an asymptotic proof**, and is nowhere used as one: the verdict
  rests on R5, which is proved, with the tables as consistency checks.
