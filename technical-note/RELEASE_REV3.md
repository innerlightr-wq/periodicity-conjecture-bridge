**DRAFT — NOT DEPOSITED. No Zenodo action has been taken.**

# RELEASE_REV3.md — Revision 3 draft package

## 1. What Revision 3 is

A **draft** of a new Zenodo version of the existing record. Revisions 1 and 2 stay retrievable at
their own version DOIs. **Nothing has been uploaded, published, or overwritten**, and the deposited
Revision 2 PDF and its erratum are byte-identical to their released state.

| | |
|---|---|
| Revision 1 version DOI | `10.5281/zenodo.23045141` |
| Revision 2 | deposited as a new version of the same record |
| Revision 3 kind | **draft**: two new theorems + six corrections |
| Revision 3 length | 34 pages (Revision 2: 21; Revision 1: 16) |

## 2. Files

| file | role | state |
|---|---|---|
| `technical-note/note_rev3.tex` | Revision 3 source | **new** |
| `technical-note/note_rev3.pdf` | Revision 3, rendered | **new**, builds clean (3 `pdflatex` passes, no undefined references or citations, no multiply-defined labels) |
| `technical-note/note_rev2.tex`, `note_rev2.pdf` | Revision 2 | **untouched**, byte-identical |
| `technical-note/note.tex`, `note.pdf` | Revision 1 | **untouched**, byte-identical |
| `technical-note/correction_notice.tex`, `.pdf` | Revision 2 erratum | **untouched**, byte-identical |

## 3. What is new

| | statement | note reference |
|---|---|---|
| N1 | quadratic irrational `α ∈ (0,1)`, **rational** `ρ` (incl. `ρ = 0`): `Φ(s(α,ρ)) ∉ ℚ` | Theorem 17.5 |
| N2 | the same for every **real algebraic** `ρ` | Theorem 18.2 |
| N2′ | the interval `[u,u+β)` whenever `ρ−u` is algebraic — `ρ`, `u` themselves unrestricted | Corollary 18.3 |
| N3 | the coverage map rebuilt on **lower ones-density**, the coordinate the existing results read | §16 |

The research record's informal labels map as: Theorem 11 → Theorem 17.5 (the named case);
Theorem 12 → Theorem 17.5; Theorem 13 → Theorem 18.2; Corollary 13.1 → Corollary 18.3. The note's
numbering is by section and carries no relation to phase numbers; §1 D5 says so explicitly.

## 4. Corrections carried

| | subject |
|---|---|
| D1 | the **Thue–Morse scope claim** of Revision 2 §19 Open 6 and §20 is **withdrawn** — it is false; the substitution supplies approximants without any square |
| D2 | the **CS Rote novelty framing** — it crosses the *counting* frontier only; the conclusion was already available from Monks–Yazinski (2004) Thm 2.7(b), CS Rote having density `1/2 < β` |
| D3 | **López–Stoll**: acknowledgement of influence, and a statement that their proposed upper-density exclusion is not used and is neither established nor disproved here |
| D4 | the **foundation paper** is now public; cited by version DOI `10.5281/zenodo.23019799`, and labelled an unrefereed **self-citation** |
| D5 | **theorem numbering** clarified (section-based, not phase-based) |
| D6 | the **polynomial logarithmic-form bound** claimed at an intermediate stage is **withdrawn**; the note states none |

## 5. Checksums

```
229ed0408ca1be7feac225918935812e3d3ba29dad915be0b8186d4ff55f69f2  technical-note/note_rev3.tex
a2c093516d32fd95077d1e407164d47dc53d67f2ad50fac93cfa3cec02d2c939  technical-note/note_rev3.pdf

# unchanged, must still match RELEASE_REV2.md §7 and ZENODO_PREP.md:
8beddcddf188b29b29d3f27c176c172a8aa0afb05f6336ccbcf5c03234bf1528  technical-note/note_rev2.tex
8daf19799b44f877a8e661109e33af4d76ebd072f8fcb35bb856b07f6513b81a  technical-note/note_rev2.pdf
2659a21a82a171e8e2624ddffc4a384ca1273645ba22ebf4adb7c7dac62fc0f1  technical-note/correction_notice.tex
0c93457cde3a2bd976321b1547121c7a0413506f8d21931628fb525e5835fde1  technical-note/correction_notice.pdf
4bd0922483738811a7bf3794bc6f3258e5b2f54b5e32faf0d9bee2d822f89136  technical-note/note.tex
b7054cee82cb847e11e003ad4f6a319e37c69c4873270ae56e93fed97fce008d  technical-note/note.pdf
```

## 6. Before any deposit — the author's checklist

1. Read §1 (Revision 3) and confirm D1–D6 say what you want said, especially D2 and D3.
2. Decide whether the acknowledgement in §16 and the Acknowledgments section is worded as you want.
3. Decide whether a **second erratum** should accompany Revision 3 for D1 and D2, as
   `correction_notice.tex` accompanied Revision 2. Not drafted.
4. Confirm the scope sentences: the note claims nothing about integer Collatz orbits, nothing about
   the Periodicity Conjecture in general, and leaves novelty formally unresolved.
5. Only then set version metadata and upload. **Nothing here does any of that.**
