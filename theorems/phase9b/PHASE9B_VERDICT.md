**PROOF CORRECT, NOVELTY FALSE — AND THE SUBSUMPTION REACHES THE WHOLE CS ROTE LADDER**

# PHASE9B_VERDICT.md

Branch `phase9-unbounded-type`, audited at HEAD `5fd7e0f`. Nothing pushed, nothing rebuilt, no
release touched (`note_rev2.pdf` `8daf1979…`, `correction_notice.pdf` `0c93457c…`, `note.pdf`
`b7054cee…`, and both `~/Downloads` copies, all byte-identical).

## 1. Is the Phase 9 Thue–Morse proof correct? **Yes.**

Reconstructed from definitions, with `Φ`'s periodic-value formula re-derived from the defining
series and checked in `ℤ/2^400`. `lcp(t, W_0^∞) = 40` at `|W_0| = 24` (two independent checks);
propagation `lcp(μx,μy) = 2 lcp(x,y)` proved; `|W_m| = 24·2^m`, `lcp = 40·2^m`, density `1/2`,
`D(W_m) = 1/2` — the last **proved** via `|Σ_{n<N}(−1)^{t_n}| ≤ 1`. Asymptotic
`(2/3)ℓ − log₂(1+3ℓ) ≤ S ≤ (2/3)ℓ + 0.05` proved and asserted, not fitted. Details:
`THUE_MORSE_INDEPENDENT_PROOF.md`.

## 2. Was Phase 9's new threshold needed? **No — that attribution is withdrawn.**

`theorems/phase1/REPETITION_HEIGHT_CRITERION.md`'s **exact** inequality has threshold
`max(1, γlog₂3)`, which at `γ = 1/2` is **`1`**. With `r = 5/3` the margin is `2/3`, and `D = 1/2`
is bounded, so the pre-existing criterion proves the result outright. Phase 9 attributed the
conclusion to its own `g(γ) = 1.396241`; that is wrong — `g(γ)` is the threshold for the case where
**nothing** is known about `D`, and Thue–Morse is not that case. The `g(γ)` theorem survives as a
modest refinement of Phase 1's *unconditional* squares theorem and is audited separately; nothing
else depends on it.

## 3. Is the result new? **No. There is an explicit prior theorem.**

> **Monks–Yazinski, Discrete Math. 275 (2004), Theorem 2.7(b).** For `x ∈ ℚ_odd` with divergent
> orbit, `ln2/ln3 ≤ liminf_n κ_n(x)/n`.

Combined with "`v` eventually periodic `⟺` the orbit of `Φ(v)` is eventually cyclic", this gives:
**`v` aperiodic and `liminf k_n(v)/n < β` `⟹` `Φ(v) ∉ ℚ`**, `β = ln2/ln3 = 0.63093`. Thue–Morse is
aperiodic with density `1/2 < β`. Done.

**That deduction is written out verbatim in this programme's own foundation paper**, §8 "What is
known", which also records that the above-`β` half is 2021 (arXiv:2101.12747) Theorem 1
— a preprint — and that "outside the critical density the conclusion for that family was already
available". Sources read first-hand. Details and the four-way classification:
`THUE_MORSE_LITERATURE_AUDIT.md`.

## 4. The subsumption is much wider than Thue–Morse

**Every CS Rote sequence has ones-density exactly `1/2`**, for every irrational slope and every
intercept: `v_n = v_0 ⊕ (k_n(u) mod 2)` with `k_n(u) = ⌊nγ+ρ⌋ − ⌊ρ⌋`, so `v_n = 1` iff `{(nγ+ρ)/2}`
lies in a fixed half-length interval, and `γ/2` is irrational. Since `1/2 < β`, Monks–Yazinski 2.7(b)
applies **directly**. Therefore the following are all consequences of a 2004 refereed theorem:

| result | class | density |
|---|---|---|
| `theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md` | CS Rote, 5 quadratic slopes | `1/2` |
| `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md` | CS Rote, quadratic slopes | `1/2` |
| `theorems/phase6/BOUNDED_TYPE_THEOREM.md` | CS Rote, bounded type, intercept `0` | `1/2` |
| Phase 8 Theorem 2 | CS Rote, bounded type, **every** intercept | `1/2` |
| Phase 9 Theorem 3 | CS Rote, **unbounded** type, parity form | `1/2` |
| Phase 9 Corollary 4.1 | Thue–Morse | `1/2` |
| Phase 9 Corollary 4.2 | 21 substitution fixed points | rational (15 below `β`, 4 above, none at `β`) |

No proof in this repository is *false*; the **novelty claims** are. The repository's own prior-art
passes searched only for the *mechanism*, never asking whether the *conclusion* was already
available by another route — even though both halves of the fact were already recorded here
(`theorems/phase1/FALSIFICATION_REPORT.md` cites Monks–Yazinski; `docs/EOC_HANDOFF_CLOSED.md`
records CS Rote one-density `= 1/2` against `β = 0.63093`).

## 5. Substitution sweep scope

"All 21 aperiodic fixed points" means: binary alphabet only; `k = 2` and `k = 3` only;
`σ(0)`-prolongable only (no `0↔1` exchange, no de-duplication); aperiodicity a **finite test**, not a
proof; and the load-bearing `D(W_m) = o(|W_m|)` bound **quoted without reference or per-row check**.
It is not a statement about automatic or morphic words, and Phase 9's suggestion to "sweep the whole
`k`-automatic family" was over-stated. Full accounting: `SUBSTITUTION_SWEEP_SCOPE.md`, which also
shows that **no primitive substitutive word can ever sit at density `β`**: substitution letter
frequencies are algebraic (Perron eigenvector of an integer matrix) while `β = log₃2` is
transcendental by Gelfond–Schneider.

## 6. Strongest justified theorem, and its attribution

> **For every aperiodic parity word `v` with `liminf_n k_n(v)/n ≠ β`, `Φ(v) ∉ ℚ`.**
> Below `β`: **Monks–Yazinski (2004), Theorem 2.7(b)** — refereed.
> Above `β`: **arXiv:2101.12747 (2021), Theorem 1** — arXiv preprint.

Everything this repository has proved about CS Rote sequences, Thue–Morse and uniform substitution
fixed points is a corollary. This repository's own contribution, stated honestly, is:

- an **independent second proof** of those cases by a genuinely different (2-adic depth-versus-height)
  mechanism, which does not use the density at all;
- exact structural results about that mechanism — the driver identity `ℓ_kE_k = q_{k−2}(m_{k−1}−1)`,
  the attainment routing, the weight law (W-y)/(W-x)/(W-int), the `g(γ)` unconditional threshold;
- corrections to the record (BHZ §5 priority, the `q_1` convention, the exceptional-orbit refutation,
  the Thue–Morse ceiling refutation) which stand regardless.

## 7. Remaining proof gap

None in the Thue–Morse proof. The gaps that remain are all in the *mechanism*, not the conclusions:
lemma **(L1)** (general-intercept intermediate-root prefix power), the odd-branch discrepancy
estimate beyond `(H)`, and the unverified `D = o(|W|)` quote in Corollary 4.2. **All three are now
of reduced value**, because the conclusions they would secure are already known.

## 8. Should the next task be L1 or sharper odd-branch discrepancy control? **Neither.**

Both serve classes at density `1/2`, which Monks–Yazinski already covers. Pursuing either would buy
a third proof of a known result. The only mathematically live target is the density the dichotomy
misses:

> **Aperiodic words with lower ones-density exactly `β = ln2/ln3`, and complexity above `n+1`.**

That is the single uncovered case, the foundation paper's own theorem is the only thing there
(Sturmian, complexity `n+1`), and it is exactly where the repository's ladder never went — every
rung sat at density `1/2`. Concretely, in order:

1. **Restate the ladder by density, not by complexity.** The complexity axis was the wrong
   coordinate: it is what made `2n` look like a frontier when the density dichotomy had already
   crossed it. `LADDER.md` and `THEOREM_STATUS.md` need this before any new work.
2. **Construct a `p(n) = 2n` class at density exactly `β`** — e.g. a Rote-type or rotation-coding
   word whose one-density is `β` rather than `1/2` — and test whether the bridge reaches it. This is
   the first genuinely open target the machinery could claim.
3. **Only then** revisit `(L1)` or the odd-branch estimate, and only if the `β` class needs them.

Note the cross-programme consistency check: `docs/EOC_HANDOFF_CLOSED.md` already established that the
EOC divergence sector requires density `≥ β` and that CS Rote is vacuous there *for exactly this
reason*. The same fact that closes that handoff is the fact that subsumes the ladder.

## 9. Corrections prepared, not applied

`CORRECTION_ADDENDUM.md` (concise, for the record) and `PROPOSED_STATUS_UPDATES.md` (exact
replacement text for `LADDER.md`, `THEOREM_STATUS.md`, `README.md`, `PRIOR_ART.md`, and Revision 2
of the deposited note). **No status file was rewritten, no PDF rebuilt, nothing published** — per
the Phase 9B instruction to hold until the theorem statements are settled. The deposited Revision 2
now owes **two** corrections: the Thue–Morse scope claim (from Phase 9) and the novelty framing of
the CS Rote ladder (from this audit). Both need author approval.
