# ROTE_COMPUTATIONAL_AUDIT.md

`scripts/rote_construction_test.py`, exact integer/`Fraction` arithmetic throughout (the surplus pass/fail test `S = L − ⌈log₂F⌉` is computed via exact bit-length comparisons on huge Python ints — never a floating-point decision).

## Bug caught and fixed (in-session, disclosed)

An earlier version of this script's continued-fraction evaluator (`cf_convergent`) had `num`/`den` swapped, silently returning the **reciprocal** of the intended slope (e.g. "silver ratio" `0.41421356` came out as `2.41421356`). This was caught because it produced an internally-impossible result — a binary word with `k=408` ones in a length-`ℓ=169` prefix (`k>ℓ` is impossible for `{0,1}` words) — while directly debugging an unexpectedly negative surplus. Fixed (`num,den` order corrected), and every result below is from the re-run **after** the fix. This is exactly the kind of self-check the falsification-first discipline is meant to catch, and it worked.

## Construction

For a Sturmian mechanical word `u` (slope `γ`, exact `Fraction` continued-fraction convergent, high precision, no floating point in the word-generation itself) and seed `v_0=0`, build the unique CS Rote sequence `v` with `S(v)=u` via `v_{n+1}=v_n⊕u_n` (confirmed construction, `ROTE_LITERATURE_AUDIT.md`).

## Transfer-lemma sanity check

Verified exactly on three small synthetic periodic examples (even-weight root, two different even-weight cases, one odd-weight root) — predicted period/exponent for `v` matches the direct construction in every case (`match=True`, all three).

## Main result: three Sturmian slopes, searched to root length 1200

For each slope, **every** initial power (`r≥1`, not pre-filtered by any exponent threshold) of both `u` and its derived `v` was examined, and the **exact** surplus `S` computed for each — the only criterion that actually matters (a fixed `r`-threshold like `r>log₂3` is **not**, on its own, unconditionally sufficient — only `r≥2` is, per `REPETITION_HEIGHT_CRITERION.md`; smaller `r` can still certify case-by-case when the discrepancy/density happen to be favorable, which is exactly what the exact-`S` test checks for directly rather than relying on a blanket exponent rule).

| Slope | `u` certifying powers (S>0) found | `v` certifying powers (S>0) found | Deepest `v` certificate |
|---|---|---|---|
| golden ratio conjugate `[0;1,1,1,...]` | 66 (up to ℓ=1199) | 32 (up to ℓ=1178) | `ℓ=1178, r≈1.018, S=6` |
| silver ratio `[0;2,2,2,...]` | 55 (up to ℓ=1183) | 20 (up to ℓ=1183) | `ℓ=1183, r≈1.059, S=53` |
| mixed CF `[0;1,2,1,3,1,4,...]` | 9 (up to ℓ=641) | 31 (up to ℓ=1187) | `ℓ=1187, r≈1.016, S=2` |

**Result: the bridge fires on the derived CS Rote sequence `v` at every tested slope**, with the count and depth of certifying instances still growing as the search window (root ≤1200) is extended — i.e. this is not a single fluke instance but a recurring phenomenon at increasing depth, consistent with (though not a proof of) the bridge reaching `v` with unboundedly many certifying depths as required for `limsup S = +∞`.

**Note on exponent size**: the certifying `r` values found are often close to `1` (e.g. `r≈1.016`–`1.06`), not large squares. This is consistent with, not contrary to, `REPETITION_HEIGHT_CRITERION.md`: the unconditional threshold is `max(1, γ·log₂3) + θ·log₂3`, and `max(1,γ·log₂3)=1` whenever density `γ<1/log₂3≈0.631` — so at low density, `r` only slightly above `1` combined with low discrepancy can genuinely certify. This was **not assumed**; it is read off directly from the exact `S` values, which is the point of testing exact surplus rather than a fixed exponent cutoff.

## Scope and honest limits

- **Three slopes, not a general theorem.** This is computational evidence for specific instances, not a proof that every CS Rote sequence's derived `v` has `limsup_ℓ S(ℓ) = +∞`. The transfer lemma shows the *mechanism* (parity-dependent exponent inheritance, halved in the worst case) but does not by itself guarantee arbitrarily deep certification for an arbitrary slope — e.g. a slope whose Sturmian `u` has bounded initial-power exponent close to `2` and *unluckily* always lands on odd-weight roots could, in principle, fail to transfer (not observed in these three tests, but not ruled out in general).
- **Both directions tested only for `v_0=0`.** The complementary sequence (`v_0=1`, or `1−v`) is exactly the "complementary symmetric" partner; by the construction's symmetry (`S(1−v)=S(v)=u`), the same `u`-derived transfer lemma applies identically — not re-tested separately, but expected identical by direct substitution (`1⊕a = 1−a` for `a∈{0,1}`, so complementing `v` complements every `V`-block but leaves period/exponent structure, and hence `S`, unchanged).

## Verdict for this rung

**Rung placement: Rung C → B, upgraded, for the three tested slopes** (`PERIODICITY_LADDER.md` updated accordingly) — genuine, exact, growing-depth certification found; not yet a general theorem covering the whole CS Rote class, hence not blanket Rung B for the entire class. `FALSIFICATION_REPORT.md` C4 updated to reflect this partial, evidence-based (not proof-based) resolution.
