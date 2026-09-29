**OBSTRUCTION CLASSIFIED — ONE LEMMA REMAINS**

# PHASE7_VERDICT.md

## Summary

No counterexample found anywhere searched — 36 structured Ostrowski digit families across 4 slopes (`theorems/phase7/STRUCTURED_INTERCEPTS.md`), plus 4 genuinely nonzero intercepts verified through the *exact, already-proved* Phase 4–6 machinery directly (`data/phase7/nonzero_intercept_direct.txt`, no reconstruction uncertainty). A major structural fact was found and re-derived from the BHZ primary source: for **all but a countable set of "return" intercepts**, the available margin (`\text{ice}=ind^*(\alpha)`) is *provably larger* than at intercept `0`, not smaller — intercept `0` is, if anything, a harder case than generic, and it is already fully proved (Phases 4–6).

## Strongest proved result

`theorems/phase6/BOUNDED_TYPE_THEOREM.md` — unchanged, intercept `0` only, frozen. This phase adds **no new proved theorem** (correctly, per its own mandate — obstruction-mapping, not theorem-proving): the countable-exceptional-set structure (`BHZ_GENERAL_INTERCEPT_MAP.md`) is proved *as a reduction*, but the individual non-`j=0` members of that countable set were not separately proved here.

## Strongest negative/counterexample finding

None against the mathematics. **One real, disclosed self-correction**: this phase's own reconstruction of BHZ's Section-3 achieving-word construction does not reproduce the conjectured root-length formula `q_k-c_kq_{k-1}` (checked, mismatched at every tested `k`, not close) — caught by `scripts/phase7/verify_phase7.py`, not hidden. This threatens no conclusion (the abstract `\text{ice}` ratio is trustworthy independent of this reconstruction, and `nonzero_intercept_direct.py`'s fully-exact route sidesteps it entirely), but is recorded honestly as an open technical gap.

## Exact remaining lemma

> For any admissible Ostrowski digit sequence `(c_k)` of a bounded-partial-quotient slope `\gamma` (`A=\sup a_n<\infty`), `\limsup_k\max(x'(k),y(k))>2`, with a margin depending only on `A`.

Classified **CONJECTURAL** (`theorems/phase7/INTERCEPT_SUFFICIENT_CONDITION.md`) — strong evidence, no proof.

## Did drift add technical power?

**No — expository only** (`theorems/phase7/DRIFT_VS_DIGITS.md`). Recorded as intended (diagnostic coordinate, not claimed as a theorem), per the task's own explicit instruction.

## Final status

```
OBSTRUCTION CLASSIFIED — ONE LEMMA REMAINS
```

The obstruction (loss of the clean `\omega(-\gamma)`-specific BHZ closed form) is precisely located, its downstream consequences fully traced, and its practical severity found to be much smaller than initially suspected — no computational evidence of failure anywhere, and a structural argument (the exceptional-orbit reduction) narrows the genuinely open cases to a countable, already-mostly-handled set plus one unproved general margin lemma. This is not "no clean classification" and not "current bridge fails" — it is a mapped, bounded obstruction with a single identified missing lemma, exactly the honest middle classification this phase's own discipline requires.
