# QUANTIFIER_AUDIT.md

## A. Intercept `0`

`u_n=\lfloor(n+1)\gamma\rfloor-\lfloor n\gamma\rfloor` — the **lower mechanical word**, re-identified in `BHZ_PRIMARY_SOURCE_AUDIT.md` as bit-identical to BHZ's `\omega(-\gamma)` (proved two independent ways there, not merely re-asserted here).

## B. Both seeds

Re-derived directly in `TRANSFER_REDERIVATION.md`: complementing `v_0` complements `v`, `V`, and `R` uniformly at every step of the induction (each step is `x\mapsto x\oplus(\text{driver})`, and complementing the seed complements every subsequent term identically) — `L_v=L+1` is **unchanged** by this substitution, since the derivation never used the specific value of `v_0`, only that both `v` and the target sequence share it. **Confirmed independently.**

## C. Every shift

Re-derived from the primary source directly (not assumed): source paper, **Proposition 2.3**, read verbatim: `\Phi(\sigma v)=T(\Phi(v))`, `T` the 3x+1 map extended to `\mathbb Z_2`, and `\Phi(v)` odd `\iff v_0=1`. `T` is a bijection of `\mathbb Z_2` (the entire premise of `\Phi` being a *conjugacy* map — cited, foundational to the whole paper, not re-derived here). `T`'s two branches, `(3x+1)/2` (odd `x`) and `x/2` (even `x`), are affine with rational coefficients in both directions (inverse `S(x)=(x-1)/2` or `2x`), so `T$ restricted to `\mathbb Q\cap\mathbb Z_2` is a **bijection of `\mathbb Q\cap\mathbb Z_2` onto itself** — re-derived here, not merely asserted. Hence `\Phi(v)\in\mathbb Q\iff\Phi(\sigma v)=T(\Phi(v))\in\mathbb Q`, **both directions**, for *every* shift `\sigma^j` (induct on `j`). **The "inverse implication" the task asks to check is exactly this bijectivity — confirmed, not merely assumed, from `T`'s explicit affine formulas.**

## D. Other intercepts — precisely which ingredient fails

**Re-confirmed as a genuine, precisely-locatable gap, not a vague caveat.** The specific quantitative bound this project's theorem rests on — `\text{term2}(k)=1+a_{2k-1}+q_{2k-3}/q_{2k-2}>2+1/(A+1)` — is BHZ's **Corollary 3.5 specialized to the `\omega(-\alpha)` case** (their own derivation, §4.1, using the specific fact that `\omega(-\alpha)`'s Ostrowski digit sequence `(c_k)` has a fixed, simple pattern making their general `x(k),y(k)` formulas collapse to the two-term `\max` used). **For a general intercept** (`(c_k)$ an arbitrary admissible sequence, not the specific one for `\omega(-\alpha)`), Corollary 3.5's formula is more complex (`x(k),x'(k),y(k)` each involving `\sum_{j\le k}(a_j-c_j)q_{j-1}` sums over the *whole* prefix of `(c_j)`, not a two-term local expression) — **this general formula was not analyzed in Phase 4 or in this audit**, and no analogous fixed-margin-above-`2` bound has been derived for it. **The failing ingredient, precisely**: the `\text{term2}(k)>2+1/(A+1)` bound (`INITIAL_POWER_QUANTIFIER_AUDIT.md`) is proved for `\omega(-\gamma)$ specifically; it is not shown, and not obviously true without further work, for `\omega(x)` at a general intercept `x`. The transfer theorem (`TRANSFER_REDERIVATION.md`) and the discrepancy bound (`ROTE_DISCREPANCY_AUDIT.md`) do **not** depend on intercept at all — **only this one specific quantitative exponent bound is intercept-restricted.**

## Conclusion

Every quantifier claimed in `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` — intercept `0`, both seeds, every shift — **re-verified independently and found correct**. The stated boundary (other intercepts not covered) is **re-confirmed as precisely located**: it is a gap in the `\text{ice}` exponent bound specifically, not in the transfer or discrepancy machinery, which are already intercept-agnostic.
