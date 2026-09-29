**PROVED — for Sturmian slopes with bounded partial quotients (Target B's hypothesis); empirically supported but not proved beyond that.**

# ROTE_ROOT_DISCREPANCY.md

## The question, precisely

For the transferred roots `V` (even-weight case) or `R=V\bar V` (odd-weight case) supplied by `ROTE_TRANSFER_THEOREM.md`, is `D(V_n)=o(\ell_n)` (or better) along the sequence of initial powers `u` is guaranteed to have (Theorem 10.2/ADQZ 2001, cited by the source paper)? **Not general balance of all Rote factors — only this specific sequence of roots.**

## Step 1 (original to this phase): the exact reduction to a classical rotation-discrepancy problem

Take `u$ the **lower mechanical word** of slope `\gamma`: `u_n=\lfloor(n+1)\gamma\rfloor-\lfloor n\gamma\rfloor`, so `k_i(W)=\lfloor i\gamma\rfloor` exactly for `W=u[0{:}\ell]` (intercept `0`; `ROTE_TRANSFER_THEOREM.md` already established the transfer theorem is intercept-agnostic, so this choice costs no generality for *this* step, though the *initial-square-existence* fact quoted in Step 3 below does implicitly use a specific intercept convention, consistent with how the source paper's own Theorem 10.2 is stated).

`V_i = k_i(W)\bmod2 = \lfloor i\gamma\rfloor\bmod2$ (the even-weight case; the odd-weight case's `R=V\bar V` differs from `V` only by a bitwise complement on alternating blocks, which changes discrepancy by at most an `O(1)` additive term relative to `V`'s own — a direct consequence of `SQUARE_DISCREPANCY_COROLLARY.md`'s non-accumulation fact applied one level up — so it suffices to bound `D(V)`).

**Claim:** `\lfloor i\gamma\rfloor` is even `\iff \{i\gamma/2\} < 1/2`, i.e. `V` is **exactly the coding of the rotation by `\beta:=\gamma/2$ against the fixed half-half partition `\{[0,1/2),[1/2,1)\}`, coded `1` on `[1/2,1)`.**

**Proof of claim.** `\lfloor i\gamma\rfloor=2m\iff 2m\le i\gamma<2m+1\iff m\le i\gamma/2<m+1/2\iff\{i\gamma/2\}<1/2` (taking `m=\lfloor i\gamma/2\rfloor`; boundary case `\{i\beta\}=1/2` exactly is impossible for `i\ge1`, `\beta$ irrational, since it would force `\beta=(2m+1)/(2i)\in\mathbb Q`). `\blacksquare`

**This is exactly a mismatched two-interval rotation coding, of the same species as `ROTATION_CODING_AUDIT.md`'s Phase 1 rotation-coding instance** — a structural connection not previously observed explicitly in Phase 1: **CS Rote sequences and non-Sturmian two-interval rotation codings are, at the level of this specific root-discrepancy question, the same underlying mechanism** (rotation by a derived angle, coded against a partition that generically does not match the rotation angle).

## Step 2 (cited, classical, not re-derived from first principles): discrepancy of an interval under a bounded-partial-quotient rotation

Write `\beta=[0;a_1,a_2,\ldots]`, convergent denominators `q_k`. **Classical fact (three-distance theorem territory; see e.g. Kuipers & Niederreiter, *Uniform Distribution of Sequences*, Ch. 2–3, or any standard treatment of the discrepancy of `\{n\beta\}`):**
```
N\cdot D_N^*(\beta) = O\Big(\sum_{i=1}^{k}a_i\Big),\qquad q_k\le N<q_{k+1},
```
where `D_N^*(\beta)$ is the star-discrepancy of `\{\beta,2\beta,\ldots,N\beta\}`. **Koksma's inequality** (elementary, Abel-summation-based, standard): for any function `f` of bounded variation `V(f)`,
```
\Big|\sum_{i<N}f(\{i\beta\}) - N\!\int_0^1\! f\Big| \le V(f)\cdot N D_N^*(\beta).
```
Applying this to `f=\mathbb 1_{[1/2,1)}` (`V(f)=2`, two jump discontinuities):
```
\big|\,\#\{i<N:\{i\beta\}\ge1/2\} - N/2\,\big| \le 2\,N D_N^*(\beta) = O\Big(\sum_{i=1}^k a_i\Big),\quad q_k\le N<q_{k+1}.
```
If `\beta$ has **bounded partial quotients** (`a_i\le A` for all `i`), `\sum_{i\le k}a_i\le Ak`. Since `q_i\ge F_i` (the `i`-th Fibonacci number, as `a_i\ge1`) grows at least geometrically, `k=O(\log q_k)=O(\log N)`. Hence
```
\big|\#\{i<N:\{i\beta\}\ge1/2\}-N/2\big| = O(A\log N) = O(\log N).
```

## Step 3: assembled bound on `D(V)`

`k_j(V)=\#\{i<j:\{i\beta\}\ge1/2\}`, and the count's deviation from `j\cdot k(V)/\ell` (the definition of `D`, using the *finite-word* density, not the limiting `1/2`) differs from the deviation-from-`j/2` bound above by at most `|k(V)/\ell - 1/2|\cdot j \le |k_\ell(V)-\ell/2| \le O(\log\ell)$ itself (density converges to `1/2` at the same `O(\log\ell)/\ell` rate, by the `N=\ell` case of the same bound) — so the two notions of deviation agree up to another `O(\log\ell)` term. **Combining:**
```
D(V_n) = O(\log \ell_n)
```
for Sturmian slopes `\gamma` with bounded partial quotients (`\beta=\gamma/2` then also has bounded partial quotients — an elementary continued-fraction fact, halving an irrational changes its CF by a bounded shift in the tail, not affecting boundedness).

## Computational corroboration (not a substitute for the proof above, but a direct check it isn't secretly wrong)

`phase2/scripts/verify_rote_root_discrepancy.py`: golden ratio and silver ratio slopes, `\ell` up to `4000`, exact `Fraction` discrepancy. `D(V_\ell)` grows from `1` (`\ell=10`) to only `3`–`4` (`\ell=4000`) — **not** linear (`\theta=D/\ell\to0$ rapidly, e.g. `\approx0.00075` at `\ell=4000`), and `D(V_\ell)/\log\ell` stays roughly bounded (`0.36`–`0.62` across three orders of magnitude in `\ell`) — consistent with the proved `O(\log\ell)` rate, not merely with a weaker `o(\ell)`.

**Contrast test (unbounded partial quotients, `a_i=i`):** at the tested scale (`\ell\le15000`), discrepancy *also* looks sub-linear (`D/\ell\to0`), but this is **not covered by the proof above** (`\sum_{i\le k}a_i$ is no longer `O(k)`, and the bound in Step 2 can fail once a very large `a_i` is reached at an `N`-scale comparable to `q_i`) — the bounded-scale test simply hasn't reached such an `i` yet. **This case is left explicitly open, not claimed.**

## Status: PROVED (bounded partial quotients), OPEN beyond that

```
PROVED — for every Sturmian slope with bounded partial quotients (Target B's exact hypothesis, `THEOREM_TARGET.md`), D(V_n) = O(log ell_n) = o(ell_n).
OPEN — PRECISE MISSING LEMMA for unbounded-partial-quotient slopes: a version of Step 2's classical bound valid without the boundedness hypothesis (the genuine classical theory here is delicate — Liouville-type β can make D_N^*(β) grow without any uniform rate, and Sturmian numbers with unbounded partial quotients are exactly the ones the source paper's own cited fact identifies as potential Liouville numbers in Φ-value, a structurally relevant coincidence noted but not pursued further here).
```

This closes exactly the gap `THEOREM_TARGET.md` anticipated: Target B (bounded partial quotients) is now fully supported by a proved discrepancy bound, not merely three computational instances.
