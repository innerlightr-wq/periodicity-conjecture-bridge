# INDEPENDENT_PROOF_REQUIREMENTS.md

Derived from: the source paper (`reference/`), `theorems/phase1/ABSTRACT_BRIDGE_THEOREM.md`, `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, and general knowledge of Sturmian/Rote combinatorics. **Phase 4's final proof was not consulted while writing this.**

## What the abstract criterion needs (fixed, from Phase 1/2, re-confirmed by reading, not assumed)

`\Phi(s)\notin\mathbb Q` follows from a sequence of witnesses `W_n` with `\text{lcp}(s,W_n^\infty)\to\infty` fast enough to beat `\log_2 F(W_n)` — concretely `\limsup_n[\text{lcp}(s,W_n^\infty)-\log_2(|2^{\ell_n}-3^{k_n}|+c_{W_n})]=+\infty`. Nothing here is CS-Rote-specific; any `s` and any witness family satisfying this works.

## What a genuinely independent attack on the quadratic CS-Rote claim would need

Working from scratch (not from Phase 2–4's specific machinery):

1. **A definition of complementary symmetric Rote sequence and its exact relationship to a Sturmian sequence** — needed before anything else, since without it there is no way to produce witnesses for `v` at all. (The Rote–Sturmian correspondence itself is external literature, not re-derivable from the abstract bridge alone.)
2. **A way to turn a Sturmian initial-power witness into a Rote initial-power witness** — some transfer mechanism, with an explicit relationship between the Sturmian witness's exponent/length and the Rote witness's exponent/length. Not obvious in advance that this exists at all, or that it is exact.
3. **A source of Sturmian initial-power witnesses with growing length and controlled exponent** — needs *some* classical fact about Sturmian repetition structure (the obvious candidate, before knowing which literature applies: "Sturmian words have arbitrarily long initial squares," a fact independently rememberable without BHZ specifically).
4. **Height control on the Rote witness** — need `c_R` (or the packaged `F(R)`) bounded in terms of `|R|` alone, which requires *some* discrepancy or balance-type control on `R`, not obviously supplied by the Sturmian-side discrepancy control unless `R`'s combinatorics are independently understood.
5. **A margin, not just an inequality** — since `\log_2 F` carries an `O(\log \ell)` correction whatever the exact packaging, a merely-`\ge` or asymptotically-vanishing exponent excess is a genuine risk; the required exponent bound must hold with either a *fixed* gap or fast-enough growth to swamp `O(\log \ell)`.

## What density does the Rote witness have, and why does it matter?

Independently, before reading Phase 4: the Rote root's *density* (fraction of `1`s) directly sets the required exponent threshold via `\max(1,\gamma\log_23)`. **This is exactly the quantity worth computing early**, since a naive worst-case assumption (`\gamma\to1`, threshold `\to\log_23`) may not reflect the actual, structurally-forced density of whatever Rote root the transfer mechanism actually produces — this is flagged here, before reading Phase 4, as the single most likely place a clean simplification (or a clean error) could live.

## Where quadratic irrationality should plausibly enter

Bounded partial quotients is the standard hypothesis under which Sturmian repetition quantities (critical exponent, initial critical exponent) are *finite and computable* at all (a fact independently known from general Sturmian combinatorics, not specific to any one paper) — quadratic irrationality (eventually periodic continued fraction) is a strictly stronger, more convenient hypothesis than "bounded partial quotients" alone, since it makes any relevant limsup/liminf computable in closed form via a finite recurrence, rather than merely finite. **Expectation, before comparison**: the proof likely only needs boundedness, and quadratic irrationality is used for computability/explicitness, not because it is load-bearing for the inequality itself.

## Comparison with Phase 4 (done after writing the above)

Phase 4's chain (`theorems/phase4/FINAL_PROOF_CHAIN.md`) matches this independently-derived requirement list point for point: Rote–Sturmian correspondence (external), exact transfer theorem, Theorem 10.2-type witness source, discrepancy control on the *actual* transferred root, and a margin argument. **The one item this independent pass flags as worth extra scrutiny, precisely because it was identified as "the single most likely place a clean simplification (or a clean error) could live" before comparison**: the Rote root's density claim (item above) — which is exactly Phase 4's central "density `1/2`" move. This is investigated on its own, independently re-derived terms, in `HALF_DENSITY_AUDIT.md` and `HALF_DENSITY_HEIGHT_REDERIVATION.md`, not taken on trust from this match.
