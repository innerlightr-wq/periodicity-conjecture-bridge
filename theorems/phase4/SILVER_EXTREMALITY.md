**FALSE — COUNTEREXAMPLE**

# SILVER_EXTREMALITY.md

## Candidate statement (as posed)

> Among all eventually periodic Sturmian slopes whose periodic continued-fraction tail consists entirely of even positive integers, the smallest asymptotically available initial repetition exponent relevant to the CS-Rote bridge is attained by the all-`2` tail.

## Attack

Tested: period-1 tails `\overline{2m}` for `m=1,2,3`; period-2 all-even tails `\overline{2,4}`; **and, critically, mixed (not all-even) tails with a locking preperiod**, since `EVEN_TAIL_PROBLEM.md` shows the "all-even" restriction was itself not the correct boundary of the lock-sustaining class.

## Counterexample

`\gamma=[0;1,4,1,5,1,\overline{6,2}]` (preperiod `1,4,1,5,1`, periodic tail `\overline{6,2}`) sustains the weight-parity lock (verified, `scripts/phase4/lock_search.py`-style search) and has
```
ice(u) ≈ 3.1547005... < 2+√2 ≈ 3.4142136...
```
(exact value: a `Fraction`-computed algebraic number from the convergent ratios at the relevant phase, `data/phase4/even_tail_exhaustive.txt`). **The candidate statement is false as stated.**

## Actual extremal family — not determined, and not needed

This phase did not find the true infimum over all lock-sustaining tails (a search over 3 locked-entry values × 8 free-entry values × preperiods to length 5, `EVEN_TAIL_MINIMIZATION.md`, is not exhaustive over all periods and preperiod lengths). **This is left explicitly unresolved** — but see `EVEN_TAIL_SURPLUS.md`: it does not need to be resolved, because `REQUIRED_EXPONENT.md`'s actual threshold (`r_u>2`) is cleared by every tested value with room to spare (smallest margin found: `\approx1.15`, still far from `0`), and `INITIAL_EXPONENT_FORMULA.md` proves a **uniform, uncoditional** lower bound `\text{ice}(u)>2+1/(A+1)>2` for **any** bounded-partial-quotient slope (max partial quotient `A`), making a search for the exact extremal tail unnecessary for the theorem this project needs.

## Classification

```
FALSE — COUNTEREXAMPLE (the specific "silver ratio is extremal at 2+sqrt(2)" claim)
```
but this failure is immediately superseded — the correct, general, unconditional bound (`INITIAL_EXPONENT_FORMULA.md`) makes the extremality question moot for the purposes of `QUADRATIC_CS_ROTE_THEOREM.md`.
