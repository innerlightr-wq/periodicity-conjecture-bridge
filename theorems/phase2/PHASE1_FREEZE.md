# PHASE1_FREEZE.md

Frozen snapshot of Phase 1's exact claims, verbatim in substance (not strengthened, not weakened), as of the checksums in `PHASE1_CHECKSUMS.txt` (29 files: 17 root-level `.md`, 1 root-level `.txt`, 8 `scripts/*.py`, 4 `data/*` outputs — note `BRIDGE_VERDICT.md` and `CURRENT_BRIDGE.md` etc. are included in the 17; the exact count/list is in the checksum file, which is the authoritative record). Phase 2 must cite this file, not re-read or re-paraphrase Phase 1 sources, to avoid silent drift.

## 1. The abstract bridge theorem (`ABSTRACT_BRIDGE_THEOREM.md`)

Setup: `s∈{0,1}ℕ`, `Φ(s)=u/v∈Q∩Z₂` in lowest terms, `v≥1` odd, `H=max(|u|,v)`. `(W_n)` finite words, `ℓ_n=|W_n|`, `k_n`=ones, `s≠W_n^∞`. `L_n=lcp(s,W_n^∞)`, `δ_n=2^{ℓ_n}−3^{k_n}`, `c_n=c_{W_n}`, `M_n=uδ_n−vc_n`.

Proved facts, exactly as stated: `M_n≠0` (else `Φ` bijectivity forces `s=W_n^∞`, contradiction); `v₂(M_n)=L_n` exactly (via Proposition 2.2, the isometry, applied with no hypothesis on `s` or `W_n` beyond membership in `{0,1}ℕ`); hence `|M_n|≥2^{L_n}` exactly, no slack. Archimedean side: `|M_n|≤H·F(W_n)`, `F(W):=max(2^{|W|},3^{k(W)})+c_W`, the "crudest fully general" bound, no discrepancy/balance/repetition hypothesis used to derive `F` itself.

**Theorem (as stated).** If `limsup_n S_s(W_n)=+∞` where `S_s(W):=lcp(s,W^∞)−log₂F(W)`, then `Φ(s)∉Q`. **Status: PROVED**, unconditional, no Sturmian/Rote-specific input anywhere in the proof.

Sharpness note recorded verbatim: **`limsup`, not `→+∞`**, is the exact hypothesis the proof uses (an oscillating `S_n` with `limsup=+∞` still suffices). No hidden log/polynomial correction terms — `(‡)` is exact for every `n`, not asymptotic.

## 2. The discrepancy-height theorem (`DISCREPANCY_HEIGHT_THEOREM.md`)

`D(W)=max_{0≤i≤ℓ}|k_i(W)−ik/ℓ|`. **Theorem (proved):** `c_W ≤ ℓ·3^{⌈D⌉}·max(2^ℓ,3^k)`. Exactly recovers the source paper's own Lemma 4.2 (`D=0→` constant `1`) and Remark 4.3/Lemma 10.4 (`D<1→` constant `3`) as special cases — flagged in Phase 1 as strong evidence, not proof, that `C(D)=3^{⌈D⌉}` is the natural completion of the paper's own technique.

**Hard combinatorial cap (proved + exhaustively verified to `ℓ≤12`):** `D(W)≤γ(1−γ)ℓ≤ℓ/4` for **every** word, at **every** density, equality only at single-block words `0^{ℓ−k}1^k`/`1^k0^{ℓ−k}`.

**Consequence (proved):** `sup_{γ∈(0,1)}[max(1,γlog₂3)+γ(1−γ)log₂3] = log₂3 <2`, so `r=2` squares need **no discrepancy hypothesis whatsoever**.

**General sublinear-discrepancy theorem (proved):** if `s` begins in `W_n^{r_n}`, `ℓ_n→∞`, `γ_n→γ_∞`, `D(W_n)=o(ℓ_n)`, and `r>max(1,γ_∞log₂3)` strictly, then `S→+∞`.

## 3. The repetition-height criterion (`REPETITION_HEIGHT_CRITERION.md`)

**Uniform theorem (proved, no density-convergence assumption):** if `r_n≥r` for all `n`, `D(W_n)=o(ℓ_n)`, `ℓ_n→∞`, densities `γ_n` **arbitrary** (no convergence assumed), and `r>sup_γ max(1,γlog₂3)=log₂3`, then `Φ(s)∉Q`.

**Unconditional-squares theorem (proved, using the discrepancy cap from §2):** arbitrarily long initial squares (`r=2`) alone, **with no discrepancy/balance/arrangement hypothesis at all**, suffice for `Φ(s)∉Q`. Margin `2−log₂3=0.41503...`.

**Boundary case recorded:** at `r=1`, the margin `1−max(1,γlog₂3)≤0` for every `γ`, i.e. `r=1` gives nothing; `r>1` strictly is essential.

**`qx+1` diagnostic recorded (Remark 10.7, cited, not re-derived in Phase 1):** the per-letter cost generalizes to `max(1,γlog₂q)`; squares (`r=2`) stop being unconditionally sufficient once `log₂q≥2`, i.e. `q≥4`; paper's own computed first-failing odd multiplier is `q=5`.

## 4. The Rote transfer lemma (`ROTE_LITERATURE_AUDIT.md` + `ROTE_COMPUTATIONAL_AUDIT.md`)

**Confirmed literature construction:** `v` is CS Rote `⟺` `u=S(v)` Sturmian, `u_i=v_i⊕v_{i+1}`. Inverse: given Sturmian `u`, seed `v_0`, unique `v` via `v_{n+1}=v_n⊕u_n` (Rote 1994; Dvořáková–Medková–Pelantová 2020, arXiv:2003.06916).

**Phase 1's original transfer lemma (stated, verified on 3 synthetic examples only — NOT proved in general in Phase 1):** if `u` has initial power `W^r` (root weight `s=ΣW`), `v` inherits exponent `r` at same root length (`s` even) or exponent `r/2` at root length `2ℓ` (`s` odd).

**Explicitly flagged Phase 1 caveat, preserved verbatim:** "the literature's own critical-exponent results ... do not directly answer the question ... concern powers occurring anywhere, not initial powers." The literature's `cr(v)≥2+1/√2≈2.707` (Dvořáková–Medková–Pelantová, global minimum over all CS Rote sequences) and repetition threshold `5/2` (Ollinger–Shallit 2024) are **background corroboration only, not the basis of any Phase 1 claim**.

## 5. The three CS Rote computational cases (`ROTE_COMPUTATIONAL_AUDIT.md`)

Exact-arithmetic search, root length ≤1200, **every** initial power examined (`r≥1`, no pre-filter), exact surplus `S` computed for each:

| Slope | `u` certifying (S>0) | `v` certifying (S>0) | Deepest `v` certificate |
|---|---|---|---|
| golden ratio conjugate | 66 | 32 | `ℓ=1178, r≈1.018, S=6` |
| silver ratio | 55 | 20 | `ℓ=1183, r≈1.059, S=53` |
| mixed CF `[0;1,2,1,3,1,4,...]` | 9 | 31 | `ℓ=1187, r≈1.016, S=2` |

**Phase 1's own explicit scope limit, preserved verbatim:** "Three slopes, not a general theorem... does not by itself guarantee arbitrarily deep certification for an arbitrary slope... not observed in these three tests, but not ruled out in general." **Rung placement recorded as "Rung C → B, upgraded, for the three tested slopes... not yet a general theorem covering the whole CS Rote class."**

**Bug disclosed and preserved:** the CF evaluator (`cf_convergent` in both `rote_construction_test.py` and `rotation_coding_test.py`) originally returned `den/num` instead of `num/den`, silently producing reciprocal slopes (e.g. `2.41421356` instead of `0.41421356` for "silver ratio"). Caught via an internally-impossible result (`k>ℓ`). Fixed; all Phase 1 numbers above are post-fix.

## 6. The non-Sturmian rotation-coding example (`ROTATION_CODING_AUDIT.md`)

One instance: golden-ratio rotation, mismatched partition `δ=1/3`, `ρ=0`. Confirmed complexity exactly `2n` (`p_s(30)=60`). Two exact positive-surplus initial squares found: `ℓ=233,r≈2.412,S=316`; `ℓ=89,r≈2.079,S=86`. **Explicitly recorded as "one concrete instance, not a general theorem over all `(γ,δ,ρ)`."**

## 7. Every remaining Phase 1 caveat (consolidated, for Phase 2 not to silently lose)

- The converse of the abstract bridge theorem (bounded surplus `⟹` rational) is **not established** (`SURPLUS_INVARIANT.md`, `FULL_PERIODICITY_GAP.md` Q5) — sufficiency only, not equivalence.
- The counting route (`Corollary 9.3`, threshold `1/log₂(3/2)=1.70951...`) and the repetition route are **not nested** — neither contains the other.
- Thue–Morse has no square below half-length 2048 — a structural limitation of *any* repetition-based method, not a gap in this specific bridge.
- No natural subclass of Rote or rotation-coding words has been **proved** (as opposed to computationally evidenced) to satisfy the bridge universally, as of the end of Phase 1.
- `PRIOR_ART_BRIDGE.md`'s negative search result is explicitly **not** claimed as proof of novelty — absence of a hit, not proof of absence.

## Freeze declaration

Nothing in this file strengthens, weakens, or reinterprets any Phase 1 statement beyond direct quotation/restatement for reference. Any theorem proved in Phase 2 that appears to contradict a Phase 1 "computational evidence only" caveat must be reconciled explicitly in the relevant Phase 2 file, not silently substituted.
