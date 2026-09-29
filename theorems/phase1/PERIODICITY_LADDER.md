# PERIODICITY_LADDER.md

*(Rote/rotation-coding/morphic rows pending literature audit results; the rungs below reflect this audit's own derived mathematics and are stable regardless of that pending content.)*

## RUNG A — already covered by counting alone

`p_s(L) ≤ cL+O(1)`, `c < 1/log₂(3/2) = 1.70951...`, `s` not eventually periodic. Covered unconditionally by `Corollary 9.3` (transported Dubickas), no repetition/height machinery needed at all. Includes all Sturmian words as a strict special case (`p_s(L)=L+1`), and any quasi-Sturmian word with complexity below the threshold.

## RUNG B — covered by the (now generalized) repetition/height bridge

Any class `𝒞` for which every `s ∈ 𝒞` has arbitrarily long initial powers of exponent `r > log₂3 ≈ 1.585`, uniformly (**no** further requirement — `CERTIFICATE_DEPENDENCY_MAP.md`). **Confirmed members**: Sturmian words (via Theorem 10.2's squares, `r=2`), and — by this audit's strengthening — any word whatsoever with arbitrarily long initial squares (`r=2`), Sturmian or not, since balance/discrepancy is no longer required. This is a **strictly larger** rung than the paper's own Section 10 scope: any non-Sturmian aperiodic word that happens to begin in arbitrarily long squares is now also covered, e.g. certain non-Sturmian words constructed to contain squares without being balanced.

## RUNG C — numerically promising, missing combinatorial theorem

A class where computation suggests initial powers of exponent `>log₂3` occur, but no general theorem *guarantees* this for the whole class (as opposed to Rung B, where the guarantee is unconditional once the exponent threshold is met).

**Confirmed members (computational evidence, not yet general theorems)**:
- **CS Rote sequences derived from three tested Sturmian slopes** (golden ratio, silver ratio, a mixed-CF slope) — `ROTE_COMPUTATIONAL_AUDIT.md`: exact, growing-depth, positive-surplus certificates found for each (deepest tested: `ℓ≈1180`, `S>0`, exact integer arithmetic), via the confirmed `S(v)=u` construction and an original parity-dependent transfer lemma. Not yet a proof for the whole CS Rote class (a slope could in principle always land on odd-weight roots at unlucky moments) — genuine evidence, not certainty.
- **A specific non-Sturmian two-interval rotation coding** (golden-ratio rotation, mismatched partition length `δ=1/3`) — `ROTATION_CODING_AUDIT.md`: confirmed factor complexity exactly `2n` (genuinely non-Sturmian), and exact positive-surplus initial squares found (`ℓ=233, r≈2.41, S=316`; `ℓ=89, r≈2.08, S=86`).

## RUNG C — SPECIAL NOTE

Both confirmed Rung-C members above are the **first computationally-confirmed instances of the bridge reaching beyond the Sturmian class**, i.e. the first non-empty content in this rung. This directly answers (with evidence, not proof) the source paper's own Section 12, Open Problem (4): the periodic-approximation/Liouville bridge **does** generalize past Sturmian words, at least for these tested instances.

## RUNG D — bridge fails

Classes where the proposed periodic approximants provably do **not** generate positive surplus. **Confirmed member**: any construction relying on repetition exponent `r ≤ log₂3` at densities near `γ=1` (`BRIDGE_CONTROLS.md` Control 3, explicit `r=1.5` counterexample) — this is a member of Rung D *for that specific exponent*, not a statement about any natural sequence class.

## RUNG E — unknown / insufficient data

Reserved for classes not yet examined at all (e.g. most morphic/substitutive families beyond Thue–Morse, which is itself Rung D via total absence of relevant initial squares below the tested half-length).

*(Rote and rotation-coding placements to be added below once literature/computational audits complete.)*
