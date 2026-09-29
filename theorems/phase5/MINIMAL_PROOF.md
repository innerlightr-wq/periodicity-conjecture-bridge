# MINIMAL_PROOF.md

Reconstructed from the smallest number of ingredients that survived this audit's independent re-derivation. Every line cites either a proved repository theorem (re-verified in this phase) or an exact primary-source theorem (re-read in this phase).

1. `\gamma$ quadratic irrational `\Rightarrow` continued fraction eventually periodic `\Rightarrow` bounded partial quotients, max value `A` (elementary).
2. `u=\omega(-\gamma)$ (BHZ's notation) equals this project's intercept-`0` lower mechanical word — `BHZ_PRIMARY_SOURCE_AUDIT.md` (re-derived from BHZ §2.1's own definitions, confirmed computationally over 2000 terms × 3 slopes, and structurally from the shared-orbit argument).
3. `\text{ice}(u)>2+1/(A+1)`, with the exponent achieved at genuine, growing-length, actually-realized initial-power prefixes of `u` (not merely a supremum) — Berthé–Holton–Zamboni 2006, Corollary 3.5, specialized to `\omega(-\alpha)$, elementary reversed-CF bound applied to their formula; re-derived and re-checked unconditionally over `k` in `INITIAL_POWER_QUANTIFIER_AUDIT.md`.
4. Exact CS-Rote transfer: `\text{lcp}(v,\text{target}^\infty)=\text{lcp}(u,W^\infty)+1` exactly, target `=V$ (even weight) or `R=V\bar V` (odd weight) — `TRANSFER_REDERIVATION.md`, re-derived from `v_{n+1}=v_n\oplus u_n` alone, verified exhaustively (114,680 cases, `scripts/phase5/independent_transfer_check.py`).
5. **Even branch**: closes because `r_u>2>\log_23`, at **any** density `\gamma_V\in(0,1)` (`\max(1,\gamma_V\log_23)<\log_23<2` always) — no further condition needed.
6. **Odd branch**: `R=V\bar V` has density **exactly** `1/2` — `|R|_1=|V|_1+|\bar V|_1=|V|=|R|/2` (two-line identity, re-derived in `HALF_DENSITY_AUDIT.md`), independent of `V`'s own structure.
7. Density `1/2` collapses the required threshold from `\log_23` to `\max(1,\tfrac12\log_23)=1` exactly — `HALF_DENSITY_HEIGHT_REDERIVATION.md`, re-derived directly from `2^{2\ell}` vs `3^\ell` (`4^\ell` strictly dominates `3^\ell` for every `\ell\ge1`, no threshold-crossing case split needed).
8. `D(R)=O(\log|R|)$ — `ROTE_DISCREPANCY_AUDIT.md`, re-derived as `D(R)\le2D(V)+\ell|\gamma_V-\tfrac12|`, both terms `O(\log\ell)` via the same three-distance/Koksma mechanism applied one level down (to `W`, giving `D(V)$ and the density-gap term).
9. Margin `1/(A+1)` (item 3) is **fixed**, independent of the witness index `k` — `UNIFORM_MARGIN_AUDIT.md`, re-derived directly from the reversed-CF bound's `k`-independence.
10. Combining 3+6+7+8+9: `S_k\ge\ell_k/(A+1)-O(\log\ell_k)\to+\infty` (odd branch); trivially `\to+\infty` even faster (even branch).
11. Abstract irrationality criterion: `\limsup_kS_k=+\infty\Rightarrow\Phi(v)\notin\mathbb Q` — `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, standing hypothesis `s\ne W_n^\infty` satisfied automatically since `v` (derived from aperiodic `u`) is itself aperiodic — re-confirmed not to be vacuous via `RATIONAL_CONTROLS.md`'s Control 2.
12. Both seeds (`v_0\in\{0,1\}`) and every shift `\sigma^j(v)` covered — `QUANTIFIER_AUDIT.md`, seed-independence re-derived directly in step 4's induction, shift-invariance re-derived from source-paper Proposition 2.3's bijectivity.

`\therefore\ \Phi(v)\notin\mathbb Q`, for every complementary symmetric Rote sequence `v` (both seeds, every shift) associated with the intercept-`0` mechanical word of any quadratic-irrational slope `\gamma`.

**Nothing from the original weight-parity automaton (Phase 3) or the `2+\sqrt2` silver-ratio bound appears in this minimal chain** — re-confirmed here, independently, as unnecessary machinery, matching `theorems/phase4/FINAL_PROOF_CHAIN.md`'s own assessment.
