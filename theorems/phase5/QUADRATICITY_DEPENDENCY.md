# QUADRATICITY_DEPENDENCY.md

## Where quadratic irrationality is actually invoked, traced through the re-derived chain

1. **`\text{term2}(k)>2+1/(A+1)`** (`INITIAL_POWER_QUANTIFIER_AUDIT.md`, re-derived): needs only `a_{2k-2}\le A` for the relevant `k`'s — i.e. **bounded** partial quotients suffice; the bound `[x;\text{rest}]<x+1` used does not care whether the sequence is eventually *periodic*, only that some fixed `A` bounds every term that arises.
2. **`D(R)=O(\log|R|)`** (`ROTE_DISCREPANCY_AUDIT.md`, re-derived): the cited three-distance/Koksma mechanism (`N D_N^*(\beta)=O(\sum_{i\le k}a_i)`) needs `\sum_{i\le k}a_i=O(k)`, which again only needs **bounded** partial quotients, not periodicity.
3. **`q_k\to\infty`**: true for *any* irrational, no boundedness even needed.
4. **BHZ's `\text{ice}(u)\ne2` for quadratic slopes** (`INITIAL_POWER_QUANTIFIER_AUDIT.md`'s cross-check): this specific *cited* fact (BHZ, §5) is stated by BHZ for quadratic slopes specifically (their Theorem 1.1's minimality characterization requires unbounded partial quotients to achieve `\text{ice}=2`, and quadratic is the standard way to guarantee boundedness) — **but this citation is not the load-bearing one**; Phase 4/5's own `\text{term2}(k)` bound (item 1) is what's actually used, and it only needs boundedness.

## Verdict: is quadraticity stronger than necessary?

**Yes, on the evidence of this re-derivation.** Every ingredient actually used in the re-derived proof chain (`term2` bound, discrepancy bound) needs only **bounded partial quotients** — a strictly weaker hypothesis than "quadratic irrational" (eventually periodic continued fraction). Quadraticity was likely adopted in Phase 2–4 for **computability/explicitness** (a periodic tail makes `A` and the limsup formulas closed-form and easy to evaluate, exactly as flagged as the expected reason in `theorems/phase5/INDEPENDENT_PROOF_REQUIREMENTS.md`, written *before* this comparison), not because the inequalities themselves require it.

## What this does — and does not — mean for this audit

**Recorded, not acted on**, per the task's explicit instruction. The headline theorem (`theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`) is **not** rewritten, expanded, or reclassified to "every bounded-partial-quotient slope" in this phase — that would be exactly the scope expansion the task prohibits. This finding is filed for a future, explicitly-scoped phase (matching `theorems/phase2/THEOREM_TARGET.md`'s own pre-existing Target B / Target C distinction, which already anticipated this exact question).
