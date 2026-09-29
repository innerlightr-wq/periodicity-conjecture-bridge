# DISCREPANCY_HEIGHT_PROOF.md

This re-derives Phase 1's `DISCREPANCY_HEIGHT_THEOREM.md` from scratch (the proof is correct and already exhaustively verified there; it is reproduced here rather than re-invented differently, with the additional "weakest sufficient condition" analysis the task asks for made explicit).

## Setup

`W` finite binary word, `\ell=|W|`, `k=$ ones, `k_i(W)=$ ones among first `i` letters, `D(W)=\max_{0\le i\le\ell}|k_i(W)-ik/\ell|`. From Proposition 4.1:
```
c_W = \sum_{i<\ell,\,W_i=1} 3^{k-k_{i+1}(W)}\,2^i.
```

## The bound, derived

Fix a `1`-position `i<\ell`. `k_{i+1}(W)\ge (i+1)k/\ell - D` (definition of `D`), so `k-k_{i+1}(W)\le k(\ell-1-i)/\ell + D`. With `\rho:=3^{k/\ell}` (so `\rho^{\ell}=3^k`):
```
3^{k-k_{i+1}(W)}2^i \le 3^D\cdot\rho^{\ell-1-i}2^i.
```
`i\mapsto\rho^{\ell-1-i}2^i = \rho^{\ell-1}(2/\rho)^i` is geometric in `i`, hence monotone, so its max over `0\le i\le \ell-1` is at an endpoint:
```
3^{k-k_{i+1}(W)}2^i \le 3^D\max(\rho^{\ell-1},2^{\ell-1}) \le 3^D\max(3^k,2^\ell).
```
Summing over at most `\ell` terms (one per `1`-position), and using the smallest integer `\ge D` in the exponent since `k-k_{i+1}(W)` moves in integer steps (a real threshold `D` only certifies the integer exponent `\lceil D\rceil`):

> **THEOREM.** `c_W \le \ell\cdot3^{\lceil D(W)\rceil}\cdot\max(2^\ell,3^k)`. `\blacksquare`

**Best elementary constant.** `C(D)=3^{\lceil D\rceil}` is exact at the two known reference points — `D=0` (constant `1`, matching Lemma 4.2's exact-count case) and `D<1` (constant `3`, matching Remark 4.3/Lemma 10.4) — so no elementary improvement to the base `3` is available without a fundamentally different argument; `\lceil D\rceil` (rather than `D` itself) is the correct, unavoidable integer rounding, since `k-k_{i+1}(W)` is integer-valued and the bound must hold for the worst achievable integer deviation, not the real-valued discrepancy statistic itself.

## Logarithmic form

```
\log_2 c_W \le \log_2\ell + \lceil D\rceil\log_2 3 + \max(\ell,k\log_2 3).
```

## Weakest sufficient condition — the full ladder, made explicit

Write `\theta(W):=D(W)/\ell` (discrepancy *rate*). The `D`-term contributes `\lceil D\rceil\log_2 3 = \Theta(D) = \Theta(\theta\ell)` to `\log_2 c_W`. For the surplus `S=L-\log_2F(W)` (with `L=r\ell` along a witness sequence) to have positive leading `\Theta(\ell)` coefficient, we need the `\theta`-term to not overwhelm the `(r-\max(1,\gamma\log_23))\ell` leading term. Four regimes, weakest to strongest hypothesis on `D`:

| Condition on `D(W_n)` | Contribution to `S_n` | Sufficient for `S_n\to+\infty`? |
|---|---|---|
| `D=O(1)` (bounded) | `O(1)`, negligible | **Yes**, whenever `r>\max(1,\gamma_\infty\log_23)` |
| `D=O(\log\ell)` | `O(\log\ell)=o(\ell)`, negligible | **Yes**, same condition |
| `D=o(\ell)` (i.e. `\theta_n\to0`) | `o(\ell)`, negligible | **Yes**, same condition — this is the general theorem below |
| `\limsup_n\theta_n \le \Theta_0` for a **fixed** `\Theta_0<\infty` | `\Theta(\theta\ell)`, **not** automatically negligible | **Only if** `r>\max(1,\gamma_\infty\log_23)+\Theta_0\log_23` — a strictly stronger requirement on `r` |
| `\theta_n\to\theta_\infty>0` fixed | same as above, exactly at the boundary | Same conditional requirement, now with equality permissible in the limit only if `r` strictly exceeds the threshold |

**The weakest condition that gives the clean, `r`-threshold-only theorem (no discrepancy-dependent adjustment to the threshold) is exactly `D(W_n)=o(\ell_n)`.** Anything weaker than that (a fixed nonzero `\limsup` discrepancy *rate*) still works, but only by paying for it with a larger required `r` — a genuinely different, weaker theorem, stated below as the general form.

> **THEOREM (general, quantitative).** Suppose `s` begins in `W_n^{r_n}`, `\ell_n\to\infty`, `\gamma_n\to\gamma_\infty`, `\theta_n:=D(W_n)/\ell_n$, and
> ```
> \liminf_n r_n > \max(1,\gamma_\infty\log_23) + \big(\limsup_n\theta_n\big)\log_23.
> ```
> Then `\Phi(s)\notin\mathbb Q`.

**Proof.** `S_n \ge \ell_n\big[r_n-\max(1,\gamma_n\log_23)-\theta_n\log_23\big] - \log_2\ell_n`. The bracket's `\liminf` is `\liminf r_n - \max(1,\gamma_\infty\log_23) - \limsup\theta_n\cdot\log_23 > 0` by hypothesis, so the bracket is bounded below by a fixed positive constant for all large `n`, giving `S_n=\Theta(\ell_n)-O(\log\ell_n)\to+\infty`. `\blacksquare`

This recovers `DISCREPANCY_HEIGHT_THEOREM.md`'s sublinear-discrepancy corollary at `\limsup\theta_n=0`, and is the form used in §9/§11 when the Rote-root discrepancy rate turns out to be genuinely `o(\ell)` rather than merely bounded.

## Status

**PROVED** (reproduced from Phase 1, cross-checked, extended with the explicit weakest-condition ladder). Computational re-verification is included in `phase2/scripts/verify_discrepancy_height.py` (§16) as an independent exhaustive check, not merely a re-citation of Phase 1's numbers.
