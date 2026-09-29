# INITIAL_POWER_QUANTIFIER_AUDIT.md

## BHZ's exact definition (primary source, §2.2)

`\text{ice}(\omega):=\limsup_{n\to\infty}(\text{prefix power of }\omega[0,n))`, where the *prefix power* of a word `w` in `\omega` is the largest `p` (possibly `\infty`) with `w^p` a prefix of `\omega`. **This ranges over every `n`, not a special subsequence** — Corollary 3.5's `\limsup_k\max(x(k),y(k))` is a **proven theorem** (not a definition) reducing this to a specific `k`-indexed family, not an assumption smuggled in.

## Distinguishing `\text{ice}(u)>2` from "arbitrarily long prefixes `W^r`, `r>2`"

**Not the same statement, and BHZ's own paper is explicit about the gap** (this is the paper's own headline example): the Fibonacci **characteristic** sequence has `\text{ice}=2` (attained, per their Theorem 1.1's characterization) yet — per their own Theorem 1.1 statement plus the general fact `\text{ice}\ge2$ — this does NOT immediately mean arbitrarily long genuine `r>2` prefixes exist for every Sturmian sequence. **The relevant fact this project needs is arbitrarily long prefixes with exponent *strictly and by a fixed margin* above `2`, which is a stronger requirement than `\text{ice}>2$ alone if `\text{ice}` is only approached, not exceeded, along the witness sequence.**

## A cleaner, more directly citable fact than Phase 4 used, found on this re-read

**BHZ, §5, immediately after Theorem 1.1** (read directly, not quoted from any Phase 1–4 file): *"In particular, no Sturmian shift with a quadratic slope can contain a sequence of `\text{ice}` equal to `2`."*" This follows because Theorem 1.1's minimality characterization for `\text{ice}=2` **requires unbounded partial quotients**, which a quadratic irrational never has. **This is a stronger, more direct, primary-source-stated fact than anything Phase 4 explicitly cited**: for *every* Sturmian sequence of *any* quadratic-irrational slope (not merely `\omega(-\gamma)$), `\text{ice}\ne2`, hence `\text{ice}>2` strictly (combined with the universal `\text{ice}\ge2`). Phase 4 derived its own `\text{ice}(u)>2+1/(A+1)` bound without citing this — the two are consistent, but Phase 4's own derivation is independently checked below rather than replaced.

## Re-verifying Phase 4's own algebraic bound, unconditionally over `k`

`\text{term2}(k)=1+a_{2k-1}+q_{2k-3}/q_{2k-2}`. Re-derived here from scratch: `a_{2k-1}\ge1` (every partial quotient) and `q_{2k-3}/q_{2k-2}=1/[a_{2k-2};a_{2k-3},\ldots,a_1]$, a **finite** reversed continued fraction whose value is `<a_{2k-2}+1` **regardless of how many further terms follow** (elementary: `[x;\text{rest}]<x+1` for any continued fraction with `\text{rest}\ge1`, independent of length). So `\text{term2}(k)>2+1/(A+1)` **for every single `k`**, not merely in the limsup — this was re-checked here and found to hold with no dependence on `k`'s size, so it applies to arbitrarily large `k` without degradation. **Re-confirmed, independently, in this audit.**

## Is the word achieving `\text{term2}(k)` an actual, growing-length prefix power?

**Yes — this is what BHZ's Corollary 3.5 proves, not assumes.** Re-reading their proof (the passage immediately preceding the Corollary): for each `k` they exhibit an **explicit word** (a specific substitution image, `\tau_0^{a_1}\circ\cdots\circ\tau_{k-1}^{a_k-c_k}(i)`, a cyclic permutation of it) that **is** a genuine prefix power of `\omega(-\alpha)` with exponent exactly `y(k)` (their own words: "this is exactly the value of `r`"), and their proof of the converse direction states the word-length formulas "do not depend on `r` or `m` at all" — i.e. the construction is unconditional in `k`. Since these substitution images strictly grow with `k` (each stage composes another morphism), **root length `\to\infty`** is guaranteed by construction, not merely plausible.

## What was NOT independently re-verified: the exact root-length formula

**Genuine, disclosed gap.** Phase 4's `even_tail_exhaustive.py` assumed the achieving word's length is `q_{2k-1}$ (a specific guess, testing a small index range and taking the best result) — **this specific identification was never derived from BHZ's own word-length formula**, which this audit did not fully extract either (it involves the substitution-image length, a more complex expression than a bare convergent denominator). **This does not threaten the theorem's correctness**, because Phase 4's computational check independently verified genuine achieved exponents via **direct `\text{lcp}` computation on the actual generated word** at several candidate lengths (not by trusting the formula's implied length) — the exact word-length correspondence is a presentation/bookkeeping gap in one script's comments, not a soundness gap in the proof.

## Conclusion

- `\text{ice}(u)>2` for quadratic `\gamma`: **confirmed two independent ways** (BHZ's own Theorem 1.1 corollary statement; Phase 4's algebraic `\text{term2}` bound, re-derived here unconditionally over `k`).
- Arbitrarily long, growing-length, actually-achieved prefix powers with this exponent: **confirmed**, via BHZ's own constructive proof of Corollary 3.5.
- Uniform (fixed, not vanishing) margin above `2`: **confirmed**, `1/(A+1)`, independent of `k`.
- The specific claim "achieved at root length `q_{2k-1}`": **not independently verified**, flagged as an unverified presentational detail in one Phase 4 script, not a mathematical gap.
