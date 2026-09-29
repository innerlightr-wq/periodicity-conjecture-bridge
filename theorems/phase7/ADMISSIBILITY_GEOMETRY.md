# ADMISSIBILITY_GEOMETRY.md

**Exploratory geometry only** — no polynomial relations established; nothing here is a variety, algebraic or otherwise.

## The picture

Each witness `W_k` is a point `\big(L_k,\ \log_2F(W_k),\ R_k,\ D(W_k)\big)`. Rationality restricts every such point to the half-space `L_k-\log_2F(W_k)\le C` (proved, `theorems/phase2/SURPLUS_THEOREM.md`'s dual theorem — re-cited, not re-derived). The Ostrowski/admissibility structure restricts which `(L_k,\ell_k,\kappa_k)` triples are *reachable at all* — a combinatorial, not geometric, constraint (admissibility condition (1), finite-alphabet-driven).

## Do general intercepts occupy a recognizably different region?

**From the data gathered (`DRIFT_VS_DIGITS.md`, `STRUCTURED_INTERCEPTS.md`): no.** Every tested intercept's witness points land comfortably inside the "certifying" half-space (`L_k-\log_2F(W_k)\to+\infty`), with `R_k$ values that are large in magnitude and slope-typical, not clustered near the resonance line or any other distinguished locus. **The admissible region for general intercepts, as far as tested, is not geometrically distinguishable from intercept `0`'s** — both occupy the same qualitative part of the `(L_k,\log_2F(W_k))` half-plane, just reached via different `(R_k,D(W_k))` paths.

## Value of this framing

Organizational, for the eventual paper (per the last conversational exchange before this phase) — a clean way to state "rationality forces a half-plane constraint; the symbolic structure supplies points that escape it" without new content. **Not used as a proof technique in this phase**; every actual certification in `OSTROWSKI_PATTERN_CLASSIFICATION.md` goes through the standard surplus inequality directly, not through this picture.
