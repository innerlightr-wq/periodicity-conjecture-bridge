# What this repository's conclusions depend on

A plain statement of the external results the conclusions rest on, and their refereeing status.
Discussion of results that are *not* used as premises belongs in the manuscript, not here.

## Relied on

| result | role | status of the source |
|---|---|---|
| Bernstein & Lagarias, *The 3x+1 conjugacy map*, Canad. J. Math. **48** (1996) 1154–1169 | `Φ` is a 2-adic isometry conjugating the shift to `T` | refereed |
| Baker, *Linear forms in the logarithms of algebraic numbers* I, Mathematika **13** (1966) 204–216; III, Mathematika **14** (1967) 220–228 | lower bound for the linear form at the `β`-boundary | refereed |
| Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*, Grundlehren **326**, Springer 2000, Thm 10.1 (and the companion survey) | the same bound with a numerical constant | refereed |
| Kuipers & Niederreiter, *Uniform Distribution of Sequences*, Ch. 2 Thm 3.4 | discrepancy of a bounded-type rotation | refereed |
| Rote, J. Number Theory **46** (1994) 196–213; Berstel & Vuillon, *Coding rotations on intervals* | factor complexity `2n` of a two-interval coding | refereed / arXiv |
| Gelfond–Schneider; Liouville's inequality; Lagrange and Perron on quadratic continued fractions | transcendence of `log₃2`; the boundary separations | classical |
| Monks & Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Math. **275** (2004) 219–236, Thm 2.7(b) | used to describe which densities are **already covered** by existing work — not used to prove anything here | refereed |
| De Jesús, *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic Integer*, doi:10.5281/zenodo.23019799 | the conjugacy-map propositions, the counting transport, and the hitting-time mechanism proposed in its §12 problem (1) | **preprint, not refereed; by the present author — a self-citation** |

## Standard applied to preprints, including the author's own

Two inputs above are unrefereed preprints and one of them is the author's. The same caution applies to
all of them: a preprint is labelled as such at every use, and a self-citation is additionally labelled
a self-citation. No preprint — the author's included — is treated as settled.

## Where the detailed record lives

- `theorems/phase13/CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md` — the full chain, sorted by provenance.
- `theorems/phase13/FAMILY_THEOREM_PRIOR_COVERAGE.md` — every located result, with the exact
  hypothesis that makes it apply or not apply.
- `REVIEW_GUIDE.md` — the compact dependency table used for specialist review.
- `PRIOR_ART.md` — index into the earlier prior-art passes.
