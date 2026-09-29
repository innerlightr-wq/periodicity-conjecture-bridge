# SQUARE_DISCREPANCY_COROLLARY.md

## Corollary S, restated

> **COROLLARY S.** If an aperiodic binary word `s` begins in infinitely many squares `W_nW_n` with `|W_n|=\ell_n\to\infty` and `D(W_n)=o(\ell_n)`, then `\Phi(s)\notin\mathbb Q`.

## Adversarial attack, item by item

**Must `W_n` be primitive?** No — `SURPLUS_THEOREM.md` §6–7 proves using a non-primitive `W_n` (a proper power of a shorter root) only **decreases** the achieved surplus relative to using the primitive root generating the same `W_n^\infty`, never invalidates the argument. **The corollary's hypothesis does not need a primitivity clause**; it is stated without one deliberately, and remains correct. (Using primitive roots is advisable only for obtaining the *strongest* witness sequence, not for correctness.)

**Could `W_n^\infty = s`?** This would require `s` to equal a purely periodic infinite word, contradicting the hypothesis that `s` is **aperiodic**. **Aperiodicity of `s` automatically guarantees `s\ne W_n^\infty` for every finite `W_n`, for every `n`** — the standing hypothesis of `ABSTRACT_IRRATIONALITY_CRITERION.md` is satisfied identically by the corollary's own hypothesis, with no per-`n` verification needed. This closes what looked like a potential gap cleanly.

**Do repeated powers create degeneracies?** No — already resolved in `SURPLUS_THEOREM.md` §6–7: `(W^m)^\infty=W^\infty` identically, so using a power never changes `L_n`, only degrades `F`. No degenerate case (division by zero, valuation blow-up, etc.) arises; the worst outcome is simply a weaker margin.

**Can density approach `1`?** Yes, freely — `REPETITION_SURPLUS_THEOREM.md`'s density-free theorem holds **uniformly** for every `\gamma_n\in(0,1)`, including sequences with `\gamma_n\to1` or `\gamma_n\to0`, since the bound `\max(1,\gamma\log_23)<\log_23` is strict on the **entire open interval**, not merely away from the endpoints. No degradation of the corollary as density approaches either extreme (only *equals* `0` or `1` are excluded, and those correspond to `k_n=0` or `k_n=\ell_n$, i.e. `W_n` constant — excluded automatically since a constant `W_n` gives `\text{lcp}(s,W_n^\infty)` bounded by the length of `s`'s own longest constant run, which cannot grow to `\ge2\ell_n$ for arbitrarily large `\ell_n` unless `s` itself is eventually constant, again periodic, excluded by aperiodicity).

**Does discrepancy of `W` versus of the infinite extension `W^\infty` differ?** This is worth deriving explicitly, since it is not obvious a priori. For `i=q\ell+r` (`0\le r<\ell`, `q\ge0`), `k_i(W^\infty) = qk+k_r(W)$ (each full period contributes exactly `k` ones), and `i\gamma = (q\ell+r)k/\ell = qk+r k/\ell`. So `k_i(W^\infty)-i\gamma = k_r(W)-rk/\ell$, which is **exactly the same quantity bounded by `D(W)`, for every `q`** — i.e. discrepancy of any-length prefix of `W^\infty` **does not accumulate over repeated periods**; it is uniformly bounded by the single-period value `D(W)`, regardless of how many periods are examined. **`D(W)` is therefore the correct and already-tight controlling quantity — no hidden growth exists across the infinite extension.**

**Does denominator cancellation change the argument?** No — resolved in `ABSTRACT_IRRATIONALITY_CRITERION.md`: the argument never forms or reduces `c_W/\delta_W` as a fraction; cancellation is structurally irrelevant to both the valuation step and the archimedean bound.

## Conclusion

**Corollary S survives every adversarial attack unchanged. Status: PROVED**, as an immediate consequence of `REPETITION_SURPLUS_THEOREM.md`'s density-free theorem at `r_n\equiv2>\log_23`, combined with the discrepancy-non-accumulation fact derived above (which confirms `D(W_n)=o(\ell_n)` — discrepancy of the finite root — is exactly the right and sufficient hypothesis, with no reinterpretation needed for the infinite periodic extension). This is the general abstraction of the source paper's Theorem 10.1, holding for *any* aperiodic binary word, Sturmian or not — the form that §§8–11 will attempt to instantiate for CS Rote sequences.
