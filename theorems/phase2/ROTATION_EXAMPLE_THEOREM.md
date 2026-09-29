**PARTIALLY PROVED**

# ROTATION_EXAMPLE_THEOREM.md

Take Phase 1's exact instance (`ROTATION_CODING_AUDIT.md`): `\gamma`=golden ratio conjugate, `\delta=1/3` (mismatched partition), `\rho=0`, `s_n=1\iff\{n\gamma\}\in[0,1/3)`.

## Discrepancy: replace computation with proof

`ROTE_ROOT_DISCREPANCY.md`'s Step 2 argument (`N D_N^*(\beta)=O(\sum a_i)`, Koksma's inequality against the indicator of an interval) used **no property specific to the interval length `1/2`** — the indicator of **any** fixed interval `I\subset[0,1)` has bounded variation `V=2`, so the identical chain of citations gives, for `\beta=\gamma` (golden ratio, bounded partial quotients `a_i\equiv1`):
```
\big|\#\{i<N:\{i\gamma\}\in[0,1/3)\} - N/3\big| = O(\log N),
```
for **every** interval, in particular `[0,1/3)`. Since the discrepancy `D(W)` of a length-`\ell` prefix of this coding is (by the identical argument used in `ROTE_ROOT_DISCREPANCY.md`'s Step 3) controlled by exactly this interval-counting deviation, **`D(W_n)=O(\log\ell_n)` for every prefix of this specific rotation coding, proved, not merely observed on two instances.**

## Periodic approximants and their depths — not proved in general

`ROTATION_CODING_AUDIT.md` itself already identified this as the exact open point: **no general theorem (analogous to Theorem 10.2 for Sturmian words) guaranteeing arbitrarily long initial powers of exponent `>\log_23` for a general two-interval coding was found in the literature search, and none is proved in this phase.** The two witnesses Phase 1 found (`\ell=233,r\approx2.412`; `\ell=89,r\approx2.079`) remain **computational instances**, not proof of an infinite sequence with `\ell_n\to\infty`.

**What this phase adds beyond Phase 1 on this front**: a plausibility argument, not a proof. The mismatched-partition coding at `\delta=1/3` is, like the CS Rote root at `\delta=1/2` (`ROTE_ROOT_DISCREPANCY.md` Step 1), a "coding of a bounded-partial-quotient rotation against a partition mismatched with the rotation's own natural scale" — and Theorem 10.2's Sturmian guarantee is itself a statement about the **matched** case (`\delta=\gamma` or `1-\gamma`). Whether the matched-case machinery (typically proved via the three-distance theorem's own combinatorics, the same tool used for discrepancy above) extends to give repetition guarantees at a *mismatched* `\delta` is exactly the open question — plausible by analogy, not derived here.

## Classification

```
PARTIALLY PROVED.
  - Height/discrepancy control: PROVED (general argument, any fixed delta, any bounded-PQ gamma).
  - Existence of arbitrarily long initial powers with r>log2(3): COMPUTATIONAL ONLY (2 witnesses, Phase 1), not proved in this phase.
```

## Is the bridge genuinely broader than the Rote–Sturmian transfer?

**Yes, structurally confirmed, even without the full existence proof.** The discrepancy-control mechanism proved above uses **no CS Rote-specific structure at all** — it is a direct application of the abstract three-distance/Koksma argument to *any* mismatched two-interval rotation coding, independent of the `S(v)=u` construction entirely. This confirms the bridge's reach is not an artifact of the specific Rote transfer lemma; the same underlying arithmetic (bounded-partial-quotient rotations have logarithmic-discrepancy interval codings) is the common engine behind **both** `ROTE_ROOT_DISCREPANCY.md` and this section — a genuine structural finding of this phase, worth recording even though the repetition-existence half remains open for the rotation-coding case specifically.
