**RELEASE-READY, NOT RELEASED — NO PUBLICATION ACTION HAS BEEN TAKEN**

# RELEASE_REV2.md — Revision 2 release package

Prepared on branch `phase8-general-intercept`. Nothing is pushed, nothing is deposited, no Zenodo
record is created or edited. The repository's own publication gate
(`docs/PUBLICATION_CHECKLIST.md`-equivalent discipline: explicit author approval) applies.

## 1. What Revision 2 is

A **new Zenodo version** of the existing record — not an edit of it. Revision 1 stays retrievable at
its own version DOI; the concept DOI resolves to Revision 2 once published.

| | |
|---|---|
| Revision 1 version DOI | `10.5281/zenodo.23045141` |
| Revision 1 title | unchanged in Revision 2 |
| Revision 2 kind | new version, corrections + strengthened main theorem |
| Revision 2 length | 21 pages (Revision 1: 16) |

## 2. Package contents

| file | role | status |
|---|---|---|
| `technical-note/note_rev2.tex` | Revision 2 source | **new** |
| `technical-note/note_rev2.pdf` | Revision 2, rendered | **new**, builds clean |
| `technical-note/correction_notice.tex` / `.pdf` | standalone 2-page erratum | **new**, builds clean |
| `technical-note/RELEASE_REV2.md` | this file | **new** |
| `technical-note/note.tex`, `note.pdf` | Revision 1 source and deposited PDF | **untouched**, byte-identical |
| `technical-note/PRESERVATION_RECORD.md`, `SOURCE_OF_TRUTH.md`, `ZENODO_RECORD.md`, `ZENODO_PREP.md`, `FINAL_RELEASE_AUDIT.md`, `TITLE_DECISION.md` | Revision 1 provenance | **untouched** (their checksums describe Revision 1 and must stay valid) |

Upload set for the new version: `note_rev2.pdf` and `correction_notice.pdf`. Sources
(`note_rev2.tex`, `correction_notice.tex`) may be included; Revision 1 deposited a PDF only.

## 3. Change summary

### 3.1 Strengthened

The headline theorem now holds at **every intercept**:

> **Theorem.** Let `γ ∈ (0,1)` be irrational with bounded partial quotients. Let `u` be **any**
> Sturmian word of slope `γ` — **any** intercept, either the upper or the lower mechanical
> convention. Let `v` be either complementary symmetric Rote sequence with `S(v) = u` (either seed),
> or any shift `σ^j(v)`. Then `Φ(v) ∉ ℚ`.

Revision 1 stated this for the intercept-`0` representative only.

### 3.2 Corrected (five items, all in Revision 1 §§12–13 and its open-problem list)

| id | defect | correction |
|---|---|---|
| C1 | Conjecture 12.1 presented as an open lemma | It is **BHZ 2006 Prop. 5.1 + 5.2**. Bounded type satisfies one hypothesis or the other by pigeonhole, giving `ice(ω) ≥ 2 + 1/(2(A_b+1)²+1)` at every intercept. Withdrawn: "not claimed proved here or anywhere in the underlying record"; "that extension remains open". |
| C2 | the "exceptional-orbit reduction": `ice = ind*(γ)` off a countable return set | **False.** BHZ Prop. 2.1(4) gives shift-invariance only off a finite set of orbits; Lemma 2.2 gives equality only almost everywhere. BHZ's own Prop. 4.1 "keep one" intercept is a counterexample, and the admissible family `{a_k−c_k ∈ {1,2}}` is uncountable with `ice` uniformly bounded. Intercept `0` is among the **easiest** intercepts, not the hardest. Open 2 withdrawn. |
| C3 | convergent denominators with `q_1 = a_1` | BHZ Prop. 2.7 sets `γ = [0; a_1+1, a_2, …]`, `q_1 = a_1+1`. All `ice` values unaffected (limsups); all **root lengths** were wrong. Explains the root-length mismatch the Phase 7 record disclosed against itself; BHZ Prop. 3.3 was never wrong. |
| C4 | `S_k ≥ A·E_k − C_A D_k − O_A(log ℓ_k)` | Leading term must scale like a length: `S_k ≥ ℓ_k E_k + 1 − ⌈D(R_k)⌉log₂3 − log₂(2ℓ_k)` on the odd branch. Revision 1's own flexible condition `E_k ≫ log ℓ_k/ℓ_k` is equivalent to `ℓ_kE_k ≫ log ℓ_k`, so this was a transcription slip; no conclusion changes. |
| C5 | `y(k)` treated as an attained power for all admissible `(c_k)` | BHZ Prop. 3.3 attains `y(k)` only when `0 < c_k < a_k`; Cor. 3.5's three observations upgrade the limsup. Revision 2 routes every case through an attained witness. |

### 3.3 One gap closed while auditing

The discrepancy step reduces to the rotation by `γ/2`, not `γ`, so it needs `γ/2` to be of bounded
type — a hypothesis Revision 1 left implicit. Supplied as a lemma:
`‖qγ‖ = ‖2q(γ/2)‖ ≤ 2‖q(γ/2)‖`, so `inf_q q‖q(γ/2)‖ ≥ ½ inf_q q‖qγ‖ > 0`, and the partial
quotients of `γ/2` are bounded by `⌊2(A+2)⌋+1`. Conclusion `D = O_A(log ℓ)` unchanged.

### 3.4 Unchanged

Abstract irrationality criterion; discrepancy–height bound; repetition–height competition; exact
XOR transfer `L_v = L_u + 1`; density-`1/2` structural fact; the intercept-`0` case and its
`term2(k) > 2 + 1/(A+1)` analysis; counting-route material; the entire self-correction history; and
every numerical finding about structured intercepts, including the identification of the
near-maximal-digit family as the empirical worst case — which Revision 2 confirms is *exactly*
extremal, with excess exactly `1/(Aβ_A)`.

### 3.5 Scope discipline added

Revision 2 separates four tiers of margin claim (`theorems/phase8/PHASE8_MARGIN_STATUS.md`) and
**demotes** the sharp-optimum claim: `δ*(γ) = 1/(Aβ_A)` is proved only for slopes whose BHZ digits
are eventually constant with `A ≥ 2` (plus the Fibonacci slope, via BHZ Prop. 4.3); elsewhere it is
numerical evidence and is not promoted. The main theorem uses none of it.

### 3.6 Attribution

The load-bearing symbolic input is Berthé–Holton–Zamboni's, not this programme's. Revision 2 says so
in the abstract, in §2, in the theorem attributions, in `LADDER.md` and in `THEOREM_STATUS.md`. The
contribution claimed is the arithmetic application: the periodic-approximation/height bridge, the
exact XOR transfer, the density-`1/2` fact, the corrected surplus inequality, and the
attained-witness bookkeeping.

## 4. Historical record

No Phase 1–7 research file was rewritten. `theorems/phase7/PHASE7_CORRECTIONS.md` is new and indexes
all five corrections; the seven affected Phase 7 files each carry a conspicuous banner at the top
pointing to it, with their original text preserved verbatim below.

## 5. Proposed Zenodo version description (verbatim, ready to paste)

> **Revision 2 (30 September 2026) — corrected and strengthened.**
>
> This version corrects Revision 1 (`10.5281/zenodo.23045141`) in five places and strengthens its
> main theorem. A standalone 2-page correction notice is included alongside the full text.
>
> **Correction of record.** Revision 1 presented the general-intercept case as blocked by one
> unproved margin lemma, stated there as Conjecture 12.1, and said it was "not claimed proved here
> or anywhere in the underlying record." That lemma is not open: it is Berthé, Holton and Zamboni,
> *Initial powers of Sturmian sequences*, Acta Arithmetica 122 (2006) 315–347, **Propositions 5.1
> and 5.2** — Section 5 of the same paper Revision 1 already cites as its primary source. Recording
> a published 2006 theorem as an open conjecture was an error of literature search on the author's
> part.
>
> **Strengthened result.** The main theorem now holds at every intercept: for every irrational slope
> with bounded partial quotients, every Sturmian word of that slope (any intercept, either
> mechanical convention), and either complementary symmetric Rote sequence built on it (either seed,
> any shift), the Bernstein–Lagarias conjugacy map sends it to an irrational 2-adic integer.
>
> **Four further corrections.** (i) A convergent-denominator indexing error: BHZ set
> `α = [0; a_1+1, a_2, …]` with `q_1 = a_1+1`, where the underlying record used `q_1 = a_1`; every
> reported initial-critical-exponent value is unaffected, every root length computed from `q_k` was
> not. (ii) A false "exceptional-orbit reduction" claiming that the initial critical exponent equals
> `ind*(α)` outside a countable set of intercepts; the exceptional set is in fact uncountable, and
> intercept 0 is among the easiest intercepts rather than the hardest. (iii) A missing length factor
> in the surplus decomposition: the leading term is `ℓ_k · E_k`, not `A · E_k`. (iv) An overstated
> attainment claim: of the two Ostrowski repetition expressions, `y(k)` is an actually occurring
> initial power only when `0 < c_k < a_k`.
>
> **Attribution.** The load-bearing symbolic input — a positive initial-critical-exponent margin
> uniform over all intercepts of a bounded-type slope — is Berthé–Holton–Zamboni's. What is original
> here is the arithmetic application: the periodic-approximation/arithmetic-height bridge, the exact
> XOR transfer, the density-1/2 structural fact of the odd-weight route, the corrected surplus
> inequality, and the attained-witness bookkeeping with explicit growing root lengths that converts a
> limsup bound on the initial critical exponent into an unbounded surplus.
>
> **What survives unchanged.** The abstract irrationality criterion, the discrepancy–height bound,
> the repetition–height competition, the exact transfer identity, the density-1/2 fact, the
> intercept-0 case and its analysis, the counting-route material, the documented self-correction
> history, and every numerical finding about structured intercepts — including the identification of
> the near-maximal-digit family as the empirical worst case, which this revision confirms is exactly
> extremal.
>
> **Scope, unchanged.** This is a technical research note on an exclusion programme for structured
> symbolic classes. It does not prove, and claims no progress toward proving, the 3x+1 Periodicity
> Conjecture in general; a structural obstruction recorded in the underlying research record shows no
> purely repetition-based method can reach every aperiodic word. The frontier moves to slopes with
> unbounded partial quotients, where Berthé–Holton–Zamboni's Theorem 1.1 produces an intercept whose
> initial critical exponent is exactly 2.

**Zenodo metadata to leave unchanged:** title, authors, ORCID, licence, keywords, resource type.
**To set:** publication date `2026-09-30`; version `Revision 2`; and a "relates to" entry pointing
at Revision 1's version DOI if the interface offers one.

## 6. Reproducibility

See §7 for the manifest and checksums, and `theorems/phase8/PHASE8_VERDICT.md` §3 for what each
script certifies. All eight Phase 8 scripts run to completion with exact-`Fraction`/integer
arithmetic and assert their own claims; `data/phase8/` holds their captured output.

## 7. Manifest and checksums

Generated by the command recorded at the end of this file.

```
# generated: cd <repo> && sha256sum technical-note/note_rev2.{tex,pdf} technical-note/correction_notice.{tex,pdf} \
#              theorems/phase8/*.md theorems/phase7/PHASE7_CORRECTIONS.md scripts/phase8/*.py

8beddcddf188b29b29d3f27c176c172a8aa0afb05f6336ccbcf5c03234bf1528  technical-note/note_rev2.tex
8daf19799b44f877a8e661109e33af4d76ebd072f8fcb35bb856b07f6513b81a  technical-note/note_rev2.pdf
2659a21a82a171e8e2624ddffc4a384ca1273645ba22ebf4adb7c7dac62fc0f1  technical-note/correction_notice.tex
0c93457cde3a2bd976321b1547121c7a0413506f8d21931628fb525e5835fde1  technical-note/correction_notice.pdf
5bb0957b3ec0f0dd7df7cea53e842e158419eae946dac369862ab29177d726c2  theorems/phase8/PHASE8_CHAIN_AUDIT.md
2ede9b6a254e753d4348de7c9441cdd4368bf1be5e38302b38ca6b9bf3db5e0e  theorems/phase8/PHASE8_MARGIN_STATUS.md
75f0be94a35dca89b2361f532fc622e7fda5f486fc39c93c94990e7581200e09  theorems/phase8/PHASE8_NEXT_TARGET.md
9af2d7ba82185e232d6c172db75a79f8d6e585b58089396006df34e2683d9024  theorems/phase8/PHASE8_PROOF_OR_OBSTRUCTION.md
2cabe89da1c821059e497a3f407da3b08569105ab145181ecc8a9d15b4207008  theorems/phase8/PHASE8_TARGET_AUDIT.md
bbbb1a4a03be8f40483f8bed120d3b928450579bc9001099753a2f1e45ca1b95  theorems/phase8/PHASE8_VERDICT.md
7f16c504d53d7592cf3737217bda5df61902ea35b537997dc20af772cc04d3fa  theorems/phase7/PHASE7_CORRECTIONS.md
24e05ef35fa46c4e846134893f4fc72bbf4e1b4d9db5e1c7a8020e8e1acb76c8  scripts/phase8/phase8_chain_audit.py
9f1d3d819819b6a45b70e61205f8787b3e6a795f054401c1fe84582e49380e12  scripts/phase8/phase8_exceptional_orbit_refutation.py
639c0b55b97211da2f9dd998497b287ce522631141cd8495eb8fac4f236bea69  scripts/phase8/phase8_ice2_boundary.py
53836bc8bc88010f8d3927c9380e85141e1a8468c550de5bc6dc0d67b00c6846  scripts/phase8/phase8_identities.py
c604e96c753f2d0c3393893c892b727558118e676ad91737d5ae6701f03de0e4  scripts/phase8/phase8_literal_prefix.py
17bb055ddd337066f75c32023433e2f76fe49da20ea7e5ebb710e1ea9a692d7c  scripts/phase8/phase8_margin_optimality.py
80f8ce88b15e6426044551693c06717c8cafc4d8dba5eb236d1e6d236dcda465  scripts/phase8/phase8_margin_search.py
e7c3ce4565c5f317796ee70b5b4ce9745d63c763687f60f114443e94be9c2125  scripts/phase8/phase8_surplus.py

# Revision 1, unchanged (must match technical-note/ZENODO_PREP.md):
4bd0922483738811a7bf3794bc6f3258e5b2f54b5e32faf0d9bee2d822f89136  technical-note/note.tex
b7054cee82cb847e11e003ad4f6a319e37c69c4873270ae56e93fed97fce008d  technical-note/note.pdf
```

## 8. Reproducibility run, 2026-09-30

```
phase8_identities                        exit=0  ALL IDENTITY CHECKS PASS.
phase8_literal_prefix                    exit=0  RESULT: ALL LITERAL CHECKS PASS
phase8_margin_search                     exit=0  ALL MARGIN CHECKS PASS.
phase8_surplus                           exit=0  ALL SURPLUS CHECKS PASS.
phase8_exceptional_orbit_refutation      exit=0  ALL REFUTATION CHECKS PASS.
phase8_chain_audit                       exit=0  ALL CHAIN-AUDIT CHECKS PASS.
phase8_margin_optimality                 exit=0  ALL MARGIN-STATUS CHECKS PASS.
phase8_ice2_boundary                     exit=0  ALL ICE-2 BOUNDARY CHECKS PASS.

[exited with code 0]
```

Every script asserts its own claims; a non-zero exit means a claim failed. PDF builds:
`pdflatex` twice on each of `note_rev2.tex` and `correction_notice.tex`, no undefined
references and no undefined citations (the single remaining warning, `OMS/cmtt/m/n`
undefined, is a font-shape substitution already present in Revision 1).
