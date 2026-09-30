**THE DEPOSITED REVISION 3 IS THE LOCAL FILE, BYTE FOR BYTE — BUT THE RECORD NEEDS FOUR FIXES**

# ZENODO_RELEASE_RECONCILIATION.md

Phase 14 / item 1. Everything below was read from the Zenodo REST API and from the downloaded file,
not from memory.

## 1. The deposit, verified

```
record            23068563
version DOI       10.5281/zenodo.23068563
concept DOI       10.5281/zenodo.23045140
title             Beyond Sturmian Words in the 3x+1 Periodicity Conjecture:
                  A Periodic-Approximation and Arithmetic-Height Bridge
creator           De Jesus, Elias
publication date  2026-09-30      created 2026-09-30T19:04:05Z
license           CC BY 4.0       access: open      version field: (unset)
file              Beyond_Sturmian_Words_Revision_3_DRAFT.pdf
                  471 520 bytes   md5:4e37bf96f28414bc51eb6f90e6b87e9e
```

| file | md5 | verdict |
|---|---|---|
| deposited `…Revision_3_DRAFT.pdf` | `4e37bf96f28414bc51eb6f90e6b87e9e` | — |
| local `technical-note/note_rev3.pdf` | `4e37bf96f28414bc51eb6f90e6b87e9e` | **byte-identical** |

> **The deposited Revision 3 is exactly the local file.** SHA-256 `a2c09351…02d2c939`, 34 pages.
> Source: `technical-note/note_rev3.tex`.

## 2. All four versions of the concept record

| record | DOI | date | file | bytes | md5 | is |
|---|---|---|---|---|---|---|
| 23045141 | `…23045141` | 2026-09-29 | `Beyond_Sturmian_Words_in_the_3x1_Periodicity_Conjecture.pdf` | 321 997 | `9b80c77c…` | **Revision 1** = local `note.pdf` |
| 23061396 | `…23061396` | 2026-09-30 | `Beyond_Sturmian_Words_Revision_2.pdf` | 374 773 | `b61d76f6…` | **Revision 2** = local `note_rev2.pdf` |
| 23068326 | `…23068326` | 2026-09-30 | `Beyond_Sturmian_Words_Latest_Built.pdf` | 374 773 | `b61d76f6…` | **Revision 2 again — a byte duplicate** |
| 23068563 | `…23068563` | 2026-09-30 | `Beyond_Sturmian_Words_Revision_3_DRAFT.pdf` | 471 520 | `4e37bf96…` | **Revision 3** = local `note_rev3.pdf` |

Every local PDF matches its deposit exactly. Two findings follow.

- **R1. Record 23068326 is a duplicate of Revision 2 under a misleading filename.** It carries the
  same bytes as 23061396, deposited from the file this repository produced for reading convenience
  and named `Beyond_Sturmian_Words_Latest_Built.pdf`. A reader who resolves that DOI gets Revision 2
  while the filename suggests the newest build. This is the DOI an earlier draft of the Phase 14
  brief mistook for Revision 3.
- **R2. The Revision 2 erratum was never deposited.** `technical-note/correction_notice.pdf`
  (md5 `afd30d3b…`) accompanies Revision 2 locally and appears on no version of the record.

## 3. What the deposited Revision 3 contains — checked against the downloaded file

| item | present? | evidence in the deposited text |
|---|---|---|
| quadratic-rotation theorem, rational intercept | **yes** | Theorem 17.5, 11 occurrences |
| **algebraic-offset theorem** | **yes** | Theorem 18.2 (5×) and Corollary 18.3 (5×) — the interval `[u,u+β)` whenever `ρ−u` is algebraic |
| repaired Baker argument | **yes** | §19, Theorem 19.1 (Baker III Thm 2), Lemma 19.2 hypotheses verified, Remark "no polynomial bound is available, and none is used" |
| acknowledgement of prior work | **yes** | §1 D3, §16, and the Acknowledgments |
| Thue–Morse scope correction | **yes** | §1 D1, and Open 6 rewritten |
| CS Rote novelty correction | **yes** | §1 D2 and §16 |
| foundation cited by public DOI, as a self-citation | **yes** | §1 D4; `10.5281/zenodo.23019799` ×2; "self-citation" ×3 |
| theorem-numbering clarification | **yes** | §1 D5 with the mapping table |
| polynomial-bound withdrawal | **yes** | §1 D6 |
| "has not been refereed" | **yes** | Acknowledgments |
| Ridout observation, labelled open | **yes** | §21 |

**Every correction outstanding at the start of Phase 13 is already in the deposited file. None is to
be redone.**

## 4. Corrections still owed — four, all new since the deposit

| | what | where | severity |
|---|---|---|---|
| **C1** | **The record description is Revision 1's.** The landing page still says the main result is for "intercept-zero complementary symmetric Rote representatives … for every irrational slope having bounded continued-fraction partial quotients". That was superseded by Revision 2 (every intercept) and is now two revisions stale: it does not mention the critical-density theorems, the algebraic offset, or any of D1–D6. The file is right; the page describing it is wrong. | Zenodo metadata | **high** — it is what a reader sees first |
| **C2** | **The deposited PDF says it has not been deposited.** §"Provenance and Verification" reads "At the time of writing Revision 3 is a draft and has not been deposited." It has been. | `note_rev3.tex`, provenance | medium |
| **C3** | **The published filename contains `DRAFT`.** `Beyond_Sturmian_Words_Revision_3_DRAFT.pdf` is the citable artifact. | Zenodo file | medium |
| **C4** | **"Open 4 — Unbounded partial quotients. THE LIVE FRONTIER."** conflates two different things. See §5. | `note_rev3.tex` §26 | **high** — it is a substantive framing error |

None of C1–C4 is an error in a proof.

## 5. C4 in detail: an unfinished bridge is not an uncovered conclusion

Revision 3 retains Open 4 from Revision 2 and labels it **the live frontier**. Two statements must be
separated, and the note currently runs them together.

- **The independent Rote bridge is unfinished there.** For a slope carrying an intercept with
  `ice(ω) = 2` exactly — and BHZ Theorem 1.1 characterises those, all with unbounded partial
  quotients — the odd-weight branch has margin exactly `0`, so this repository's own sufficient
  criterion does not apply. That is true, and it is a real limitation of the method.
- **The irrationality conclusion there is not uncovered.** Every complementary symmetric Rote
  sequence has ones-density exactly `1/2`, and that is a structural fact about the doubled root,
  **independent of the slope's partial quotients**. Since `1/2 < β`, Monks–Yazinski (2004) Theorem
  2.7(b) already gives `Φ(v) ∉ ℚ` for every CS Rote sequence over every irrational slope, bounded
  type or not.

So Open 4 asks for a **second proof of an available conclusion by a method that currently cannot
reach it** — a methodological question, not an open irrationality question. Calling it "the live
frontier" is exactly the framing error that D2 corrects one page earlier for the bounded-type case;
D2 was applied to Theorem 17.5's ancestors and not propagated to Open 4. The live frontier, on the
coverage map the note itself builds in §16, is lower ones-density `≥ β` — which is where
Theorems 17.5 and 18.2 sit.

Proposed replacement text is in §6.

## 6. Proposed patch, not applied

**(a) Zenodo description.** Replace with a description of the file actually deposited:

> This technical note develops a periodic-approximation and arithmetic-height approach to structured
> sectors of the 3x+1 Periodicity Conjecture. The central mechanism compares the 2-adic depth with
> which an aperiodic binary word agrees with periodic approximants against the archimedean height of
> their rational images under the Bernstein–Lagarias conjugacy map; if the resulting surplus is
> unbounded, rationality is impossible.
>
> Revision 3 adds two theorems at the critical density β = ln2/ln3. For every quadratic irrational
> slope α ∈ (0,1) and every rational intercept, and then for every real algebraic intercept, the
> coding s_n = 1 ⟺ {nα+ρ} ∈ [0,β) has irrational conjugacy value; more generally the interval may be
> [u, u+β) whenever the offset ρ−u is algebraic, with ρ and u themselves unrestricted. These words are
> aperiodic, have factor complexity 2n, and have lower ones-density exactly β.
>
> Revision 3 also rebuilds the coverage map on lower ones-density rather than factor complexity, and
> corrects the framing of the earlier complementary-symmetric-Rote results accordingly: their
> conclusion was already available from Monks–Yazinski (2004), since those words have density 1/2,
> and what this programme contributes there is an independent second proof together with effective
> height bounds. A claimed polynomial bound on a linear form in logarithms is withdrawn and replaced
> by the correct algebraic-coefficient estimate, and an incorrect claim that the Thue–Morse word
> obstructs every repetition-based method is withdrawn.
>
>
> Nothing here proves the Collatz conjecture or the 3x+1 Periodicity Conjecture in general, and no
> novelty claim is asserted as established. The note has not been refereed.

**(b) Provenance sentence (C2).** Replace "At the time of writing Revision 3 is a draft and has not
been deposited." with:

> Revision 3 is deposited as Zenodo version DOI `10.5281/zenodo.23068563` (concept DOI
> `10.5281/zenodo.23045140`), a new version of the record leaving Revisions 1 and 2 retrievable.

**(c) Open 4 (C4).** Replace the label and opening of Open 4 with:

> **Open 4 — Unbounded partial quotients.** *(An unfinished proof, not an open conclusion.)* Remove
> the bounded-partial-quotient hypothesis from Theorem \ref{thm:boundedtype}. Two things must be kept
> apart here. The *conclusion* is not open: every complementary symmetric Rote sequence has
> ones-density exactly `1/2` whatever the slope's partial quotients, so Corollary \ref{cor:my} already
> gives `Φ(v) ∉ ℚ` for all of them. What is open is whether *this* method reaches them, and there the
> obstruction is sharp: BHZ Theorem 1.1 characterises the slopes carrying an intercept with
> `ice(ω) = 2` exactly, all of unbounded partial quotients, and at such an intercept the odd-weight
> branch has margin exactly `0`. So Open 4 asks for an independent second proof of an available
> conclusion, by a mechanism that presently cannot supply one. [remainder of the item unchanged]

**(d) Filename (C3).** If a further version is deposited, name the file `Beyond_Sturmian_Words_Revision_4.pdf`
or similar, without `DRAFT`. The deposited Revision 3 file cannot be renamed in place.

**(e) Duplicate record (R1).** Zenodo versions cannot be withdrawn by an author. The practical
remedies are to leave 23068326 alone and never cite it, and to state in the next version's
description that record 23068326 duplicates Revision 2. **A decision for the author; nothing done.**

**(f) Erratum (R2).** Decide whether `correction_notice.pdf` should be attached to a future version.

## 7. Citation form to use from here

> De Jesús, Elias. *Beyond Sturmian Words in the 3x+1 Periodicity Conjecture: A
> Periodic-Approximation and Arithmetic-Height Bridge*. Zenodo, 30 September 2026. Revision 3,
> version DOI **10.5281/zenodo.23068563**; concept DOI **10.5281/zenodo.23045140**. CC BY 4.0.
> Preprint, not refereed.

Do **not** cite `10.5281/zenodo.23068326` (duplicate of Revision 2) or `…23061396` (Revision 2) when
Revision 3 is meant.
