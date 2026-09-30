# FINAL_RELEASE_AUDIT.md

Final release audit of `technical-note/note.tex` / `note.pdf` before Zenodo deposition. Performed against `technical-note/SOURCE_OF_TRUTH.md`, the frozen Phase 1–7 files at commit `a4ac46aebf17fb2ce14cea50f5ce60a58704da15`, and the foundation paper's own PDF (`reference/sturmian-conjugacy-map-irrational-2adic-integer.pdf`). No Phase 1–7 file was read to be modified and none was modified. Corrections were applied only to `technical-note/note.tex`.

## 1–4. Claim/quantifier/scope audit

| CLAIM | SOURCE | NOTE LOCATION | STATUS | ACTION NEEDED |
|---|---|---|---|---|
| Title: "Beyond Sturmian Words... Periodic-Approximation and Arithmetic-Height Bridge" | Matches actual scope (extends foundation paper's Sturmian result via Route B) | Title page | EXACTLY SUPPORTED | None |
| Abstract: headline theorem (bounded partial quotients, intercept-0, either seed, any shift) | `theorems/phase6/BOUNDED_TYPE_THEOREM.md` | Abstract | EXACTLY SUPPORTED | None |
| Abstract: "does not prove... Periodicity Conjecture in general" | `theorems/phase1/FULL_PERIODICITY_GAP.md` (Q4, structural ceiling) | Abstract, last sentence | EXACTLY SUPPORTED | None |
| Abstract: exploratory probe "reported honestly as inconclusive, not as a result" | Session diagnostic work (Experiments 1–2) | Abstract | EXACTLY SUPPORTED | None |
| §1: Lagarias's Periodicity Conjecture, exact statement | Foundation paper PDF p.1, verbatim ("No aperiodic parity vector has a rational Φ-value", citing Lagarias 1985 §2) | §1 | EXACTLY SUPPORTED (verified directly against the PDF, not the secondary summary) | None |
| §1: "very little is known unconditionally in the converse direction" | Foundation paper PDF p.1 abstract, near-verbatim | §1 | EXACTLY SUPPORTED | None |
| §12: general-intercept extension explicitly open | `theorems/phase7/PHASE7_VERDICT.md` ("OBSTRUCTION CLASSIFIED — ONE LEMMA REMAINS") | §12, Conjecture 12.1 | EXACTLY SUPPORTED | None |
| §18 Open 4: general CS Rote (unbounded partial quotients) not claimed | `THEOREM_STATUS.md` open-problems list | §18 | EXACTLY SUPPORTED | None |
| No claim anywhere of $p(n)>2n$ results | Checked: no occurrence of a proved/claimed result beyond $p(n)=2n$ | whole document | EXACTLY SUPPORTED | None |
| §16: symmetry probe labeled INCONCLUSIVE | Session diagnostic work | §16 | EXACTLY SUPPORTED | None |
| §19 (orig.): "Editorial note" on prompt truncation, visible in public PDF | Internal provenance, not manuscript content | §19 (now removed) | **UNSUPPORTED PRESENCE** (correct information, wrong venue — belongs in internal docs, not a Zenodo manuscript) | **FIXED** — blockquote removed from `note.tex`; provenance retained only in this audit and the conversation record |

## 3. Strongest theorem — quantifier-by-quantifier check

| Quantifier in note | Quantifier in `theorems/phase6/BOUNDED_TYPE_THEOREM.md` | STATUS |
|---|---|---|
| "irrational with bounded partial quotients ($A:=\sup_n a_n<\infty$)" | identical | EXACTLY SUPPORTED |
| "intercept-$0$ lower mechanical word of $\gamma$" | identical | EXACTLY SUPPORTED |
| "either seed" | identical | EXACTLY SUPPORTED |
| "any shift $\sigma^j(v)$" | identical | EXACTLY SUPPORTED |
| conclusion "$\Phi(v)\notin\Q$" | identical | EXACTLY SUPPORTED |

Theorem 10.1 in the note is a **verbatim** reproduction of the frozen theorem statement (word for word, modulo LaTeX markup). The note says no more and no less than the audited theorem; the accompanying Remark (§10) explicitly forecloses over-reading "uncountable" as a density or measure claim.

## 5. Numerical constants

| Constant | Value used in note | Verified against | STATUS |
|---|---|---|---|
| $1/\log_2(3/2)$ | $1.709511\ldots$ / $1.70951129$ (both forms used, consistent truncations) | Foundation paper PDF abstract ("$p_s(L)>1.70951129L$"); `theorems/phase1/FULL_PERIODICITY_GAP.md` ("$1.70951\ldots$") | EXACTLY SUPPORTED |
| $\log_2 3$ | $1.58496\ldots$ | Standard; used consistently in margin $2-\log_2 3=0.41503\ldots$ | EXACTLY SUPPORTED |
| Sturmian complexity $p(n)=n+1$ | used throughout | `LADDER.md` | EXACTLY SUPPORTED |
| CS Rote complexity $p(n)=2n$ | used throughout | `LADDER.md`, `THEOREM_STATUS.md` | EXACTLY SUPPORTED |
| Experiment 1: $r\approx0.208$, $r\approx-0.125$, $n=74$ | §16 | Session diagnostic run | EXACTLY SUPPORTED |
| Experiment 2: $r\approx-0.0058$, log–log $r\approx-0.0319$, $n=724$ | §16 | Session diagnostic run | EXACTLY SUPPORTED |
| Transfer-matrix cross-check $150/150$ | §17 | Session diagnostic run | EXACTLY SUPPORTED |
| Clamping caveat $596/724$ ($82\%$) | §16 | Session diagnostic run ($596/724=82.32\%$) | EXACTLY SUPPORTED |

## 6–7. Bibliography and the two-independent-proofs claim

Every external bibliography entry was checked against the foundation paper's own References page (p.22 of the PDF), read directly, not reconstructed:

| Entry | STATUS | ACTION NEEDED |
|---|---|---|
| Bernstein & Lagarias 1996, *Canadian J. Math* 48(6), 1154–1169 | EXACTLY SUPPORTED | None |
| Bernstein 1994, *Proc. AMS* 121(2), 405–408 | EXACTLY SUPPORTED | None |
| Berthé–Holton–Zamboni 2006, *Acta Arithmetica* 122(4), 315–347 | EXACTLY SUPPORTED | None |
| Allouche–Davison–Queffélec–Zamboni 2001, *J. Number Theory* 91(1), 39–66 | EXACTLY SUPPORTED (this is "ADQZ 2001") | None |
| Dubickas 2009, *Glasgow Math. J.* 51(2), 243–252 | EXACTLY SUPPORTED | None |
| *Integers* **9** (2009), A13, 141–162 | EXACTLY SUPPORTED | None |
| arXiv:2101.12747 (2021), "The 3x+1 periodicity conjecture in ℝ" | Present in bibliography but **never cited in body text** | **FIXED** — added a citing sentence in §1 |
| Lothaire 2002, *Algebraic Combinatorics on Words*, Ch. 2 (Sturmian words) | **SUPPORTED BUT MISATTACHED** — this chapter is specifically about Sturmian words, not Rote sequences; it was cited directly in support of the CS-Rote complexity claim $p(n)=2n$, which it does not itself establish | **FIXED** — decoupled from the specific numeric claim; kept only as general background, with the existing sourcing caveat left in place |
| G. Rote (1994), primary CS-Rote source | Not independently held/verified in the repository record | Already correctly hedged in the bibliography note (no fabricated page numbers); no action needed beyond what was already there |

**Two-independent-proofs claim (item 7):** the original note wording ("using the critical-density Sturmian word... extended to every irrational slope and... to arbitrary intercept") compressed three distinct steps the PDF states separately: (a) the second proof is for **the specific case that preprint's own paper had identified as open**; (b) it is then generalized to every irrational slope; (c) a **further, separate argument** removes the intercept-0 restriction. Classified **SUPPORTED BUT WORDING TOO BROAD**. **FIXED** — §6 rewritten to state the three steps in the PDF's own order and attribution.

## 8. Section 19 / Future-Work Roadmap

The "Editorial note" disclosing that the roadmap section's source instructions were truncated is accurate but does not belong in a Zenodo manuscript. **Removed** from `note.tex`; the roadmap content itself (synthesized from §18's six open problems) is retained unchanged, now introduced by a single neutral sentence.

## 9. LaTeX / typesetting audit

| Check | Result |
|---|---|
| Undefined `\ref`/`\label` | Zero (three-pass compile clean) |
| Undefined `\cite` | Zero (cite-key vs. bibitem-key diff is empty both directions except one now-fixed uncited entry) |
| Overfull hboxes | One found at **268.2pt** (Route B implication chain, a single-line display equation wider than the text block — a real content-overflow risk) and one at **12.0pt** (General Intercepts $x'(k),y(k),\text{ice}(\omega)$ formula). **Both fixed** by reflowing to inline text / splitting into two display lines. One residual **6.2pt** overfull remains in a bibliography line (two long file-path tokens in one entry); visually confirmed non-disruptive (nothing is cut off or runs past the page edge) — left as a cosmetic, sub-visual-threshold imperfection. |
| Underfull hboxes | A handful, all `\sloppy`-induced loose-spacing warnings from dense provenance/bibliography paragraphs with long monospaced tokens; no visual defect. |
| Blank pages | None (16 pages, continuous content, TOC page count matches body) |
| Scratch paths / internal filenames in prose | None found (grepped for session/tmp/scratchpad paths, agent/fork/subagent language — zero hits) |
| Claude/tool/session language | Present only in the Acknowledgments section, **by design**, mirroring the foundation paper's own acknowledgment practice (verified against the PDF, which contains an equivalent AI-assistance disclosure). Not a defect. |
| TODO/FIXME markers | None |
| Page numbers | Correct, continuous, TOC entries match rendered page numbers |
| Bibliography completeness | Complete after fix; all 37 entries resolve, none orphaned |

## 10. Minimal edits applied to `note.tex`

1. Removed the internal "Editorial note" blockquote from §19 (public-manuscript hygiene).
2. Tightened §6's description of the foundation paper's second Sturmian proof to match the PDF's own attribution and step order.
3. Decoupled the `Lothaire2002` citation from the CS-Rote complexity claim it does not itself support (§7).
4. Fixed a missing math-mode space before a citation in §8 (cosmetic; also removed a redundant duplicate-citation artifact introduced while fixing it).
5. Removed an unsupported, vaguely-defined auxiliary clause ("$\varepsilon_k := E_k\cdot(\text{scale factor})$") from §13's flexible sufficient condition, keeping only the one verified inequality.
6. Added the missing citation to `arXiv:2101.12747` in §1.
7. Reflowed the Route B implication chain (§2.2) from an overflowing display equation into wrapping inline text.
8. Split the General Intercepts $x'(k),y(k),\text{ice}(\omega)$ display equation (§12) into two lines to fit the margin.
9. Added `\sloppy` document-wide and one targeted `\allowbreak` to resolve paragraph-packing overfull boxes caused by long monospaced repository file paths.

No Phase 1–7 file was modified. No claim's substance changed — every fix is either a citation-precision correction, a public/internal-content boundary correction, or a typesetting fix.

## 12–13. Recompilation and delivery

- Recompiled three times (`pdflatex -interaction=nonstopmode -halt-on-error`), clean exit each time.
- Pages: **16**
- File size: **321,997 bytes**
- SHA-256: **`b7054cee82cb847e11e003ad4f6a319e37c69c4873270ae56e93fed97fce008d`**
- Copied to `~/Downloads/Beyond_Sturmian_Words_in_the_3x1_Periodicity_Conjecture.pdf`
- Checksum of the Downloads copy: **identical** to the repository copy (verified by direct comparison, not assumed)

## 14. Confirmed not done

No commit. No push. No Zenodo upload. No DOI invented anywhere in the repository or this note.
