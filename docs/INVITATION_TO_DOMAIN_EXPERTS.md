# An invitation to number theorists and domain experts

*Elias De Jesús — independent researcher*

## Who I am, and why that matters for reading this

I work on this as an independent researcher. My professional experience is outside mathematics: in
electronics technology, in computer systems, and in an immunogenetics laboratory. I have not trained
as a number theorist, and I do not present myself as one.

That background does shape what I bring. In each of those fields the useful habits are much the same:
look closely at how a system actually behaves rather than how it is supposed to behave; find the
interfaces where two components meet and check that each side means the same thing by the values it
passes; treat an assumption as unverified until something independent confirms it; and build a test
that would fail loudly if the thing you believe is wrong. A laboratory teaches you to distrust a
result you cannot reproduce, and to write the procedure down so that someone else can run it.

Applied here, that has meant: re-deriving each step from its definitions rather than inheriting it;
separating what is proved from what is merely computed; doing every pass/fail comparison in exact
integer or exact algebraic arithmetic, so that no floating-point value ever decides a result; and
recording the verification procedure alongside the claim, in scripts anyone can run.

**I want to be plain about the limits of this.** Careful engineering of a verification is not the same
thing as mathematical expertise, and it cannot substitute for it. Checking that an argument is
internally consistent, and that its computations are correct, does not establish that the argument is
valid, that its citations support what they are asked to support, or that the result is new. Those are
judgements for specialists, and **they have not yet been made here.** Nothing in this repository has
been refereed. My perspective is meant to complement mathematical expertise, not to stand in for it.

## What the work actually is

The repository studies the Bernstein–Lagarias conjugacy map `Φ`, which sends a binary parity word to
the 2-adic integer whose `3x+1` trajectory has that word as its parity itinerary. The Periodicity
Conjecture is equivalent to saying that `Φ` sends every word that is *not* eventually periodic to an
irrational 2-adic integer. The programme tries to establish that for particular, precisely specified
classes of words.

The method is elementary in its ingredients:

- **Periodic approximation.** A finite word `W` gives a periodic word `W^∞` whose `Φ`-value is the
  rational `c_W/(2^{|W|} − 3^{|W|_1})`. If the target word agrees with `W^∞` for a long prefix, then
  `Φ` of the target is 2-adically very close to that rational.
- **A height comparison.** If `Φ(s)` were rational with height `H`, the 2-adic closeness forces
  `2^{L} ≤ H·F(W)` where `L` is the agreement length and `F(W)` a simple height of the approximant.
  Finding approximants where `L` outruns `log₂F(W)` by an unbounded margin therefore excludes
  rationality.
- **Exact arithmetic comparisons.** Every decision in the verification scripts is an exact integer or
  exact algebraic-number comparison. Where a transcendental constant such as `log₃2` must be compared
  against, a certified high-precision bracket is used and the comparison either decides or raises.
- **Computational verification.** The scripts re-run the full chain and report every check; they are
  written to be run independently of one another.
- **Quantitative height bounds.** Beyond the qualitative conclusion, the same inequality yields
  explicit lower bounds on the height of any rational that could equal a given conjugacy value — for
  example `H ≥ 2^{15998}` for one named word, a 4 816-digit bound, obtained by exact integer
  comparison with no analytic input.

**The reported results concern the specified symbolic classes only.** They are not a proof of the
Collatz conjecture, and not a proof of the full `3x+1` Periodicity Conjecture, which quantifies over
all aperiodic parity words — an uncountable family of which the classes treated here form a set of
measure zero. Nothing here bears on divergent orbits of positive integers.

## What is proved, what is checked, and what is open

I try to keep four categories apart throughout, and I would rather be corrected on the classification
than be read as claiming more than I have:

- **Proved arguments.** The chains written out in `theorems/phase*/`, resting on cited published
  results. These are mathematical claims and are open to mathematical objection.
- **Certified finite checks.** Exact computations at specific parameters — for instance the five
  explicit height floors for the named word. These are facts about particular integers. They do not
  by themselves establish any asymptotic statement.
- **Conjectures and open questions.** Recorded as such, with the smallest missing ingredient named
  where I can identify it.
- **Unresolved novelty.** Repeatedly and deliberately left unresolved. Several literature passes have
  not located a result covering the classes treated here, and I have tried to record for each
  candidate result *why* it does or does not apply rather than reporting an empty search. **A
  negative search is evidence, not proof, of absence.** No novelty claim in this repository should be
  read as established.

One consequence of that standard: some of the work builds on preprints of my own, which are not
refereed either. **I apply the same caution to my own preprints as to anyone else's** — where a
foundation result of mine is used, it is labelled as a self-citation to an unrefereed preprint, and it
is as open to correction as any external citation.

## What I am asking for

I would be glad of the attention of number theorists, and of specialists in symbolic dynamics,
combinatorics on words, Diophantine approximation, and `p`-adic dynamics. Please examine any part of
this you find worth your time. I would rather learn that something is wrong, already known, or
achievable more simply, than have it stand unexamined. Corrections are as welcome as extensions, and
a demonstration that a result is already in the literature is a genuinely useful contribution that I
would record with thanks and full attribution.

You are also welcome to take any of this further on your own — to prove a stronger theorem, to find
the right general statement, or to replace an argument here with a better one. I ask only for
appropriate attribution, and note that the repository's existing licensing continues to apply: the
code and written analysis are under the Apache License 2.0 (see `LICENSE` and `NOTICE`), and material
under `reference/` retains its own separate copyright.

### Concrete targets, if you are looking for one

1. **The algebraic-coefficient logarithmic-form estimates, and their application.** The arc-at-`β`
   bound rests on a lower bound for `|A_m log 3 − log 2|` with `A_m` algebraic of bounded degree and
   polynomially bounded height. The citations used are Baker, *Linear forms in the logarithms of
   algebraic numbers* (I, Theorem 1.1; III, Theorem 2), and Waldschmidt's explicit
   algebraic-coefficient measure. I would welcome scrutiny of whether the hypotheses are met exactly
   as stated, whether a sharper or cleaner estimate applies, and whether my reading of the height and
   degree conventions is right. An earlier phase of this work cited a polynomial bound that the
   sources do not support; that was withdrawn, and I would not be surprised if more of this kind
   remains.
2. **The rotation hitting-time and endpoint arguments.** The agreement length is identified with the
   first entry time of a rotation orbit into one of two arcs at the partition endpoints. The
   half-open endpoint conventions matter, an unstated non-wrapping hypothesis was found and added
   late, and the treatment of orbits that hit a boundary exactly is delicate. This is the part I would
   most like a combinatorics-on-words specialist to read.
3. **Explicit discrepancy constants and height bounds.** The height inequality carries constants
   coming from a classical discrepancy estimate (Kuipers–Niederreiter) that I have not evaluated
   numerically. Making them explicit is bookkeeping rather than new mathematics, and it is the last
   step to a fully numerical bound at every parameter.
4. **Prior-result coverage and attribution.** The coverage map turns on lower ones-density relative to
   `β = ln2/ln3` and on factor complexity relative to a counting threshold. I would value a check of
   whether the results I cite are stated with the hypotheses I ascribe to them, and of whether
   something I have not found already covers the same ground. Attribution corrections are welcome
   without qualification.

   One acknowledgement belongs here rather than in a footnote. **López–Stoll's work on density and the
   3x+1 conjugacy map helped guide this programme toward the critical density `β = ln2/ln3`. I
   acknowledge that influence.** The critical-density Sturmian word is theirs, and so is the
   observation that critical density is where the existing methods stop — which is why `β` turned out
   to be the place worth working. The results presented here are established through the independent
   arguments given in this repository and do not require their proposed upper-density exclusion; I
   take no position on that proposal in either direction. See
   [`DEPENDENCE_ON_PRIOR_RESULTS.md`](DEPENDENCE_ON_PRIOR_RESULTS.md).
5. **Extensions beyond algebraic offsets.** The current statement covers codings where the offset
   between the intercept and the interval endpoint is algebraic. When that offset is transcendental
   both of the boundary bounds fail, and I do not see a route. Whether that is a real barrier or a
   gap in my imagination is a good question for someone who knows the area.
6. **Possible transcendence results — clearly open.** A measurement, not a theorem: at some of the
   approximants the 2-adic approximation exponent exceeds the threshold in Ridout's `p`-adic analogue
   of Roth's theorem. If that happened along an infinite subsequence with a fixed margin, the
   conclusion would strengthen from irrationality to transcendence. **I have no proof that it does,
   and I am not claiming one.** The underlying question is whether a certain hitting time exceeds a
   fixed multiple of the period infinitely often.

## How to reach the work

Issues and pull requests on this repository are welcome and are the best channel for corrections,
questions, and proposed changes. Citation metadata, including my ORCID, is in `CITATION.cff`.

Useful entry points:

- `README.md` — orientation and repository layout.
- `THEOREM_STATUS.md` — the consolidated status map.
- `docs/DEPENDENCE_ON_PRIOR_RESULTS.md` — exactly which external results the conclusions rest on.
- `theorems/phase13/CONSOLIDATED_THEOREM_AND_DEPENDENCIES.md` — the full dependency chain, sorted by
  provenance, with the separations described above made explicit.
- `scripts/` — the verification scripts. Standard library only; every pass/fail decision exact.

Thank you for reading this far. If you find an error, I would genuinely like to know.
