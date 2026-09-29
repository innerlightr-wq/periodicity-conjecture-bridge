# BRIDGE_CONTROLS.md

Four control types, testing exactly which part of the bridge fails (or, surprisingly, does *not* fail) in each case.

## Control 1 — eventually periodic `s` (`Φ(s) ∈ Q`): the bridge must stay silent

Already verified, in exact arithmetic, in the paper's own Appendix A (not reproduced here, only cited): for `Φ(w₃^∞) = −5`, the 2-adic depths against further periodic approximants **freeze** at `10 = q₃+q₄−1` rather than growing; for rational mechanical words `1c_{p/q}`, the integer `M_n = uδ_n − vc_n` vanishes **exactly** at the last (necessarily finite) convergent level, making the lower bound `|M_n|≥2^{L_n}` vacuous. **This is the correct failure mode**: the 2-adic lower bound `(★)` in `ABSTRACT_BRIDGE_THEOREM.md` degenerates because `M_n=0` is now possible (indeed forced, once `s=W_n^∞` exactly for the relevant `n`) — the bridge's *hypothesis* `s ≠ W_n^∞` fails, not its logic.

## Control 2 — aperiodic words with no useful initial repetitions: Thue–Morse

Already verified in the paper's own Appendix A: the Thue–Morse word has **no square at all** below half-length 2048. This is not a counterexample to anything — it shows the *hypothesis* of `REPETITION_HEIGHT_CRITERION.md`'s theorems (arbitrarily long initial squares) simply **does not apply** to this word; the bridge is silent, correctly, because it was never invoked. Thue–Morse's own irrationality (if true — not addressed by this bridge at all) would need an entirely different method (Section 9's counting bound *does* apply, since Thue–Morse has linear complexity `p(L) ≤ cL` for some explicit `c`, likely `< 1.70951`, a separate and much easier route not audited further here).

## Control 3 — long repetitions, bad height: only possible below the `r=2` margin

`REPETITION_HEIGHT_CRITERION.md`'s strongest finding (squares survive *any* discrepancy, unconditionally) means **no control of this type exists at `r=2`** — this was actively sought and could not be constructed, which is itself the falsification-relevant finding (see `FALSIFICATION_REPORT.md`, target C1). A genuine control **does** exist at smaller exponents, since `sup_γ c(γ) = log₂3 ≈ 1.585`:

> **Explicit control.** Let `r = 1.5 < log₂3`. Take `W = 0^{(1−γ)ℓ}1^{γℓ}` (single-block, maximal discrepancy `D=γ(1−γ)ℓ`) at density `γ` close enough to `1` that `c(γ) = max(1,γlog₂3)+γ(1−γ)log₂3 > 1.5` — e.g. `γ=0.95` gives `c(γ)≈1.583` (computed directly: `max(1,0.95·1.585)=1.506`, `+0.95·0.05·1.585=0.0753`, total `1.581`). Then for a hypothetical `s` beginning in `W^{1.5}` at this `γ`, the surplus `S ≈ ℓ(1.5 − 1.581) = −0.081ℓ → −∞`: **the bridge fails to prove irrationality here**, exactly because `r=1.5` does not clear the worst-case height cost at this density.

This confirms the general mechanism (repetition exponent must exceed the worst-case density-dependent height cost) is real and can fail — just not at `r=2`, which was the one exponent the paper's own Theorem 10.2 actually supplies.

## Control 4 — low-height approximants, insufficient depth

Any single fixed word `W` used as a *non-repeating* one-shot approximant (`r=1`, i.e. `L_n ~ ℓ_n` with no surplus repetition) gives `margin = 1 − max(1,γlog₂3) ≤ 0` for every `γ∈(0,1)` (`REPETITION_HEIGHT_CRITERION.md`, boundary case) — the depth from a bare, non-repeated prefix agreement is **never** enough on its own, regardless of how low the discrepancy is. This is the cleanest possible confirmation that *some* genuine repetition (`r>1` strictly) is structurally necessary, independent of any height consideration — a `D`-side control (arbitrarily low discrepancy) cannot compensate for an `r`-side failure (no repetition at all).

## Summary: which half of the bridge fails, per control

| Control | `s≠W_n^∞`? | Repetition available? | Discrepancy control? | Failure point |
|---|---|---|---|---|
| 1. Eventually periodic | **No** (fails) | — | — | Hypothesis of the abstract theorem itself |
| 2. Thue–Morse | Yes | **No squares at all** | — | Repetition hypothesis of `REPETITION_HEIGHT_CRITERION.md` never triggers |
| 3. `r=1.5`, `γ=0.95` block | Yes | Yes, but exponent too small | Worst-case, at the edge | Margin `r − c(γ) < 0` |
| 4. `r=1` (no repetition) | Yes | **No** (trivial exponent) | Irrelevant | Margin `1 − max(1,γlog₂3) ≤ 0` always |

Controls 1–2 test the *hypotheses* of the theorems (correctly silent when violated); Controls 3–4 test the *margin* itself, and confirm it can be made negative — but only by degrading the repetition exponent below `log₂3`, never by degrading discrepancy alone at `r=2`, which is the paper's own regime.
