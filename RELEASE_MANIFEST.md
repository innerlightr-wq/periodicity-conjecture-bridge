# RELEASE_MANIFEST.md — Revision 4 package

**Status: prepared for review. Nothing deposited, uploaded, or published.**
Branch `phase15-corrected-release`. Commit recorded in §5 below.

## 1. New artifacts

| file | pages | SHA-256 |
|---|---|---|
| `technical-note/note_rev4.tex` | — | `5abccf4352305fdf4e183170ee7484e97b1bda4684b67de626e785078de44332` |
| `technical-note/note_rev4.pdf` | 39 | `861d9994dddbc2df2b37c6dc6e80e308cc432cc760f048621d6f21854eeeacdf` |
| `technical-note/correction_notice_rev4.tex` | — | `9fc42ed8f2f007bb9fdee3deb4e734989800cdb0cc22724db89d7bdc9580fe37` |
| `technical-note/correction_notice_rev4.pdf` | 2 | `b7edea35887d1065b73db5b6b67b3a59b9ffc3b4630efce179620b77ef7fd78b` |
| `technical-note/ZENODO_DESCRIPTION_REV4.md` | — | `f60af3df6bdd9ab32b55f15dc1e35d3450d66ad914ceb3da10b5ce81bd06e3ec` |
| `REVIEW_GUIDE.md` | — | `11dee4da6d5324936ea7ee1c954f40f7d7d617b01f52c9d939f98d38aedd366a` |
| `RELEASE_MANIFEST.md` | — | (this file) |

## 2. Deposited artifacts — unchanged, byte for byte

Every deposited file is untouched by this phase. Verified at the time of the commit:

| file | deposited as | SHA-256 | md5 |
|---|---|---|---|
| `technical-note/note.pdf` | Revision 1, `10.5281/zenodo.23045141` | `b7054cee82cb847e11e003ad4f6a319e37c69c4873270ae56e93fed97fce008d` | `9b80c77cb374270066492980f40ee5ba` |
| `technical-note/note_rev2.pdf` | Revision 2, `10.5281/zenodo.23061396` (and, byte-identically, `…23068326`) | `8daf19799b44f877a8e661109e33af4d76ebd072f8fcb35bb856b07f6513b81a` | `b61d76f6a3a0d23ec6d148f1aeea658b` |
| `technical-note/note_rev3.pdf` | Revision 3, `10.5281/zenodo.23068563` | `a2c093516d32fd95077d1e407164d47dc53d67f2ad50fac93cfa3cec02d2c939` | `4e37bf96f28414bc51eb6f90e6b87e9e` |
| `technical-note/correction_notice.pdf` | Revision 2 erratum — **never deposited** | `0c93457cde3a2bd976321b1547121c7a0413506f8d21931628fb525e5835fde1` | `afd30d3bbeba5350efd8dc4be3670f7b` |
| `reference/…irrational-2adic-integer.pdf` | foundation paper, `10.5281/zenodo.23019799` | `e125c75248f5ca1c47a061f408013ec15368d246d1001dc84672a84df0eba8f4` | `54732e14b939c39f74c118097a069f30` |

## 3. Deposit history of the concept record `10.5281/zenodo.23045140`

| version DOI | date | file | contents |
|---|---|---|---|
| `10.5281/zenodo.23045141` | 2026-09-29 | `Beyond_Sturmian_Words_in_the_3x1_Periodicity_Conjecture.pdf` | Revision 1, 16 pp |
| `10.5281/zenodo.23061396` | 2026-09-30 | `Beyond_Sturmian_Words_Revision_2.pdf` | Revision 2, 21 pp |
| `10.5281/zenodo.23068326` | 2026-09-30 | `Beyond_Sturmian_Words_Latest_Built.pdf` | **the same file as Revision 2, byte for byte** |
| `10.5281/zenodo.23068563` | 2026-09-30 | `Beyond_Sturmian_Words_Revision_3_DRAFT.pdf` | Revision 3, 34 pp |

Record `…23068326` is documented, not altered. Zenodo versions are permanent by design; the correct
response is accurate citation guidance, which is given in the manuscript's provenance table, in the
correction notice, and in the proposed description. **Cite Revision 2 as `10.5281/zenodo.23061396`.**

## 4. Build and verification record

**Manuscript.** `pdflatex` × 3 passes, `-halt-on-error`. Result: 39 pages, **no undefined references,
no undefined citations, no multiply-defined labels, no overfull or underfull boxes.** Pre-build static
checks on the source: 0 duplicate labels, 0 dangling `\ref`, 0 missing `\cite`, 0 unused `\bibitem`,
0 stray Markdown.

**Visual page inspection.** All 39 pages examined via extracted text: section and subsection heads
land where intended, the new §19 sits between §18 (the analytic input) and §20 (finite certificates),
the revision history appears as Appendix A, and there is exactly **one** theorem-mapping table (the
duplicate that the appendix move created was removed). The only near-empty page is the last, being the
tail of the bibliography.

**Theorem renumbering.** Moving the two correction sections into the appendix shifted section numbers
by one, so Revision 3's Theorem 17.5 / 18.2 / Corollary 18.3 are Revision 4's **16.5 / 17.2 / 17.3**.
All internal references use `\ref` and updated automatically; the mapping table in §1 and the
cross-references in `README.md`, `LADDER.md`, `THEOREM_STATUS.md` and `REVIEW_GUIDE.md` were updated by
hand and checked.

**Computational checks.** No changed statement created a new verification need: §19's content is
exactly what `scripts/phase14/explicit_constants.py` already verifies (the Kuipers–Niederreiter
specialisation, `Δ(N) ≤ 4.880840 log₂N + 7`, `C` and `C₀` against exact surpluses at twelve
convergents, the proved `H(A_m) ≤ 2601m²`, `c₁`, `f(M)` and the threshold). All five relevant scripts
were re-run: see §5.

**Cross-document agreement.** `C = 24.207846`, `C₀ = 35.869175`, `M₀ ≈ 1.78·10^18`,
`c₁ = 2.38907·10^13`, `H ≥ 2^15998`, and all five DOIs were checked for agreement across the
manuscript, `README.md`, `LADDER.md`, `THEOREM_STATUS.md`, `REVIEW_GUIDE.md`, the proposed description
and the two Phase 14 documents. **No contradictory value found.**

## 5. Script results and commit

All five relevant scripts re-run in this worktree, all exit 0:

```
phase12/independent_audit.py     ALL PHASE-12 INDEPENDENT-AUDIT CHECKS PASS.
phase12/general_quadratic.py     ALL PHASE-12 GENERALIZATION CHECKS PASS.
phase13/algebraic_intercept.py   ALL PHASE-13 ALGEBRAIC-INTERCEPT CHECKS PASS.
phase13/ridout_exponent.py       ALL PHASE-13 RIDOUT-EXPONENT COMPUTATIONS COMPLETE (a measurement)
phase14/explicit_constants.py    ALL PHASE-14 EXPLICIT-CONSTANT CHECKS PASS.
```

**Branch:** `phase15-corrected-release`, cut from `phase14-release-reconciliation` at `2c298f5`
(ancestry verified: `2c298f5`, `5d04064`, `ec035dd` and `46b0d0a` are all ancestors).
**Commit:** `82cb949`

## 6. Readable local copies

| file | pages | SHA-256 |
|---|---|---|
| `~/Downloads/Beyond_Sturmian_Words_Revision_4.pdf` | 39 | `861d9994dddbc2df2b37c6dc6e80e308cc432cc760f048621d6f21854eeeacdf` |
| `~/Downloads/Beyond_Sturmian_Words_Revision_4_Correction_Notice.pdf` | 2 | `b7edea35887d1065b73db5b6b67b3a59b9ffc3b4630efce179620b77ef7fd78b` |

Neither filename contains `DRAFT`. Neither overwrote a different existing file.

```bash
xdg-open ~/Downloads/Beyond_Sturmian_Words_Revision_4.pdf
xdg-open ~/Downloads/Beyond_Sturmian_Words_Revision_4_Correction_Notice.pdf
```

## 7. What is deliberately not done

- Nothing pushed; nothing deposited; no Zenodo field edited; no review invitation sent.
- No deposited PDF modified or renamed.
- No mathematical statement of Revision 3 altered or withdrawn.
- The duplicate record is documented, not deleted.
