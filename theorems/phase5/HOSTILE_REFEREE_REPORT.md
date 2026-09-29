# HOSTILE_REFEREE_REPORT.md

Line-by-line attack on `MINIMAL_PROOF.md`.

## A genuine finding, caught while attacking the "both seeds" claim (line 12)

**Checked**: does `c_W` (the exact arithmetic quantity, Proposition 4.1) actually satisfy `c_{V\bar V}=c_{\bar VV}`, as `TRANSFER_REDERIVATION.md`'s "seed-flip complements `R` uniformly, `S` unaffected" claim would suggest if read carelessly? **No — direct test, 8/8 random odd-weight `V`, `c_{V\bar V}\ne c_{\bar VV}`, often by an order of magnitude.** This looked like a genuine contradiction against `scripts/phase5/random_quadratic_stress.py`'s finding of **exact** `S`-equality across seeds in 25/25 cases.

**Resolved, not swept aside**: `bridge_surplus_exact` (traced to `scripts/phase1/bridge_toolkit.py`) does **not** use the exact `|δ_R|+c_R` quantity — it uses `F_bound(W)=(1+\ell\cdot3^{\lceil D\rceil})\max(2^\ell,3^k)`, the **discrepancy-based conservative bound** from `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`, which depends on `R` only through `(\ell,k,D(R))` — **not through `c_R` directly**. Checked directly: `D(V\bar V)=D(\bar VV)` exactly, in every one of 15 random tests. **This is why `F`, and hence every reported "exact surplus" throughout Phases 1–5, is seed-symmetric** — not because `c_R` is secretly symmetric (it is not), but because the scripts never compute the tighter `c_R`-based bound at all.

**Consequence, stated precisely**: every "exact surplus `S`" reported anywhere in this repository (Phases 1–5) is an exact, rigorously-computed **lower bound** on the true surplus (via the conservative `F_bound`, itself an exact-arithmetic quantity, so the reported `S` values are themselves exact integers, just not the *tightest possible* ones). This is **conservative, not unsound** — a positive `S` computed this way is a stronger, not weaker, certificate than one computed via the tighter `|δ|+c_R` bound would be (harder to achieve, so achieving it is more convincing). **`MINIMAL_PROOF.md`'s claimed seed-independence of `S` is correct in what the actual scripts compute, for a subtly different reason than the proof text states — flagged for correction.**

## Systematic pass over every checklist item

- **Quantifiers correct?** Re-checked in `QUANTIFIER_AUDIT.md` — yes, with the intercept boundary precisely located, not glossed over.
- **Constants uniform where needed?** Yes (`UNIFORM_MARGIN_AUDIT.md`, `1/(A+1)` fixed per slope, re-derived `k`-independently).
- **`\limsup` used as a limit?** No — `MINIMAL_PROOF.md` line 10/11 correctly uses `\limsup$; re-confirmed against `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`'s own sharpness discussion, which this audit re-read and did not find overstated.
- **Supremum treated as attained?** No — `\text{ice}$ is a `\limsup` by BHZ's own definition; the proof only needs infinitely many actual achieving prefixes exceeding a fixed threshold, which BHZ's Corollary 3.5 constructively supplies (`INITIAL_POWER_QUANTIFIER_AUDIT.md`), not "the sup is attained."
- **Infinite subsequence actually produced?** Yes, `q_k\to\infty` trivially, root lengths of the achieving words grow by BHZ's own construction.
- **Root length `\to\infty`?** Yes, re-confirmed.
- **Discrepancy on the correct word?** Yes, `R` not `V` (`ROTE_DISCREPANCY_AUDIT.md`).
- **Height reduced/unreduced consistently?** Yes — **and now more precisely characterized**: consistently *unreduced*, and in fact consistently using the conservative `F_bound`, not even the unreduced-but-exact `|δ|+c_W` — consistent throughout, per the finding above.
- **Shift/complement silently introduced?** **Caught one instance** (above) — not silently wrong, but silently *imprecisely justified*; corrected here.
- **Strict inequality preserved after `O(\log n)`?** Yes (`UNIFORM_MARGIN_AUDIT.md`, fixed margin dominates).
- **Does "quadratic" guarantee the exact property invoked?** Yes, and **more than needed** (`QUADRATICITY_DEPENDENCY.md` — bounded partial quotients alone would suffice for every ingredient actually used).

## One item this report cannot close

The exact word-length formula in BHZ's proof of Corollary 3.5 (tying `\text{term2}(k)` to a specific, explicitly-lengthed achieving word) was **not** fully extracted and checked against Phase 4's `q_{2k-1}`-indexed computational search (`INITIAL_POWER_QUANTIFIER_AUDIT.md`'s disclosed gap). This referee finds the mathematical conclusion **not threatened** (BHZ's theorem guarantees *some* growing-length achieving sequence, which is all that's needed; the computational scripts independently re-verify actual achieved exponents via direct `\text{lcp}`, not by trusting the formula's implied length) — but flags this as the one item a maximally thorough audit would still chase further.

## Overall referee assessment

One real, previously-unstated subtlety found and resolved (the `F_bound`-vs-`c_W` distinction). No soundness-threatening gap found. The theorem's logic survives.
