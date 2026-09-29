# COUNTEREXAMPLE_AUDIT.md

## Where a genuine near-failure was found — and against which claim

Searching specifically to break the (working-hypothesis) claim `\text{ice}(u)\ge2+\sqrt2` for lock-sustaining tails (`EVEN_TAIL_MINIMIZATION.md`), a broad sweep over period-2 tails `[e,m]` with `e\in\{2,4,6\}` (the necessarily-even "locked" entry) and `m$ ranging over `\{1,\ldots,7,10,15,20,30,50,80,150,300\}` (the free entry, any value), with preperiods up to length `6` over digits `\{1,\ldots,5\}`, found:

```
gamma = [0;1,4,1,5,1,\overline{6,2}]
ice(u) ≈ 3.1547005... < 2+√2 ≈ 3.4142136...
```

**This is a genuine counterexample to the `2+\sqrt2` hypothesis** (`SILVER_EXTREMALITY.md`: FALSE — COUNTEREXAMPLE). Per the task's own instruction ("if any true failure occurs, stop trying to prove universality and characterize the failure") — this failure **was** characterized (`SILVER_CONSTANT_AUDIT.md`, `EVEN_TAIL_MINIMIZATION.md`) rather than patched over, and led directly to `REQUIRED_EXPONENT.md`'s correction of the threshold itself.

## Does the corrected theorem (`r_u>2`) also fail anywhere tested?

**No failure found.** The same near-boundary slope, and every other tail tested in `COMPUTATIONAL_STRESS_TEST.md` (11 configurations, including the near-boundary one specifically), satisfies `r_u>2+1/(A+1)>2$ with a comfortable margin, and its **exact** surplus `S` is positive and growing (`S=62237` at the tested depth for this exact slope — matches `theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`'s original discovery of this mechanism, now explained rather than merely observed).

## Wider search attempted against the corrected threshold

An informal check (not a separate saved script — reusing `even_tail_exhaustive.py`'s search machinery) tried pushing the free entry `m` arbitrarily large (`m` up to `500`) paired with the smallest possible even locked entry (`e=2`) — the configuration one would expect to be most dangerous for a threshold that scales with `A=\max(e,m)`. **`\text{ice}` plateaued** around `3.26` rather than continuing to fall as `m\to\infty` (`EVEN_TAIL_MINIMIZATION.md`'s table) — consistent with `\text{ice}` depending on the formula's `\limsup$ over **all** phases `k`, not just the one phase where the large free entry appears, so a single large free entry cannot alone drag the limsup down. **No configuration found in this project's searches gets `\text{ice}(u)$ anywhere close to `2`** — the smallest found is `\approx3.15$, still `\ge1.15` above the corrected threshold.

## Conclusion

No counterexample to the theorem actually used (`QUADRATIC_CS_ROTE_THEOREM.md`, threshold `r_u>2`) was found by active search. The one real failure found (against the `2+\sqrt2` over-strong working hypothesis) was productive: it forced the reframing in `REQUIRED_EXPONENT.md` that produces the clean, general, unconditionally-proved bound this project settles on.
