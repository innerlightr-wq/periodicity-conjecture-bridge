# SOURCE_OF_TRUTH.md

Every statement below was extracted from the actual, frozen repository files at HEAD `a4ac46aebf17fb2ce14cea50f5ce60a58704da15` (see `PRESERVATION_RECORD.md` for checksums). Quotes are verbatim; none reconstructed from conversation memory. Classification labels follow the scheme requested for the technical note:

`KNOWN/CITED` · `PROVED IN FOUNDATION PAPER` · `PROVED IN BRIDGE PROJECT` · `COMPUTATIONALLY VERIFIED` · `COUNTEREXAMPLE` · `REJECTED HYPOTHESIS` · `OPEN` · `EXPLORATORY ONLY`

---

### A. Bernstein–Lagarias conjugacy/isometry facts

**A1 — the conjugacy map itself.** `KNOWN/CITED` (classical, external). The map Φ sending a 0/1 (parity) sequence to a 2-adic integer via the 3x+1 conjugacy relation is the construction of Bernstein & Lagarias, *The 3x+1 conjugacy map*, Trans. AMS (1996) — cited by name, not re-derived or re-verified in this repository; standard background.

**A2 — Φ is a 2-adic isometry.** `PROVED IN FOUNDATION PAPER` (self-citation; see note below). `THEOREM_STATUS.md`: "`Φ` is a 2-adic isometry (`v₂(Φ(a)−Φ(b))=lcp(a,b)`) | KNOWN (source paper, Prop. 2.2)." This is the load-bearing fact the entire bridge exploits: agreement of two sequences up to length `L` forces their images to agree 2-adically to depth `L`.

**Author-identity note.** `reference/sturmian-conjugacy-map-irrational-2adic-integer.pdf` — *"The 3x + 1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-Adic Integer,"* Elias De Jesús, unpublished, September 2026 (`CITATION.cff` lines 21–28, `NOTICE`). This is the **same author's own prior/companion unpublished paper**, not third-party literature. The technical note must present it as such (a self-citation to a companion manuscript), not as an external source.

### B. Periodic-value formula

`PROVED IN FOUNDATION PAPER`. `THEOREM_STATUS.md`: "Periodic-value formula `Φ(W^∞)=c_W/(2^ℓ−3^k)` | KNOWN (source paper, Prop. 4.1)." `c_W` is an explicit integer functional of the finite word `W` (defined in the source paper); `ℓ=|W|`, `k=|W|_1`.

### C. Abstract periodic-approximation irrationality criterion

`PROVED IN BRIDGE PROJECT`. Two forms exist in the repo; the note should use the final (Phase 2) form and cite Phase 1 as its origin.

- Phase 1 origin (`theorems/phase1/ABSTRACT_BRIDGE_THEOREM.md`, lines 42–48): defines `S_n = S_s(W_n) := L_n − log₂F(W_n)` and states: *"Theorem (abstract periodic-approximation bridge). Let `s ∈ {0,1}ℕ` and `(W_n)` finite words with `s ≠ W_n^∞` for all `n`. If `limsup_n S_s(W_n) = +∞`, then `Φ(s) ∉ Q`."*
- Canonical final form (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, lines 54–61): *"THEOREM (abstract 2-adic periodic-approximation criterion). Let `s∈{0,1}^ℕ` and `(W_n)_{n≥1}` finite binary words with `s≠W_n^∞` for all `n`. Define `S_s(W):=lcp(s,W^∞) - log₂(|2^{|W|}-3^{|W|_1}|+c_W)`. If `limsup_{n→∞} S_s(W_n) = +∞`, then `Φ(s)∉ℚ`."* Repo's own gloss: *"This is the exact foundation §§5–7 build on, and it contains no Sturmian or Rote terminology."*

### D. Surplus formulation

`PROVED IN BRIDGE PROJECT` (definition + dual necessity theorem). Canonical definition (`theorems/phase2/SURPLUS_THEOREM.md`, confirming `theorems/phase1/SURPLUS_INVARIANT.md`): `S_s(W) := lcp(s,W^∞) - log_2(|δ_W|+c_W)`, `δ_W = 2^ℓ-3^k` — described as *"the proof-native quantity, not a convenient after-the-fact packaging."*

Dual (necessity) theorem: *"THEOREM (uniform surplus bound under rationality). If `Φ(s)=u/v∈ℚ` (lowest terms, height `H=max(|u|,v)`), then for every finite word `W` with `s≠W^∞`, `S_s(W) ≤ log₂ H`."* — `PROVED`; converse direction explicitly flagged open. Also proves primitive roots are optimal: power roots strictly decrease surplus (`S_s(W^m) → −∞`).

### E. Discrepancy-height theorem

`PROVED IN BRIDGE PROJECT`, `COMPUTATIONALLY VERIFIED` for `ℓ≤16`. `theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`: discrepancy `D(W) = max_{0≤i≤ℓ} |k_i(W) − ik/ℓ|` (lines 5–7); theorem: *"For every finite word `W` with `ℓ = |W|`, `k` ones, `D = D(W)`: `c_W ≤ ℓ · 3^{⌈D⌉} · max(2^ℓ, 3^k)`"* (lines 11–14). Hard combinatorial cap: `D(W) ≤ γ(1−γ)ℓ` (line 46). Sublinear-discrepancy version (lines 64–68): if `s` begins in `W^r` with `ℓ→∞`, `γ=k/ℓ→γ_∞`, `D(W)=o(ℓ)`, and `r > max(1, γ_∞ log₂3)` strictly, then surplus `→+∞`, so `Φ(s)∉ℚ`.

### F. Repetition-surplus criterion

`PROVED IN BRIDGE PROJECT`. `theorems/phase1/REPETITION_HEIGHT_CRITERION.md`: uniform criterion (lines 21–25) needs `r > sup_{γ∈(0,1)} max(1,γlog₂3) = log₂3`. Sharpest unconditional form (lines 48–52): *"Theorem (squares alone suffice, unconditionally). If `s` begins in arbitrarily long initial squares `W_nW_n` — with no hypothesis whatsoever on the discrepancy, balance, or internal arrangement of the roots `W_n` — then `Φ(s) ∉ Q`."* Numeric margin: `r=2 > log₂3=1.58496...`, margin `0.41503...`.

### G. Square + sublinear-discrepancy corollary

`PROVED IN BRIDGE PROJECT`. `theorems/phase2/SQUARE_DISCREPANCY_COROLLARY.md`, line 5: *"COROLLARY S. If an aperiodic binary word `s` begins in infinitely many squares `W_nW_n` with `|W_n|=ℓ_n→∞` and `D(W_n)=o(ℓ_n)`, then `Φ(s)∉ℚ`."* Described as the direct generalization, beyond Sturmian, of the source paper's Theorem 10.1.

### H. Transported Dubickas counting threshold

`PROVED IN FOUNDATION PAPER` (source paper transports an external classical theorem). `THEOREM_STATUS.md`: "`p(n)<1.70951...n`, not eventually periodic ⟹ `Φ∉ℚ` | KNOWN (source paper, Cor. 9.3, Dubickas 2009 transported)." Exact constant, confirmed independently (`theorems/phase1/FULL_PERIODICITY_GAP.md`, line 11): the route "covers every word with `liminf_L p_s(L)/L < 1/log₂(3/2) = 1.70951...`"

### I. Sturmian foundation theorem

`PROVED IN FOUNDATION PAPER`. `THEOREM_STATUS.md`: "Sturmian words have arbitrarily long initial squares | KNOWN (source paper, Thm 10.2, cites ADQZ 2001)"; "Sturmian, `p(n)=n+1` ⟹ `Φ∉ℚ` | KNOWN (source paper, Thm 10.1)."

### J. Exact CS-Rote XOR transfer

`PROVED IN BRIDGE PROJECT`. `theorems/phase2/ROTE_TRANSFER_THEOREM.md`, line 7: *"`v` is CS Rote ⟺ `u=S(v)` is Sturmian, `u_i=v_i⊕v_{i+1}` for all `i≥0`."* Inverse map (line 9): `v_{n+1} = v_n ⊕ u_n`. Noted intercept-agnostic (line 49): applies verbatim regardless of intercept.

### K. Exact +1 depth

`PROVED IN BRIDGE PROJECT`, independently re-derived `COMPUTATIONALLY VERIFIED`. Same file, lines 17–21: *"THEOREM (exact transfer, with a +1 bonus). Let `L_v := lcp(v,target^∞)`, target=`V` (even case) or `R=V V̄` (odd case). Then `L_v = L + 1`, exactly, not merely `≥L` or `≈L`."* Re-derived independently in Phase 5 (`theorems/phase5/TRANSFER_REDERIVATION.md`), cross-checked exhaustively over 114,680 cases, 0 failures.

### L. Odd-root `V·V̄` mechanism

`PROVED IN BRIDGE PROJECT` — the key structural breakthrough. `theorems/phase4/REQUIRED_EXPONENT.md`, lines 17–19: *"Claim. For the odd-weight case, `R=V\bar V` has density exactly `1/2`, for every `V`, unconditionally. Proof. `|R|_1 = |V|_1 + |\bar V|_1 = |V|_1 + (|V|-|V|_1) = |V| = ℓ`. `|R|=2ℓ`. Density `=ℓ/(2ℓ)=1/2` exactly."*

### M. Density exactly 1/2

`PROVED IN BRIDGE PROJECT` — same result as L (the density claim *is* the mechanism); listed separately per the note's outline. Consequence (same file, lines 33–40): required exponent collapses to `r_required(γ) = 2` uniformly for both even- and odd-weight routes — correcting the earlier (Phase 3) working estimate of `2log₂3≈3.17`.

### N. Actual-root discrepancy theorem

`PROVED IN BRIDGE PROJECT` for bounded-partial-quotient slopes; `OPEN` beyond that. `theorems/phase2/ROTE_ROOT_DISCREPANCY.md`: *"PROVED — for every Sturmian slope with bounded partial quotients... `D(V_n) = O(log ℓ_n) = o(ℓ_n)`. OPEN — precise missing lemma for unbounded-partial-quotient slopes."* This bound is proved directly for `V` (even branch). For the odd branch's actual root `R=V\bar V`, the relevant discrepancy control was established indirectly, as part of the Phase 5 seed-independence repair (`theorems/phase5/HOSTILE_REFEREE_REPORT.md`): the surplus bound `F_bound(W)` depends on the root only through `(ℓ,k,D(root))`, and `D(V\bar V)=D(\bar VV)` exactly, checked 15/15. No separate closed-form discrepancy theorem for `R` beyond `V`'s bound is claimed in the repo; the note should present it exactly this way — proved for `V`, extended in effect to `R` via the F_bound reduction, not via an independently stated `D(R)=O(log)` theorem.

### O. Quadratic CS-Rote theorem and its generalization

`PROVED IN BRIDGE PROJECT`. `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`, lines 7–10 (verbatim): *"THEOREM. Let `γ∈(0,1)` be any quadratic irrational, `A` the largest partial quotient in its eventually-periodic continued fraction, `u` its lower mechanical (intercept-0) Sturmian word. Let `v` be either complementary-symmetric Rote sequence with `S(v)=u` (seed `v_0∈{0,1}`), or any shift `σ^j(v)` of such a `v`. Then `Φ(v) not in Q`."* Classification: *"PROVED — PRECISE SUBCLASS... NOT proved: CS Rote sequences associated with other intercepts of the same slope γ."* Superseded (without weakening any quantifier) by item P.

### P. Final bounded-type intercept-0 theorem

`PROVED IN BRIDGE PROJECT` — the repository's headline result. `theorems/phase6/BOUNDED_TYPE_THEOREM.md`, lines 7–10 (verbatim): *"THEOREM. Let `γ∈(0,1)` be irrational with bounded partial quotients (`A:=sup_n a_n<∞`). Let `u` be the intercept-0 lower mechanical word of `γ`. Let `v` be either complementary symmetric Rote sequence with `S(v)=u` (either seed), or any shift `σ^j(v)`. Then `Φ(v) not in Q`."* Status block (lines 32–37): *"PROVED — PRECISE SUBCLASS ... Supersedes `theorems/phase4/QUADRATIC_CS_ROTE_THEOREM.md`... without weakening any of its quantifiers. Boundary unchanged: other intercepts of the same slope remain uncovered."*

### Q. Arbitrary-intercept obstruction

`PARTIALLY PROVED` (the obstruction itself is fully mapped and classified) / `OPEN` (the extension theorem). `theorems/phase7/PHASE7_VERDICT.md`, line 1: *"OBSTRUCTION CLASSIFIED — ONE LEMMA REMAINS."* Closing paragraph (lines 29–33): *"The obstruction (loss of the clean `ω(-γ)`-specific BHZ closed form) is precisely located, its downstream consequences fully traced, and its practical severity found to be much smaller than initially suspected — no computational evidence of failure anywhere, and a structural argument (the exceptional-orbit reduction) narrows the genuinely open cases to a countable, already-mostly-handled set plus one unproved general margin lemma."*

### R. BHZ/Ostrowski remaining lemma

`OPEN`, classified `CONJECTURAL`. `theorems/phase7/PHASE7_VERDICT.md`, lines 17–19 (verbatim): *"For any admissible Ostrowski digit sequence `(c_k)` of a bounded-partial-quotient slope `γ` (`A=sup a_n<∞`), `limsup_k max(x'(k),y(k))>2`, with a margin depending only on `A`."* Status (`theorems/phase7/INTERCEPT_SUFFICIENT_CONDITION.md`, lines 21–25): *"CONJECTURAL. Strong, broad computational evidence (36/36 configurations, including the identified worst-case family, across a range of A). No general algebraic proof attempted to completion. This is the exact remaining lemma for a full all-intercepts theorem."*

### S. Symmetry/resonance exploratory probe status

`EXPLORATORY ONLY` — must never be presented as a result in the Abstract or as a proved/refuted claim. Two independent lines of work converge on the same conclusion:

- **Phase 7's own drift-coordinate probe** (`theorems/phase7/DRIFT_COORDINATES.md`, `DRIFT_VS_DIGITS.md`): `R(W):=ℓ-k·log₂3` is a reparameterization, not a new invariant — *"No new information is encoded by `R` that `γ` did not already carry"*; *"Resonance did not materially help or hurt in any tested case."*
- **The later (uncommitted) `symmetry_tradeoff_probe.py` experiment**, diagnosed and run in this same consolidation session: Experiment 1 (`n=74`) gave `A(W)` vs `S(W)` `r≈0.208` and `A(W)` vs `L/ell` `r≈-0.125` — both below the script's own 0.3 "worth pursuing" threshold. Experiment 2, after fixing a runtime bug (word-length blowup in `build_witness_word`, replaced by an exactly cross-checked transfer-matrix computation, 150/150 exact agreement with brute force), gave `n=724`, `A(W)` vs `N_sym` `r≈-0.0058`, log-log `r≈-0.0319` — but 596/724 points (82%) had `A(W)` pinned to exactly `1.0` by the probe's own float-underflow clamp, an artifact, not a genuine near-resonance measurement. **Verdict: INCONCLUSIVE**, both by the script's own criterion and because the measurement does not resolve the near-resonance regime where any real signal would have to live.

---

## Cross-cutting facts used throughout the note (not individually lettered above)

- **Weight-parity automaton and dichotomy** (`theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`): 8-state automaton, exactly one bad all-odd cycle `(A,0)↔(C,1)`; counterexample `γ=[0;1,1,1,\overline2]` has all-odd weight parity forever, disproving the universal claim; dichotomy proved for odd-tail case, strongly evidenced (not fully proved in general) for all-even-tail case.
- **Structural ceiling on the entire program** (`theorems/phase1/FULL_PERIODICITY_GAP.md`, Q4): *"the Thue–Morse word has no square at all below half-length 2048... An adversarially constructed aperiodic word can have no useful initial power at all, making this bridge... inapplicable to it by construction — this is not a gap in the method, it is a structural limitation."* This is the load-bearing fact behind "this note does not settle the full conjecture."
- **BHZ formula and citation**: Berthé, V., Holton, C., Zamboni, L.Q., *Initial powers of Sturmian sequences*, Acta Arithmetica **122** (2006), 315–347. Exact Corollary 3.5 form (intercept-0 case) and general (arbitrary-intercept) `x'(k), y(k)` form both quoted from `theorems/phase4/INITIAL_EXPONENT_FORMULA.md` and `theorems/phase7/BHZ_GENERAL_INTERCEPT_MAP.md` respectively.

## Self-correction items (Section 10 of the note)

- **A. Universal even-weight witness hypothesis — REJECTED HYPOTHESIS.** Counterexample `γ=[0;1,1,1,\overline2]`, all-odd weight parity forever (`theorems/phase3/WEIGHT_PARITY_CLASSIFICATION.md`, line 13). Odd-weight transfer route still succeeds.
- **B. Silver-ratio extremality — REJECTED HYPOTHESIS, COUNTEREXAMPLE.** `γ=[0;1,4,1,5,1,\overline{6,2}]` has `ice(u)≈3.1547 < 2+√2≈3.4142` (`theorems/phase4/SILVER_EXTREMALITY.md`, lines 15–19), yet still certifies since the true threshold is `r>2`, not `2+√2` (`SILVER_CONSTANT_AUDIT.md`).
- **C. Seed-independence via complement-invariance of `c_W` — REJECTED HYPOTHESIS, repaired.** `theorems/phase5/HOSTILE_REFEREE_REPORT.md`, lines 7–9: *"does `c_W` satisfy `c_{V\bar V}=c_{\bar VV}`? No — direct test, 8/8 random odd-weight `V`, `c_{V\bar V}≠c_{\bar VV}`, often by an order of magnitude."* Repaired reason: `D(V\bar V)=D(\bar VV)` exactly (15/15), and `F_bound` depends on the root only through `(ℓ,k,D)`.
- **D. Phase 6 small-k boundary correction.** `theorems/phase6/ARROW_BY_ARROW_RECONSTRUCTION.md`, line 9: `term2(2)` exactly equals `2+1/(A+1)` (`=7/3`) in the Fibonacci-coded non-periodic control, the only non-strict instance out of 232 checks — never a violation, never recurring for larger `k`; does not weaken the theorem since only infinitely many *growing* witnesses are required.

## Open problems (Section 19 of the note) — repo's own framing

`THEOREM_STATUS.md`, "Open, precisely stated": (1) CS Rote sequences at other intercepts of the same slope; (2) unbounded-partial-quotient slopes, "genuinely out of reach of the discrepancy mechanism used"; (3) the rotation-coding repetition-existence gap (`theorems/phase2/ROTATION_EXAMPLE_THEOREM.md`); (4) the "next frontier" beyond `p(n)=2n` (`LADDER.md`), "deliberately not started."
