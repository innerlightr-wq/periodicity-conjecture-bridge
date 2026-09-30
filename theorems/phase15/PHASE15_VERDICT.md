**REVISION 4 IS BUILT AND READY FOR YOUR REVIEW — NOTHING DEPOSITED**

# PHASE15_VERDICT.md

Branch `phase15-corrected-release`, cut from `phase14-release-reconciliation` at **`2c298f5`** as
expected; ancestry verified (`2c298f5`, `5d04064`, `ec035dd`, `46b0d0a` all ancestors), tree clean.
Nothing pushed, nothing deposited, no Zenodo field edited, no invitation sent, and **every deposited
PDF byte-identical** (`RELEASE_MANIFEST.md` §2).

## 1. Release record reconciled

Phase 14's reconciliation confirmed: the deposited Revision 3 (`10.5281/zenodo.23068563`) already
contains the critical-density theorems, the repaired Baker argument and the acknowledgement of
prior work. **None of those was redone.** Four corrections had arisen *since* the deposit, and
all four are now discharged in the prepared release:

| | correction | how |
|---|---|---|
| E1 | Revision 3 said it "has not been deposited" | replaced by the full deposit table, §"Provenance" |
| E2 | `DRAFT` in the filename | issued as `note_rev4.pdf`; nothing labelled a draft |
| E3 | Open 4 framed as "THE LIVE FRONTIER" | rewritten; see §3 |
| E4 | constants effective but not numerical | new §19, `S ≥ (L−ℓ) − 24.207846 log₂ℓ − 35.869175` and `H ≥ 2^{f(M)}` |

The proposed record text is `technical-note/ZENODO_DESCRIPTION_REV4.md`: the current description is
**Revision 1's** and advertises a result superseded two revisions ago.

**The duplicate deposit is documented, not altered.** `10.5281/zenodo.23068326` carries Revision 2's
file byte for byte under a filename suggesting a later build. It appears factually in the manuscript's
provenance table, in the correction notice, and in the proposed description, each with the guidance
"cite Revision 2 as `10.5281/zenodo.23061396`". **No deletion or withdrawal is proposed** — Zenodo
versions are permanent by design and documenting the history is better than rewriting it.

## 2. One coherent manuscript, not an audit diary

`technical-note/note_rev4.{tex,pdf}`, **39 pages**, numbered Revision 4 to match the actual release
history (1, 2, the duplicate, 3, now 4).

The structural change worth naming: Revision 3 opened with **two long correction sections** before any
mathematics. Those are now **Appendix A, "Revision History"**, and §1 is a short four-item summary
carrying only what a reader needs up front — the acknowledgement, the self-citation notice, and the
theorem-numbering map. A standalone erratum (`correction_notice_rev4.pdf`, 2 pp) holds the
correction detail for anyone who wants it without the paper.

Consequence to be aware of: the appendix move shifted section numbers by one, so Revision 3's
**Theorem 17.5 / 18.2 / Corollary 18.3 are Revision 4's 16.5 / 17.2 / 17.3**. Internal references
updated automatically; `README.md`, `LADDER.md`, `THEOREM_STATUS.md` and `REVIEW_GUIDE.md` updated by
hand and checked.

The two scales are kept explicitly apart in Remark 19.6: `f(M)` first says something at
`M ≈ 1.8·10^18`, with a witness of length about `2^{7.4·10^16}` — never exhibitable, and its value is
that it is *written down*; the exact certificates up to `H ≥ 2^15998` come from integer comparisons at
lengths `≤ 6765` and are the only numerically useful statements. "Neither improves the other."

## 3. E3, the one substantive correction

Complementary symmetric Rote sequences have ones-density exactly `1/2` **whatever** the slope's partial
quotients — the density-`1/2` fact concerns the doubled root and is independent of the continued
fraction. Since `1/2 < β`, Monks–Yazinski (2004) Thm 2.7(b) already gives `Φ(v) ∉ ℚ` for every CS Rote
sequence over **every** irrational slope. So Open 4 asks for **an independent second proof of an
available conclusion**, by a mechanism whose odd-weight branch has margin exactly `0` at an
`ice(ω) = 2` intercept — not for a new exclusion. It remains worth answering, because that mechanism
is what supplies effective height bounds, but it is not a frontier of knowledge about irrationality.
Revision 2's judgement that Open 4(i) was "the single highest-value target" is downgraded in the
roadmap, and the higher-value item is now completing the explicit constants.

## 4. Review package

`REVIEW_GUIDE.md` (228 lines): the exact theorem with its three assumptions and what is *not* assumed;
an eleven-row dependency table with each source's refereeing status; the four priority checks (a)
Waldschmidt hypotheses and the Weil-versus-classical height conversion, (b) discrepancy, interval
wrapping and index conventions, (c) Liouville separation and exact boundary hits, (d) coverage by prior
results — each with precise file and manuscript-section references and the specific sub-questions I
most doubt; a table of **what would invalidate or narrow the theorem**, distinguishing failures that
kill it from failures that only move constants; reproduction instructions; and the statement that
computations are supporting verification of finitely many instances and **do not replace the
arguments**. The invitation and the background paragraph are retained, with the limits stated plainly.

## 5. Verification

39 pages; `pdflatex` × 3; **no undefined references, no undefined citations, no multiply-defined
labels, no overfull or underfull boxes**; 0 dangling `\ref`, 0 missing `\cite`, 0 unused `\bibitem`.
All 39 pages inspected: heads land where intended, exactly one theorem-mapping table (the duplicate
created by the appendix move was removed). All five relevant scripts re-run, all exit 0. Cross-document
agreement checked on `C`, `C₀`, `M₀`, `c₁`, `2^15998` and all five DOIs across seven documents plus the
manuscript: **no contradictory value**. No new check was needed — §19 states exactly what
`scripts/phase14/explicit_constants.py` already verifies.

## 6. Still requiring your review

1. **Deposit decision.** Revision 4 is built and not deposited. §6 of `ZENODO_DESCRIPTION_REV4.md`
   lists the metadata to set, including a "is new version of" relation and, for the first time, a
   populated `version` field.
2. **Whether to attach the Revision 2 erratum.** `correction_notice.pdf` (md5 `afd30d3b…`) exists
   locally and appears on no version of the record. Attaching it to Revision 4 would complete the
   history; leaving it out is also defensible.
3. **The acknowledgement and the Acknowledgments section name that preprint directly.** Read those
   paragraphs — they concern real people and should sound like you.
4. **E3's tone.** It says, in the paper, that a judgement of Revision 2's was wrong. I believe that is
   correct and worth stating; how prominently is your call.
5. **The background paragraph in `REVIEW_GUIDE.md` §6** describes your professional experience. Check
   that it is accurate and that you are comfortable with it in a document aimed at specialists.

## 7. Not done, deliberately

No push, no deposit, no Zenodo edit, no contact with anyone. No deposited PDF modified or renamed. No
mathematical statement of Revision 3 altered or withdrawn. No new generalization attempted.
