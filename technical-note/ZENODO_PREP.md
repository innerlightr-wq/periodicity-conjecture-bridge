# ZENODO_PREP.md

**Status: DEPOSITED.**

DOI: **10.5281/zenodo.23045141**
Canonical URL: https://doi.org/10.5281/zenodo.23045141

Citation:

> De Jesus, Elias. (2026). Beyond Sturmian Words in the 3x+1 Periodicity Conjecture: A Periodic-Approximation and Arithmetic-Height Bridge. Zenodo. https://doi.org/10.5281/zenodo.23045141

Deposited PDF SHA-256 (must match `technical-note/note.pdf` and the archival copy at `~/Downloads/Beyond_Sturmian_Words_in_the_3x1_Periodicity_Conjecture.pdf`):

```
b7054cee82cb847e11e003ad4f6a319e37c69c4873270ae56e93fed97fce008d
```

`note.tex` and `note.pdf` were **not** altered as part of recording this deposit — this file, `README.md`, `CITATION.cff`, and `technical-note/ZENODO_RECORD.md` are the only files updated.

---

## What was done, in order

1. **Deposit.** `technical-note/note.pdf` was uploaded to Zenodo; Zenodo minted DOI `10.5281/zenodo.23045141`.
2. **`CITATION.cff` updated.** A `preferred-citation` block (type `article`) now carries the DOI, title, author, ORCID, and year for the technical note, alongside the existing top-level software citation for the repository itself — the repository was not incorrectly turned into "the Zenodo publication" at the top level; see `CITATION.cff` directly.
3. **`README.md` updated.** A "Technical Note" section near the top now names the note, gives the DOI as visible text and a link, and states plainly that the full Periodicity Conjecture and the general-intercept extension both remain open. No Zenodo badge was added, since `README.md` did not use badges before this change (see `technical-note/ZENODO_RECORD.md` item 7 for the reasoning).
4. **`technical-note/ZENODO_RECORD.md` created** as the permanent provenance record of this deposit.

## Not done, by design (this deposit)

- **The PDF itself was not touched or re-deposited.** The original `ZENODO_PREP.md` (prior version) sketched an optional Step 4 — adding a `\thanks{DOI: ...}` line inside `note.tex` and recompiling to produce a self-describing PDF, then depositing that as a new Zenodo version. That step was **deliberately not performed** in this pass: the task that produced this deposit explicitly required the deposited PDF's SHA-256 to remain unchanged and forbade regenerating it. If a self-describing PDF (with the DOI printed on its own title page) is wanted later, it requires a **new, separate decision** to edit `note.tex`, recompile, and deposit a new Zenodo version — not an automatic follow-on to this file.
- No Phase 1–7 research file was touched.
- No further DOI, version, or Zenodo record was created beyond the one above.
