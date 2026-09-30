**PROOF CORRECT — BUT IT NEEDS ONLY THE PRE-EXISTING CRITERION, NOT PHASE 9'S NEW THRESHOLD**

# THUE_MORSE_INDEPENDENT_PROOF.md

Independent reconstruction, from definitions, of `Φ(Thue–Morse) ∉ ℚ`.
Script: `scripts/phase9b/tm_independent_proof.py`; output `data/phase9b/tm_independent_proof_output.txt`.
(For whether the result is *new*, see `THUE_MORSE_LITERATURE_AUDIT.md`. It is not.)

## 1. Conventions, stated explicitly

**Thue–Morse.** `t_n := popcount(n) mod 2`; equivalently `t` is the fixed point of `μ(0)=01`,
`μ(1)=10` at `0`. Both constructions were built and compared over `2^18` letters — they agree.
`t = 0110100110010110…`

**Conjugacy map.** `T(x) = x/2` for even `x`, `(3x+1)/2` for odd `x`, on `ℤ₂`. `Φ` sends a parity
vector `v ∈ {0,1}^ℕ` to the 2-adic integer it codes. Source paper Prop. 2.1:

```
Phi(v) = - sum_{i : v_i = 1} 3^{-k_{i+1}(v)} 2^i ,      k_j(v) := |v[0:j]|_1 .
```

Prop. 2.2 (isometry): `v₂(Φ(a) − Φ(b)) = lcp(a,b)`. Prop. 4.1 (periodic value):
`Φ(W^∞) = c_W/(2^ℓ − 3^k)` with `c_W = Σ_{i<ℓ, W_i=1} 3^{k−k_{i+1}(W)}2^i`.
**Prop. 4.1 was re-derived here from Prop. 2.1** by summing the geometric series and checked
numerically in `ℤ/2^400` on three words — the convention is not taken on trust. This `Φ` is the
same map as López–Stoll's (their eq. for `Φ(v)` is identical), which matters in the audit.

**Discrepancy.** The repository's definition (`theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`):

```
D(W) := max_{0 <= i <= ell} | k_i(W) - i*k/ell | ,      k := |W|_1 .
```

Deviation of prefix counts from the root's **own** density. Not a star-discrepancy of a rotation,
not relative to any external density. This matters: Phase 9's `g(γ)` bound uses the *combinatorial
cap* on this quantity, whereas the Thue–Morse proof uses its *exact* value.

## 2. The base root

`W_0 := t[0:24] = 011010011001011010010110`, `|W_0| = 24`, `|W_0|_1 = 12`, density exactly `1/2`.

```
t[24:40]  = 0110100110010110
W_0[0:16] = 0110100110010110     equal
t[40] = 0 ,  W_0[16] = 1         differ
```

So `lcp(t, W_0^∞) = 40` exactly, prefix power `40/24 = 5/3`. Verified by the scanning routine and
again by the explicit character comparison above.

## 3. Propagation under `μ`

> **Lemma.** For finite/infinite words `x ≠ y`, `lcp(μ(x), μ(y)) = 2·lcp(x,y)`.

*Proof.* `μ` is 2-uniform, so the images of the first `lcp(x,y)` equal letters agree, giving
`≥ 2·lcp`. At the first differing position the letters are `0` and `1`, and `μ(0) = 01`,
`μ(1) = 10` differ **in their first letter**, so the images differ at position `2·lcp` exactly. ∎

With `μ(t) = t` and `μ(W^∞) = μ(W)^∞`, setting `W_m := μ^m(W_0)`:

| | value | checked |
|---|---|---|
| `|W_m|` | `24·2^m` | `m = 0..12` |
| `lcp(t, W_m^∞)` | `40·2^m` | `m = 0..12` |
| prefix power | `5/3`, constant | `m = 0..12` |
| `|W_m|_1 / |W_m|` | `1/2` exactly (`μ` sends each letter to one `0` and one `1`) | `m = 0..12` |
| `W_m = t[0 : 24·2^m]` | yes (`μ` maps prefixes of `t` to prefixes of `t`) | `m = 0..12` |

## 4. Discrepancy — bounded, and proved so

> **Lemma.** `D(W_m) = 1/2` for every `m`.

*Proof.* Let `S(N) := Σ_{n<N} (−1)^{t_n}`. Since `t_{2n} = t_n` and `t_{2n+1} = 1 − t_n`, each pair
`(2n, 2n+1)` contributes `(−1)^{t_n} + (−1)^{1−t_n} = 0`, so `S(2M) = 0` for every `M`; and
`S(2M+1) = S(2M) + (−1)^{t_{2M}} = (−1)^{t_M} ∈ {−1,+1}`. Hence `|S(N)| ≤ 1` for all `N`. For a
prefix of even length `ℓ` with `k = ℓ/2`, `k_i − i/2 = −S(i)/2`, so `D = max_i|k_i − i/2| = 1/2`. ∎

Verified to `N = 2^16`: `S(even) = 0`, `|S(odd)| = 1`, throughout. **`D` is bounded, not merely
sublinear** — this is what makes the short route available.

## 5. `t ≠ W_m^∞`, and the arithmetic contradiction

`t` is aperiodic (classical: overlap-free, Thue 1912; verified here that no preperiod `< 200` with
period `< 3000` fits a `2^15` prefix). Each `W_m^∞` is periodic, so `t ≠ W_m^∞` — the only standing
hypothesis the abstract criterion places on the pair.

Suppose `Φ(t) = u/v` in lowest terms; `v` is odd since `Φ(t) ∈ ℤ₂`. Put `H := max(|u|, v)`, a fixed
finite integer **once `u/v` is chosen**. With `M_m := u·δ_m − v·c_{W_m}` (`δ_m := 2^{|W_m|} − 3^{|W_m|_1}`):

- `δ_m ≠ 0` and odd; `M_m ≠ 0` because `Φ` is injective and `t ≠ W_m^∞`;
- `v₂(M_m) = v₂(vδ_m) + v₂(Φ(t) − Φ(W_m^∞)) = 0 + L_m`, so `|M_m| ≥ 2^{L_m}`;
- `|M_m| ≤ H(|δ_m| + c_{W_m}) = H·F(W_m)`.

Hence `S_m := L_m − log₂F(W_m) ≤ log₂H` **for every `m`**, while `S_m → +∞` (§7). Contradiction, for
every choice of `u/v`. The quantifier order is the safe one: `H` is fixed after `u/v` but before `m`,
and a single `m` with `S_m > log₂H` already refutes that `u/v`.

## 6. Which criterion is actually needed — the Phase 9 attribution was wrong

`theorems/phase1/REPETITION_HEIGHT_CRITERION.md` states the **exact** inequality

```
S >= ell*[ r - max(1, gamma log2 3) ] - ceil(D) log2 3 - log2 ell .
```

At `γ = 1/2` the threshold is `max(1, (log₂3)/2) = max(1, 0.79248) = 1`.

| route | threshold | `r − threshold` | needs a discrepancy hypothesis? |
|---|---|---|---|
| **Phase 1 exact inequality at `γ = 1/2`** | **1.000000** | **0.666667** | yes — `D = o(ℓ)`, and here `D = 1/2` |
| Phase 1 uniform packaging (`sup` over `γ`) | 1.584963 | 0.081704 | yes |
| Phase 9 `g(γ)` at `γ = 1/2` | 1.396241 | 0.270426 | no |

All three clear, but the **first** is the shortest chain and is the one to cite. **Phase 9 attributed
the Thue–Morse conclusion to its own `g(γ)` threshold; that attribution is withdrawn.** `g(γ)` is the
threshold one must use when *nothing* is known about `D`; Thue–Morse is not such a case, since
`D = 1/2` exactly. The `g(γ)` theorem remains valid and is audited separately (§8).

## 7. Numerator, denominator, and the asymptotic — proved, not fitted

- `|δ_W| = 2^ℓ(1 − (√3/2)^ℓ)`, so `log₂|δ_W| ∈ [ℓ − 0.048, ℓ]` for `ℓ ≥ 24`.
- `c_W ≤ ℓ·3^{⌈D⌉}·max(2^ℓ,3^{ℓ/2}) = 3ℓ2^ℓ` (since `⌈1/2⌉ = 1`); and `c_W ≥ 2^{i*}` where `i*` is the
  largest index with `W_{i*} = 1`, here `ℓ−2`, so `c_W ≥ 2^{ℓ−2}`.
- Hence `ℓ − 0.05 ≤ log₂F(W) ≤ ℓ + log₂(1+3ℓ)`, and

```
(2/3) ell - log2(1 + 3 ell)   <=   S   <=   (2/3) ell + 0.05 .
```

So `S/ℓ → 2/3` with error `O(log ℓ / ℓ)` — a **proved** asymptotic. Every computed row for
`m = 0..8` lies inside that bracket (asserted, not merely observed): `S = 14.73, 30.67, 62.68,
126.67, 254.68, 510.67, 1022.68, 2046.67, 4094.68`, with `S/ℓ = 0.614 … 0.6665`. Note the numerator
and denominator are separately tracked: `log₂|δ| − ℓ → 0` and `log₂c_W − ℓ ≈ 0.58`, so neither
dominates and the crude packaging `F = |δ| + c_W` is within `1.33` bits of `2^ℓ` throughout.

## 8. Status of the `g(γ)` theorem, separately

`g(γ) := max(1, γlog₂3) + γ(1−γ)log₂3` is the threshold obtained by substituting the *universal
combinatorial cap* `D(W) ≤ γ(1−γ)ℓ` (`theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md`) into the
exact inequality. It is a genuine, if modest, refinement of Phase 1's **unconditional** squares
theorem, which used `sup_γ g(γ) = log₂3` and concluded `r = 2` suffices with no discrepancy
hypothesis: keeping `γ` instead of taking the sup lowers the bar to `g(γ) < log₂3` for `γ < 1`.
It is **not** a refinement of the main criterion, and it is **not** used by the Thue–Morse proof.
It stands or falls on its own audit, and nothing in this file depends on it.

## 9. Verdict on correctness

The proof is **correct**. Shortest dependency chain:

```
source paper Prop. 2.1 (series)  ->  Prop. 4.1 (periodic value; re-derived here)
source paper Prop. 2.2 (2-adic isometry)
theorems/phase1/DISCREPANCY_HEIGHT_THEOREM.md   (c_W bound)
theorems/phase1/REPETITION_HEIGHT_CRITERION.md  (EXACT inequality, at gamma = 1/2)
+ Thue-Morse facts: r = 5/3 at ell = 24*2^m ; gamma = 1/2 ; D = 1/2 ; aperiodic.
```

Phase 9's `g(γ)` is **not** in this chain.
