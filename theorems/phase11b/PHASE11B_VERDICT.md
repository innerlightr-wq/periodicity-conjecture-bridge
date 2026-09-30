**THEOREM 11 SURVIVES — THE CITATION WAS WRONG, THE THEOREM IS NOT**

# PHASE11B_VERDICT.md

Isolated branch `phase11b-baker-audit`, cut from `phase11-explicit-word` at HEAD `2eb6976`
(expected and actual agree). Nothing pushed, nothing published, no release rebuilt;
`note_rev2.pdf` `8daf1979…` and both `~/Downloads` copies byte-identical. The pending Revision-2
corrections remain pending.

## 1. The defect, and its correction

Phase 11 R4 claimed `c_m ≥ C₂m^{−κ}` from "Baker, *Transcendental Number Theory*, Theorem 3.1".
**That claim is withdrawn**: for **algebraic** coefficients the source gives a *stretched
exponential in `log B`*, not a polynomial in `B`. The correct citation, read first-hand:

> **Baker, *Linear forms in the logarithms of algebraic numbers III*, Mathematika 14 (1967),
> Theorem 2.** … `κ > n`, `B` the maximum height of `β₁,…,β_n` …
> `|β₁logα₁ + ⋯ + β_nlogα_n| > C·e^{−(log B)^κ}`, `C` effectively computable.

The three notions are kept apart: **nonvanishing** of `Λ_m` is available without Baker (from the
transcendence of `log₃2`); the bound is **effective**; it is **not polynomial**. No
integer-coefficient theorem was substituted.

## 2. The repaired chain

With `H(A_m) = O(m²)` (explicit: `A_m = (a_m + 7m√5)/14`, `a_m = −7m+2−14j_m`, minimal polynomial
`196x² − 28a_mx + (a_m²−245m²)`, degree `≤ 2`):

```
c_m   >=  exp( -c_1 (log(m+2))^kappa )                        (Baker 1967, Thm 2, kappa > 2)
C_M   >=  exp( -c_1 (log(M+2))^kappa )
ell(M) <  1/t(M) = max(1/C_M, 147M)   ->   log ell(M) = O( (log(M+2))^kappa )
ell(M) >  49 M                        ->   ell(M) -> infinity
L(ell(M)) - ell(M)  >=  M
S  >=  M - (C c_1/ln2)(log(M+2))^kappa - C_0   ->   +infinity      since (log M)^kappa = o(M)
```

using the golden continued fraction's bounded consecutive ratio `q_{k+1} ≤ 2q_k` and the two-sided
estimate `1/(q_{k+1}+q_k) < ‖q_kα‖ < 1/q_{k+1}` explicitly. **A polynomial bound on `C_M` is
unnecessary.**

> **THEOREM 11 (unchanged statement, repaired proof).** For `α = (√5−1)/2`, `ρ = 1/7`,
> `β = ln2/ln3` and `s_n = 1 ⟺ {nα+ρ} ∈ [0,β)`: **`Φ(s) ∉ ℚ`**, effectively.

## 3. Two further findings of the audit

- **An unstated hypothesis.** The closed-form arc description requires `|δ| ≤ min(β,1−β) = 0.36907`.
  Checked: 0 disagreements with the definition where it holds, 39 where it fails — all at `q = 1`.
  The construction has `|δ| < 1/294`, so it holds with a factor `≈108` to spare. **R2 is
  unconditional** and survives the wrap, and the proof routes through R2, so nothing downstream was
  affected — but it was assumed, not checked.
- **Measured constants removed.** Phase 11's `|e_ℓ| ≤ 0.41`, `D(W) ≤ 2.02` were valid only on the
  computed range. Replaced by proved bounds `|e_ℓ| ≤ C_D log₂ℓ + C_D'`, `D(W) ≤ 2C_D log₂ℓ + 2C_D'`
  (Phase 10 Lemma D + Kuipers–Niederreiter Ch. 2 Thm 3.4, all `a_i = 1` for the golden CF), giving
  absolute `C = 1 + 3C_D log₂3` and `C_0 = 1 + log₂3(3C_D'+1)`.

## 4. Explicit finite certificates versus the effective asymptotic argument

These are logically independent and are now stated separately.

**Finite certificates — Baker-free.** For any rational `u/v = Φ(s)` with `H = max(|u|,v)`, the
inequality `2^{L} ≤ H·F(W)` gives `H ≥ 2^{S}` at each computed witness. These are exact integer
facts (`2^L > F(W)` compared as integers) and use **no** analytic input whatever:

```
ell =  377   H >= 2^462
ell =  610   H >= 2^838
ell = 1597   H >= 2^872
ell = 2584   H >= 2^2469
ell = 6765   H >= 2^15998        (a 4816-digit lower bound)
```

**Effective asymptotic argument — Baker-dependent.** That the family continues for *every* `M`, with
`S ≥ M − O((log M)^κ) → ∞`, rests on Baker 1967 Theorem 2. Because that theorem is effective, so is
every constant in the conclusion.

## 5. Verdict

**Successful.** The analytic dependency is resolved, not merely relocated: the corrected bound is
weaker than what Phase 11 assumed, and the argument was rebuilt to need only `log ℓ(M) = o(M)`,
which the corrected bound supplies with room to spare. No remaining analytic obligation.

## 6. Scope — unchanged and deliberately not extended

The Phase 11 scope note stands. Other rational `ρ = p/q` and other quadratic `α` are routine
(replace `147` by `3q²`; R4 unchanged in form, with `H(A_m)` still `O(m²)`), but they are
**unwritten**, and irrational `ρ` remains genuinely open because R3 collapses there. The dependency
being resolved unblocks those extensions in principle; it does not perform them, and nothing here
is generalised to another slope or intercept.

**Novelty remains a separate, unresolved question**, exactly as recorded in Phase 10: no prior
result was located covering lower ones-density exactly `β` at complexity `2n`, and absence of a hit
is not proof of absence.
