**PROVED — CONJECTURE 12.1 IS A THEOREM (PRIORITY: BHZ 2006 §5), AND THE GENERAL-INTERCEPT BRIDGE CLOSES**

# PHASE8_PROOF_OR_OBSTRUCTION.md

## 0. Summary

Conjecture 12.1 is true. It is **already a published theorem**: Berthé–Holton–Zamboni (2006),
Propositions 5.1 and 5.2 — Section 5 of the very paper Phases 4–7 use as their primary source.
Phase 8 (i) records that priority, (ii) gives an independent, self-contained re-proof with a
clean constant and, crucially, with **explicit attained root lengths** that BHZ §5 does not
tabulate and that the bridge needs, and (iii) closes the chain to `Φ(v) ∉ Q` at every intercept.

Conventions and indexing are audited in `PHASE8_TARGET_AUDIT.md`; the `q_1 = a_1 + 1` shift (F1)
and the `0 < c_k < a_k` attainment restriction (F3) are load-bearing below.

## 1. Notation

`γ ∈ (0,1)` irrational, `γ = [0; A_1, A_2, A_3, …]`, `A := sup_k A_k < ∞` (bounded type).
`q_k` the convergent denominators: `q_0 = 1`, `q_1 = A_1`, `q_k = A_k q_{k-1} + q_{k-2}`.
BHZ digits: `a_1 = A_1 − 1`, `a_k = A_k` for `k ≥ 2` (so `a_k ≤ A`, `a_k ≥ 1` for `k ≥ 2`).
`(c_k)_{k≥1}` an admissible Ostrowski digit sequence: `0 ≤ c_k ≤ a_k`, and `c_k = a_k ⇒ c_{k-1} = 0`.
Put

```
d_k    := a_k - c_k  in  [0, a_k]
lam_k  := q_{k-1}/q_k  in  (0,1]          (lam_0 = 0, lam_k = 1/(A_k + lam_{k-1}))
S_k    := sum_{j=1}^{k} d_j q_{j-1},   t_k := S_k/q_k   (t_0 = 0)
m_k    := t_{k-1} + d_k
```

BHZ §4.1: `x'(k) = S_{k+1}/q_k`, `x(k) = 1_{a_{k+2}=c_{k+2}} + x'(k)`,
`y(k) = 1 + S_k/(q_k − c_k q_{k-1})`, and `ice(ω) = limsup_k max(x'(k), y(k))`.

**Attainment (BHZ Prop. 3.3, converse half).** For *every* `k`, `x(k)` is the prefix power of an
actual initial power of `ω` whose primitive root has length exactly `q_k`. For every `k` with
`0 < c_k < a_k`, `y(k)` is the prefix power of an actual initial power whose root has length
exactly `q_k − c_k q_{k-1}`. Nothing is asserted about `y(k)` as an attained power otherwise.

## 2. Four identities

> **Lemma 1.** For `k ≥ 1`: `t_k = lam_k m_k` and `m_{k+1} = lam_k m_k + d_{k+1}`; hence
> `x'(k) = m_{k+1}`.
> For `k ≥ 2`: `q_k − c_k q_{k-1} = q_{k-1}(lam_{k-1} + d_k)`, hence
> `y(k) = 1 + m_k/(lam_{k-1} + d_k)` and
>
> ```
>              lam_{k-1} ( m_{k-1} - 1 )
> y(k) - 2  =  -------------------------
>                 lam_{k-1} + d_k
> ```

*Proof.* `t_k = S_k/q_k = (S_{k-1} + d_k q_{k-1})/q_k = lam_k(t_{k-1} + d_k) = lam_k m_k`, and
`m_{k+1} = t_k + d_{k+1}`. Then `x'(k) = S_{k+1}/q_k = (S_k + d_{k+1}q_k)/q_k = t_k + d_{k+1} = m_{k+1}`.
For `k ≥ 2`, `q_k − a_k q_{k-1} = q_{k-2}` gives
`q_k − c_k q_{k-1} = q_{k-2} + d_k q_{k-1} = q_{k-1}(lam_{k-1} + d_k)`, and
`S_k/q_{k-1} = S_{k-1}/q_{k-1} + d_k = t_{k-1} + d_k = m_k`. Finally
`m_k − lam_{k-1} − d_k = t_{k-1} − lam_{k-1} = lam_{k-1}(m_{k-1} − 1)`. ∎

Two immediate consequences, both used below: **`y(k) > 2` if and only if `m_{k-1} > 1`**, and
`lam_k ≥ 1/(A+1)` for all `k ≥ 1` (from `q_k ≤ (A_k+1)q_{k-1}`).

**Verification.** `scripts/phase8/phase8_identities.py` checks all of Lemma 1 against a direct
exact-`Fraction` evaluation of BHZ Corollary 3.5: 27 774 admissible digit sequences exhaustively
(both `q`-conventions, 467 828 assertions) plus 480 random sequences of length 60 with `A ≤ 12`,
**0 failures**. The same script reproduces BHZ's own three Corollary-3.5 observations exactly
(3915 + 3911 + 6874 verified instances) and their §4.2 closed forms for the characteristic
sequence and `ω(−α)`.

## 3. The margin theorem

> **Lemma 2 (mass floor).** For every `k ≥ 3`, `m_k ≥ 1/(A+1)`; and if `d_k ≥ 1` then `m_k ≥ 1`.

*Proof.* If `d_k ≥ 1` then `m_k = t_{k-1} + d_k ≥ d_k ≥ 1`. If `d_k = 0` then `c_k = a_k`, so
admissibility forces `c_{k-1} = 0`, i.e. `d_{k-1} = a_{k-1} ≥ 1` (using `k−1 ≥ 2`); then
`m_{k-1} ≥ 1` by the first case and `m_k = t_{k-1} = lam_{k-1}m_{k-1} ≥ 1/(A+1)`. ∎

> **Theorem 1 (general-intercept margin, with attained witnesses).**
> Let `γ` be irrational with `A = sup_k A_k < ∞`, and let `ω` be **any** Sturmian sequence of
> slope `γ` — any intercept, either mechanical convention. Put
>
> ```
> delta(A) := 1 / (2 (A+1)^2) .
> ```
>
> Then for every `k ≥ 7` there is an index `k'` with `k − 4 ≤ k' ≤ k` and a word `W` of length
> `|W| ≥ q_{k-4}` such that `W^r` is a prefix of `ω` with
>
> ```
> r >= 2 + delta(A) .
> ```
>
> In particular `ice(ω) ≥ 2 + delta(A)`, the bound holds along witnesses of **unboundedly
> growing** root length, and `delta` depends only on `A` — not on the intercept, not on `(c_k)`,
> not on `γ` beyond `A`.

*Proof.* Fix `k ≥ 7`. Exactly one of three cases holds.

**(Z) Some `j ∈ {k, k−1, k−2}` has `d_j = 0`.** Then `c_j = a_j`, so `c_{j-1} = 0`, i.e.
`d_{j-1} = a_{j-1} ≥ 1`. By Lemma 1, `y(j) − 2 = m_{j-1} − 1` (the denominator is `lam_{j-1}`),
so `y(j) = 1 + m_{j-1} = 1 + a_{j-1} + t_{j-2} ≥ 2 + lam_{j-2}m_{j-2}`, and Lemma 2 (`j−2 ≥ 3`)
gives

```
y(j) >= 2 + 1/(A+1)^2 .
```

This value is attained: BHZ's first Corollary-3.5 observation gives `y(j) = x(j−2)` when
`c_j = a_j`, and `x(j−2)` is attained with root length `q_{j-2} ≥ q_{k-4}`.

**(B) `d_j ≥ 1` for `j ∈ {k, k−1, k−2}`, and `d_k ≥ 2`.** Then
`x'(k−1) = m_k = t_{k-1} + d_k ≥ 2 + lam_{k-1}m_{k-1} ≥ 2 + 1/(A+1)^2` by Lemma 2. Since
`x(k−1) ≥ x'(k−1)` and `x(k−1)` is attained with root length `q_{k-1} ≥ q_{k-4}`:

```
x(k-1) >= 2 + 1/(A+1)^2 .
```

**(C) `d_k = 1` and `d_{k-1}, d_{k-2} ≥ 1`.** By Lemma 2, `m_{k-2} ≥ 1`, so
`m_{k-1} − 1 = t_{k-2} + d_{k-1} − 1 ≥ t_{k-2} = lam_{k-2}m_{k-2} ≥ 1/(A+1)`. With
`lam_{k-1} ≥ 1/(A+1)` and `lam_{k-1} + d_k = lam_{k-1} + 1 ≤ 2`, Lemma 1 gives

```
y(k) - 2  >=  (1/(A+1)) * (1/(A+1)) / 2  =  1 / (2(A+1)^2) .
```

Attainment. Here `c_k = a_k − 1`. If `a_k ≥ 2` then `0 < c_k < a_k`, so `y(k)` is itself attained
with root length `q_k − c_k q_{k-1} = q_{k-1}(lam_{k-1}+1) ≥ q_{k-1} ≥ q_{k-4}`. If `a_k = 1`
then `c_k = 0`, and BHZ's remaining two observations apply: if `c_{k+1} < a_{k+1}` then
`y(k) ≤ x(k)`, attained with root `q_k`; if `c_{k+1} = a_{k+1}` then `y(k) < y(k+1) = x(k−1)`,
attained with root `q_{k-1}`.

The three cases are exhaustive, and in each one an **attained** initial power of exponent at
least `2 + min{ (A+1)^{-2}, (2(A+1)^2)^{-1} } = 2 + delta(A)` occurs, with root of length at
least `q_{k-4} → ∞`. ∎

*Remark (primitivity).* Each witness root is a cyclic permutation of a standard word
(BHZ Prop. 3.3's explicit words), hence primitive. Nothing downstream uses this: `F(W)`, `c_W`
and the surplus criterion are defined for arbitrary finite `W`, and
`theorems/phase2/SURPLUS_THEOREM.md` notes a non-primitive witness only weakens the margin.

*Remark (case (C) is the real one).* Cases (Z) and (B) give the stronger floor `(A+1)^{-2}`;
only case (C) — `d_k ≡ 1`, i.e. BHZ's "keep one" intercept `c_k = a_k − 1` — costs the extra
factor `2`. That is not an artefact: §3.1 shows case (C) is exactly extremal.

### 3.1 A matching upper bound, and why no `A`-free margin exists

For constant `a_k = A` and `d_k ≡ 1`, Lemma 1 solves in closed form. With `β = β_A := (A + √(A²+4))/2`
and `lam = 1/β`, the fixed point of `m ↦ lam·m + 1` is `m* = β/(β−1)`, and since
`β² − 1 = Aβ`,

```
x'(k) = m*      = beta/(beta-1)   < 2   for A >= 2 ,
y(k)  = 1 + m*/(lam+1) = 2 + 1/(A beta_A) .
```

So `ice(keep-one) = 2 + 1/(Aβ_A) = 2 + Θ(A^{-2})` exactly. Two consequences, and one
non-consequence:

- **Proved upper bound.** `δ*(γ) ≤ 1/(Aβ_A)` for every slope whose BHZ digits are eventually
  `≡ A`, so `delta(A) = 1/(2(A+1)^2)` is off by at most a bounded factor
  `2(A+1)^2/(A beta_A)` — `4.90` at `A=1`, `3.73` at `A=2`, `3.23` at `A=3`, `2.40` at `A=10`,
  decreasing to `2` as `A → ∞`.
- **No `A`-free margin.** Since `1/(Aβ_A) → 0`, no margin uniform in `A` can exist; the
  `A`-dependence in Conjecture 12.1's statement is necessary, not a convenience. This also
  recovers BHZ Prop. 4.1 from the other side: their `ice("keep one") ≤ 1 + θ` and the Phase-8
  lower bound pin the keep-one value between `2 + 1/(Aβ_A)` and `1 + θ`.
- **Not claimed here:** that `1/(Aβ_A)` *is* the infimum over all intercepts. That is proved
  only for slopes with eventually-constant BHZ digits and `A ≥ 2` (plus the Fibonacci slope,
  via BHZ Prop. 4.3); on every other bounded-type slope it is numerical evidence. The four
  tiers are separated in **`PHASE8_MARGIN_STATUS.md`**, which is the authority for this
  paragraph. **Theorem 2 uses none of it** — it needs only the `delta(A) > 0` of Theorem 1, or
  even BHZ Prop. 5.1/5.2 alone.

**Adversarial verification** (`data/phase8/margin_search_output.txt`, exact `Fraction`
throughout, three independent adversaries):

- exhaustive over **all** admissible periodic digit cycles up to period 7 for constant slopes
  `A = 1..10` and up to period 4 for nine multi-term slopes — the minimiser is `d_k ≡ 1` in every
  case, and the observed infimum equals `1/(Aβ_A)` to 8 decimals;
- a greedy minimising adversary on genuinely non-eventually-periodic bounded-type slopes
  (`a_k` read off an irrational rotation), `A = 1..6` — margin always `≥ 0.185`;
- exhaustive **branch-and-bound over every admissible digit string** of length 18 for `A ≤ 3`:
  global minima `2.5278`, `2.2010`, `2.1001`, minimiser tail `d_k ≡ 1` in each case.

Every configuration clears `2 + delta(A)`. Separately, the Theorem-1 case tree itself is checked
on 432 digit sequences (random with `A ≤ 10`, plus the characteristic, `ω(−α)`, keep-one and
eventually-maximal families on 8 slopes): all 9 504 branch instances satisfy both the exponent
floor and `root ≥ q_{k-4}`; branch usage `Z=3579, B=3280, C-y=1424, C-x(k)=850, C-x(k−1)=371`
— all five sub-branches are exercised. Tightest observed exponent `2.019187` at `A = 10`
(floor `2.004132`).

### 3.2 Priority: this is BHZ 2006 §5

> **BHZ Proposition 5.1.** If `(s,t)` is a pair of integers with `s > 1` such that
> `(a_k, a_{k+1}) = (s,t)` for infinitely many `k`, then **every** `ω ∈ X_α` has
> `ice(ω) ≥ 2 + 1/(2(s+1)(t+1)+1)`.
>
> **BHZ Proposition 5.2.** If `(a_k, a_{k+1}, a_{k+2}) = (1,1,t)` for infinitely many `k`, then
> every `ω ∈ X_α` has `ice(ω) ≥ 2 + 1/(8t+1)`.

For a bounded-type slope there are finitely many digit pairs, so by pigeonhole either some
`(s,t)` with `s>1` recurs infinitely often (Prop. 5.1, `s,t ≤ A`), or `a_k = 1` for all large `k`
and `(1,1,1)` recurs infinitely often (Prop. 5.2, `t = 1`). Hence

```
ice(omega) >= 2 + 1/(2(A+1)^2 + 1)   for every omega in X_alpha ,
```

which **is** Conjecture 12.1. BHZ's own three-case proof of Prop. 5.1 (`C1: c_{k+2}=a_{k+2}`,
`C2: c_{k+2} ≤ a_{k+2}−2`, `C3: c_{k+2} = a_{k+2}−1`) is structurally the same trichotomy as
Theorem 1's `(Z)/(B)/(C)`, reached independently here; the constants agree to a factor of
`1 + 1/(2(A+1)^2)`. Theorem 1 adds the explicit root-length bound `q_{k-4}` and the
attainment routing, which BHZ leave to a reference back to Prop. 3.3.

**`X_α` is the set of all Sturmian sequences of slope `α`**, i.e. every intercept under both
`R_α` and `R̃_α` (BHZ §2.1) — exactly the quantifier the bridge needs, covering both the upper
and the lower mechanical convention.

## 4. The surplus inequality, re-derived with every length factor explicit

From the integer periodic-value formula (`theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`),
for a finite word `W`, `ell = |W|`, `k = |W|_1`:

```
delta_W = 2^ell - 3^k ,   c_W = sum_{i<ell, W_i=1} 3^{k - k_{i+1}(W)} 2^i ,   F(W) = |delta_W| + c_W
S_s(W)  = lcp(s, W^infty) - log_2 F(W) ,
log_2 F(W) <= log_2 ell + ceil(D(W)) log_2 3 + max(ell, k log_2 3) + O(1)
```

and the criterion is: `limsup_n S_v(W_n) = +∞ ⟹ Φ(v) ∉ ℚ`.

Let `W = W_k` be a Theorem-1 witness for `u`, `ell = |W|`, `r_u = L_u/ell` with
`L_u = lcp(u, W^∞)`, and let `V = v[0:ell]`. By `theorems/phase2/ROTE_TRANSFER_THEOREM.md`
(intercept-agnostic), `L_v = L_u + 1` **exactly**, at root `V` if `|W|_1` is even, or
`R = V·V̄` (length `2ell`) if `|W|_1` is odd.

**Odd branch** (the binding one). `γ_R = 1/2` exactly, so `max(1, γ_R log_2 3) = 1`, and
`ell_R = 2ell`, `r_v = (L_u+1)/(2ell)`:

```
S >= ell_R * [ r_v - max(1, gamma_R log_2 3) ] - ceil(D(R)) log_2 3 - log_2 ell_R
   = 2 ell [ (L_u+1)/(2 ell) - 1 ] - ceil(D(R)) log_2 3 - log_2(2 ell)
   = ell * (r_u - 2) + 1 - ceil(D(R)) log_2 3 - log_2(2 ell) .
```

**Even branch.** `max(1, γ_V log_2 3) ≤ log_2 3 < 2` for every `γ_V ∈ (0,1]`, so

```
S >= ell * (r_u - log_2 3) + 1 - ceil(D(V)) log_2 3 - log_2(ell) .
```

The even branch needs **no** discrepancy hypothesis at all: by
`theorems/phase1/REPETITION_HEIGHT_CRITERION.md`'s unconditional form, the combinatorial cap
`D(V) ≤ γ_V(1−γ_V)ell` together with `sup_γ [max(1,γ log_2 3) + γ(1−γ) log_2 3] = log_2 3 < 2`
already gives `S ≥ (r_u − log_2 3)·ell − o(ell)`. Only the odd branch needs
`D(R) = o(ell)`.

So the leading term is `ell · E` with `E := r_u − 2` (odd) or `ell · (r_u − log_2 3)` (even) —
**not** `A · E` as `theorems/phase7/SURPLUS_DECOMPOSITION.md` and the deposited note §13 write
it (audit finding F6). Substituting Theorem 1's `r_u ≥ 2 + δ(A)`:

```
odd branch :  S_k >= delta(A) * ell_k + 1 - ceil(D(R_k)) log_2 3 - log_2(2 ell_k)
even branch:  S_k >= (2 - log_2 3) * ell_k + 1 - ceil(D(V_k)) log_2 3 - log_2(ell_k)
```

With `D = O_A(log ell_k)` (`theorems/phase5/ROTE_DISCREPANCY_AUDIT.md`, intercept-agnostic
because the three-distance/Ostrowski discrepancy bound is uniform in the starting phase of the
rotation) and `ell_k ≥ q_{k-4} → ∞` from Theorem 1, both branches give `S_k → +∞`. This lands
in the **first** row of `theorems/phase7/FLEXIBLE_MARGIN_BOUNDARY.md`'s table (`ε_k ≍ const`);
the flexible machinery is not needed.

**Exact-integer verification** (`scripts/phase8/phase8_surplus.py`, `data/phase8/surplus_output.txt`):
263 attained Ostrowski witnesses across 6 slopes × {characteristic, `ω(−α)`, keep-one,
eventually-maximal, random} intercepts. In every one: literal `lcp` equals the Ostrowski
prediction (**0** mismatches), `L_v = L_u + 1` (**263/263**), `γ_R = 1/2` exactly on the odd
branch, and `2^{L_v} > F(R)` as exact integers. Growth along one general intercept
(`a_k = 2`, keep-one, `A = 2`, so `δ*(2) = 0.20711`):

```
  k  branch     ell    ell_R      r_u   E=r_u-2   D(R)         S
  5     odd      58      116  2.18966   0.18966   2.00      9.99
  7     odd     338      676  2.20414   0.20414   2.00     68.00
  9     odd    1970     3940  2.20660   0.20660   3.00    406.00
 11     odd   11482    22964  2.20702   0.20702   3.00   2376.00
```

`S` grows linearly in `ell` with slope `→ δ*(2)`, and `D(R)` stays at `2–3` while `ell` grows
200-fold — consistent with `O(log ell)`, far from the `o(ell)` that is all the criterion needs.
Purely periodic controls (`01`, `001`, `1101`, `011`) produce no contradiction, as required.

## 5. The closed chain

> **Theorem 2 (general-intercept CS Rote bridge).**
> Let `γ ∈ (0,1)` be irrational with bounded partial quotients, `A := sup_n a_n < ∞`.
> Let `u` be **any** Sturmian word of slope `γ` — **any** intercept `ρ`, either the upper or the
> lower mechanical convention. Let `v` be either complementary symmetric Rote sequence with
> `S(v) = u` (either seed), or any shift `σ^j(v)`. Then
>
> ```
> Phi(v) not in Q .
> ```

*Proof.* Quantifiers first: `u ∈ X_γ`, and `X_γ` is BHZ's set of *all* Sturmian sequences of
slope `γ`, over every intercept and both interval-exchange conventions.

1. **Symbolic input.** By Theorem 1 (equivalently BHZ Prop. 5.1/5.2 plus Prop. 3.3), there are
   infinitely many `k` and primitive words `W_k` with `ell_k := |W_k| ≥ q_{k-4} → ∞` such that
   `W_k^{r_k}` is a prefix of `u` with `r_k ≥ 2 + δ(A)`, `δ(A) = 1/(2(A+1)^2) > 0`.
2. **Transfer.** `theorems/phase2/ROTE_TRANSFER_THEOREM.md` (proved intercept-agnostic there):
   `v` begins in `V_k^{…}` or `R_k^{…}`, `R_k = V_k V̄_k`, to depth exactly `L_v = L_u + 1`.
3. **Density.** `theorems/phase4/REQUIRED_EXPONENT.md`: `γ_{R_k} = 1/2` exactly (odd branch,
   structural); `γ_{V_k} ∈ (0,1)` arbitrary (even branch). Required exponent `r_u > 2` (odd),
   `r_u > log_2 3` (even) — both supplied by step 1 with margin `δ(A)` resp. `2 − log_2 3`.
4. **Discrepancy.** `theorems/phase5/ROTE_DISCREPANCY_AUDIT.md`: `D(R_k) = O_A(log ell_k)`,
   uniform in the intercept (the bound is on the rotation's own discrepancy, and the classical
   `N D*_N = O(Σ_{i≤k} a_i)` estimate is uniform in the starting phase).
5. **Surplus.** §4: `S_k ≥ δ(A)·ell_k + 1 − O_A(log ell_k) → +∞`.
6. **Conclusion.** `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md` /
   `theorems/phase2/PHASE1_FREEZE.md`: `limsup_k S_k = +∞ ⟹ Φ(v) ∉ ℚ`.
7. **Both seeds** — via `D(V V̄) = D(V̄ V)`; **every shift `σ^j(v)`** — via the source paper's
   Proposition 2.3. Both arguments are continued-fraction-independent and apply verbatim
   (`theorems/phase6/BOUNDED_TYPE_THEOREM.md`). ∎

This **supersedes `theorems/phase6/BOUNDED_TYPE_THEOREM.md`** by removing its single stated
boundary ("intercept `0` only; other intercepts of the same slope remain uncovered") without
weakening any other quantifier. The bounded-partial-quotient hypothesis on `γ` is unchanged and
is **not** removed here (see §7).

## 6. The intrinsic-square bypass is not needed — and its gap is now explained

`theorems/phase7/INTRINSIC_SQUARE_ROUTE.md` correctly identifies that bare squares (`r = 2`,
Allouche–Davison–Queffélec–Zamboni via the source paper's Theorem 10.2, no exceptional slopes or
intercepts) suffice for the even-weight branch (`2 − log_2 3 ≈ 0.415` of margin) but give
**exactly zero** margin on the odd-weight branch, where `r_v = r_u/2 = 1`. Phase 8 confirms that
reading and makes it moot: Theorem 1 supplies `r_u > 2` strictly at every intercept, so both
branches close and the general-intercept weight-parity automaton that Phase 7 flagged as
unattempted is never needed. No primary-source search for a stronger intrinsic-square theorem
was required; the route is superseded, not repaired.

The one thing worth preserving from that route: it is the only part of the chain that would
survive dropping the bounded-partial-quotient hypothesis, since ADQZ has no hypothesis on `γ`.
That is the natural starting point for §7's open problem.

## 7. What is **not** proved

1. **Unbounded partial quotients.** `δ(A) = Θ(A^{-2}) → 0`, and BHZ Theorem 1.1 shows the margin
   genuinely vanishes: for slopes satisfying their condition (necessarily of unbounded partial
   quotients) there **exists** an intercept with `ice(ω) = 2` exactly. At such an intercept the
   odd-weight branch has zero margin and this method gives nothing. So the bounded-type
   hypothesis is not an artefact of the proof — it is where the *symbolic* input dies. Any
   extension must either force the even branch (weight-parity control) or leave the
   initial-power mechanism entirely.
2. **Complexity beyond `2n`.** Untouched; the ladder rung is unchanged.
3. **The full Periodicity Conjecture.** Untouched, and structurally unreachable by this family
   of methods (`theorems/phase1/FULL_PERIODICITY_GAP.md` Q4: Thue–Morse admits no useful initial
   powers at all). Theorem 2 widens one rung; it is not progress on the conjecture.
4. **Novelty of the symbolic lemma.** None claimed. Conjecture 12.1 = BHZ 2006 Prop. 5.1 + 5.2.
   What Phase 8 contributes is the priority identification, the attained-root bookkeeping, the
   corrected surplus inequality, and the bridge consequence (Theorem 2).
5. **No Lean formalisation.** Everything here is paper mathematics plus exact-`Fraction`/integer
   Python diagnostics. The diagnostics are certificates against the primary source's formulas,
   never a substitute for the proof.
