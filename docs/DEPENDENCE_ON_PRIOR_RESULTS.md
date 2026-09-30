# What this repository's conclusions depend on

A short, current-facing statement of which external results the conclusions rest on, and which they do
not. This is the canonical wording; where an older phase file uses sharper language, the phase file is
retained as the audit record and carries a pointer here.

## Relied on

| result | role | status of the source |
|---|---|---|
| Bernstein & Lagarias, *The 3x+1 conjugacy map*, Canad. J. Math. **48** (1996) 1154–1169 | `Φ` is a 2-adic isometry conjugating the shift to `T` | refereed |
| Baker, *Linear forms in the logarithms of algebraic numbers* I, Mathematika **13** (1966) 204–216; III, Mathematika **14** (1967) 220–228 | lower bound for the linear form at the `β`-boundary | refereed |
| Waldschmidt, explicit algebraic-coefficient measure (*Diophantine Approximation on Linear Algebraic Groups*, Grundlehren **326**, Springer 2000, and the companion survey) | the same bound with a numerical constant | refereed |
| Kuipers & Niederreiter, *Uniform Distribution of Sequences*, Ch. 2 Thm 3.4 | discrepancy of a bounded-type rotation | refereed |
| Rote, J. Number Theory **46** (1994) 196–213; Berstel & Vuillon, *Coding rotations on intervals* | factor complexity `2n` of a two-interval coding | refereed / arXiv |
| Gelfond–Schneider; Liouville's inequality; Lagrange and Perron on quadratic continued fractions | transcendence of `log₃2`; the boundary separations | classical |
| Monks & Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Math. **275** (2004) 219–236, Thm 2.7(b) | used to describe which densities are **already covered** by existing work — not used to prove anything here | refereed |
| De Jesús, *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic Integer*, doi:10.5281/zenodo.23019799 | the conjugacy-map propositions, the counting transport, and the hitting-time mechanism proposed in its §12 problem (1) | **preprint, not refereed; by the present author — a self-citation** |

## Acknowledged influence

**López & Stoll**, *The 3x+1 conjugacy map over a Sturmian word*, **Integers 9 (2009), A13, 141–162**
[refereed], and *The 3x+1 periodicity conjecture in ℝ*, **arXiv:2101.12747 (2021)** [preprint].

> López–Stoll's work on density and the 3x+1 conjugacy map helped guide this programme toward the
> critical density `β = ln2/ln3`. We acknowledge that influence. The results presented here are
> established through the independent arguments given in this repository and do not require their
> proposed upper-density exclusion.

Concretely, and with the credit made specific rather than general:

- The **critical-density Sturmian word `1c_β`** is theirs — the foundation reference names it "the
  critical-density Sturmian word of López and Stoll, the hardest case here", and takes its notation
  from their 2009 paper.
- The observation that **critical density is exactly where the existing methods stop** is theirs, and
  it is what makes `β` the right place to work. This programme's Phases 9B–13 arrived at the same
  point from the complexity side and then had to move to density exactly `β` to find anything
  uncovered; that the interesting boundary was at `β` was already known from their work.
- The deduction of irrationality for slopes `γ < β` from Monks–Yazinski is, per the foundation
  reference, "made explicitly by López and Stoll".

So the debt is to their **refereed 2009 paper** as much as to the 2021 preprint, and it is a debt of
**direction**, not of premise: no step of any theorem here invokes either paper.

## Not relied on as a premise

**López & Stoll, *The 3x+1 periodicity conjecture in ℝ*, arXiv:2101.12747 (2021), Theorem 1** — the
proposed upper-density exclusion.

Two clarifications, so that this is not read as more than it says:

- We have **neither established nor disproved** their theorem, and we take no position on it. It is
  cited where it is relevant to the literature landscape, and it is not used as a premise anywhere.
- Because it is not used, the coverage statements in this repository are phrased against what is
  independently available. Concretely: the densities already covered by refereed work are those with
  lower ones-density below `β = ln2/ln3` (Monks–Yazinski 2004, Thm 2.7(b)). The classes treated here
  sit at lower ones-density exactly `β`, so they are outside that range whether or not the
  upper-density result holds. **No conclusion of this repository changes in either case.**

A technical observation about one step of that paper, raised by a third party, is recorded in the
audit files with its source reference and its verification status — see
`theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md` §1 and
`theorems/phase12/CRITICAL_ROTATION_PRIOR_RESULTS.md` §3. That observation has **not** been verified
by us, is not a result of this repository, and is retained as part of the audit record rather than as
a claim.

## Standard applied to preprints, including my own

Some inputs above are unrefereed preprints, and one of them is mine. The same caution applies to all
of them: a preprint is labelled as such at every use, and a self-citation is additionally labelled as
a self-citation. No preprint — mine included — is treated as settled.

## Where the detailed record lives

- `theorems/phase13/CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md` — the full chain, sorted by provenance.
- `theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md` — every located result, with the exact
  hypothesis that makes it apply or not apply.
- `PRIOR_ART.md` — index into the earlier prior-art passes.
- `docs/INVITATION_TO_DOMAIN_EXPERTS.md` — where specialist review would help most.
