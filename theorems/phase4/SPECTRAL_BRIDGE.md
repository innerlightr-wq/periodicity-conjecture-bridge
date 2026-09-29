# SPECTRAL_BRIDGE.md

## Setup

For periodic tail `b_1,\ldots,b_r`, transfer matrix `P=A(b_r)\cdots A(b_1)`, `A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix}`. `P`'s Perron eigenvalue `\lambda_P>1` governs `q_{n+r}/q_n\to\lambda_P` (standard CF theory: `\binom{q_n}{q_{n-1}}` transforms by `A(a_n)` each step, so `r` steps transform by (a cyclic rotation of) `P`).

## Depth growth rate vs. height growth rate

`\ell_k\sim\lambda_P^{k/r}` (up to a bounded multiplicative constant depending on phase). The transferred surplus's leading term (`EVEN_TAIL_SURPLUS.md`) is `S_k=\Theta(\ell_k)` — **linear** in `\ell_k`, not exponential in `k` alone; the *rate at which `\ell_k` itself grows* (`\lambda_P`) does not enter the sign of the leading coefficient at all, only the *speed* at which a fixed positive linear-in-`\ell` surplus accumulates. This matches `DIRECT_SURPLUS_RECURRENCE.md`'s finding exactly: the eigenvalue (`(1+\sqrt2)^2` for the silver tail, i.e. `\lambda_P^2` since two convergent-index-steps correspond to one full `2\times2`-block per period-1 tail) shows up in **how fast** `S_k` grows, confirming the theorem is not merely a limsup fact but a genuine `\Theta(\ell_k)` divergence — it does not change **whether** `S_k` is eventually positive, which is governed by `\text{term2}>2+1/(A+1)` (`INITIAL_EXPONENT_FORMULA.md`), an `O(1)`-level fact independent of `\lambda_P`.

## Does bridge closure reduce to a spectral inequality?

**No — this is the honest negative finding of this section.** The natural spectral candidate ("depth growth rate `>` height growth rate") would compare two *exponential* rates, but the abstract bridge (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`) is fundamentally a comparison of `L_n` (linear in `\ell_n`, via the exponent `r_u`) against `\log_2F(W_n)` (also linear in `\ell_n`, via `\max(1,\gamma\log_23)`) — **both sides are already `\Theta(\ell_n)`, not exponential in `\ell_n`**, so there is no exponential-rate comparison for a spectral radius to naturally govern. The Perron eigenvalue `\lambda_P` controls the *reparametrization* `k\mapsto\ell_k` (how many witnesses occur up to a given length), not the *per-length* margin. **The initial-critical-exponent route (`INITIAL_EXPONENT_FORMULA.md`) is the natural and sufficient tool here; the spectral route is a genuine but secondary corroboration of the growth *rate*, not an alternative proof of positivity, and is not used in `QUADRATIC_CS_ROTE_THEOREM.md`.**
