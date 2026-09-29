# PRIOR_ART_BRIDGE.md

Adversarial search: is the abstract bridge (`ABSTRACT_BRIDGE_THEOREM.md` — 2-adic depth lower bound `|M_n|≥2^{L_n}` vs. archimedean height upper bound `|M_n|≤H·F(W_n)`, contradiction as `L_n→∞`) already a known technique, under a different name, applied to this or an adjacent problem?

## What was searched

- "Adamczewski Bugeaud combinatorial transcendence method continued fractions Diophantine repetition"
- "2-adic Liouville number periodic approximation irrationality criterion combinatorics on words repetition depth height"
- "Dubickas irrationality 3x+1 parity sequence counting complexity transcendence"
- "Bernstein Lagarias 3x+1 conjugacy map parity vector 2-adic periodic approximation irrationality"

## Closest body of work found: Adamczewski–Bugeaud combinatorial transcendence

Ferenczi–Mauduit (1997) first combined combinatorics-on-words with Diophantine approximation, proving transcendence of numbers whose base-`b` expansion is Sturmian, via the **p-adic extension of Roth's theorem**. Adamczewski–Bugeaud subsequently generalized this considerably using the **Schmidt Subspace Theorem** (the multidimensional extension of Roth's theorem), producing transcendence criteria for numbers whose continued-fraction or base-`b` expansion is "quasi-periodic" — containing arbitrarily long blocks that recur precociously.

**Mechanism comparison**:
- **Adamczewski–Bugeaud**: archimedean (real- or `b`-adic-expansion) setting; repeated blocks feed into the Schmidt Subspace Theorem, a deep, non-elementary tool from Diophantine approximation over number fields.
- **This audit's abstract bridge** (and the source paper it generalizes): **2-adic** setting; repeated blocks feed into an elementary integer inequality (`|2^ℓ−3^k|`-based depth/height comparison) — no Roth/Schmidt machinery, no algebraic number theory beyond exact integer arithmetic. Structurally analogous **in spirit** (repetition ⟹ contradiction with rationality) but a **different, more elementary mechanism**, native to the 2-adic isometry property of `Φ` (`Proposition 2.2`) rather than to a general repeated-block Diophantine theorem.

**No source found in this search applies Adamczewski–Bugeaud-style methods, or any other named transcendence criterion, directly to Bernstein–Lagarias parity vectors / the 3x+1 conjugacy map `Φ`.**

## A genuinely adjacent, contemporaneous paper found

**Stephan (2026)**, *Transcendence criteria for the minimal word of the rational base 3/2*, arXiv:2609.19007 (submitted July 2026, revised September 2026 — essentially simultaneous with the source paper's own September 2026 date). Studies the orbit of `x_{n+1}=⌈3x_n/2⌉` and its associated `{0,1}`-word `w` (the "minimal word" of Akiyama–Frougny–Sakarovitch's rational base-`3/2` numeration, related to Dubickas's own prior work — the same Dubickas cited as `Corollary 9.3`'s source in the paper this audit is built on). Proves: automaticity of `w` ⟹ transcendence of the associated constant `K`; and **complexity exceeding every linear bound, or `K` irrational** — i.e. a **complexity-threshold irrationality criterion**, structurally the *counting* route (`Corollary 9.3`'s sibling), not the repetition/height route. **No mention found of a depth-vs-height 2-adic comparison, repetition measure in the sense used here, or the Bernstein–Lagarias framework.** This is close in flavor (a `3/2`-multiplier dynamical system, parity-type word, irrationality via combinatorial complexity) but methodologically on the **counting** side of the source paper's own two independent routes, not the **repetition/height (Liouville-style)** side this audit has been generalizing.

## Verdict

- **No direct prior-art hit** for the specific 2-adic depth-vs-height elementary bridge mechanism, applied to any word class. Absence of a hit in this search is evidence, not proof, of absence — a more exhaustive search (full-text database access, not just search-engine snippets) could not be performed here.
- **The counting/complexity route** (`Corollary 9.3`, transported Dubickas) sits in an actively-worked contemporary research area (Stephan 2026 being essentially simultaneous), confirming that route is *not* novel in kind, only in its specific transport to the 3x+1 setting (already acknowledged by the source paper itself).
- **The repetition/height route**, and this audit's generalization of it, appears to be structurally original relative to everything found — flagged with appropriate epistemic humility (a negative literature search result, not a proof of originality) rather than claimed as a discovery.
