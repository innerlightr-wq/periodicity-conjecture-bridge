**ONE UNCOVERED TARGET, ONE PROOF OBLIGATION — AND ONE UNEXPECTED SURVIVOR FROM PHASES 1–9B**

# PHASE10_VERDICT.md

Isolated branch `phase10-critical-density`, cut from `phase9-unbounded-type`.
**State note:** the instruction expected HEAD `1c365b4` (Phase 9B); the actual HEAD was `67cbb9d`,
because a first Phase 10 pass had already been committed. This pass builds on it rather than
repeating it, and adds what that pass omitted: the **qualitative/quantitative split** (item 2) and
**explicit proofs** of the finite-scale bounds (item 4). Nothing pushed, nothing published, no
release rebuilt; `note_rev2.pdf` `8daf1979…` and both `~/Downloads` copies byte-identical.
The bridge repository has no `AGENTS.md`; the one in `collatz-symbolic-periodicity` governs that
repository only and was not written to.

## (a) What remains valid from Phases 1–9B

**Every proof, every script, every `data/` record.** Nothing is withdrawn as mathematics. Three
strands survive as contributions rather than as covered conclusions:

1. **The mechanism (C).** The abstract irrationality criterion; the discrepancy–height bound
   `c_W ≤ ℓ3^{⌈D⌉}max(2^ℓ,3^k)`; the repetition–height criterion and its exact inequality; the exact
   XOR transfer `L_v = L_u + 1`; the odd-branch density-`1/2` fact; the `g(γ)` unconditional
   threshold; the Phase 8 driver identity `ℓ_kE_k = q_{k−2}(m_{k−1}−1)` with its attainment routing;
   the Phase 9 weight law (W-y)/(W-x)/(W-int); the proved `O(log N)` interval discrepancy for
   bounded-type rotations.
2. **The corrections to the record.** BHZ §5 priority (Phase 8); the `q_1 = a_1+1` convention error;
   the refutation of the exceptional-orbit reduction; the refutation of the Thue–Morse
   structural-ceiling inference; the Phase 9B withdrawal of the `g(γ)` attribution. All stand.
3. **The quantitative content (Q) — the unexpected survivor.** T1 and T2 are *purely qualitative*:
   T1's proof is a limiting argument over `m → ∞` whose discarded-term count depends on the unknown
   `x`; T2's is an accumulation-point argument. **Neither bounds the height of a hypothetical
   rational value.** The bridge does: `H ≥ 2^{S_n}` with `S_n` explicit and unbounded — e.g. for
   Thue–Morse, `H ≥ 2^{510.7}` at `ℓ = 768`, a 154-digit floor, certified by the integer comparison
   `2^L > F`. **Caveat that keeps this honest:** the foundation paper already claims "the height
   floors" and "the independent effective Liouville proof" as its own novelty, for Sturmian words.
   So this is *new instances of an already-claimed method*, not a new method.

## (b) Which conclusions were already known

Every qualitative irrationality claim in Phases 2–9, without exception:

| class | density | already covered by |
|---|---|---|
| CS Rote — Phases 2, 4, 6, 8, 9 (quadratic → bounded type → every intercept → unbounded type) | exactly `1/2` | **T1** (refereed, 2004) |
| Thue–Morse — Phase 9 Cor. 4.1 | `1/2` | **T1** |
| 21 substitution fixed points — Phase 9 Cor. 4.2 | rational | **T1** (15), **T2** (4, preprint) |
| rotation coding at interval `1/3` — Phases 1–2 | `1/3` | **T1** |

All are reclassified as **independent proofs of covered conclusions**, with genuine **(Q)** content
attached. The coverage was found by **implication** — compute the density, apply T1/T2 — not by any
paper naming these classes. That is precisely what the repository's three prior-art passes, all of
which searched for the *mechanism*, could not find.

## (c) The candidate family, and why the exclusions do not reach it

> **`C(α, ρ)`**: `β := log₃2`; `α` a **quadratic irrational**; `ρ ∉ ℤα + ℤ`;
> ```
> s_n = 1   <=>   { n*alpha + rho }  in  [0, beta) .
> ```

| requirement | status |
|---|---|
| aperiodic | **PROVED** — a proper arc is not invariant under a non-trivial rotation |
| lower ones-density **exactly `β`** | **PROVED** — Weyl; the limit exists, so neither `< β` nor `> β`, and both T1 and T2 are strict |
| complexity not excluded by T3 | `p(n) = 2n`, so `liminf p(L)/L = 2 > 1.70951129…`. **Cited** (Rote, *J. Number Th.* **46** (1994) 196–213; Berstel–Vuillon, arXiv:math/0106217, since `β` transcendental and `α` algebraic give `β ∉ ℤα+ℤ`) and **verified exactly** at `n = 6, 12, 20` on 15 `(α,ρ)` pairs |
| not covered by T4 | `p(20) = 40 ≠ 21`; T4 is the complexity-`(n+1)` line |
| not a disguised covered word | it is the repository's **own** class with one parameter moved: CS Rote is this same coding at interval length `1/2`. Same complexity; only the density changes. No shift, finite modification or rationality-preserving transformation relates the two, because the density — the only thing T1/T2 read — differs |
| drift and discrepancy | **PROVED** (Lemmas D and E, `CRITICAL_DENSITY_TARGET.md` §4): `|k_N − Nβ| = O_A(log N)` uniformly in `ρ`, hence `k_ℓ log₂3 − ℓ = O_A(log ℓ)` and `D(W) = O_A(log ℓ)` |

Note the caution the instruction demanded: a complexity coefficient `≥ 1/log₂(3/2)` escapes T3 but
establishes nothing by itself. Novelty here rests on the **density being exactly `β`**, which is what
takes it outside T1 ∪ T2; complexity only keeps it off T3's region and T4's line.

**Repetition is not assumed.** The existence of the required initial powers is exactly the open
obligation below — it is not inferred from the rotation structure.

## (d) The smallest remaining proof obligation

Because `β·log₂3 = 1` exactly, the usual leading term `ℓ[r − max(1, γlog₂3)]` degenerates to
`ℓ(r−1)` and the requirement collapses onto the **overshoot**:

```
S  >=  (L - ell)  -  ( ceil(D(W)) + max(0, k_ell - ell*beta) ) * log2 3  -  log2 ell ,
```

with both correction terms `O_A(log ℓ)` by Lemmas D and E. Hence:

> **(L2)** For `s = s(α,ρ)` there are infinitely many `ℓ` with
> `lcp(s, (s[0:ℓ])^∞) − ℓ ≫ log ℓ`.

**(L2) ⟹ `Φ(s) ∉ ℚ`**, directly — no transfer, no weight parity, no Ostrowski machinery.
Geometrically, `L − ℓ` at `ℓ = q_k` is the first entry time of `({mα+ρ})` into a union of **two**
arcs of length `‖q_kα‖`; (L2) asks that this exceed `log q_k` infinitely often, against a generic
value of `≈ q_{k+1}/2`.

**Tested adversarially before any attempt at proof**, in certified rational brackets (every
membership test decided or raised): 5 slopes × 3 intercepts, `ℓ` at convergent denominators to
3927. With `ρ ∉ ℤα+ℤ` the ratio `(L−ℓ)/log₂ℓ` reached `5 267`, with per-slope minima `0.46`–`11.7`
and ratio `> 1` at 15/17, 9/9, 7/7, 5/5, 11/12, 17/17 of scales. Exact integer surplus positive at
45/62 triples; **every** failure is a `ρ = 0` row with `L − ℓ = 0`, which is why `ρ ∉ ℤα+ℤ` is part
of the definition rather than cosmetic.

## (e) Next highest-value action

**Prove (L2), for one explicit `ρ` first.** It is a pure inhomogeneous-Diophantine statement about
`α`, `ρ` and `β` jointly — three-distance combinatorics, no arithmetic input. Two sub-steps:

1. Fix `ρ` (say `1/7`) and let `k` vary: show the first entry time into
   `(−θ_k, 0) ∪ (β−θ_k, β)`, `θ_k = ‖q_kα‖`, cannot be `O(log q_k)` for *every* `k` unless `ρ` is
   simultaneously extremely well approximated by the orbits of `0` **and** of `β` — an explicitly
   describable, measure-zero condition. Excluding it for one `ρ` already yields a single named word
   in the uncovered region, with an effective height floor attached.
2. Only then aim for all `ρ ∉ ℤα+ℤ`.

**Do not** return to `(L1)` or to sharper odd-branch discrepancy control: both serve density-`1/2`
classes that T1 already covers qualitatively, and the `(Q)` content there is already recorded.

Repository corrections are prepared in `theorems/phase9b/CORRECTION_ADDENDUM.md` and
`theorems/phase9b/PROPOSED_STATUS_UPDATES.md` (both extended by this pass). Historical records are
preserved; nothing is rewritten. **No deposit, no publication, no rebuild** — the two corrections
owed on Revision 2 remain owed and still need author approval.

## Evidence classification

| status | items |
|---|---|
| **PROVED here** | aperiodicity, density `= β`, Lemmas D and E, the exact requirement, `(L2) ⟹ Φ(s)∉ℚ`, `β` transcendental, the coverage geometry, and that T1/T2 are qualitative (by reading both proofs) |
| **CITED** | T1 (refereed), T2 (preprint), T3 (Dubickas refereed + proved transport), T4; `p(n)=2n` (Rote 1994) |
| **PROVED EARLIER HERE** | the `O(log N)` interval discrepancy, now restated for `[0,β)` |
| **CERTIFIED FINITE CHECK** | `p(n)=2n` at `n ≤ 20`; drift and `D(W)` magnitudes; 62 exact-integer surplus evaluations; Thue–Morse height floors |
| **NUMERICAL EVIDENCE ONLY** | (L2) |
| **OPEN** | (L2) |
