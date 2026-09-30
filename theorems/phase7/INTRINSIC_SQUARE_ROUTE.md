> **SUPERSEDED BY PHASE 8 (reading confirmed) — see
> [`theorems/phase7/PHASE7_CORRECTIONS.md`](PHASE7_CORRECTIONS.md).** This file's analysis is
> correct: bare squares give zero margin on the odd-weight branch. Phase 8 Theorem 1 supplies
> `r_u > 2` strictly at every intercept, so the bypass is unnecessary rather than repaired.

# INTRINSIC_SQUARE_ROUTE.md

## The candidate strategy

Source paper's Theorem 10.2 (cited, ADQZ): every Sturmian word begins in arbitrarily long initial squares (`r\ge2`), **at every slope and every intercept, no exceptions** ("no exceptional slopes or intercepts", source paper's own words, re-confirmed reading `Section 10`). This is exactly how the source paper itself solved the all-intercept problem for `u`'s own irrationality — bypass the intercept-`0`-only convergent depth law, use intrinsic squares instead.

## Does the analogous strategy bypass Ostrowski-digit control for the Rote-transferred `v`?

**No — and the exact re-entry point is precise, not vague.**

**Even-weight branch: yes, fully bypasses it.** At `r=2` exactly (the bare Theorem 10.2 guarantee, no margin needed beyond this), the even-weight threshold is `\max(1,\gamma\log_23)<\log_23\approx1.585<2` for **any** density `\gamma\in(0,1)` — so `r=2` exactly already gives a fixed margin `\ge2-\log_23\approx0.415`, **unconditionally, at every intercept, with no Ostrowski-digit analysis needed at all** (this is exactly `theorems/phase1/REPETITION_HEIGHT_CRITERION.md`'s "unconditional squares" theorem, re-applied here, intercept-agnostic because it never used any Sturmian-specific fact beyond `r=2` and the *combinatorial* discrepancy cap).

**Odd-weight branch: does not bypass it — this is the exact re-entry point.** At `r=2` exactly, the odd-weight (density-`1/2`, `theorems/phase4/REQUIRED_EXPONENT.md`) threshold is `\max(1,\tfrac12\log_23)=1` — and `r_v=r_u/2=2/2=1` **exactly**, giving **zero margin**, the same boundary failure already identified in Phase 1 (`r=1` gives nothing). **Bare squares (`r=2`) are insufficient for the odd branch; strict excess `r>2` is required, exactly as at intercept `0`.**

## Where this reconnects to the weight-parity question

Whether the Theorem-10.2 square witness at a given intercept lands in the even or odd branch is governed by the **same weight-parity mechanism** as `theorems/phase3`'s automaton — but now for a **general-intercept** prefix-count function, not the `\rho=0`-specific one Phase 3 analyzed. **This project did not re-derive a general-intercept weight-parity automaton** (out of scope for this phase's time budget) — instead, `theorems/phase7`'s BHZ-margin route sidesteps the question entirely, exactly as Phase 6 discovered for intercept `0`: since `r>2` **strictly** (not merely `\ge2`) is available from BHZ's formula at (empirically) every tested intercept, **both** branches work regardless of which one a given witness lands in, so the weight-parity question never needs answering.

## Verdict

The intrinsic-square route **does not dominate** the BHZ-formula approach — it is strictly weaker (only gives `r=2` exactly, insufficient for the odd branch) unless combined with a general-intercept weight-parity analysis that was not attempted here. **The BHZ margin route (`INITIAL_POWER_QUANTIFIER_AUDIT`-style excess above `2`) remains the load-bearing mechanism for general intercepts**, not a bypass of it.
