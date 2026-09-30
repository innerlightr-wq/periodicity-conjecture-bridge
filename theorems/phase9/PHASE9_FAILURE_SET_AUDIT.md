**FAILURE-SET AUDIT — THE PARITY SHORTCUT IS WRONG AS STATED; DISJOINTNESS FAILS; THE INTERSECTION IS NON-EMPTY BUT ONLY DEFEATS THE ESTIMATE**

# PHASE9_FAILURE_SET_AUDIT.md

## 1. The weight law — Phase 8's parity shortcut is **not** valid as stated

Phase 8's next-target analysis used `w(k,d) = d p_{k-1} + p_{k-2}` as the weight of the prefix of
length `ℓ(k,d)`, and read parity off it. **That formula is not universally exact.** Stress-tested
against literal certified prefixes over many random admissible intercepts:

```
offset (actual prefix weight - predicted)     -1: 32      0: 1945     +1: 53      (intermediate roots)
                                              -1: 11      0:    0     +16        (x-roots with x(k) < 1)
                                                          0: 2032                 (x-roots with x(k) >= 1)
                                                          0:  952                 (y-roots, 0 < c_k < a_k)
```

The law is **exactly**: the formula holds on **attained power roots** and can fail by `±1`
otherwise.

> **(W-y)** If `0 < c_k < a_k` the prefix of length `ℓ_k` **is** the root of an attained initial
> power (BHZ Prop. 3.3, second case); that root is a cyclic permutation of
> `τ_0^{a_1}∘⋯∘τ_{k-1}^{a_k−c_k}(i)`, whose weight is `p_k − c_kp_{k-1} = d_kp_{k-1}+p_{k-2}` by
> BHZ Lemma 2.6; cyclic permutation preserves weight. **Exact: 952/952.**
>
> **(W-x)** The prefix of length `q_k` is a power root only when `x(k) ≥ 1`; then its weight is
> exactly `p_k`. **Exact: 2032/2032.** When `x(k) < 1` it is not a root and the weight deviated in
> **27/27** cases — i.e. *always*.
>
> **(W-int)** A genuinely intermediate length carries no attainment guarantee; its weight deviated
> in 85/2030 cases and **must be read off the word**.

**Consequences for the record.** (i) Phase 8's `PHASE8_NEXT_TARGET.md` §4 identified the weights
correctly for the *guaranteed* roots but then applied the same formula to `d = 1` intermediate
roots — that step is not licensed. (ii) The deviations concentrate at small `k` (largest observed:
`k = 8`), so they are Ostrowski boundary effects; but *nothing proved here shows they stop*, so any
parity statement must be either restricted to attained roots or computed from the word. Every
Phase 9 script that uses an intermediate root asserts `w == sum(u[:ℓ])` on the actual word.

## 2. The numerator-parity characterisation, re-derived in the corrected convention

With `p_1 = 1` and `p_2 = a_2p_1 + p_0 = a_2`:

> **Finite form.** `p_k` is odd for **every** `k ≥ 1` `⟺` `a_2` is odd **and** `a_k` is even for
> all `k ≥ 3`.

*Proof.* `p_1 = 1` is odd. `p_2 = a_2`, so `a_2` must be odd. Once `(p_{k-2},p_{k-1}) ≡ (1,1)`,
`p_k ≡ a_k + 1`, so `p_k` odd `⟺` `a_k` even, and the state stays `(1,1)`. ∎
Note the common trap: an **all-even** digit string fails immediately, because `p_2 = a_2` is then
even. Verified on six digit strings, including that trap.

> **Asymptotic form** — the one the bridge needs. If `a_k` is even for all `k > K` then
> `p_{k+1} ≡ p_{k-1}`, so the parity pair is 2-periodic from `K` on: `p_k` is odd for all `k ≥ K−1`
> **iff both** `p_{K-1}, p_K` are odd, and otherwise `p_k` is **even for infinitely many** `k`.
> Conversely an odd `a_k` encountered at state `(1,1)` forces `p_k` even. Hence
> **`p_k` odd for all large `k` ⟹ `a_k` even for all large `k`.**

Write `P_k := (p_{k-1}, p_k) mod 2 ∈ {(0,1),(1,0),(1,1)}` (never `(0,0)`: `gcd(p_k,p_{k-1}) = 1`).
Transitions: `(0,1) → (1, a_{k+1} mod 2)`, `(1,0) → (0,1)`, `(1,1) → (1, (a_{k+1}+1) mod 2)`.

**The witness parities, exactly:**

```
x-root weight p_k even            <=>  P_k = (1,0)
y-root weight even                <=>  p_{k-1} d_k == p_{k-2}  (mod 2), i.e.
                                       P_{k-1} = (0,1) and d_k even,  or  P_{k-1} = (1,1) and d_k odd
                                       (never when P_{k-1} = (1,0))
```

So the parity condition **couples** the digit parities and the intercept digits; it is not a
property of the slope alone, which is where Phase 8's sketch was loose.

## 3. Disjointness: **false**, as the task warned

Phase 8 hoped the odd-weight obstruction and the height-growth obstruction were disjoint. They are
not, and the reason is exactly the one flagged: **parity restrictions permit arbitrarily large even
partial quotients.** `a_k = 2·2^{2^k}` is even and tower-fast simultaneously. Any argument assuming
disjointness is void.

But the failure sets are also not what Phase 8 described, because the correct even-branch threshold
is `g(γ_V) < log₂3`, not `2`, and because the even branch needs **no** hypothesis on `γ`. Measured
coverage of the guaranteed-root even branch (30 random instances per cell):

```
slope family              c=0     keep-one   c=a_k-2   random
bounded, a_k in 1..4      100%    100%       100%      100%
bounded, a_k in 1..12     100%     97%       100%      100%
a_k = k                   100%      0%       100%      100%
a_k = 2^k                 100%      0%       100%      100%
a_k = k!                  100%      0%       100%      100%
all even, a_k in 2..8       0%    100%         0%      100%
all even, fast (2^k)        0%    100%         0%      100%
```

Two clean structural readings, both consistent with §2:

- on an **all-even-tail** slope (all `p_k` odd, `P_{k-1} ≡ (1,1)`) the even branch needs `d_k` **odd**
  — so `c_k = 0` and `c_k = a_k−2` fail and **keep-one (`d_k = 1`) always works**;
- on a slope with `a_k` odd infinitely often, `P_{k-1}` visits `(0,1)`, so even-`d_k` intercepts work
  and keep-one can fail.

66 distinct slope/intercept pairs had **no** guaranteed even-weight witness; 62 of them lie in the
all-even-tail family.

## 4. On the failure set: intermediate roots, and two genuine survivors

On the 24 failure-set pairs examined with literal prefix powers and **actual** weights:

- **22 are rescued by an intermediate root** — an even-weight root with `r > g(γ)`, exact integer
  surplus positive in every case. E.g. `a_k = k` at keep-one (an `ice = 2` slope): the `(k,d)=(6,2)`
  root has `ℓ = 837`, even weight, `r = 1.573477 > g = 1.383684`, exact surplus `478.3`, `2^{L_v} > F`.
- **2 resist the even branch entirely**: `a_k = 2^k` and `a_k = k!`, both at keep-one. There
  `p_k` alternates parity, so `P_{k-1}` never equals `(1,1)` and the `d_k = 1` `y`-root is always
  odd-weight; the `x`-root is even-weight at even `k` but has exponent `≈ 1 + λ_k → 1 < g(γ)`.
  **Both fall to the odd branch**, with positive exact integer surplus (`a_k = 2^k`: `k = 4`,
  `ℓ = 120`, `r_u = 2.0333`, `D(R) = 2`, `S = 3.08`, `2^{L_v} > F`). For `a_k = k!` no odd-branch
  witness fell inside the computable window `30 ≤ ℓ ≤ 4000` — recorded as **not tested**, not as a
  failure.

Separately, on the hostile all-odd-numerator family the `d = 1` intermediate root has even weight
(`w = p_{k-1}+p_{k-2}`, both odd) and clears `g` at every scale tested: 27 hostile slope/intercept
pairs, **zero** with no clearing even-weight root, and **144 exact even-branch surplus evaluations,
every one positive**, growing linearly in `ℓ` (e.g. `ℓ = 1591 → S = 1120.67`). Measured `D(V) = 3–5`
against a combinatorial cap of `960–5600` — the cap is 2–3 orders of magnitude pessimistic.

## 5. The intersection — a genuine double-failure family, and exactly what it defeats

To defeat **both** branches a slope/intercept must satisfy three conditions at once:

1. `a_k` even for all large `k` with both boundary numerator parities odd, so **every** `p_k` is odd
   → the `x`-root always has odd weight;
2. `d_k` **even** for all large `k`, so the `y`-root weight `≡ d_k + 1 ≡ 1` is odd too → **no
   guaranteed even-weight root at any scale** (a structural statement, not a sampling artefact);
3. tower-fast growth of `a_k`, so the estimated discrepancy penalty outruns the driver.

Condition 2 rules out keep-one. An explicit witness:

```
a = [3, 1, 2*2^(2^1), 2*2^(2^2), 2*2^(2^3), ...] = [3, 1, 8, 32, 512, 131072, ...]
c = a_k - 2      (so d_k = 2, even for every k)          admissible: yes
all convergent numerators odd: yes        x(k), y(k) at k = 3,4,5: 2.364, 2.118, 2.021  (all > 2)
```

Its own driver against its own penalty estimate:

```
 k   ell_k    driver ell_k*E_k    sum b_i   penalty est   driver/penalty   (H)?
 4      93              11          15         30.77          0.357        NO
 5    2870              60          32         62.72          0.957        NO
```

**Level-by-level, kept strictly apart:**

| level | statement | verdict on this family |
|---|---|---|
| **(a)** | the sufficient growth condition `(H)` | **FAILS** from `k = 4` on |
| **(b)** | the estimated surplus bound (`D(R)` replaced by its three-distance estimate) | **FAILS**, same estimate |
| **(c)** | the **exact** integer surplus at selected witnesses | **HOLDS wherever computable**: `k = 3` (`ℓ = 44`, `D(R) = 2`, `S = 15.33`) and `k = 4` (`ℓ = 93`, `D(R) = 2`, `S = 10.34`), `2^{L_v} > F` in both. Beyond `k = 5`, `q_k > 10^{150}` and `(c)` is **not determined** — no computation and no proof |
| **(d)** | failure over **every** available witness family | **NOT DETERMINED**, and strictly stronger than (c) |

The `k = 4` row is the decisive one: `(a)` and `(b)` already fail there, and `(c)` nevertheless
**holds**. The reason is visible — the three-distance bound gives `Σb_i = 15`, penalty `30.8`,
while the actual `D(R) = 2` gives penalty `≈ 10.7` against a driver of `11`. **The obstruction is in
the estimate of `D(R)`, not in the arithmetic.**

So the intersection of the failure sets is non-empty, and what lives in it defeats the **current
sufficient criterion** — not the bridge, and not `Φ(v) ∉ ℚ`. Reporting this family as a
counterexample would be exactly the (b)→(c) conflation the task forbids.
