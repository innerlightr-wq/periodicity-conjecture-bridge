# MULTIPLIER_DIAGNOSTIC.md

Diagnostic only, per the task's instruction — not a `qx+1` project. Confirms the abstract theorem captures the phenomenon the source paper's own Remark 10.7 already observes.

## Formal verification via the abstract theorem

For a general odd multiplier `q`, the periodic-value formula (Proposition 4.1's structure, replacing `3\to q` by direct analogy — the conjugacy map's own construction is `q$-independent in form, only the specific dynamics change) gives `\delta_W=2^\ell-q^k`, `F(W)=|\delta_W|+c_W` with `c_W=\sum_{i:W_i=1}q^{k-k_{i+1}(W)}2^i`. Repeating `ABSTRACT_IRRATIONALITY_CRITERION.md`'s derivation verbatim with `3\to q` throughout (nothing in Steps 1–4 used the specific value `3`, only that it is odd, which every odd `q` satisfies, keeping `\delta_W` odd):
```
S \ge r\ell - \max(1,\gamma\log_2q)\cdot\ell - o(\ell).
```

## Why `q=3` is special for universal square-based arguments

`r=2` clears the threshold `\max(1,\gamma\log_2q)` **uniformly over every density** `\iff 2>\sup_\gamma\max(1,\gamma\log_2q)=\log_2q$ (by the identical argument as `REPETITION_SURPLUS_THEOREM.md`'s density-free theorem) `\iff q<4`. Since `q` is odd, the multipliers satisfying this are exactly `q\in\{1,3\}` (`q=1` trivial/degenerate), i.e. **`q=3` is the unique nontrivial odd multiplier for which squares alone suffice at every density, unconditionally.**

For `q\ge5`: `\log_2q\ge\log_25\approx2.3219>2`, so **there exist densities** (`\gamma` close to `1`, specifically `\gamma>2/\log_2q`) **at which squares (`r=2`) no longer suffice**, even with perfect (zero) discrepancy — matching the source paper's own Remark 10.7, cited in Phase 1, identifying `q=5` as the first odd multiplier where the square-based method's universal coverage breaks down. **This phase's abstract theorem reproduces this threshold exactly and mechanically, confirming Remark 10.7 is a special case of the general `\log_2q` formula, not a `q=3`-specific coincidence requiring separate derivation.**

## Scope discipline

This is the full extent of the diagnostic. No `qx+1` conjugacy map is constructed, no `qx+1` analogue of Propositions 2.2/4.1 is proved, and no claim is made about `qx+1` Sturmian or Rote sequences — the formula above is a direct algebraic consequence of substituting `q$ for `3` in the already-proved threshold expression, offered only to confirm this phase's machinery correctly explains a phenomenon the source paper already flagged, not to open a new research direction.
