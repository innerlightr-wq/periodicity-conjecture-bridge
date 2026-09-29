# ROTE_DISCREPANCY_AUDIT.md

## Re-derivation: does the arithmetic theorem need `D(R)` or `D(V)`?

**`D(R)`, unambiguously** — `DISCREPANCY_HEIGHT_PROOF.md`-type bounds are applied to whatever word supplies `c_W` in `\Phi(W^\infty)=c_W/(2^{|W|}-3^{|W|_1})`; in the odd-weight branch that word is `R`, not `V`. Re-confirmed: `\text{HALF_DENSITY_HEIGHT_REDERIVATION.md}` used `D(R)` throughout, correctly.

## Deriving `D(R)` from `D(V)`, from scratch

`D(R):=\max_{0\le i\le2\ell}|k_i(R)-i/2|$ (density `1/2`, exact — `HALF_DENSITY_HEIGHT_REDERIVATION.md`). For `i\le\ell`: `k_i(R)=k_i(V)`, so `|k_i(R)-i/2|=|k_i(V)-i\gamma_V+i(\gamma_V-\tfrac12)|\le D(V)+\ell|\gamma_V-\tfrac12|` (`\gamma_V=|V|_1/\ell`, `D(V)` relative to *`V`'s own* density). For `\ell<i\le2\ell`, `j=i-\ell`: `k_i(R)=k_\ell(V)+k_j(\bar V)=k_\ell(V)+j-k_j(V)`, and a short computation gives `|k_i(R)-i/2|=|(k_\ell(V)-\ell\gamma_V)-(k_j(V)-j\gamma_V)+(\text{terms in }\gamma_V-\tfrac12)|\le2D(V)+\ell|\gamma_V-\tfrac12|$ (worst case, two `D(V)`-sized deviations). So:
```
D(R) <= 2*D(V) + ell*|gamma_V - 1/2|.
```

## The extra term: is `\ell|\gamma_V-\tfrac12|` bounded?

**This is the term Phase 4 needed and this audit re-derives independently, not by quoting Phase 4's own claim.** `\gamma_V=k_\ell(V)/\ell`; taking `i=\ell` in `D(V)`'s own definition gives `|k_\ell(V)-\ell\gamma_V|=0` trivially (it's `V`'s own count at its own full length) — **that's a tautology, not what's needed.** What's needed is `|\gamma_V-\tfrac12|` itself, i.e. how far `V`'s *actual* density sits from `1/2` — a fact about `V`, not extractable from `D(V)$ alone. **Re-derived via `V`'s own combinatorial origin**: `V_i=k_i(W)\bmod2` (`W=u[0{:}\ell]`), so `k_\ell(V)=\#\{i<\ell:k_i(W)\text{ odd}\}$. This is exactly the interval-count studied in `theorems/phase2/ROTE_ROOT_DISCREPANCY.md`'s reduction (coding of rotation by `\gamma/2` against `[1/2,1)`), and the *same* three-distance/Koksma bound (below) gives `|k_\ell(V)-\ell/2|=O(\log\ell)` directly — i.e. `\ell|\gamma_V-\tfrac12|=O(\log\ell)`, **not** merely bounded but sublinear, for bounded-partial-quotient slopes. Combined: `D(R)\le2D(V)+O(\log\ell)$, and `D(V)` itself is `O(\log\ell)` by the identical mechanism (one level down, on `W$ instead of `V`) — **`D(R)=O(\log\ell)` overall, confirmed independently.**

**Numerically re-checked** (`scripts/phase5/rote_discrepancy_independent.py`, golden-ratio slope, `\ell` to `1400`): `D(R)` (measured against the correct target density `1/2`) tracks `D(V)` plus a small, non-growing gap term, consistent with `O(\log\ell)`, not linear growth — matches the derivation above.

## Auditing the cited discrepancy theorem's hypotheses, precisely

The mechanism used (`ROTE_ROOT_DISCREPANCY.md`, re-verified here): `N\cdot D_N^*(\beta)=O(\sum_{i\le k}a_i)` for `q_k\le N<q_{k+1}` — this is the **star discrepancy** of the orbit `\{i\beta\}_{i<N}` (sup over *all* intervals, a `\ge` bound on any specific interval's own discrepancy — valid to use as an upper bound for our one specific interval, direction-checked: using a bound for the worst interval is always safe as an upper bound for a better-behaved specific one). Koksma's inequality (elementary, standard: `|\sum f(\{i\beta\})-N\int f|\le V(f)\cdot N D_N^*(\beta)` for `f` of bounded variation `V(f)`) applies to `f=\mathbb 1_{[1/2,1)}$ (`V=2`), giving the **prefix-count deviation** (not literally "prefix discrepancy" as a named technical term, but exactly the quantity `|k_i(V)-i/2|$ we need) — **hypothesis match confirmed**: bounded partial quotients (needed for `\sum_{i\le k}a_i=O(k)=O(\log N)`); interval type (any fixed interval, our `[1/2,1)` qualifies); starting point (the bound is uniform in the starting phase, since it bounds the *orbit's* discrepancy, not a single trajectory's transient); constants depend on the slope only through the partial-quotient bound `A`, exactly as used.

## Verdict

`D(R)=O(\log|R|)` for bounded-partial-quotient slopes, **re-derived independently from `D(V)$ plus an explicitly-bounded extra term**, not merely asserted by citing `theorems/phase2/ROTE_ROOT_DISCREPANCY.md`. No gap found; the citation's hypotheses genuinely match the use.
