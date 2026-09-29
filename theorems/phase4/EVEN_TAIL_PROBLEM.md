# EVEN_TAIL_PROBLEM.md

## Restating Phase 3's classification precisely — it was incomplete

Phase 3 (`theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`) framed the open problem as "all-even continued-fraction tail." **Verified against the automaton directly (not assumed) in this phase, this framing is incomplete**: a *mixed*-parity tail can also sustain the bad (all-odd-weight) lock, given the right preperiod — e.g. tail `\overline{2,1}` with preperiod `(1,1,1,1)` locks bad, confirmed computationally (`scripts/phase4/lock_search.py`).

**Corrected classification.** The bad `(A,0)\leftrightarrow(C,1)` cycle locks forever iff, once the trajectory settles into its eventual period, **every tail entry landing at an `(A,0)`-phase visit is even** — entries landing at `(C,1)`-phase visits are unconstrained (any parity). For a tail of period `r`: if `r` is odd, this forces the **entire** tail even (matches Phase 3's examples, which all happened to have `r=1`); if `r` is even, only **one specific residue class mod 2** within the tail need be even, and the other can be anything — genuinely broader than "all-even."

## Why this reframing turns out not to matter

Section 3 below shows the required threshold for the odd-weight route does not depend on the continued-fraction tail's fine structure at all — so the exact boundary of "which tails can lock bad" turns out to be a **red herring** for the actual theorem. It is documented here for accuracy (Phase 3's classification is corrected, not silently left wrong) but is not the load-bearing fact for `QUADRATIC_CS_ROTE_THEOREM.md`.

## What Rote witnesses are available, and why the even-weight shortcut can fail

- Root length: `\ell_k = q_k` (continued-fraction convergent denominators of `\gamma`), the standard-word witnesses (Theorem 10.2, cited).
- Weight: `k(W_k)\bmod2`, governed by the weight-parity automaton (Phase 3).
- Transferred approximation depth: **exactly `L_k+1`** where `L_k=\text{lcp}(u,W_k^\infty)` (`theorems/phase2/ROTE_TRANSFER_THEOREM.md`), at root length `\ell_k` (even weight) or `2\ell_k` (odd weight).
- The even-weight shortcut (`r_v=r_u` directly) is **unavailable** whenever the trajectory is locked into the bad cycle — by definition, every witness in that locked regime has odd weight, forcing the `\tau=1/2$ (doubled-root) transfer route for every one of them.

## The inequality that must hold for the odd-weight route to succeed

`REQUIRED_EXPONENT.md` derives this exactly; stated here for context: the odd-weight route succeeds whenever `r_u/2 > \max(1,\gamma_R\log_23)` asymptotically, where `\gamma_R` is the density of the doubled root `R=V\bar V`. Section 3 shows `\gamma_R=1/2` **always**, automatically — the single fact that resolves this entire phase.
