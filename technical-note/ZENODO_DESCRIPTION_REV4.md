**PROPOSED — STILL NOT APPLIED.** Revision 4 was deposited on 2026-09-30 as
`10.5281/zenodo.23070093`, and the record's description carried over from Revision 1 unchanged. The
text below is the proposed replacement; no Zenodo field has been edited from this repository.

# Proposed Zenodo description for Revision 4

## Why a new description is needed

The record's current description is **Revision 1's**. It still advertises the main result as being for
"intercept-zero complementary symmetric Rote representatives … for every irrational slope having
bounded continued-fraction partial quotients" — superseded by Revision 2 (every intercept) and two
revisions stale by now. It mentions none of the critical-density work, none of the corrections, and
none of the attribution language. **The deposited file is right; the page describing it is wrong.**

## Metadata to set alongside it

| field | value |
|---|---|
| title | unchanged |
| version | `Revision 4` (earlier versions left the field unset; setting it from here on is worthwhile) |
| publication date | date of deposit |
| license | CC BY 4.0 (unchanged) |
| file | `note_rev4.pdf` — **no `DRAFT` in the filename** |
| additional file | `correction_notice_rev4.pdf` |
| related identifier | "is new version of" `10.5281/zenodo.23068563` (Revision 3) |
| keywords | 3x+1 problem, Collatz, Periodicity Conjecture, Bernstein–Lagarias conjugacy map, 2-adic, Sturmian words, Rote sequences, rotation codings, linear forms in logarithms, discrepancy |

## Proposed description text

> This technical note develops a periodic-approximation and arithmetic-height approach to structured
> sectors of the 3x+1 Periodicity Conjecture. The central mechanism compares the 2-adic depth to which
> an aperiodic binary word agrees with periodic approximants against the archimedean height of their
> rational images under the Bernstein–Lagarias conjugacy map Φ. If the resulting approximation surplus
> is unbounded, rationality is impossible.
>
> **Main results (critical density).** Let β = ln2/ln3 and let α ∈ (0,1) be a quadratic irrational. For
> every rational intercept ρ, and then for every real algebraic ρ, the two-interval rotation coding
> s_n = 1 ⟺ {nα+ρ} ∈ [0,β) satisfies Φ(s) ∉ ℚ. More generally the interval may be [u, u+β) modulo 1
> whenever the offset ρ−u is algebraic, with ρ and u themselves unrestricted — so both may be
> transcendental; what the theorem constrains is the offset between the intercept and the interval's
> left endpoint, not the intercept. These words are aperiodic, have factor complexity exactly 2n, and
> have lower ones-density exactly the critical value β.
>
> **The independent arithmetic bridge, and quantitative bounds.** The argument is elementary in its
> ingredients: a 2-adic isometry, an explicit height for periodic values, a discrepancy estimate, and
> two lower bounds at the partition endpoints — Liouville's inequality at 0, and a logarithmic-form
> estimate with algebraic coefficients at β. Beyond the qualitative conclusion it yields explicit lower
> bounds on the height of any rational that could equal a given conjugacy value: exact integer
> certificates up to H ≥ 2^15998 for one named word (a 4816-digit bound, from integer comparisons
> alone, with no analytic input), and a written-down function f(M) with H ≥ 2^{f(M)} for every integer
> M ≥ 2. Revision 4 supplies the constants numerically for that named example — C = 24.207846,
> C₀ = 35.869175 in the surplus estimate — where earlier revisions said only "effective". The
> threshold beyond which f(M) is positive is about 1.8 × 10^18 and is not a computational claim; it does
> not compete with the exact certificates, which are the numerically useful statements.
>
> **Prior results, and what is not new.** The coverage map is rebuilt on lower ones-density rather than
> factor complexity, because that is the coordinate the existing exclusion results read.
> Monks–Yazinski (2004, Theorem 2.7(b)) excludes every aperiodic word of lower ones-density below β,
> whatever its complexity. Every complementary-symmetric-Rote result of earlier revisions sits at
> density exactly 1/2 < β, so its conclusion was already available; what this note contributes there is
> an independent second proof by a different mechanism together with effective height bounds, which a
> density argument does not supply. The same applies to the Thue–Morse word. Lower ones-density exactly
> β is the one place no density or counting criterion reaches, and that is where the new theorems sit.
> The mechanism itself — reading the agreement excess as a first entry time of a rotation orbit into an
> arc at a partition endpoint — is proposed in the author's own earlier preprint and is not original
> here.
>
>
> **Attribution.** Every external result the conclusions rest on is listed in the manuscript, with
> its refereeing status; the mechanism itself is proposed in the author's own earlier preprint and is not
> original here.
>
> **Novelty and refereeing.** Novelty of the critical-density results is **formally unresolved**.
> Several literature passes located no result covering lower ones-density exactly β at factor
> complexity 2n, and for each candidate result the note records why it does or does not apply; but
> absence of a hit in a literature search is evidence, not proof, of absence. **Neither this note nor
> the foundation paper it builds on (10.5281/zenodo.23019799, by the same author) has been refereed.**
> Specialist review by number theorists and by experts in symbolic dynamics, combinatorics on words,
> Diophantine approximation and p-adic dynamics is actively invited; the repository contains a review
> guide naming the four checks most likely to repay attention.
>
> **Scope.** This note does not prove the Collatz conjecture, and does not prove the 3x+1 Periodicity
> Conjecture, which quantifies over all aperiodic parity vectors — an uncountable family of which the
> classes treated here form a two-parameter set of measure zero. Nothing here bears on divergent orbits
> of positive integers.
>
> **Revision 4** corrects Revision 3 (10.5281/zenodo.23068563) in four places without altering any
> mathematical statement: it records that Revision 3 is deposited, removes "draft" labelling, corrects
> the framing of one open problem (general complementary-symmetric-Rote irrationality is already
> covered by Monks–Yazinski; what is unfinished there is this note's own independent bridge, not the
> irrationality conclusion), and adds the explicit constants described above. A standalone correction
> notice accompanies it, and the full revision history is in an appendix. Note for readers of the
> version history: record 10.5281/zenodo.23068326 contains the same file as Revision 2 byte for byte,
> deposited under a filename suggesting a later build; Revision 2 should be cited as
> 10.5281/zenodo.23061396.

## Note on the duplicate record

`10.5281/zenodo.23068326` carries the identical file to Revision 2 (`10.5281/zenodo.23061396`),
md5 `b61d76f6a3a0d23ec6d148f1aeea658b`, under the filename `Beyond_Sturmian_Words_Latest_Built.pdf`.

It is recorded factually in the description above and in the manuscript's provenance table so that a
reader who arrives at it knows what it holds. **Nothing is proposed to be deleted, withdrawn, or
altered**: it is part of the record's history, Zenodo versions are permanent by design, and rewriting
history would be worse than documenting it. The only action is accurate citation guidance.
