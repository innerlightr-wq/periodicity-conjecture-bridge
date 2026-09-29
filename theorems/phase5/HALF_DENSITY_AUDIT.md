# HALF_DENSITY_AUDIT.md

The elementary identity `\text{density}(R)=1/2` (`|R|_1=|V|_1+|\bar V|_1=|V|$, `|R|=2|V|`) is not in dispute — re-derived trivially, confirmed. **The real question, as the task frames it: is `R=V\bar V` actually the object the arithmetic-height theorem is correctly applied to, in every case?**

## Can `R` reduce to a shorter period?

**Yes — confirmed by direct search, not merely possible in principle.** `scripts/phase5/half_density_period_search.py`: exhaustive search over odd-weight `V` of length `\le8` finds **5** cases where `R=V\bar V` is non-primitive:
```
V=[0,1,0]  (ell=3) -> R has period 2, not 6
V=[1,0,1,0,1]  (ell=5) -> R has period 2, not 10
V=[0,1,1,0,0,1]  (ell=6) -> R has period 4, not 12
V=[1,0,0,1,1,0]  (ell=6) -> R has period 4, not 12
V=[0,1,0,1,0,1,0]  (ell=7) -> R has period 2, not 14
```
This is a real, non-vacuous phenomenon (roughly `5` out of `\sum_{\ell\le8,\text{odd wt}}2^{\ell-1}\approx510` odd-weight words tested — small but nonzero).

## Does reduction change the density?

**No** — density is a property of the finite word `R` as given (`|R|_1/|R|`), unaffected by whether `R` happens to be expressible as a shorter word's power. Every listed example still has density exactly `1/2` in its reduced form too (a proper power of a density-`1/2` word is itself density-`1/2`, trivially, since `k'/\ell'=k/\ell` for `R=(R')^m$).

## Is `c_R` computed using `R` or its reduction? Does it matter?

**Proposition 4.1 (source paper) places no primitivity hypothesis on its argument** — `c_W$ is defined by an explicit finite sum for *any* finite word `W`, and `\Phi(W^\infty)=c_W/(2^{|W|}-3^{|W|_1})` holds regardless of whether `W` is primitive (re-confirmed: this is a statement about the fixed infinite periodic sequence `W^\infty`, and if `W=(W')^m`, `W^\infty=(W')^\infty` — the **same** infinite sequence — so the identity must hold for both representations, just as *different*, generally *unreduced-relative-to-each-other*, fractions for the same 2-adic value; this is exactly the "unreduced fraction" situation already handled in general in `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`). **Phase 4's exact-arithmetic scripts (`bridge_surplus_exact`) compute `c_R` on `R` exactly as given, never checking or reducing to a primitive root** — confirmed by re-reading `scripts/phase1/bridge_toolkit.py`'s `c_W` function, which has no primitivity check. **This is valid, not a bug**: using the non-reduced `R` gives a *valid but non-tightest* height bound (larger `F(R)$ than the primitive root would give, since `F` scales with `|R|` directly) — meaning any surplus found this way is a **conservative** (understated) certificate, never an invalid one.

## Does non-primitivity ever actually threaten a Phase 4 result?

**Checked directly against Phase 4's own tested slopes.** None of the specific `V`'s arising from Phase 4's tested slopes (golden, silver, the near-boundary `\overline{6,2}$ tail, etc.) coincide with the 5 small non-primitive examples above (cross-checked: those slopes' actual `V`'s at the tested witness depths have length in the hundreds to millions, and a random/structured `V` of that length having the special self-complementary-periodic structure needed for `R` to collapse is not observed — `scripts/phase5/half_density_period_search.py` also spot-checks primitivity of the actual `R`'s used in `theorems/phase4/COMPUTATIONAL_STRESS_TEST.md`'s 11 configurations, and reports zero non-primitive cases among them). **No actual Phase 4 result relied on an unnoticed non-primitive `R`.**

## Denominator reduction (`\gcd(c_R,\delta_R)>1`)

Out of scope for the density question specifically — this is the *separate* reduced-fraction refinement already flagged (not used, not needed) in `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` and `theorems/phase2/SURPLUS_THEOREM.md`. It is a possible further tightening, never a soundness risk, and is not re-litigated here.

## Discrepancy: measured on `R` or `V`?

**On `R`, correctly** — re-confirmed: `theorems/phase4/EVEN_TAIL_SURPLUS.md`'s discrepancy claim is stated for `R` (not `V`) with the telescoping argument explicitly tracking the density shift from `V`'s own density to `R`'s forced `1/2`. This is re-derived independently, from scratch, in `HALF_DENSITY_HEIGHT_REDERIVATION.md` and `ROTE_DISCREPANCY_AUDIT.md`, not merely re-quoted here.

## Verdict

No mismatch found between the claimed mechanism and its actual use. Non-primitivity of `R` is a real, confirmed, non-vacuous phenomenon, but is shown here to be harmless to every claim actually made (conservative, not invalid, and not observed to occur among Phase 4's actual tested witnesses).
