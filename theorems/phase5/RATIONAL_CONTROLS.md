# RATIONAL_CONTROLS.md

`scripts/phase5/rational_controls.py`, output `data/phase5/rational_controls_output.txt`. Exact integer arithmetic throughout.

## Control 1: eventually periodic `u` (rational-`\Phi`-value stand-in)

`u` = preperiod `[1,1,0]` then period `[0,1,1,0,1]` (odd weight, forcing the `R=V\bar V` route) repeated `4000` times. The derived `v` is likewise eventually periodic. Testing surplus against the *true* period, lengthened (`m=2,\ldots,64` copies): `S=-14,-25,-46,-87,-168,-329` — **negative and getting more negative, not diverging to `+\infty`.** The mechanism fails exactly as it should: `\text{lcp}` against the true period stays pinned near `1` (the preperiod's own short mismatch point) while the height cost grows with the witness length — the opposite of the certifying pattern. **The bridge correctly stays silent on a genuinely rational input.**

## Control 2: a subtlety the density-`1/2` argument does *not* bypass

Deliberately constructed a **purely periodic** `v=R^\infty` with `R` chosen to have density exactly `1/2` by the same `V\bar V` construction (so `\Phi(v)$ is manifestly rational — `v` literally equals a periodic word). Testing surplus against `R` itself, lengthened: `S=92,390,1588,5986,19985$ — **positive and growing**, at first glance looking like a false certificate.

**This is not a false positive — it is the abstract criterion's own excluded case, confirmed by direct inspection.** `\Phi(s)\notin\mathbb Q` requires the standing hypothesis `s\ne W_n^\infty` (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, re-verified in `TRANSFER_REDERIVATION.md`'s re-derivation: `M_n\ne0` is proved *from* `s\ne W_n^\infty`, via `\Phi`'s bijectivity). Here `v` **does** equal `W^\infty$ for the tested witness (`v=R^\infty` by construction, and `W=R^m$ shares the same periodic extension) — the hypothesis is violated, `M_n=0` identically, and the criterion's conclusion (whatever `S` numerically computes to) **simply does not apply**. **The density-`1/2` observation does not, by itself, produce a false certificate — it is the separately-checked, always-required `s\ne W_n^\infty` (equivalently: genuine aperiodicity of `s`, and `W_n` a *proper* finite prefix pattern, not literally the whole tail) hypothesis that screens this case out, exactly as it is designed to.** In every actual Phase 4/5 application, `s=v` is derived from an aperiodic (irrational-slope) Sturmian `u`, so `v` is provably aperiodic and this degenerate case cannot arise — but this control confirms the *mechanism* genuinely depends on that hypothesis, rather than the density-`1/2` fact alone being strong enough to force a conclusion.

## Verdict

Both controls behave exactly as required: genuine rational input stays silent (bounded/negative surplus); a deliberately constructed density-`1/2` *periodic* input shows numerically positive `S` but is correctly excluded by the criterion's own standing hypothesis, not by any accident of the specific numbers. **No false-positive risk found in the half-density mechanism itself.**
