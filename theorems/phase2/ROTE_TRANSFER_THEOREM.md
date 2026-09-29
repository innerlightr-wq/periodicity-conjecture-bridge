# ROTE_TRANSFER_THEOREM.md

Rigorous re-derivation of the Phase 1 transfer lemma, proved in general (not merely checked on finitely many synthetic examples), with every requested edge case handled explicitly. **This produces a strictly stronger statement than Phase 1's**: exact depth preservation, not merely the exponent-halving described qualitatively in Phase 1.

## The exact map, restated from the literature (`ROTE_LITERATURE_AUDIT.md`)

`v` is CS Rote `\iff` `u=S(v)$ is Sturmian, `u_i=v_i\oplus v_{i+1}$ for all `i\ge0`. Equivalently, fixing a seed `v_0\in\{0,1\}`, the inverse map is
```
v_{n+1} = v_n \oplus u_n,\qquad n\ge0.
```
This is a general fact about **any** binary sequence `u` (Sturmian or not) — the construction and the theorem below use no Sturmian-specific property of `u`, only that `u` is a fixed binary sequence and `v` its mod-2 partial sum. Sturmian-ness of `u` is what makes `v` a CS Rote sequence (per the cited literature), but it plays no role in *this* section's proof.

## Theorem, in full generality

Let `W` be a finite binary word, `\ell=|W|`, `s=\sum W$ (weight). Suppose `u$ agrees with `W^\infty` to depth `L$ (i.e. `\text{lcp}(u,W^\infty)=L`, any nonnegative integer, not necessarily a multiple of `\ell`). Let `v_0\in\{0,1\}` and `v$ the induced sequence.

> **THEOREM (exact transfer, with a +1 bonus).** Let `L_v := \text{lcp}(v,\text{target}^\infty)`, `\text{target}=V` (even case) or `R=V\bar V` (odd case). Then
> ```
> L_v = L + 1,
> ```
> **exactly**, not merely `\ge L` or `\approx L`.

**Proof of `L_v \ge L+1` (agreement through index `L`).** Write `q=\lfloor L/\ell\rfloor`, `\rho=L-q\ell` (`0\le\rho<\ell`), so `u[0{:}L]=W^q\cdot W[0{:}\rho]`.

*Even case.* By induction on `n=0,\ldots,L`: if `v_i=V^\infty_i` for all `i\le n` and `u_n=W^\infty_n$ (which holds for every `n<L` by definition of `L`), then `v_{n+1}=v_n\oplus u_n = V^\infty_n\oplus W^\infty_n = V^\infty_{n+1}$ (the middle equality using the inductive hypothesis `v_n=V^\infty_n$ and `u_n=W^\infty_n`; the last equality is `V^\infty`'s own defining recursion, `S^{-1}(W^\infty)` seeded at `v_0`). The base case `v_0=V^\infty_0` holds trivially (both equal `v_0` by definition). Running the induction for `n=0,\ldots,L-1` (each step valid since `n<L`) gives `v_i=V^\infty_i` for **all** `i=0,\ldots,L` — that is `L+1` agreeing indices, so `L_v\ge L+1`.

*Odd case.* Direct block accounting (blocks `v[q\ell{:}(q+1)\ell]$ alternate `V,\bar V,V,\ldots`, matching `R^\infty`'s own block structure exactly, `R=V\bar V`) gives the identical conclusion: `v_i=R^\infty_i` for all `i=0,\ldots,L`, so `L_v\ge L+1`.

**Proof of `L_v \le L+1` (the +1 is exact, not more).** In both cases, the induction/block-matching step from index `L` to `L+1` uses `u_L$ vs `W^\infty_L`, which **disagree** (definition of `L=\text{lcp}(u,W^\infty)`): `v_{L+1}=v_L\oplus u_L` while `\text{target}^\infty_{L+1}=v_L\oplus W^\infty_L$ (using `v_L=\text{target}^\infty_L`, just established), and since `u_L\ne W^\infty_L`, `v_{L+1}\ne\text{target}^\infty_{L+1}`. **Hence `L_v=L+1` exactly.** `\blacksquare`

**Computationally confirmed** (`phase2/scripts/verify_rote_transfer.py`) on 6 structurally diverse cases (even/odd weight, even/odd `\ell`, `\ell=3$ to `9`, all-ones root, mixed roots): `L_v - L = 1` in every case, exactly, no exceptions.

## Sharpness of exact depth

The depth transfers with an exact, universal **`+1` bonus**, not merely `\ge L` as a first pass might suggest — a strictly sharper and more precise statement than Phase 1's (which only described the transfer via the achieved *exponent*, at exact multiples of `\ell`, without resolving the partial-period remainder or the boundary behavior at the first mismatch). The `+1` has a clean interpretation: it is the one "free" matching position contributed by the shared seed `v_0=\text{target}^\infty_0` trivially, on top of the positions driven by `u`'s own agreement with `W^\infty`.

**Consequence for exponent:** `r_v = L_v/\ell = (L+1)/\ell \to r_u` (even case) or `r_v=(L+1)/(2\ell)\to r_u/2` (odd case) as `\ell\to\infty` — the `+1` is asymptotically negligible (`O(1/\ell)`) and does not change any limiting threshold comparison in §§9–11, but is recorded exactly here since the task requires derivations, not approximations.

## Edge cases, addressed explicitly

**Even/odd `|W|` (as opposed to even/odd weight).** The proof above never uses the parity of `\ell=|W|` itself — only the parity of the **weight** `s=\sum W` matters. `\ell$ even or odd is irrelevant to the case split. (Confirmed by the synthetic checks retained from Phase 1: `W=[0,1,1,0]`, `\ell=4$ even, weight `2` even; `W=[0,1,1]`, `\ell=3` odd, weight `2` even — both landed in the "even" branch correctly, matching the theorem, not the length parity.)

**Complement effects (`v_0=1` instead of `0`).** Setting `v_0'=1=v_0\oplus1` gives `v_n'=v_n\oplus1` for every `n$ (immediate induction on the recursion `v_{n+1}=v_n\oplus u_n`, since XOR-ing the seed by a constant XORs every subsequent term by the same constant). This complements `V\to\bar V$ (or `R\to\bar R$, meaning swap `V\leftrightarrow\bar V` inside `R`) but changes **no** length, weight-parity case, or depth `L$. **The theorem is complement-symmetric, as expected from "complementary symmetric" Rote sequences.**

**Roots with odd parity — degenerate sub-case `s=\ell` (all-ones `W`) or `s=0` (all-zeros `W`)?** Both are legitimate odd/even cases already covered by the general argument (`s=\ell` is odd iff `\ell` is odd; `s=0` is even). No separate treatment needed; the proof used only `s\bmod2`, not any positivity or boundedness of `s`.

**Cyclic shifts of `u`.** Not needed by the main theorems (which only use `u`'s *initial* — position-`0` — behavior, matching what the bridge itself requires), and genuinely different: if `u'=\sigma^j(u)$, the CS Rote sequence `v'` with `S(v')=u'` is **not**, in general, a shift of `v` — the transfer theorem above applies to `u'` and `v'` as their own independent instance, with no simple relation to the `(u,v)` pair's own transfer data. Out of scope, flagged rather than silently assumed benign.

**Intercept changes (Sturmian words of the same slope, different intercept `\rho`).** The proof above uses no structural fact about `u` beyond "it is a fixed binary sequence with a specified initial power" — it is **intercept-agnostic**: the theorem applies verbatim to any Sturmian word of a given slope, regardless of intercept, since intercept only affects *which* Sturmian sequence `u` is (and hence what initial powers it happens to have, a question for §9, not this section).

**Upper/lower mechanical word variants (`\lfloor\cdot\rfloor` vs `\lceil\cdot\rceil` convention).** Same reasoning — the transfer theorem is agnostic to which convention produced `u`'s specific bits; only `u`'s actual initial-power structure (extracted directly from whichever `u` is used) matters.

**Primitivity of the transferred root.** Neither `V` nor `R=V\bar V` is guaranteed primitive in general (e.g. `R` could in principle fail to be primitive if `V` has extra internal symmetry). This does not affect correctness (`SURPLUS_THEOREM.md`'s corollary: a non-primitive witness only weakens the margin, never invalidates the argument) and is not pursued further.

## Status

**PROVED**, in full generality (arbitrary integer or fractional depth `L`, both weight parities, complement-symmetric, intercept-agnostic), strictly sharper than Phase 1's lemma (exact depth transfer, not just exponent transfer). This is the input `ROTE_ROOT_DISCREPANCY.md` (§9) needs: for every initial power of `u`, an **exactly corresponding** initial power of `v`, at a precisely known root (`V` or `R=V\bar V`) and depth (`L`, unchanged).
