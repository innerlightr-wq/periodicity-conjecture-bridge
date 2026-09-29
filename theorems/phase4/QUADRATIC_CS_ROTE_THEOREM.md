**PROVED — PRECISE SUBCLASS**

# QUADRATIC_CS_ROTE_THEOREM.md

## Statement

> **THEOREM.** Let `\gamma\in(0,1)` be any quadratic irrational, `A` the largest partial quotient in its eventually-periodic continued fraction, `u` its lower mechanical (intercept-`0`) Sturmian word. Let `v` be **either** complementary-symmetric Rote sequence with `S(v)=u` (seed `v_0\in\{0,1\}`), or **any shift** `\sigma^j(v)` of such a `v`. Then
> ```
> Phi(v) not in Q.
> ```

## Auditing the quantifiers, as required

- **Canonical representative only?** No — both seed choices `v_0\in\{0,1\}` are covered (`ROTE_TRANSFER_THEOREM.md`'s complement-symmetry: identical period/exponent/surplus structure either way).
- **Every shift?** **Yes, covered — but via a *different*, already-established fact, not by re-running the argument.** `\Phi(\sigma(s))=T(\Phi(s))` for a fixed bijection `T` (Proposition 2.3, cited in `theorems/phase1/SURPLUS_INVARIANT.md`), so `\Phi(s)\notin\mathbb Q \iff \Phi(\sigma(s))\notin\mathbb Q` for **any** shift `\sigma`. Once `\Phi(v)\notin\mathbb Q` is proved for the seed-`0`/`1` representatives at position `0`, every shift is free.
- **Every member of the associated CS-Rote subshift, i.e. every intercept?** **No — this is the honest limit of what is proved here.** A CS Rote sequence `v'` associated with a *different* intercept of `\gamma` (i.e. `S(v')=u'` for `u'$ a Sturmian word of slope `\gamma` but a different starting phase than `u`) is generally **not** a shift of `v` (shifting `v` changes the associated Sturmian word to a shift of `u`, not to an independently-chosen different intercept). The specific quantitative bound this theorem rests on (`INITIAL_EXPONENT_FORMULA.md`'s `\text{term2}>2+1/(A+1)`) was derived for the `\omega(-\gamma)=0\omega` case (BHZ's Corollary 3.5, specialized) and **was not re-derived for BHZ's fully general (arbitrary-intercept) Corollary 3.5 formula**. BHZ's own cited universal fact (`\text{ice}(\omega)\ge2$ for *every* Sturmian sequence, any intercept) is suggestive that the theorem likely extends, but this phase does not complete that extension.
- **Every intercept — the missing lemma, if Target Q is read as fully general.** State precisely: *does `\text{term2}(k)>2+\varepsilon(A)$ (uniformly, some fixed `\varepsilon(A)>0`) hold for BHZ's general Corollary 3.5 expression, at every intercept `c\in\prod_k\{0,\ldots,a_k\}$, not just `c\equiv0`?* Not attempted here.

## Classification

```
PROVED — PRECISE SUBCLASS: every complementary symmetric Rote sequence v with S(v) a SHIFT of the
  lower mechanical (intercept-0) Sturmian word of any quadratic-irrational slope gamma (both seeds,
  every shift of v covered). NOT proved: CS Rote sequences associated with other intercepts of the
  same slope gamma (a well-posed, precisely stated, plausible-but-unattempted extension).
```

This is **strictly broader** than Phase 2's five-explicit-slope result (`theorems/phase2/ROTE_IRRATIONALITY_THEOREM.md`) — it now covers **every** quadratic irrational, not five — and **strictly narrower** than the most general possible reading of "every CS Rote sequence associated with a quadratic-irrational slope," for the intercept reason stated above.
