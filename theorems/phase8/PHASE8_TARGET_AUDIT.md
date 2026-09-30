**TARGET AUDIT — SIX SOURCE DISCREPANCIES FOUND, ONE PHASE-7 CLAIM REFUTED, TARGET (b) FOUND ALREADY PUBLISHED**

# PHASE8_TARGET_AUDIT.md

Audit of the exact general-intercept target *before* attempting to prove it, against the
Berthé–Holton–Zamboni primary source read first-hand.

## 0. Source of truth

| repository | branch | HEAD | dirty | notes |
|---|---|---|---|---|
| `innerlightr-wq/periodicity-conjecture-bridge` | `main` | `edb9ed4` "Document EOC handoff closure and cross-program limits" | clean | no `AGENTS.md` present |
| `innerlightr-wq/collatz-symbolic-periodicity` | `main` | `38fb58f` "Dubickas transfer written up; …" | clean | `AGENTS.md` read and obeyed; also has `audit/literature-first-hand-2026-09` |

Nothing in either checkout is newer than the attached papers. Phase 8 works in the isolated
worktree `phase8-general-intercept` cut from `edb9ed4`; no existing file is modified, nothing
is pushed, and no deposited paper is touched. `collatz-symbolic-periodicity` is **not** written
to (its `AGENTS.md` rules 1–7 confine Phase 8 to the bridge repository; in particular the
third-party BHZ PDF is cached only under the session scratchpad, never committed).

All seven Phase-7 filenames named in the task resolve verbatim under `theorems/phase7/`.

## 1. The exact target, reconstructed

`Conjecture 12.1` lives in the **deposited** technical note (Zenodo
[10.5281/zenodo.23045141](https://doi.org/10.5281/zenodo.23045141), §12), and verbatim in
`theorems/phase7/INTERCEPT_SUFFICIENT_CONDITION.md` and `theorems/phase7/PHASE7_VERDICT.md`:

> **Conjecture 12.1 (The one remaining lemma).** For any admissible Ostrowski digit sequence
> `(c_k)` of a bounded-partial-quotient slope `γ` (`A = sup_n a_n < ∞`),
> `limsup_k max(x'(k), y(k)) > 2`, with a margin depending only on `A`.

This is statement **(b)** of the task's trichotomy. It is classified `CONJECTURAL` in the
repository and stated as not proved "here or anywhere in the underlying record" in the note.

## 2. Translation from BHZ, checked directly against the primary source

Primary source re-fetched first-hand: Berthé, Holton, Zamboni, *Initial powers of Sturmian
sequences*, Acta Arith. **122** (2006) 315–347, `https://www.irif.fr/~berthe/Articles/sturm15.pdf`.
Six discrepancies, in decreasing severity.

### F1. **The `q_1` convention is wrong in the repository code.** (real defect, now diagnosed)

BHZ Prop. 2.7 (p. 9) fixes

```
alpha = [0; a_1 + 1, a_2, a_3, ...] ,   p_0=0, q_0=1 ,  p_1=1, q_1 = a_1 + 1 ,
q_k = a_k q_{k-1} + q_{k-2}  (k >= 2)
```

— the BHZ *digit* `a_1` is **one less** than the first partial quotient of `α`, while `(q_k)`
are the ordinary convergent denominators of `α`. `scripts/phase7/bhz_general_witness.py::convergents()`
sets `q_1 = a_1`, i.e. it computes the denominators of `[0;a_1,a_2,…]`. `theorems/phase7/BHZ_GENERAL_INTERCEPT_MAP.md`
records only "`q_0=1`, `q_{-1}=0`" and "`(a_k)` = partial quotients of the slope", so the shift
is absent from the written record as well.

*Consequence.* The `limsup` values are unaffected (a single shifted digit cannot change a
`limsup`), which is why Phase 4–7's `ice` numbers (`2.618…`, `3.414…`) are right. But every
**root length** is wrong. This is the complete explanation of the self-correction disclosed in
`theorems/phase7/PHASE7_VERDICT.md` ("does not reproduce the conjectured root-length formula
`q_k − c_k q_{k-1}`, checked, mismatched at every tested `k`, not close"). Under BHZ's own
convention the formula reproduces **exactly**: `scripts/phase8/phase8_literal_prefix.py`
verifies `562` attained initial powers against literal longest common prefixes with **0**
failures, and the same witnesses fail under the `q_1 = a_1` convention.
**The formula was never wrong; the convergents were.**

### F2. Admissibility — correct, verbatim

BHZ p. 2 and Prop. 2.7 eq. (1): `a_k ≥ c_k ≥ 0` for all `k`; `a_k ≥ 1` for `k ≥ 2`; and
**if `c_k = a_k` then `c_{k-1} = 0`**. The repository's statement matches character for
character (including the direction of the implication — `c_{k-1}`, not `c_{k+1}`). BHZ also
give the equivalent global form `K_α = {(c_k) : c_1q_0 + ⋯ + c_kq_{k-1} ≤ q_k − 1}`, which the
repository does not record and which is useful as an independent admissibility check.

### F3. **`y(k)` is an attained prefix power only when `0 < c_k < a_k`.** (real omission)

BHZ Prop. 3.3 gives two formulas for the largest prefix power `r`, according to whether
`m = s_k − 1` or `m = s_k − c_k − 1`, and the second case carries the standing hypothesis
`0 < c_k < a_k`; the converse half of Prop. 3.3 likewise says "for each `k` **such that
`0 < c_k < a_k`**". Corollary 3.5 then writes `ice(ω) = max(limsup_k x(k), limsup_{k, 0<c_k<a_k} y(k))`
and only *afterwards* upgrades this to `limsup_k max(x(k),y(k))` using three observations:

```
c_k = a_k                      =>  y(k) = x(k-2)
c_k = 0 and c_{k+1} = a_{k+1}  =>  y(k) < y(k+1) = x(k-1)
c_k = 0 and c_{k+1} < a_{k+1}  =>  y(k) <= x(k)
```

`theorems/phase7/BHZ_GENERAL_INTERCEPT_MAP.md` quotes the *upgraded* form and states
"These are real, growing-length, actually-occurring initial powers, for any admissible `(c_k)`"
without the `0 < c_k < a_k` restriction or the three observations. For computing a `limsup`
that is harmless; for a proof that must hand the bridge an **attained** root it is not, because
the branch of the argument that is tightest at `A = 1` is exactly `d_k = 0`, i.e. `c_k = a_k`,
where `y(k)` is *not* directly attained. Phase 8's proof therefore routes every case through an
attained witness explicitly. All three observations are re-verified exactly
(`scripts/phase8/phase8_identities.py`: 3915 + 3911 + 6874 verified instances).

### F4. `x` versus `x'` — conservative, no defect

BHZ §4.1: `x(k) = 1_{a_{k+2}=c_{k+2}} + x'(k)`, and `limsup max(x,y) = limsup max(x',y)`. The
repository uses `x'`, dropping the indicator. Since `x(k) ≥ x'(k)`, every lower bound proved
with `x'` is valid for the attained power `x(k)`. Direction checked; safe.

### F5. Root lengths — correct, and now literally confirmed

`x(k)`: root length `q_k`, attained for **every** `k`. `y(k)`: root length `q_k − c_k q_{k-1}`,
attained when `0 < c_k < a_k`. Both verified against literal longest common prefixes of the
actual word, built from BHZ's own S-adic composition
`ω = T^{c_1}τ_0^{a_1} ∘ T^{c_2}τ_1^{a_2} ∘ ⋯` with certified prefixes (two continuations
starting with different letters, intersected — BHZ Lemma 2.4), 562 checks, 0 failures.
Phase 8 also records the identity `q_k − c_k q_{k-1} = q_{k-1}(λ_{k-1} + d_k) ≥ q_{k-1}`
(`λ_k := q_{k-1}/q_k`, `d_k := a_k − c_k`), which makes the root growth explicit.

### F6. **The recorded surplus decomposition is dimensionally incomplete.** (real defect)

`theorems/phase7/SURPLUS_DECOMPOSITION.md` and the deposited note §13 both write

```
S_k >= A * E_k - C_A * D_k - O_A(log ell_k)        with  E_k := max(r'_k, r_k) - 2
```

The leading term cannot be `A · E_k`: `A` is the partial-quotient bound, a pure number, while
`S_k` must grow like a length. Re-derived from the integer periodic-value formula in
`PHASE8_PROOF_OR_OBSTRUCTION.md` §4, the correct statement is

```
odd branch :  S_k >= ell_k * E_k          + 1 - ceil(D(R_k)) log_2 3 - log_2(2 ell_k)
even branch:  S_k >= ell_k * (r_k - log_2 3) + 1 - ceil(D(V_k)) log_2 3 - log_2(ell_k)
```

with `ell_k = |W_k|` the **Sturmian** root length. The note's own flexible condition
`E_k >> log(ell_k)/ell_k` is equivalent to `ell_k E_k >> log ell_k`, i.e. it is consistent with
`ell_k · E_k` and inconsistent with `A · E_k` — so `A` in the displayed inequality is a
transcription slip for `ell_k`, not a different constant. The conclusions drawn from it are
unaffected; the displayed inequality is not correct as written.

## 3. The three statements, kept apart

| | statement | status found by this audit |
|---|---|---|
| **(a)** | every individual intercept has `ice(ω) > 2` strictly | **PROVED, and published**: immediate from BHZ **Theorem 1.1**. A bounded-type slope can never satisfy BHZ's characterising condition (finitely many `a_k > 1` pairs forces `a_k = 1` eventually, which then produces `(1,1,1)` infinitely often), so no `ω ∈ X_α` has `ice(ω) = 2`; with `ice ≥ 2` always (BHZ, citing Allouche–Davison–Queffélec–Zamboni) this gives `ice(ω) > 2`. BHZ state the corollary themselves: "no Sturmian shift with a quadratic slope can contain a sequence of `ice` equal to 2". |
| **(b)** | a positive margin uniform over all slopes and intercepts with partial quotients `≤ A` — **this is Conjecture 12.1** | **PROVED, and published**: BHZ **Proposition 5.1** gives `ice(ω) ≥ 2 + 1/(2(s+1)(t+1)+1)` for *every* `ω ∈ X_α` when `(a_k,a_{k+1}) = (s,t)`, `s>1`, infinitely often; BHZ **Proposition 5.2** gives `ice(ω) ≥ 2 + 1/(8t+1)` when `(a_k,a_{k+1},a_{k+2}) = (1,1,t)` infinitely often. Bounded type falls into one or the other by pigeonhole, giving `δ(A) ≥ 1/(2(A+1)^2 + 1)`. Independently re-proved from scratch in `PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 1 with `δ(A) = 1/(2(A+1)^2)` **plus explicit attained root lengths**, which BHZ §5 does not tabulate. |
| **(c)** | usable roots whose repetition gain dominates the arithmetic-height penalty | **PROVED here**, but it does **not** follow from (b) alone: it needs (b) *together with* attained witnesses of root length `→ ∞` and the corrected surplus inequality of F6. Supplied in `PHASE8_PROOF_OR_OBSTRUCTION.md` Theorem 2. |

(a) `⇏` (b): (a) permits `ε_k → 0`. (b) `⇏` (c): a margin on a `limsup` says nothing about
whether the witnesses achieving it are attained powers with growing primitive roots — precisely
the gap F3 and F5 are about.

## 4. Does the Phase-7 "exceptional-orbit reduction" prove any of them? **No — and it is false.**

`theorems/phase7/BHZ_GENERAL_INTERCEPT_MAP.md` asserts:

> "Translated to intercepts: `ice(ω_ρ) = ind*(α)` for **every** intercept `ρ` except those in
> the countable set `{jα mod 1 : j ∈ Z}` … the genuinely open cases are the countable
> exceptional set."

and `PHASE7_VERDICT.md` concludes from it that "intercept `0` is, if anything, a harder case
than generic" and that the open cases are "a countable, already-mostly-handled set".

**This is refuted** (`scripts/phase8/phase8_exceptional_orbit_refutation.py`, exact arithmetic).
The two cited ingredients do not support the claim: BHZ Prop. 2.1(4) gives only that `ice` is
shift-invariant *off a finite set of orbits*, and Lemma 2.2 only that `ice = ind*(α)`
**almost everywhere** for the unique invariant measure. A measure-zero exceptional set need not
be countable, and here it is not. BHZ's own Proposition 4.1 supplies the counterexample: the
"keep one" intercept `c_k = a_k − 1` for all `k` has `ice(ω) ≤ 1 + θ = 2.618…` at **every**
irrational slope (their Lemma 4.2), while `ind*(α) = 2 + limsup_k[a_k;a_{k-1},…,a_1]` grows
without bound in `A`. Its digit string is not eventually `0` and matches neither shift-orbit
pattern of the characteristic sequence, so its intercept is not a "return" intercept:

```
a_k = 2 :  ice(keep-one) = 2.207107   ice(characteristic) = 3.414214   ind*(alpha) = 4.414214
a_k = 3 :  ice(keep-one) = 2.100925   ice(characteristic) = 4.302776   ind*(alpha) = 5.302776
a_k = 4 :  ice(keep-one) = 2.059017   ice(characteristic) = 5.236068   ind*(alpha) = 6.236068
a_k = 5 :  ice(keep-one) = 2.038516   ice(characteristic) = 6.192582   ind*(alpha) = 7.192582
```

Worse, the whole family `F_A := {(c_k) admissible : a_k − c_k ∈ {1,2}}` (uncountable, and
automatically admissible because `c_k < a_k` makes the admissibility clause vacuous) has
`ice ≤ 1 + 2β_A/(β_A − 1) ≤ 5` uniformly, while `ind*(α) = 2 + β_A → ∞`. So for every `A ≥ 2`
an **uncountable** set of intercepts has `ice(ω) < ind*(α)`.
(`ind*(α) = 1 + ice(characteristic)` is BHZ Theorem 1.2, and the script asserts that identity as
a cross-check on its own `ind*` evaluation.)

Two Phase-7 conclusions must therefore be withdrawn: (i) the reduction of the open cases to a
countable set, and (ii) "intercept `0` is a harder case than generic". The truth is the
opposite — the *hardest* intercepts are the keep-one family, at which `ice → 2` as `A → ∞`,
whereas intercept `0` has `ice = ind*(α) − 1 → ∞`. Every numerical finding in
`STRUCTURED_INTERCEPTS.md` and `INTERCEPT_SUFFICIENT_CONDITION.md` stands (including the
identification of the near-maximal-digit family as the empirical worst case, which Phase 8
confirms as *exactly* the worst case); only the structural reduction built on top of them fails.

## 5. What actually remained, and what the margin really is

The genuine content of Conjecture 12.1 is a lower bound on `limsup_k max(x'(k),y(k))`, uniform
over admissible `(c_k)`. Phase 8 identifies the extremal family exactly: for constant `a_k = A`
and `d_k := a_k − c_k ≡ 1` (BHZ's "keep one"),

```
y(k) -> 2 + 1/(A beta_A),    beta_A = (A + sqrt(A^2+4))/2,
```

so the true optimal margin is `δ*(A) = Θ(A^{-2})`, verified to `A = 10` by exhaustive periodic
scan, by a greedy minimising adversary on non-eventually-periodic bounded-type slopes, and by
exhaustive branch-and-bound over *all* admissible digit strings for `A ≤ 3`
(`data/phase8/margin_search_output.txt`). In particular **no margin uniform in `A` exists** —
the `A`-dependence in Conjecture 12.1's statement is necessary, not a convenience.

## 6. Dependency map for the closed chain

| step | source | intercept-dependence |
|---|---|---|
| attained initial powers `r_k ≥ 2 + δ(A)`, `ell_k → ∞` | **BHZ Prop. 5.1/5.2** (priority) and `PHASE8_PROOF_OR_OBSTRUCTION.md` Thm 1 (re-proof, with roots) | the only intercept-dependent step — **now closed** |
| exact transfer `L_v = L_u + 1` | `theorems/phase2/ROTE_TRANSFER_THEOREM.md` | intercept-agnostic (proved so in that file) |
| odd branch density `γ_R = 1/2` exactly | `theorems/phase4/REQUIRED_EXPONENT.md` | structural, intercept-free |
| `D(R_k) = O_A(log ell_k)` | `theorems/phase5/ROTE_DISCREPANCY_AUDIT.md` | intercept-agnostic (three-distance bound is uniform in the starting phase) |
| surplus `⇒ Φ(v) ∉ Q` | `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`, `PHASE1_FREEZE.md` | no symbolic hypothesis at all |
| both seeds, every shift | `theorems/phase6/BOUNDED_TYPE_THEOREM.md` | CF-independent, applies verbatim |

## 7. Non-claims

- Nothing here is progress on the full Lagarias Periodicity Conjecture; `LADDER.md`'s structural
  ceiling (`theorems/phase1/FULL_PERIODICITY_GAP.md` Q4, Thue–Morse) is untouched.
- The symbolic lemma closed here is **not new mathematics**: it is BHZ 2006 §5. What is new is
  the bridge consequence and the attained-root bookkeeping.
- The deposited note's §12 needs an erratum; see `PHASE8_VERDICT.md` §5.
