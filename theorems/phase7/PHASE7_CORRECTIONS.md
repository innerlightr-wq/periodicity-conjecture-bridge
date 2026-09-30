**CORRECTION NOTICE FOR PHASE 7 — READ BEFORE USING ANY FILE IN THIS DIRECTORY**

# PHASE7_CORRECTIONS.md

Phase 8 audited Phase 7 against the Berthé–Holton–Zamboni primary source read first-hand and
found five defects. **No file in `theorems/phase7/` has been altered**: the historical record is
preserved verbatim, and each affected file carries a banner pointing here. Authority for the
corrected statements is `theorems/phase8/`.

| # | Phase 7 claim | verdict | corrected statement |
|---|---|---|---|
| C1 | `INTERCEPT_SUFFICIENT_CONDITION.md` and `PHASE7_VERDICT.md`: the general-intercept margin lemma is **CONJECTURAL**, "strong evidence, no proof" | **SUPERSEDED — it is a published theorem** | BHZ 2006 **Propositions 5.1 and 5.2** prove it: `ice(ω) ≥ 2 + 1/(2(A_b+1)²+1)` for every `ω ∈ X_α` of bounded type. Phase 7 read BHZ §2–§4 and did not reach §5. See `theorems/phase8/PHASE8_TARGET_AUDIT.md` §3, `theorems/phase8/PHASE8_MARGIN_STATUS.md` T1. |
| C2 | `BHZ_GENERAL_INTERCEPT_MAP.md`: "`ice(ω_ρ) = ind*(α)` for **every** intercept except the countable return set `{jα mod 1}`"; hence (`PHASE7_VERDICT.md`) the open cases are countable and "intercept `0` is, if anything, a harder case than generic" | **REFUTED** | BHZ Prop. 2.1(4) gives only shift-invariance off a *finite set of orbits*, and Lemma 2.2 only `ice = ind*(α)` **almost everywhere**; a measure-zero set need not be countable, and here it is not. BHZ's own Prop. 4.1 "keep one" intercept (`c_k = a_k − 1`) has `ice ≤ 1 + θ` at every slope while `ind*(α) = 2 + β_A → ∞`, and the family `{a_k − c_k ∈ {1,2}}` is uncountable with `ice ≤ 5` uniformly. Intercept `0` has `ice = ind*(α) − 1 → ∞`, so it is one of the **easiest** intercepts. See `theorems/phase8/PHASE8_TARGET_AUDIT.md` §4 and `scripts/phase8/phase8_exceptional_orbit_refutation.py`. |
| C3 | `BHZ_GENERAL_INTERCEPT_MAP.md`, `OSTROWSKI_WITNESS_MAP.md`, `scripts/phase7/bhz_general_witness.py`: convergent denominators with `q_1 = a_1` | **INDEXING ERROR** | BHZ Prop. 2.7 fixes `α = [0; a_1 + 1, a_2, a_3, …]`, `q_1 = a_1 + 1`. Limsups are insensitive to the shift, so every `ice` value Phases 4–7 report is right; every **root length** is wrong. This is the complete explanation of the mismatch `PHASE7_VERDICT.md` honestly disclosed — BHZ Prop. 3.3 was never wrong. See `theorems/phase8/PHASE8_TARGET_AUDIT.md` F1 and `scripts/phase8/phase8_literal_prefix.py`. |
| C4 | `SURPLUS_DECOMPOSITION.md`: `S_k ≥ A·E_k − C_A·D_k − O_A(log ℓ_k)` | **DIMENSIONALLY INCOMPLETE** | The leading term must be a length: `S_k ≥ ℓ_k·E_k + 1 − ⌈D(R_k)⌉log₂3 − log₂(2ℓ_k)` on the odd branch. The file's own flexible condition `E_k ≫ log ℓ_k/ℓ_k` is consistent with `ℓ_k·E_k`, so this is a transcription slip, not a different claim; conclusions drawn from it are unaffected. See `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md` §4. |
| C5 | `BHZ_GENERAL_INTERCEPT_MAP.md`: `y(k)`'s witnesses are "real, growing-length, actually-occurring initial powers, for any admissible `(c_k)`" | **OVERSTATED** | BHZ Prop. 3.3 attains `y(k)` only when `0 < c_k < a_k`; Corollary 3.5's three observations (`c_k = a_k ⇒ y(k) = x(k−2)`, etc.) are what upgrade the `limsup`. Phase 8 Theorem 1 routes every case through an attained witness explicitly. See `theorems/phase8/PHASE8_TARGET_AUDIT.md` F3. |

## What in Phase 7 stands unchanged

- **Every numerical finding.** `STRUCTURED_INTERCEPTS.md`'s 36/36 configurations, the
  identification of the near-maximal-digit family as the empirical worst case
  (`INTERCEPT_SUFFICIENT_CONDITION.md`), and the `~1/A²` decay rate are all correct — Phase 8
  confirms the near-maximal family (`d_k ≡ 1`, BHZ's "keep one") is *exactly* extremal and the
  rate is exactly `1/(Aβ_A)`.
- **`FLEXIBLE_MARGIN_BOUNDARY.md`.** Its table and its own conclusion ("not needed in practice")
  are correct; Phase 8 lands in the first row (`ε_k ≍ const`).
- **`INTRINSIC_SQUARE_ROUTE.md`.** Its reading is correct and is confirmed by Phase 8: bare
  squares give a fixed margin on the even-weight branch and **exactly zero** on the odd-weight
  branch. The route is superseded (Theorem 1 supplies `r_u > 2` strictly), not repaired.
- **The disclosure discipline.** `PHASE7_VERDICT.md` flagged its own root-length mismatch rather
  than hiding it. That disclosure is what made C3 findable.

## Net effect on the record

Phase 7's classification "OBSTRUCTION CLASSIFIED — ONE LEMMA REMAINS" should be read as
**superseded**: the lemma was not remaining, and the structural reduction offered alongside it was
false. The general-intercept case is closed in `theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md`
(Theorem 2).
