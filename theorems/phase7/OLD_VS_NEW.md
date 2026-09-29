# OLD_VS_NEW.md

## Already proved — not re-derived, not re-litigated in this phase

- **Abstract surplus criterion.** For aperiodic `s`, witnesses `W_n$, `S_n:=L_n-\log_2(|2^{\ell_n}-3^{k_n}|+c_{W_n})`, `L_n=\text{lcp}(s,W_n^\infty)`: if `\Phi(s)=u/v\in\mathbb Q`, `H=\max(|u|,v)`, then `S_n\le\log_2H` for **every** `n` — so `\limsup_nS_n=+\infty\Rightarrow\Phi(s)\notin\mathbb Q`. (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, `theorems/phase2/SURPLUS_THEOREM.md`.)
- **Discrepancy-height bound**, `c_W\le\ell\cdot3^{\lceil D\rceil}\cdot\max(2^\ell,3^k)`, and its weakest-condition ladder. (`theorems/phase2/DISCREPANCY_HEIGHT_PROOF.md`.)
- **Repetition-surplus criteria**, both density-convergent and density-free forms. (`theorems/phase2/REPETITION_SURPLUS_THEOREM.md`.)
- **Exact Sturmian→Rote XOR transfer**, `L_v=L_u+1` exactly, both parity branches, re-derived and exhaustively re-verified (114,680 cases) independently in Phase 5. (`theorems/phase2/ROTE_TRANSFER_THEOREM.md`, `theorems/phase5/TRANSFER_REDERIVATION.md`.)
- **Odd-weight root `R=V\bar V` has density exactly `1/2`**, unconditionally, any `V`. (`theorems/phase4/REQUIRED_EXPONENT.md`, re-derived `theorems/phase5/HALF_DENSITY_HEIGHT_REDERIVATION.md`.)
- **Actual-root discrepancy control**, `D(R)=O_A(\log|R|)` for bounded-partial-quotient slopes, re-derived directly on `R` (not a proxy). (`theorems/phase5/ROTE_DISCREPANCY_AUDIT.md`.)
- **Bounded-type, intercept-`0` theorem**: `\Phi(v)\notin\mathbb Q` for every CS Rote sequence associated with the intercept-`0` mechanical word of any bounded-partial-quotient slope (both seeds, every shift). (`theorems/phase6/BOUNDED_TYPE_THEOREM.md`.)

None of the above is re-proved, weakened, or renamed in Phase 7. Any new file in this phase that appears to restate one of these must cite it, not reintroduce it as new.

## What is genuinely new in Phase 7

**Everything upstream of "does a witness with adequate margin exist" was intercept-`0`-specific.** The intercept-`0` proof works only because `u=\omega(-\gamma)`'s Ostrowski digit sequence `(c_k)` has one fixed, simple pattern, collapsing BHZ's general Corollary 3.5 formula to a two-term `\max` with a clean, `A`-only margin. **Phase 7's actual open question**: for a *general* admissible `(c_k)`, does BHZ's general (uncollapsed) formula still supply witnesses whose surplus, run through the *unchanged* downstream machinery (transfer, density, discrepancy), diverges? This is a question about **witness existence and quality as a function of Ostrowski digits** — nothing about the downstream machinery itself is in question.
