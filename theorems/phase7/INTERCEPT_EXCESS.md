# INTERCEPT_EXCESS.md

## The `E_k:=L_k-2\ell_k` form — when it applies, and when it doesn't

For the **odd-weight branch** (`R=V\bar V`, density exactly `1/2`, `theorems/phase4/REQUIRED_EXPONENT.md`), the critical depth **is** `2\ell_k` (since the required exponent is exactly `2` on the *doubled* root — equivalently `1` on `R` itself, i.e. `L_k>2\ell_k` on the Sturmian side transfers to `L_k>|R_k|` on the Rote side). **This form is valid for the odd branch specifically, and is the binding branch** (even branch needs only `r_k>\log_23<2`, comfortably implied whenever `r_k>2`). So `E_k=L_k-2\ell_k$ is used as the primary quantity, **not assumed universally** — for a witness landing in the even branch, the correct excess is `E_k^{\text{even}}=L_k-\log_23\cdot\ell_k`, a strictly weaker requirement, always satisfied whenever the odd-branch form is.

## The general criterion

```
E_k >> D(R_k) + log(ell_k)
```
Since `D(R_k)=O_A(\log\ell_k)` (`SURPLUS_DECOMPOSITION.md`), this reduces to
```
E_k / log(ell_k)  ->  +infinity
```
along some subsequence — **the weakest sufficient asymptotic statement**, re-derived directly from `theorems/phase2/DISCREPANCY_HEIGHT_PROOF.md`'s general ladder (not the fixed-margin shortcut Phases 4–6 used because it was available and simpler at intercept `0`).

## Why this is a much weaker requirement than a fixed margin

`E_k\gg\log\ell_k` is satisfied by **any** `E_k` that is eventually bounded below by a growing function of `\ell_k` dominating `\log\ell_k` — in particular by any **fixed positive constant** (trivially, since a constant `\gg\log\ell_k` fails for large `\ell_k`... **correction, checked carefully**: a *fixed positive constant* `E_k\equiv\delta>0` gives `E_k\ell_k=\delta\ell_k\gg\log\ell_k` automatically (`\delta\ell_k/\log\ell_k\to\infty`), so **the criterion `E_k\ell_k\gg\log\ell_k`, not `E_k\gg\log\ell_k`, is the one actually needed** — re-reading `theorems/phase2/DISCREPANCY_HEIGHT_PROOF.md`'s ladder precisely: the surplus is `\ge E_k\ell_k-C_AD_k-O_A(\log\ell_k)`, so the condition is on `E_k\ell_k$ against `\log\ell_k`, not on `E_k` alone against `\log\ell_k`. **Corrected form**:
```
E_k * ell_k  >>  log(ell_k)     i.e.     E_k  >>  log(ell_k)/ell_k
```
This is dramatically weaker than "`E_k` bounded away from `0`" — `E_k\sim1/\sqrt{\ell_k}$, or even `E_k\sim(\log\ell_k)^2/\ell_k`, would still suffice, since both dominate `\log(\ell_k)/\ell_k`. `theorems/phase7/FLEXIBLE_MARGIN_BOUNDARY.md` works out the exact boundary among the task's suggested asymptotic families.
