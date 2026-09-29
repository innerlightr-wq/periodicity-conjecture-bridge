# REQUIRED_EXPONENT.md

## Setup, from the abstract bridge (not re-derived, cited from Phase 2)

For a witness `W` of length `\ell`, density `\gamma=k/\ell`, the asymptotic sufficient condition (`theorems/phase2/REPETITION_SURPLUS_THEOREM.md`) is
```
r > \max(1,\gamma\log_23),\qquad\text{discrepancy } D(W)=o(\ell).
```
raw form: `S = L - \log_2(|2^\ell-3^k|+c_W) \to+\infty` iff `\big[r-\max(1,\gamma\log_23)\big]\ell - o(\ell)\to+\infty`.

## The Rote transfer, exactly (cited from Phase 2)

`\text{lcp}(u,W_u^\infty)=L_u`, transferred depth `L_u+1` exactly (`theorems/phase2/ROTE_TRANSFER_THEOREM.md`), at root `V` (length `\ell`, even weight) or `R=V\bar V` (length `2\ell`, odd weight). So `r_v = L_u/\ell` (even) or `r_v=L_u/(2\ell)=r_u/2` (odd), matching the task's schematic exactly, now with the precise `+1` tracked (asymptotically negligible, `O(1/\ell)`, does not affect any threshold comparison).

## The key fact this phase adds: `\gamma_R` is not a free parameter — it is always `1/2`

**Claim.** For the odd-weight case, `R=V\bar V` has density **exactly** `1/2`, for every `V`, unconditionally.

**Proof.** `|R|_1 = |V|_1 + |\bar V|_1 = |V|_1 + (|V|-|V|_1) = |V| = \ell$. `|R|=2\ell`. Density `=\ell/(2\ell)=1/2` exactly. `\blacksquare`

This is a **structural** fact about the complementary-symmetric construction itself — it needs no continued-fraction hypothesis, no discrepancy estimate, nothing beyond the definition `R=V\bar V`.

## Consequence: the required exponent, both forms

**A. Raw depth/height form.**
```
transferred depth  >  arithmetic height cost
L_u + 1  >  \log_2\big(|2^{2\ell}-3^{\ell}|+c_R\big)          [odd-weight case, since k(R)=ell exactly]
```

**B. Normalized exponent form.** Even-weight case: need `r_v=r_u>\max(1,\gamma_V\log_23)`, `\gamma_V` whatever `V`'s own density happens to be (bounded above by `1`, so `\max(1,\gamma_V\log_23)<\log_23<2` always — **this branch needs only `r_u>\log_23`, in fact `r_u\ge2` suffices with room to spare, per Theorem 10.2 alone**). Odd-weight case: need `r_v=r_u/2>\max(1,\tfrac12\log_23)`. Since `\tfrac12\log_23\approx0.7925<1`, **`\max(1,\tfrac12\log_23)=1` always** — the density-dependent term is never the binding one. So:
```
r_required(gamma) for the odd-weight route  =  2   (exactly, not 2*log2(3))
```

**This is the central correction of this phase**: the earlier working hypothesis (Phase 3, "`r_u` must exceed `2\log_23\approx3.170`") **overstated the requirement by using the worst-case-density threshold `\log_23` instead of the odd-weight route's own automatic density `1/2`, whose threshold is only `1`.** The true required Sturmian exponent is
```
r_required(gamma) = 2      [uniformly, for BOTH the even- and odd-weight routes]
```
with the odd-weight route needing `r_u>2` (giving `r_v=r_u/2>1`) and the even-weight route needing only `r_u>\log_23<2` (so `r_u>2` covers it too, with more room). **A single threshold, `r_u>2`, suffices for either transfer route.**
