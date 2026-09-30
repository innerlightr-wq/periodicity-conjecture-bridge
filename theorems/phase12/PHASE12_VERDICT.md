**AUDIT PASSED; THEOREM GENERALIZED; ONE PRIOR-ART RESULT DOWNGRADED**

# PHASE12_VERDICT.md

Isolated worktree `/home/elias/scratch/phase12-bridge`, branch `phase12-audit-generalize`, cut from
`phase11b-baker-audit` at HEAD `c1bbff4` (expected and actual agree; tree was clean). Nothing pushed,
nothing published, no release rebuilt, no PDF regenerated. `note_rev2.pdf` `8daf1979…`,
`correction_notice.pdf` `0c93457c…`, `note.pdf` `b7054cee…` and both `~/Downloads` copies are
byte-identical. The pending publication corrections remain pending, and Phase 12 adds two more.

## 1. Item 1 — independent reconstruction: **PASS**

Theorem 11 was rebuilt from the definitions in fresh code (`scripts/phase12/qfield.py` +
`independent_audit.py`; `scripts/phase11` is not imported). The reconstruction reproduces the word,
the hitting-time table, the drift table, the periodic-value formula (checked mod `2^60` against the
raw series), and **all five height certificates including `H ≥ 2^15998`**. Every one of the eleven
dependencies the task listed is confirmed: `THEOREM11_INDEPENDENT_AUDIT.md` §2.

**Baker, checked first-hand against two independent sources.** Phase 11B's citation is **correct and
its transcription accurate**: Baker, *Linear forms in the logarithms of algebraic numbers III*,
Mathematika **14** (1967), Theorem 2, verified verbatim against (a) Mathematical Reviews MR0220680
(review by G. J. Rieger, reprinted Bull. AMS **43** (2006) 405–406) and (b) the Chim MPhil thesis
Theorem 1.3. The "**either** `log α₁,…,log αₙ` **or** `β₁,…,βₙ` linearly independent over `ℚ`"
condition is a disjunction; we use the **first** branch (`log 2, log 3` independent). The second branch
**fails at `m = 0`**, where `A_0 = 1/7 ∈ ℚ` — Phase 11B named the branch it used but not that the other
one is unavailable. Two fallback citations were located (Part I Thm 1.1 with `κ > n+1`; Part II Thm 2.2
with `κ > 2n+1`), so the analytic input survives the loss of any single one.

**Three corrections to the record, none touching the truth of Theorem 11:**

1. **A one-line uniform nonvanishing argument.** `j_m` is the *nearest* integer to `mα+ρ−β`, so
   `|A_m − β| ≤ 1/2`, and `β > 1/2`; hence **`A_m > β − 1/2 = 0.13093 > 0`** for every `m ≥ 0`, every
   quadratic `α`, every rational `ρ`. This supersedes Phase 11B's two-case argument and removes the
   only place where `m = 0` looked exceptional for Baker's hypotheses.
2. **A signed refinement of the relaxation**, new here: under the no-wrap hypothesis,
   `0 ∈ M(δ) ⟺ δ < 0`. Not needed for Theorem 11; it is what carries `ρ = 0` in the generalization.
3. **"Effective" must be split.** The five height floors are explicit and Baker-free. The `S → ∞`
   conclusion is effective *in principle* — Baker's `C` and the Kuipers–Niederreiter constants are
   computable from their proofs — but **no numerical value for them is supplied anywhere in this
   repository**. Phase 11 said "effective" without drawing that line.

## 2. Item 2 — prior results: classification **(d)**, plus a downgrade

> **(d) an application not located in the searched literature.**

Ten located results were placed against the conclusion with their exact hypotheses
(`CRITICAL_ROTATION_PRIOR_RESULTS.md`). Why each fails: T1/T2 read only the density and ours is
exactly `β`; T3 needs `liminf p(L)/L < 1.70951…` and ours is `2`; T4 needs Sturmian; T5/T6 (the
Adamczewski–Bugeaud `p`-adic low-complexity line and the subspace-theorem engine behind it) are about
the **Hensel digit expansion**, and `Φ` is a 2-adic isometry conjugating the shift to `T` — it is not
digit-preserving, so neither complexity bounds the other; T7 (Sharpe) is about positive-integer seeds
at slope `< 5/3`; T8 (arXiv:2601.04289) is archimedean and its authors disclaim any bearing on the
Periodicity Conjecture.

**On coverage above `β`.** The only located result reaching lower ones-density `> β` is a preprint
(arXiv:2101.12747, Thm 1). It is not used as a premise anywhere here, and coverage is stated against
what is independently available: the densities reached by refereed work are those below `β`.

**An attribution point that must not be lost.** The foundation paper's own §12 open problem (1)
already proposes the mechanism: "the first entry time of the orbit `{jγ+ρ}` into an interval of length
`jD_n` at the partition endpoint". That is Theorem 11's R1. **The hitting-time idea is the foundation
paper's, not new in Phase 11.** What is new is its execution at two discontinuities.

## 3. Item 3 — the generalization: **PROVED**

> **THEOREM 12.** Let `α ∈ (0,1)` be a quadratic irrational, `ρ ∈ ℚ` (reduce mod 1; **`ρ = 0`
> allowed**), `β = ln2/ln3`, and `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`. Then `s` is aperiodic, has ones-density
> exactly `β` and factor complexity `2n`, and **`Φ(s) ∉ ℚ`**.

Constants: `A := max` partial quotient of `α`, `K := (A+2)q²` with `q` the reduced denominator of `ρ`
— recovering Theorem 11's `147 = 3·7²`. Eleven steps, every qualification stated
(`QUADRATIC_RATIONAL_INTERCEPT_THEOREM.md` §3), verified over 5 slopes × 5 intercepts: 50 end-to-end
rows with `L − ℓ ≥ M`, 25 cases of `min_m K·m·‖mα+ρ‖ > 1`, 45 000 height/degree samples, 0 failures.

**Answers to the specific questions asked:**

- **`m = 0`**: handled separately and explicitly. Its orbit point is `{ρ}`. For `ρ ≠ 0`,
  `‖ρ‖ ≥ 1/q > 1/(KM) > |δ|`, so it is outside both arcs and the two-sided relaxation suffices.
- **Can a rational intercept land exactly on the boundary at `0`?** Only at `m = 0`, and only for
  `ρ = 0`: `mα + p/q ∈ ℤ` with `m ≥ 1` forces `α ∈ ℚ`. So there is **exactly one** boundary hit, for
  **exactly one** rational intercept.
- **`ρ = 0` needs neither a finite shift nor a separate argument.** A shift is actively wrong: `σ¹s`
  has intercept `{α}`, *irrational*, destroying the one thing the arc-at-`0` bound needs. What `ρ = 0`
  breaks is only the two-sided relaxation (`‖0‖ = 0`, so `t₀ = 0`). The fix is the signed form: for
  `δ > 0`, `M(δ) = [β−δ,β) ∪ [1−δ,1)` contains neither `0` nor `{ρ}=0`. Restrict `ℓ(M)` to the
  convergents with `δ(q_k) > 0`; the sign alternates, so infinitely many qualify, and
  `q_{k+1} ≤ (A+1)q_k` absorbs the cost of skipping every other one. `ρ = 0` is also exactly the case
  `ρ ∈ ℤα+ℤ` among rationals — the only rational intercept whose orbit meets a discontinuity — and it
  still has `p(n) = 2n` at `n = 6,12,20` for all five slopes.
- **The `β`-boundary cannot be hit**: `mα+ρ ≡ β (mod 1)` would make `β` algebraic. Uniform in `α, ρ, m`.
- **Bounded consecutive convergent-denominator ratios**: quadratic ⟹ eventually periodic continued
  fraction ⟹ `a_i ≤ A` ⟹ `q_{k+1} = a_{k+1}q_k + q_{k−1} ≤ (A+1)q_k`. Used twice: to size `ℓ(M)` when
  every other convergent is skipped, and in `‖q_kα‖ > 1/((A+2)q_k)`. Verified `max q_{k+1}/q_k ≤ A+1`.
- **Uniform drift and discrepancy for the actual coding**: Kuipers–Niederreiter Ch. 2 Thm 3.4 plus
  `Σ_{i≤k+1}a_i ≤ A(k+1)` and `k = O(log N)`; shifting the orbit by `ρ` turns one interval into at most
  two, so the bound is **uniform in `ρ`** — necessary, since `ρ` is an arbitrary rational.

**No obstruction appeared**, so no retreat to a subclass was needed. The honest limits are recorded
rather than glossed: `ρ` irrational is **open** (the arc at `0` has no effective rate); `α`
transcendental is **impossible** by this route; `α` algebraic of degree `≥ 3` with bounded partial
quotients is covered verbatim by the same proof, but whether any such `α` exists is a well-known open
problem, so the extra generality is currently vacuous and the theorem is stated for quadratics.

## 4. Item 4 — the corrected research record

`CLAIM_AND_DEPENDENCY_LEDGER.md` sorts every link of Theorem 12 into five columns: eight established
source results `S1–S8` (including `S8`, the foundation paper's own mechanism proposal), five
adaptations `A1–A5`, twelve mechanism results `M1–M12` proved here (three of them new in Phase 12),
the quantitative outputs, and the one potentially new qualitative conclusion. Withdrawn claims are
listed as withdrawn.

`PHASE12_PROPOSED_UPDATES.md` consolidates **eleven** outstanding corrections spanning Phases 9B–12
into one file with exact replacement text for `THEOREM_STATUS.md`, `LADDER.md`, `README.md`,
`PRIOR_ART.md`, `theorems/phase10/PRIOR_RESULT_COVERAGE.md` and the deposited note. It **absorbs and
supersedes** `theorems/phase9b/PROPOSED_STATUS_UPDATES.md`. Nothing is applied. Historical files keep
their text and receive pointers.

## 5. The strongest verified theorem, and its attribution

**Theorem 12**, §3. Carried by six published results (Bernstein–Lagarias/foundation Props. 2.2 & 4.1;
Lagrange–Perron on quadratic continued fractions; **Baker, Mathematika 14 (1967) Part III Thm 2**;
Kuipers–Niederreiter Ch. 2 Thm 3.4; Rote 1994 / Berstel–Vuillon 2001; Gelfond–Schneider) **and one
mechanism proposal that is the foundation paper's own** (§12 problem (1)). This repository contributes
the execution at two discontinuities, the arc-at-`0` / arc-at-`β` split, the witness-size calculus, the
`ρ = 0` treatment, and the generalization in both parameters.

## 6. Remaining gaps

1. **`ρ` irrational** — the real boundary. `‖mα+ρ‖` admits no effective lower bound; R3 collapses.
2. **Numerically explicit constants** — `c₁` (Baker) and `C, C₀` (discrepancy) are computable in
   principle and are not computed. Until they are, only the finite floors are explicit.
3. **Interval `[u, u+β)` with `u ≠ 0`** — plausible for algebraic `u` (a second Baker application),
   hopeless for transcendental `u`. Not attempted.
4. **Foundation paper problem (4)** — all `s` with `p_s(L) ≤ 2L` — untouched. Theorem 12 is one
   two-parameter family inside it.
5. **Novelty** — formally unresolved, as it has been since Phase 10.

## 7. Publication corrections required

Four for the deposited note, listed in `PHASE12_PROPOSED_UPDATES.md` §7: the Thue–Morse scope claim;
the CS Rote novelty framing; **the Baker citation**; **the T2 downgrade**. None is an error in a proof.
A single Revision 3 is the right vehicle. **Do not rebuild a release or deposit until the Theorem
11/12 statements are settled.**

## 8. Next highest-value mathematical task

> **Get an explicit, algebraic-coefficient linear independence measure for `log 2, log 3` in
> degree 2 — and do not substitute an integer-coefficient theorem to get it.**

The single quantity standing between Theorem 12 and a fully explicit result is

```
c_m = | A_m log 3 - log 2 | / log 3 ,     A_m algebraic, deg A_m = 2, H(A_m) = O(m^2).
```

What is needed is an **explicit lower bound for `|β₁ log 3 + β₂ log 2|` with `β_j` algebraic of degree
`≤ 2` and height `≤ H`** — equivalently, an explicit *measure of algebraic approximation of degree 2*
to `β = log₃2`. Where to look: **Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*,
Grundlehren 326, Springer (2000), Ch. 9–10**, and his survey *Linear independence of logarithms of
algebraic numbers*, which treat exactly the algebraic-coefficient case with explicit constants.

**Two reasons this is the right next task, and one trap.**

*It would make every constant explicit.* `c₁` is the only non-explicit input on the analytic side;
`C, C₀` on the discrepancy side are a separate, easier bookkeeping exercise in the
Kuipers–Niederreiter constants. With both done, Theorem 12 yields a written-down height floor
`H ≥ 2^{f(M)}` at every `M`, not only at the five computed witnesses. That is the only axis on which
this line of work has an uncontested contribution (`CLAIM_AND_DEPENDENCY_LEDGER.md` §5).

*It may restore the stronger rate.* At **fixed** degree these measures are typically *polynomial* in
the height rather than stretched-exponential. For orientation: Waldschmidt, *Transcendence measures
for exponentials and logarithms*, J. Austral. Math. Soc. Ser. A **25** (1978) 445–465, Theorem 3.6 /
Corollary 3.7 give a transcendence measure for `log α` of the shape
`C₁₅(α)N²(log H + N log N)(1+log N)^{−1}`, which **at `N = 2` is `C(α)(log H + O(1))`, i.e. a bound
`|log α − ξ| > c·H^{−C}` — polynomial in `H`.** If an analogue of that shape holds for the
*homogeneous two-logarithm* form, then `c_m ≥ C₂m^{−κ}` — the bound Phase 11 asserted — becomes true
after all, with a citation that actually supports it, and `ℓ(M) = O(M^κ)` is restored.

*The trap, stated explicitly.* Theorem 3.6 bounds `|log α − ξ|`: an **inhomogeneous** form in
`1` and one logarithm. Ours is **homogeneous** in two logarithms with an algebraic coefficient. The
shape is suggestive; it is not the quantity. And **Laurent–Mignotte–Nesterenko and Baker–Wüstholz,
the two standard sources of explicit bounds, require rational integer coefficients and must not be
used here** — substituting an integer-coefficient theorem for an algebraic-coefficient one is exactly
the error Phase 11B was opened to repair. Any bound imported must be checked to hold for algebraic
`β_j`, first-hand, as in `THEOREM11_INDEPENDENT_AUDIT.md` §4.

The alternative — attacking irrational `ρ` — is not the right next task: the missing ingredient there
is an effective irrationality measure for `ρ` relative to `α`, which for a general irrational `ρ` does
not exist. Gap 1 is a genuine boundary, not a gap in effort.
