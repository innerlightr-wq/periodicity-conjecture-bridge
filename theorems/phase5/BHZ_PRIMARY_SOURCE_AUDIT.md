**MATCH AFTER EXPLICIT TRANSFORMATION** (transformation: none needed for the sequence itself — the "transformation" is the coordinate change between BHZ's `[-\alpha,1-\alpha)` domain and this project's `[0,1)` mechanical-word convention; the two are verified to produce bit-identical sequences)

# BHZ_PRIMARY_SOURCE_AUDIT.md

Re-fetched directly from `https://www.irif.fr/~berthe/Articles/sturm15.pdf` (Berthé, Holton, Zamboni, *Initial powers of Sturmian sequences*, Acta Arithmetica 122(4), 2006), not read via any Phase 1–4 quotation.

## Their definitions, exactly as stated (§2.1)

Two interval exchanges on `[-\alpha,1-\alpha)` / `(-\alpha,1-\alpha]`:
```
R_alpha(z)  = z+alpha    if z in [-alpha, 1-2alpha)     R~_alpha(z)  = z+alpha    if z in (-alpha, 1-2alpha]
            = z+alpha-1  if z in [1-2alpha, 1-alpha)                  = z+alpha-1  if z in (1-2alpha, 1-alpha]
```
A Sturmian sequence of slope `\alpha`, **intercept** `x`, is the itinerary of `x` under `R_\alpha` (or `\tilde R_\alpha`) against the two-piece partition, `\omega_k=0\iff R_\alpha^k(x)\in[-\alpha,1-2\alpha)`.

**The characteristic sequence** has intercept `0` and its **two shift preimages** code the orbits of `-\alpha` (under `R_\alpha`) and `1-\alpha` (under `\tilde R_\alpha`) — **this is BHZ's own definition of `\omega(-\alpha)` and `\omega(1-\alpha)`**, stated explicitly in their preliminaries, not merely inferable from later notation.

## Identification, proved two ways

**1. Computational, from the exact definitions above (not from any Phase 1–4 file).** `scripts/phase5/bhz_identification_check.py` implements BHZ's `R_\alpha`/`\tilde R_\alpha` literally (exact `Fraction` interval-membership tests, half-open intervals matched exactly as stated — `[,)` for `R_\alpha`, `(,]` for `\tilde R_\alpha`) and compares against this project's `u_n=\lfloor(n+1)\gamma\rfloor-\lfloor n\gamma\rfloor` over **2000 terms**, three slopes (golden, silver, the Phase 4 near-boundary tail):
```
u_ours == omega(-alpha), every slope, all 2000 terms:  True
u_ours == omega(1-alpha), every slope:                  False (differs at index 0)
```
**Exact bit-for-bit agreement with `\omega(-\alpha)$, not `\omega(1-\alpha)`, disambiguated cleanly (they differ already at the first symbol).**

**2. Structural, independent of computation.** Both `u` and `\omega(-\alpha)` are, by construction, forward itineraries of the **same point** (`-\alpha`, equivalently `0` shifted back one step under the rotation) under a rotation by the **same angle** `\alpha`, coded by a two-interval partition whose lengths are `\{1-\alpha,\alpha\}` in both cases — the `[-\alpha,1-\alpha)`-domain partition and the `[0,1)`-domain lower-mechanical-word partition are the same partition up to the affine identification `z\mapsto z+\alpha` (BHZ's own text: "these can be considered as rotations... conjugate, after identification of points `-\alpha` and `1-\alpha`, to a circle rotation"). Two codings of the same orbit under the same partition, differing only by this fixed coordinate shift, produce **identical symbol sequences** — this is not a coincidence needing separate proof, it is what "conjugate coding" means.

## Additional cross-check: Section 4.4 (Fibonacci case), read independently

BHZ's own Proposition 4.3 states: "the function `\text{ice}` is shift invariant on `X_\theta`, and `\text{ice}(\omega)=1+\theta` if `\omega` belongs to **the Z-orbit** of the characteristic sequence" — note *two-sided* (`\mathbb Z`) orbit, not the one-sided forward shift orbit the paper's own introduction contrasts against (which is where the *different*, larger value `2+\theta` applies, and only conditionally — Proposition 4.3's "if and only if... arbitrarily long strings of consecutive `0`s" in the Ostrowski expansion). Since `\omega(-\alpha)=0\omega` is a one-step **backward** shift of the characteristic sequence, it is in the two-sided `\mathbb Z`-orbit, giving `\text{ice}(\omega(-\alpha))=1+\theta` for golden ratio — **exactly** the `2.618\ldots` value computed via Corollary 3.5's formula in Phase 4 and re-confirmed independently here (`scripts/phase5/bhz_identification_check.py`'s golden-ratio row, and the direct formula re-evaluation in `INITIAL_POWER_QUANTIFIER_AUDIT.md`). This is an independent internal consistency check within BHZ's own paper (two different sections, two different arguments, same numeric answer), not merely a self-check of this project's earlier work.

## Classification

```
MATCH AFTER EXPLICIT TRANSFORMATION: u (this project's intercept-0 lower mechanical word)
  IS BIT-IDENTICAL to BHZ's omega(-alpha), verified from BHZ's own stated interval-exchange
  definitions (not quoted secondhand), confirmed computationally (2000 terms, 3 slopes, exact
  arithmetic) and structurally (same orbit, same partition, coordinate-shift-only difference).
  omega(1-alpha) is a DIFFERENT sequence (differs at index 0) and is NOT what this project uses
  -- Phase 4's use of the omega(-alpha)-specific Corollary 3.5 formula (not the omega(1-alpha)
  formula) is CORRECT.
```

**Phase 4's identification survives this audit.** No mismatch found.
