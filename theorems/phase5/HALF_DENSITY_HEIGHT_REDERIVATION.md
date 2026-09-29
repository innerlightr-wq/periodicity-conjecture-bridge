# HALF_DENSITY_HEIGHT_REDERIVATION.md

Re-derived from scratch: `R` length `m=2\ell`, `k=m/2=\ell` ones (exact — `R=V\bar V` gives `k(R)=|V|_1+|V|-|V|_1=|V|=\ell` exactly, re-confirmed, not merely "density `1/2`" as a limiting statement — the count is *exactly* `\ell$ for *every* `\ell`, no asymptotics needed here at all).

## The two exponentials

`\Phi(R^\infty)=c_R/(2^m-3^k)`, `m=2\ell`, `k=\ell`. `2^m=2^{2\ell}=4^\ell`. `3^k=3^\ell`. Since `4>3`, `2^m` **strictly and exponentially dominates** `3^k` for every `\ell\ge1` — not merely asymptotically: `4^\ell/3^\ell=(4/3)^\ell\to\infty`, and already at `\ell=1`, `4>3`. **`\max(2^m,3^k)=2^m=4^\ell` for every `\ell\ge1`, exactly, no threshold crossing to worry about (unlike the general-density case, where `\max(2^\ell,3^k)` can favor either term depending on `\gamma$).**

## Archimedean cost, with discrepancy

Using the discrepancy-height bound (re-derivable exactly as in `theorems/phase2/DISCREPANCY_HEIGHT_PROOF.md`, itself re-verifiable independent of density): `c_R\le m\cdot3^{\lceil D(R)\rceil}\cdot\max(2^m,3^k)=2\ell\cdot3^{\lceil D(R)\rceil}\cdot4^\ell`. So
```
log_2 F(R) <= log_2(2*ell) + ceil(D(R))*log2(3) + 2*ell.
```
**The leading term is exactly `2\ell`, not `\ell\cdot\max(1,\gamma\log_23)` for a generic `\gamma$** — this is the density-`1/2` case's own clean closed form, re-derived here directly rather than obtained by substituting `\gamma=1/2` into the general formula (both must agree, and do: `\max(1,\tfrac12\log_23)\cdot m=1\cdot2\ell=2\ell`, confirming consistency, but the direct route above needed no case-split on `\max(1,\cdot)` at all since `4>3` settles it outright).

## Required depth

Transferred depth `L_v\approx L=r\ell` (r = Sturmian exponent, `theorems/phase5/TRANSFER_REDERIVATION.md`'s `+1` is `O(1)`, negligible here). Normalized against `R`'s own length `m=2\ell`:
```
L_v/m ≈ r*ell / (2*ell) = r/2.
```
**Need `L_v>\log_2F(R)`, i.e. `r\ell>2\ell+O(\log\ell)`, i.e. `r>2+O(\log\ell)/\ell\to2`.** So the required threshold, re-derived independently here, is
```
r > 2      (exactly — matching the task's own worked sketch, and Phase 4's REQUIRED_EXPONENT.md, now re-derived without consulting either)
```
with the precise sense of the inequality being: **`r` fixed and `>2` strictly suffices, since the `O(\log\ell)/\ell` correction `\to0`** — but (flagging exactly the task's own stated hinge) this requires `r-2` to be a **fixed positive number**, not merely `r\to2^+` with a shrinking gap; a gap that shrinks *too* fast (faster than `O(\log\ell)/\ell$) would fail. This is exactly why `theorems/phase4/INITIAL_EXPONENT_FORMULA.md`'s `\text{term2}(k)>2+1/(A+1)` — a *fixed*, non-shrinking margin — matters, and is re-audited independently for that fixedness in `INITIAL_POWER_QUANTIFIER_AUDIT.md` and `UNIFORM_MARGIN_AUDIT.md`.

## Conclusion

This re-derivation, done independently from the raw `2^m` vs `3^k` comparison rather than by specializing the general `\max(1,\gamma\log_23)` formula, **agrees exactly** with Phase 4's claimed threshold `r>2`. No discrepancy found in this hinge step.
