**CORRECTION ADDENDUM — PREPARED, NOT PUBLISHED**

# CORRECTION_ADDENDUM.md

Concise correction record from the Phase 9B audit. Nothing here has been applied to a status file,
a released PDF, or a Zenodo record.

## C1. The Thue–Morse conclusion does not need Phase 9's threshold

`Φ(Thue–Morse) ∉ ℚ` follows from `theorems/phase1/REPETITION_HEIGHT_CRITERION.md`'s **exact**
inequality, whose threshold at density `γ = 1/2` is `max(1, (log₂3)/2) = 1`, against a prefix power
of `5/3` and a **bounded** discrepancy `D = 1/2`. Phase 9's `g(γ) = 1.396241` is not needed and the
attribution to it is withdrawn. `g(γ)` remains valid as a refinement of Phase 1's *unconditional*
squares theorem, for the case where nothing is known about `D`.

## C2. The result is not new — an explicit prior theorem covers it

**Monks–Yazinski, Discrete Math. 275 (2004), Theorem 2.7(b)**: for `x ∈ ℚ_odd` with divergent orbit,
`ln2/ln3 ≤ liminf κ_n(x)/n`. Hence any aperiodic `v` with `liminf k_n(v)/n < β = ln2/ln3` has
`Φ(v) ∉ ℚ`. Thue–Morse has density `1/2 < β`. The deduction is stated verbatim in this programme's
own foundation paper, §8.

## C3. The same theorem subsumes the entire CS Rote ladder

Every CS Rote sequence has ones-density **exactly `1/2`**, for every irrational slope and every
intercept (`v_n = v_0 ⊕ (k_n(u) mod 2)`; Weyl equidistribution for `γ/2`). So Phases 2, 4, 6, 8 and
9's CS Rote theorems, and the 21-substitution sweep, are all corollaries of the 2004 result (the
four sweep members above `β` via López–Stoll 2021 Theorem 1, a preprint). **No proof is false; the
novelty claims are.** The uncovered case is density **exactly `β`**, which is where the foundation
paper's own theorem lives and where this repository's ladder never went.

## C4. The method-scope statement, corrected

Replace, wherever it appears (`theorems/phase1/FULL_PERIODICITY_GAP.md` Q4, `LADDER.md`,
`THEOREM_STATUS.md`, Revision 2 of the note §15 Open 6 and its abstract):

> ~~"The Thue–Morse word has no square whatsoever below half-length 2048, making every method in
> this note — indeed, every purely repetition-based method — structurally inapplicable to it by
> construction."~~

with:

> "The Thue–Morse word has no **initial square** below half-length 2048. That does **not** put it
> beyond a repetition-based method: the criterion's requirement is a prefix power exceeding
> `max(1, γ log₂3)` (or `g(γ)` when the discrepancy is uncontrolled), which at density `γ = 1/2` is
> `1`, not `2`. Thue–Morse has initial powers of exponent exactly `5/3` at every scale `24·2^m`,
> with discrepancy exactly `1/2`, and the criterion reaches it. **Useful fractional initial powers
> can suffice; absence of initial squares proves nothing.** A structural ceiling for this method does
> exist — a word whose prefix powers satisfy `r_n → 1` fast enough is out of reach, since the
> threshold always exceeds `1` — but it must be stated as a quantitative condition on
> `limsup ℓ_n(r_n − max(1, γ_n log₂3))`, and no explicit aperiodic word is currently known to this
> record to satisfy it."

## C5. The prior-art procedure, corrected

`PRIOR_ART.md`'s three searches all targeted the **mechanism**. None asked whether the **conclusion**
was already available by a different route. Both halves of the answer were already in this
repository (`theorems/phase1/FALSIFICATION_REPORT.md` cites Monks–Yazinski; `docs/EOC_HANDOFF_CLOSED.md`
records CS Rote density `= 1/2` against `β`). Any future prior-art pass must check the conclusion
against the **density dichotomy** first, as a standing gate.

## C6. Substitution sweep, scope corrected

"All 21 aperiodic fixed points" = binary alphabet, `k ∈ {2,3}`, `σ(0)`-prolongable, aperiodicity by
finite test, and one quoted-but-unverified discrepancy bound. It is not a statement about automatic
or morphic words. Phase 9's proposal to "sweep the whole `k`-automatic family" is withdrawn: no
primitive substitutive word can sit at density `β` (algebraic frequencies versus transcendental `β`),
so no such sweep can reach the one uncovered case.

## C7. The coverage is by density, not by complexity (Phase 10)

The framing "crossing the counting frontier at `p(n) = 2n`" compares only against the transported
Dubickas criterion (T3). T3 is not the binding constraint: **T1 covers every complexity at every
density `< β`, and T2 every complexity at every density `> β`.** Moving from `p(n) = n+1` to
`p(n) = 2n` at a fixed density `1/2` therefore buys nothing. Withdraw "`p(n) = 2n` is a frontier";
replace with: the frontier is the **density** `β = log₃2`, and complexity matters only insofar as a
target must stay off T4's complexity-`(n+1)` line and above T3's `1.70951129…` line.

## C8. The quantitative content is not covered — but the method is already claimed (Phase 10)

T1 and T2 are **purely qualitative**. T1's proof (Monks–Yazinski §4.1) fixes `m`, discards a
finitely many orbit terms whose number depends on the unknown `x`, and lets `m → ∞`; T2's proof
concludes from the existence of accumulation points. Neither bounds the height `H = max(|u|,v)` of a
hypothetical rational `Φ(v) = u/v`. The bridge does: `H ≥ 2^{S_n}`, explicit and unbounded (for
Thue–Morse, `H ≥ 2^{510.7}` at `ℓ = 768`).

So each reclassified result carries genuine quantitative content **in addition to** a covered
qualitative conclusion. **However**, the foundation paper already claims "the height floors" and
"the independent effective Liouville proof" as its own novelty, for Sturmian words. The correct
statement is therefore: *Phases 2–9 supply new instances of an already-claimed effective method.*
Do not upgrade this into a new irrationality result, and do not omit it either — it is the part of
those phases that is not subsumed.
