# CERTIFICATE_DEPENDENCY_MAP.md

## The paper's own stated chain (Section 10)

```
STURMIAN
  ↓
infinitely many initial squares (Theorem 10.2, ADQZ 2001)
  +
periodic roots are cyclic permutations of standard words, hence balanced (Theorem 10.3, BHZ 2006)
  ↓
low-height periodic approximants (Lemma 10.4, discrepancy<1 ⟹ constant 3)
  +
depth ≥ 2ℓ (trivial, from the square itself)
  ↓
positive Liouville surplus (margin c(γ) ≥ 2−log₂3 > 0)
  ↓
Φ(s) irrational
```

## Removing each box — what this audit found

**Remove "Sturmian complexity" entirely.** Nothing in the chain from "infinitely many initial squares" onward uses Sturmian-ness *as such* — only the two specific quoted facts (10.2, 10.3) do, and only to *establish* squares-exist and roots-are-balanced for the Sturmian class specifically. **Conclusion survives** for any class where those two facts (or weaker substitutes) hold. This is exactly why the audit's generalization program is well-posed.

**Remove "periodic roots are cyclic permutations of standard words" (Theorem 10.3), replace with "balanced" (`D=O(1)`) directly.** **Conclusion survives** — this is `DISCREPANCY_HEIGHT_THEOREM.md`'s `D=O(1)` case, a strict weakening of the hypothesis (many balanced words are not cyclic permutations of standard words — the paper's own Remark 10.7-adjacent note, line 1062-1067, gives four explicit examples: `0110, 1001, 01110, 10001`).

**Weaken further to "discrepancy `D=o(ℓ)`" (no balance at all).** **Conclusion survives** — `DISCREPANCY_HEIGHT_THEOREM.md`'s sublinear-discrepancy theorem, proved directly from Propositions 2.2/4.1 alone.

**Weaken further to "no discrepancy hypothesis at all" (arbitrary arrangement).** **Conclusion still survives**, provided the repetition exponent stays at `r=2` — `REPETITION_HEIGHT_CRITERION.md`'s unconditional theorem, using only the hard combinatorial cap `D(W)≤γ(1−γ)ℓ≤ℓ/4` that *every* word automatically satisfies. **This is the true minimal certificate for the `r=2` route: only "infinitely many initial squares" is needed. Balance, discrepancy control, and Theorem 10.3 are all dispensable.**

**Remove "infinitely many initial squares" (Theorem 10.2), replace with weaker repetition `r<2`.** **Conclusion fails in general** — `BRIDGE_CONTROLS.md` Control 3 gives an explicit example (`r=1.5`, `γ=0.95`, single-block root) where the margin turns negative. Repetition exponent strictly above `log₂3≈1.585` (uniformly in density) is load-bearing and **cannot** be dropped or weakened below that threshold without a separate argument.

**Remove repetition altogether (`r=1`).** **Conclusion fails always** — `REPETITION_HEIGHT_CRITERION.md`'s boundary-case remark, margin `≤0` for every density.

**Remove "`s ≠ W_n^∞`" (i.e. allow `s` itself periodic).** **Conclusion fails, correctly** — `BRIDGE_CONTROLS.md` Control 1; this is not a weakness of the method but the exact boundary the Periodicity Conjecture is about.

## The sharpened dependency map

```
ANY s (no Sturmian assumption)
  ↓
infinitely many initial squares  [LOAD-BEARING — cannot weaken below r>log₂3, uniformly in density]
  ↓
[nothing else needed: discrepancy is automatically capped at γ(1-γ)ℓ for
 every word, and this cap never threatens r=2's margin against log₂3]
  ↓
positive Liouville surplus (margin 2−log₂3 > 0, uniform in density)
  ↓
Φ(s) irrational
```

**Continued fractions** (Convention 5.1/8.1, Lemma 5.2/8.2, Theorem 5.3/8.3) belong to an **entirely separate, independent sub-certificate** (the Section 5–8 route, intercept-0 only) that this map does not touch — the paper itself notes the two routes are independent (Remark 10.6), and this audit's generalization program works exclusively with the **initial-squares route**, which is the one Section 10 itself already identifies as intercept-independent and therefore the natural one to generalize beyond Sturmian words.

## What this means for the search for new rungs

The true combinatorial certificate needed for a new class `𝒞` is now precisely identified: **`𝒞` must (a) provide arbitrarily long initial powers of exponent `r>log₂3≈1.585` (not necessarily squares — anything above this threshold works, per the uniform theorem), with (b) no further requirement on the roots' arrangement whatsoever.** This is a dramatically smaller ask than the paper's own quoted machinery (Theorems 10.2 **and** 10.3) — the search for Rote words, rotation codings, and morphic words (Sections 7–10 of the task) should therefore focus **entirely on (a)**, the existence of sufficiently long initial powers, since (b) is now known to be automatic.
