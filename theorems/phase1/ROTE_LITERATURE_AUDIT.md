# ROTE_LITERATURE_AUDIT.md

## Definitions and sources actually found (adversarial search, not assumed)

**Rote sequence**: a binary infinite word `v` with factor complexity `C_v(n) = 2n` for every `n ≥ 1`. Originally studied by Rote (1994, cited as [24] in Dvořáková–Medková–Pelantová 2020, arXiv:2003.06916). A Rote sequence is **complementary symmetric (CS)** if its language is closed under the letter exchange `0↔1`.

**The exact structural fact** (Rote 1994, confirmed and used throughout Dvořáková–Medková–Pelantová 2020): `v` is a CS Rote sequence **if and only if** `u = S(v)` is Sturmian, where `S` is the first-difference-mod-2 map: `u_i = v_i ⊕ v_{i+1}` for all `i`. Equivalently — the direction this audit needs — given any Sturmian `u` and a seed bit `v_0`, there is a unique CS Rote sequence `v` (and its complement) with `S(v)=u`, obtained as the mod-2 partial sum ("discrete antiderivative") of `u`: `v_{n+1} = v_n ⊕ u_n`.

**Complementary symmetric Rote sequences, 2n complexity**: confirmed by Medková's own return-word papers (arXiv:1812.03748, "Derivated sequences of complementary symmetric Rote sequences") — `C_v(n)=2n` for all `n≥1`, and: "a complementary symmetric Rote sequence is primitive substitutive if and only if its associated Sturmian sequence is primitive substitutive."

## Critical exponent results found — and why they do NOT directly answer this audit's question

**Dvořáková–Medková–Pelantová (2020, arXiv:2003.06916)**, *Complementary symmetric Rote sequences: the critical exponent and the recurrence function* (DMTCS vol 22:1, #20):
- Give an exact formula (Theorem 33) for `cr(v)` — the **critical exponent** of a CS Rote sequence `v` (sup of exponents of powers occurring **anywhere** in `v`, via `ind_v(v) = sup` of the *index* of every factor, not restricted to prefixes) — in terms of the continued-fraction/S-adic directive sequence of the associated Sturmian `u=S(v)` (Theorem 14 gives the general `v`-vs-`S(v)` relation via return words to bispecial factors).
- The **global minimum** of `cr(v)` over **all** CS Rote sequences is `2+1/√2 ≈ 2.707` (proved by Currie–Mol–Rampersad, cited as [8], resolving a conjecture of Baranwal–Shallit), strictly larger than the paper-derived bridge threshold `log₂3 ≈ 1.585`.
- The minimum `cr(u)` over **all** Sturmian sequences is reached by the Fibonacci word, `cr(fib) = 3+(1+√5)/2 ≈ 4.62` (their stated value; the in-text numeric "∼3.602" appears to be a rendering artifact of the source PDF, not trusted verbatim — the algebraic formula is the reliable part).

**Ollinger–Shallit (2024, arXiv:2406.17867)**, *The Repetition Threshold for Rote Sequences*: proves the **repetition threshold** for the full Rote class (not just complementary-symmetric) is exactly `5/2`, via the Walnut automatic theorem prover. `5/2 = 2.5 > log₂3` as well.

**Why none of this settles the question this audit actually needs.** `cr(v)` (critical exponent, and the repetition threshold, which is an infimum of `cr` over the class) measures the largest exponent of a power occurring **anywhere** in `v` — it is not, by definition, about **initial** powers (the quantity `ABSTRACT_BRIDGE_THEOREM.md` and `REPETITION_HEIGHT_CRITERION.md` actually require: arbitrarily long *prefix* powers). The literature's own "initial critical exponent" (`ice`, studied for Sturmian words by Berthé et al., irif.fr/~berthe/Articles/sturm15.pdf, and generally `ice(ω) ≤ cr(ω)`, not always equal) is not addressed for Rote sequences in any source found in this search. **Reporting `cr(v)≥2.707` as if it settled "Rote sequences have arbitrarily long initial squares" would be an unsupported leap — flagged and avoided.**

## What this audit derived instead (original, not from the literature)

Given the confirmed exact construction `v_{n+1}=v_n⊕u_n`, `u` Sturmian, this audit proves an elementary **initial-power transfer lemma** (verified computationally, exact arithmetic, `scripts/rote_construction_test.py`):

> If `u` has an initial power `u[0:rℓ]=W^r` with root weight `s=Σ W`, then `v` inherits an initial power of exponent `r` at the **same** root length `ℓ` (if `s` even), or exponent `r/2` at root length `2ℓ` (if `s` odd — the "V, V̄, V, V̄, ..." alternation forced by the parity flip each period).

This is the correct, load-bearing fact for this audit — not the literature's `cr`/repetition-threshold results, which remain background context (they at least corroborate that Rote sequences are "repetition-rich" as a class in the qualitative sense, consistent with this audit's own direct finding below) but are not cited as the basis for any claim in `ROTE_COMPUTATIONAL_AUDIT.md`.

## Adversarial angle: is the bridge itself already known?

See `PRIOR_ART_BRIDGE.md` for the full search; summary here: the closest established body of work (Ferenczi–Mauduit 1997; Adamczewski–Bugeaud, Schmidt Subspace Theorem-based combinatorial transcendence) proves transcendence/irrationality via **archimedean** repetition arguments in continued-fraction or base-`b` expansions, using Roth's theorem's multidimensional extension. The bridge audited here is a **non-archimedean (2-adic) elementary integer-comparison** argument (`M_n = uδ_n − vc_n`, depth vs. height, no Roth/Schmidt machinery). No source found in this search states or uses this specific 2-adic mechanism for parity-vector/Bernstein–Lagarias-style sequences; it appears to be the source paper's own construction, not a rediscovery of a named prior theorem — reported as a **negative search result** (absence of a hit is not proof of absence, and is reported with that caveat).
