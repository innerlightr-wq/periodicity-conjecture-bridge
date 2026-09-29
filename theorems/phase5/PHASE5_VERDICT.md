**THEOREM SURVIVES AFTER REPAIR**

# PHASE5_VERDICT.md

## 1. Is the BHZ word identification exact?

Yes. `BHZ_PRIMARY_SOURCE_AUDIT.md`: re-derived from BHZ's own `\S2.1` definitions (not secondary quotation), confirmed computationally (2000 terms, 3 slopes, exact arithmetic) and structurally (shared-orbit argument). `u=\omega(-\gamma)`, not `\omega(1-\gamma)` — disambiguated cleanly.

## 2. Does BHZ actually provide arbitrarily long usable witnesses?

Yes. `INITIAL_POWER_QUANTIFIER_AUDIT.md`: their Corollary 3.5 is a proven theorem constructively exhibiting, for each `k`, an actual growing-length prefix power with the claimed exponent — not merely an abstract limsup.

## 3. Is there a uniform positive exponent margin above `2` for each fixed quadratic slope?

Yes, `\delta(\gamma)=1/(A+1)`, `k`-independent, re-derived from scratch in `UNIFORM_MARGIN_AUDIT.md` (**PASS**).

## 4. Is the exact Rote transfer theorem correct?

Yes. `TRANSFER_REDERIVATION.md`, re-derived from `v_{n+1}=v_n\oplus u_n` alone; `scripts/phase5/independent_transfer_check.py`, **114,680** exhaustive cases, 0 failures, independently coded (not reusing Phase 2's script).

## 5. Is the `+1` depth correct?

Yes, re-derived and exhaustively re-verified (item 4).

## 6. Is the odd root exactly `V\bar V`?

Yes, as constructed — and `HALF_DENSITY_AUDIT.md` found it is **sometimes not primitive** (5 explicit small counterexamples), which does not threaten correctness (conservative, not invalid) and was confirmed absent from every actually-tested Phase 4 witness.

## 7. Is its density exactly `1/2` in the sense required by the height proof?

Yes, exactly (`|R|_1=\ell$ for every `\ell`, not asymptotic), and `HALF_DENSITY_HEIGHT_REDERIVATION.md` independently re-derives that this collapses the required threshold to `r>2` via the direct `4^\ell` vs `3^\ell` comparison, matching Phase 4's claim without consulting it during derivation.

## 8. Does possible period reduction matter?

No — checked explicitly (`HALF_DENSITY_AUDIT.md`): density, `c_R$'s validity (Proposition 4.1 has no primitivity hypothesis), and the depth identity are all unaffected.

## 9. Is discrepancy sublinear for the actual Rote roots?

Yes, `D(R)=O(\log|R|)`, re-derived as `D(R)\le2D(V)+\ell|\gamma_V-\tfrac12|` with both terms independently shown `O(\log\ell)` (`ROTE_DISCREPANCY_AUDIT.md`), numerically re-confirmed (`scripts/phase5/rote_discrepancy_independent.py`).

## 10. Does the height inequality genuinely reduce the odd-route threshold to `2`?

Yes, re-derived independently and directly (not by specializing the general formula) in `HALF_DENSITY_HEIGHT_REDERIVATION.md`.

## 11. Does surplus provably tend to infinity?

Yes, `S_k\ge\ell_k/(A+1)-O(\log\ell_k)\to+\infty`, fixed margin (item 3), unbounded root length (item 2).

## 12. Are both seeds covered?

Yes — with a **correction**: `HOSTILE_REFEREE_REPORT.md` found the original justification ("complementing uniformly complements `R`, `S` unaffected") is imprecise (`c_R$ is *not* complement-invariant, checked directly, 8/8 counterexamples); the actual reason the computed `S` is seed-invariant is that the scripts use the discrepancy-based `F_bound`, which depends on `R` only through `(\ell,k,D(R))`, and `D(V\bar V)=D(\bar VV)` exactly (checked, 15/15). **The conclusion (both seeds work) survives; the stated reason in `theorems/phase4`/Phase 5's own first-draft `TRANSFER_REDERIVATION.md` needed this repair.**

## 13. Are all shifts covered?

Yes, re-derived directly from source-paper Proposition 2.3 (`\Phi(\sigma v)=T(\Phi(v))`, `T$ bijective on `\mathbb Q\cap\mathbb Z_2`, re-derived from `T`'s explicit affine formulas) — `QUANTIFIER_AUDIT.md`.

## 14. Is intercept `0` exactly the current boundary?

Yes, and now **precisely located**: the specific failing ingredient is `\text{term2}(k)$'s `\omega(-\gamma)`-specific derivation from BHZ's general Corollary 3.5; the transfer and discrepancy machinery are intercept-agnostic (`QUANTIFIER_AUDIT.md`).

## 15. Did rational controls remain silent?

Yes on the genuine rational case (Control 1, bounded/negative surplus). **Control 2 required care**: a deliberately-constructed density-`1/2` *periodic* target gave numerically positive, growing `S`, but this is the abstract criterion's own explicitly-excluded degenerate case (`s=W_n^\infty`), confirmed by direct inspection, not a false positive of the density-`1/2` mechanism (`RATIONAL_CONTROLS.md`).

## 16. Did the bad parity-cycle example certify independently?

Yes — `scripts/phase5/bad_cycle_control.py`, independently coded, reproduces Phase 3/4's exact numbers (`S=5,55,365,2191,12852,75014`) at the same witnesses, confirming density `1/2` exactly at every one (assertion never failed).

## 17. Did random quadratic stress testing find any anomaly?

No — 25 random quadratic slopes (`scripts/phase5/random_quadratic_stress.py`), 0 flagged anomalies (no missing witnesses, no density mismatches, no seed asymmetry, no persistent non-positivity).

## 18. Is the final theorem correctly stated?

Yes, as stated in `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` — re-confirmed by this audit's independent re-derivation, with its own stated boundary (other intercepts) re-confirmed precisely, not merely repeated.

## 19. What, if anything, must be weakened?

**Nothing in the headline theorem's statement.** One repair to a *justification* (item 12) — the seed-independence conclusion is correct, but the reason given in the Phase 4/5 write-up (uniform complementation of `c_R`) is false as literally stated; the true reason (via `F_bound`'s discrepancy-only dependence) is weaker in scope of claim but sufficient in consequence. This is a proof-presentation fix, not a theorem weakening.

## 20. Final status

```
THEOREM SURVIVES ADVERSARIAL AUDIT AFTER REPAIR
```

**Repair required**: correct the stated justification for seed-independence (item 12 / `HOSTILE_REFEREE_REPORT.md`'s finding) — from "`c_R` is complement-invariant" (false) to "the discrepancy-based `F_bound` used in every verification script depends on `R` only through `(\ell,k,D(R))`, and `D(V\bar V)=D(\bar VV)` exactly" (true, re-checked). **No other repair needed.** The headline theorem of `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` stands, independently re-derived end to end in this phase.
