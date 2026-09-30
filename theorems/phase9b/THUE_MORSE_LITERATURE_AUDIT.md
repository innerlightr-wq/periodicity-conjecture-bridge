**NOT NEW — AND NEITHER IS THE CS ROTE LADDER. AN EXPLICIT PRIOR THEOREM SUBSUMES BOTH.**

# THUE_MORSE_LITERATURE_AUDIT.md

## 0. Headline

`Φ(Thue–Morse) ∉ ℚ` is an immediate consequence of **Monks–Yazinski (2004), Theorem 2.7(b)** — a
refereed result that this programme's **own foundation paper cites, states and uses**. The same
deduction subsumes every CS Rote theorem in this repository (Phases 2, 4, 6, 8, 9) and the whole
Phase 9 substitution sweep.

## 1. The explicit prior theorem

> **Monks, K. G. and Yazinski, J., *The autoconjugacy of the 3x+1 function*, Discrete Mathematics
> **275** (2004), 219–236. Theorem 2.7.** Let `x ∈ ℚ_odd`.
> **(a)** If the orbit of `x` is eventually cyclic then `lim_n κ_n(x)/n` exists and
> `ln2/(ln3 + 1/m) ≤ lim κ_n(x)/n ≤ ln2/(ln3 + 1/M)`, where `m, M` are the least and greatest
> cyclic elements of `O(x)`.
> **(b)** If the orbit of `x` is divergent then `ln2/ln3 ≤ lim inf_n κ_n(x)/n`.
>
> Here `ℚ_odd` = rationals with odd denominator in reduced form (`= ℚ ∩ ℤ₂`), and `κ_n(x)` is the
> number of **odd** elements among the first `n` orbit terms — i.e. the number of `1`s in the first
> `n` entries of the parity vector of `x`. Read first-hand from the authors' PDF.

Monks–Yazinski state that (b) extends to all of `ℚ_odd` an inequality Lagarias had recorded for
integers whose orbit diverges to `±∞` ([4, eq. (2.31)]).

### 1.1 The deduction, stated verbatim in this programme's own foundation paper

De Jesús, *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic Integer*, §8
("What is known"):

> "Monks and Yazinski [16, Theorem 2.7(b)] proved that if `x ∈ ℚ ∩ ℤ₂` has a `T`-orbit which is not
> eventually cyclic — equivalently, whose orbit set is infinite — then `liminf_{n→∞} k_n(v(x))/n ≥ β`.
> Since a word is eventually periodic if and only if its `Φ`-value has an eventually cyclic orbit,
> this gives at once: **if `v` is aperiodic and `liminf k_n(v)/n < β`, then `Φ(v) ∉ ℚ`.**"

with `β = ln2/ln3 = log₃2 = 1/log₂3 = 0.6309297535714575…`. The paper adds that the deduction "is
made explicitly by that preprint [12, p. 6]".

**Thue–Morse is aperiodic with `liminf k_n/n = 1/2 < β`. Apply the boxed sentence. Done.**

## 2. The other half of the dichotomy

> ***The 3x+1 periodicity conjecture in ℝ*, arXiv:2101.12747 (2021),
> Theorem 1.** `Φ` maps an aperiodic parity word of lower ones-density **strictly greater** than `β`
> to an aperiodic (hence irrational) 2-adic integer; and if a rational 2-adic integer had a
> non-cyclic trajectory its lower ones-density would be exactly `β`.

Read first-hand (abstract and Theorem 1). **Status: arXiv preprint, not established as refereed.**
Its `Φ` is the same map as ours (their displayed series for `Φ(v)` matches source-paper Prop. 2.1).

Together: **everything except lower ones-density exactly `β` was already known**, with the
below-`β` half refereed (2004) and the above-`β` half a preprint (2021).

## 3. Classification of the Phase 9 claims, in the four categories requested

| claim | category | prior result |
|---|---|---|
| `Φ(Thue–Morse) ∉ ℚ` (Phase 9 Cor. 4.1) | **(a) explicit prior theorem, applied** | Monks–Yazinski 2004 Thm 2.7(b), density `1/2 < β`. Refereed. |
| Phase 9 Cor. 4.2, the 15 sweep members with density `< β` | **(b) consequence of an existing theorem** | Monks–Yazinski 2004 Thm 2.7(b). Refereed. |
| Phase 9 Cor. 4.2, the 4 sweep members with density `> β` | **(b) consequence of an existing theorem** | arXiv:2101.12747 (2021) Thm 1. **Preprint only.** |
| Phase 9 Theorem 3 (CS Rote, unbounded type) | **(b) consequence of an existing theorem** | CS Rote has ones-density exactly `1/2 < β`; Monks–Yazinski 2004. |
| Phase 8 Theorem 2, Phase 6, Phase 4, Phase 2 CS Rote theorems | **(b) consequence of an existing theorem** | same — all at density `1/2`. |
| Phase 9 Theorem 4, the `g(γ)` threshold (a *criterion*, not a class) | **(c) not located in the searched literature** | it is a refinement of this repository's own Phase 1 unconditional theorem; no external source searched for or found. Novelty **unresolved** — and it is a minor sharpening, not a headline. |
| The foundation paper's own theorem at density **exactly** `β` | **not subsumed** | the paper says so itself: "outside the critical density the conclusion for that family was already available". |

## 4. Why every class in this repository is subsumed

**CS Rote sequences have ones-density exactly `1/2`, for every irrational slope and every intercept.**
`v_n = v_0 ⊕ (k_n(u) mod 2)` and `k_n(u) = ⌊nγ+ρ⌋ − ⌊ρ⌋`, so `v_n = 1` iff `{(nγ+ρ)/2}` lies in a
fixed half-length interval; `γ/2` is irrational, so Weyl equidistribution gives density exactly `1/2`
— **with no bounded-type, intercept or parity hypothesis**. Measured over `3·10^5` terms for the
golden, silver, an unbounded-type and the critical slope, at two intercepts each: all `0.5000 ± 2·10⁻⁵`.

Since `1/2 < β`, Monks–Yazinski 2.7(b) applies to **every aperiodic CS Rote sequence directly**.
The bounded-type hypothesis, the intercept analysis, the Ostrowski machinery, the weight-parity
work, the growth condition — none of it is needed for the *conclusion*.

For the substitution sweep: for a `k`-uniform substitution the letter frequencies are the normalised
left Perron eigenvector for the **integer** eigenvalue `k`, hence rational, hence `≠ β` (which is
irrational). Measured: 15 of the 21 lie below `β`, 4 above, **none at `β`** (the 2 remaining are the
`k = 2` rows, densities `1/3` and `1/2`, both below).

## 5. Why the repository's own prior-art passes missed this

`PRIOR_ART.md` records three adversarial searches, all for the **mechanism**: the 2-adic
depth-versus-height bridge (Phase 1), weight-parity + transfer + three-distance discrepancy
(Phase 2), and the exact final chain (Phase 4). **None asked whether the *conclusion* was already
available by a different route.** Both halves of the fact were in the repository:

- `theorems/phase1/FALSIFICATION_REPORT.md` cites Monks–Yazinski's density argument explicitly, as a
  "completely different mechanism" reaching `Φ(1c_γ) ∉ ℚ` for `γ < β`;
- `docs/EOC_HANDOFF_CLOSED.md` §6, `README.md`, `LADDER.md` and `THEOREM_STATUS.md` all record that
  CS Rote one-density is **exactly `1/2`** and that `β = 0.63093`.

They were never combined. The novelty framing throughout ("crossing the counting frontier") compares
only against the **Dubickas counting** route, which indeed fails at complexity `2n` — but the
**density** route does not care about complexity at all.

## 6. What this does and does not mean

- It does **not** mean any theorem here is *false*. Every proof audited across Phases 8, 9 and 9B
  stands. The bridge is a different, genuinely 2-adic mechanism.
- It does mean the **novelty claims** are wrong: the classes reached were already covered.
- The one place the machinery is not subsumed is **density exactly `β`** — which is precisely where
  the foundation paper's own main theorem lives, and which it already claims correctly.
- The honest description of Phases 2–9 is therefore: *an independent second proof, by a different
  mechanism, of results already available from the density dichotomy* — plus a body of exact
  structural work (the driver identity, the weight law, the attainment routing) that is about the
  mechanism rather than the class.

## 7. Search record

Targeted searches run: Thue–Morse × Collatz/3x+1 parity vector; automatic sequences × Collatz
parity; Bernstein–Lagarias conjugacy × morphic/automatic; rational 2-adic trajectories × parity
density. Sources read first-hand: Monks–Yazinski 2004 (full PDF, Theorem 2.7 and surrounding text);
arXiv:2101.12747 (2021) (abstract, conventions §1, Theorem 1 statement and its citation of
Monks–Yazinski at line 1643 of the extracted text); Rozier arXiv:1805.00133 (full PDF — *not*
relevant: it concerns the inverse transform, ergodicity on small invariant sets, cycles and a plane
embedding; it contains no density theorem and no mention of Thue–Morse or automatic sequences, so
the search-engine summary attributing a density result to it was wrong); the foundation paper
(full text, §§1, 8, 12). Dvořáková–Medková–Pelantová arXiv:2003.06916 was read at abstract level
only in Phase 8 and is **not** used anywhere here.

**Standing caveat.** Absence of a hit is not proof of absence. But in this case the audit did not
return "no result found": it returned an **explicit prior theorem**, with a number, hypotheses and
a first-hand reading — and the deduction already written out in the programme's own paper.
