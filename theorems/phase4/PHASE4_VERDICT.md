# PHASE4_VERDICT.md

## 1. What is the exact all-even-tail problem?

**It was not quite what it was named.** Phase 3 posed it as: does every quadratic-irrational slope whose continued-fraction tail is entirely even partial quotients still certify via the odd-weight Rote-transfer route? This phase found (`EVEN_TAIL_PROBLEM.md`) that "all-even tail" is not even the precise boundary of the weight-parity lock — a mixed-parity tail can also lock, given the right preperiod (e.g. `\overline{2,1}` with preperiod `(1,1,1,1)`). The real problem, correctly stated, is: **for any quadratic irrational whose standard-word witnesses are forced into the odd-weight (halved-root) Rote transfer, does the bridge still certify?** — a question independent of exactly which continued-fraction pattern causes the forcing.

## 2. Why did the even-weight shortcut fail as a universal principle?

Because the shortcut isn't universal by construction — the weight of `u`'s standard-word witnesses is governed by a finite automaton (Phase 3) that has one genuine "trap" cycle, `(A,0)\leftrightarrow(C,1)`, and any slope whose continued fraction feeds that trap forever (mixed or all-even, `EVEN_TAIL_PROBLEM.md`) produces witnesses with **no** even-weight option, ever. This is not a bug in the construction; it is a real structural feature of the mod-2 partial-sum map defining CS Rote sequences.

## 3. Why can odd-weight witnesses nevertheless succeed?

**Because the odd-weight route's transferred root `R=V\bar V` has density exactly `1/2`, always, by an elementary structural fact** (`REQUIRED_EXPONENT.md`: a word concatenated with its own complement is automatically half-and-half). This collapses the required threshold from the generic worst-case `\log_23\approx1.585` (used, incorrectly conservatively, throughout Phase 3) down to `\max(1,\tfrac12\log_23)=1` — meaning the odd-weight route only needs `r_u>2` (not `r_u>2\log_23\approx3.17`), a threshold Theorem 10.2 combined with the Berthé–Holton–Zamboni initial-critical-exponent formula supplies unconditionally, with an explicit margin `1/(A+1)` (`A`= largest partial quotient), for **every** bounded-partial-quotient slope.

## 4. What repetition threshold is actually required?

```
r_required = 2        (NOT 2*log2(3) ~ 3.170, and NOT 2+sqrt(2) ~ 3.414)
```
uniformly for **both** transfer routes (`TRANSFER_EFFICIENCY.md`): the even-weight case needs only `r_u>\log_23<2`, and the odd-weight case needs `r_u>2\cdot\max(1,\tfrac12\log_23)=2` exactly — so a single threshold, `r_u>2`, covers either mechanism. This is supplied, with a quantified positive margin, by `\text{ice}(u)>2+1/(A+1)` (`INITIAL_EXPONENT_FORMULA.md`), proved directly from the cited Berthé–Holton–Zamboni (2006) closed form, for **every** quadratic-irrational slope.

## 5. Was the `2+\sqrt2` working hypothesis correct, useful, or a mistake?

**A mistake, caught by this phase's own stress test, and instructive.** It was an exact fact about one specific slope (silver ratio) promoted, from four favorable examples, to a general lower bound it does not satisfy (`SILVER_EXTREMALITY.md`: a counterexample was found, `\text{ice}\approx3.1547<2+\sqrt2`). Actively searching for a counterexample (per this phase's own instruction, section 12) is exactly what surfaced this — and in doing so, exposed that the whole `2+\sqrt2`-vs-`2\log_23` comparison was solving a harder problem than necessary, because it never accounted for the odd-weight route's forced density of `1/2`.

## 6. What is proved, precisely, and what is the honest remaining gap?

**Proved** (`QUADRATIC_CS_ROTE_THEOREM.md`, classification `PROVED — PRECISE SUBCLASS`): `\Phi(v)\notin\mathbb Q` for every complementary symmetric Rote sequence `v` associated (via the intercept-`0` mechanical word, either seed, any shift of `v`) with **any** quadratic-irrational Sturmian slope. **Not proved**: CS Rote sequences at *other* intercepts of the same slope — a well-posed, precisely stated, plausible-but-unattempted extension, not a known obstruction.

## 7. Does this close the quadratic CS Rote rung of the ladder?

**Yes, for the stated precise subclass** — `LADDER.md` rung 3 is updated to `PROVED — precise subclass` accordingly. The rung is not claimed closed for literally every CS Rote sequence of every quadratic-irrational slope's full subshift (item 6's gap), so rung 4 (a genuinely new complexity class or the intercept extension) remains open, per this phase's own narrow-scope mandate.

## 8. Final status

```
TARGET: Close or precisely classify the all-even-tail quadratic-irrational CS-Rote case.
RESULT: Classified precisely, and CLOSED for a strictly larger class than originally scoped
        (every quadratic-irrational slope, not merely all-even-tail ones) -- because the correct
        general threshold (r_u>2) is far easier to meet than the originally-hypothesized one
        (r_u>2+sqrt(2)), making the tail-parity classification itself unnecessary for the theorem.
REMAINING GAP: one precisely stated intercept extension (item 6), not pursued.
NO advance to a new complexity class. NO paper drafted. Phase 1-3 files unmodified (checksum-verified).
```
