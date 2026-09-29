# THEOREM_TARGET.md

## TARGET A — strongest plausible statement

> **THEOREM R (Target A).** Let `v` be any complementary symmetric Rote sequence. Then `Φ(v) ∉ Q`.

**Assessed plausibility: not currently provable with the tools in hand, and probably false as a blanket statement without qualification.** The bridge is a *sufficient*, repetition-based criterion; nothing rules out a CS Rote sequence whose associated Sturmian slope is a Liouville number with such wild partial-quotient growth that neither the repetition route nor the counting route can certify it (Phase 1's own `FULL_PERIODICITY_GAP.md` Q4 makes exactly this point for aperiodic words in general — arbitrary CS Rote sequences are not exempt). Target A is recorded as the aspirational ceiling, not the working target.

## TARGET B — the actual target of this phase

> **THEOREM R (Target B).** Let `u` be a Sturmian sequence whose slope `γ` is *badly approximable* (bounded partial quotients: `sup_i a_i(γ) < ∞`, where `γ=[0;a_1,a_2,...]`). Let `v` be any complementary symmetric Rote sequence with `S(v)=u`. Then `Φ(v) ∉ Q`.

This is an **infinite, natural, classically-recognized class** — badly approximable numbers have full Hausdorff dimension (though Lebesgue measure zero), include every quadratic irrational (golden ratio, silver ratio, all `[0;\overline{a_1,...,a_p}]`), and are the standard "next natural class" after eventually-periodic continued fractions in Diophantine approximation theory. This is the working target for §§8–11 below, motivated by the structural observation (derived in this phase, §9) that a CS Rote root's discrepancy reduces to a classical *interval-discrepancy-under-rotation* question, controllable precisely when the rotation angle has bounded partial quotients.

## TARGET C — minimal fallback, still strictly beyond the source paper

> **THEOREM R (Target C).** Let `γ` be any quadratic irrational in `(0,1)` (i.e. `γ=[0;\overline{a_1,...,a_p}]`, purely periodic continued fraction tail). Let `u` be the Sturmian sequence of slope `γ`, and `v` any CS Rote sequence with `S(v)=u`. Then `Φ(v) ∉ Q`.

Target C is a special case of Target B (every quadratic irrational is badly approximable, with the bound on partial quotients given explicitly by the period of the continued fraction) and is recorded only as a fallback in case the bounded-partial-quotient argument needed for Target B turns out to require machinery beyond what can be derived cleanly here — Target C would still constitute a proved infinite non-Sturmian class (uncountably many CS Rote languages, one per quadratic irrational slope, each associated with infinitely many distinct CS Rote sequences by choice of seed bit and shift) strictly beyond the Dubickas counting threshold, since CS Rote sequences have complexity exactly `2n`, always exceeding `1/log₂(3/2)·n` for large `n`.

## Minimum success condition

**Met by Target C alone; exceeded if Target B closes.** Both are proved infinite non-Sturmian classes with complexity `2n > (1/log₂(3/2))n` for all `n≥2` (`2 > 1.70951...`), hence genuinely beyond the counting route, requiring the repetition/height mechanism.

## Working order

§§3–7 build the general (class-independent) machinery. §8 re-derives the transfer lemma rigorously. §9 is the decisive step — it is attacked with Target B's hypothesis (bounded partial quotients) in mind, since that is exactly the hypothesis under which the classical three-distance-theorem discrepancy bound for rotation-coded intervals is provable elementarily. If §9 closes for Target B, §11 proves Target B (which contains Target C). If §9 only closes for Target C's narrower hypothesis, §11 proves Target C and Target B is left open with the precise missing step identified.
