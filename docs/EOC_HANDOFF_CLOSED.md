# EOC handoff: route closed

**Status: ROUTE CLOSED / CIRCULAR.** This document records the outcome of a falsification-first
cross-program audit (2026-09-29) that tested whether the periodic-approximation and
arithmetic-height bridge developed in this repository can be handed off to the surviving
divergence sector of the companion EOC programme,
[`innerlightr-wq/eoc-divergence`](https://github.com/innerlightr-wq/eoc-divergence).

It changes no theorem in this repository. The bounded-type CS Rote theorem
(`theorems/phase6/BOUNDED_TYPE_THEOREM.md`) and every other proved result stand exactly as
stated. What this document records is a **limit on their applicability to one specific external
question**.

**Novelty discipline.** The qualitative conclusion was already on record in both programmes
before this audit — EOC Revision 7's Observation 5.9 ("the separating invariant is height
amortization, not symbolic complexity") and this repository's own `LADDER.md` closing note (no
purely repetition-based method can close the Periodicity Conjecture alone). *The audit supplies
the exact identity, the quantified obstruction, and certified verification — not the original
qualitative observation.* Nothing here is claimed as new mathematics beyond that.

---

## 1. The exact question tested

The EOC programme's headline reduction (`Divergence.divergent_iff_zeroConfined`, machine-checked,
no hypotheses) is

```
    ∃ M odd with a divergent 3x+1 orbit   ⟺   ∃ m odd that is zero-confined,
```

where `m` is *zero-confined* when `2^{S_n} ≤ 3^n` at every depth `n`, with
`a(m) = v₂(3m+1)`, `T(m) = (3m+1)/2^{a(m)}`, `S_n = Σ_{i<n} a(T^i m)`.

A divergent integer orbit has `Φ(s) = m₀ ∈ ℚ` for its parity word `s`, and `s` is not eventually
periodic. So any theorem of the form "property `P` ⟹ `Φ(s) ∉ ℚ`" excludes divergent orbits whose
parity word has `P`. The tested chain was:

```
    divergent integer orbit
        ↓
    EOC survivor constraints (zero confinement, and everything else EOC proves)
        ↓
    periodic approximants W_n with unbounded surplus            ← the step under test
        ↓
    Φ(s) ∉ ℚ                                                     ← this repository's Theorem T4
        ↓
    contradiction
```

**The middle step was not assumed.** The audit's task was to prove it, disprove it, or isolate
the missing lemma.

## 2. The exact 2-adic dictionary

Both programmes code the same map; this repository uses the standard Lagarias coding
(`T(x) = x/2` or `(3x+1)/2`), EOC the accelerated one. The standard parity word of an odd `m` is
`concat_i (1 0^{a_i − 1})`, so at accelerated depth `n` one has `ℓ = S_n`, `k = n`, and
`c_W = C_n` (the EOC aggregate carry). Under `v₂(Φ(a) − Φ(b)) = lcp(a,b)`:

```
    x_i ≡ x_j  (mod 2^L)      ⟺      s[i : i+L] = s[j : j+L]
```

and, specialised to prefixes (`W_ℓ := s[0:ℓ]`),

```
    lcp(s, W_ℓ^∞)  =  ℓ + v₂( m₀ − T^ℓ(m₀) ).
```

Both directions are exact. The `⟹` half is the EOC repository's
`Divergence.modEq_of_parity_prefix`; the `⟸` half is the Terras / Bernstein–Lagarias bijectivity
of `Q_L : ℤ/2^L → {0,1}^L`. **Verified exactly** on 400 random odd seeds below `10¹²` × 12 000
`(i,j,L)` triples, and on every zero-confined checkpoint of 17 certified EOC record holders:
0 failures.

Consequence for this repository's own toolkit: *only prefixes can carry positive surplus.* If
`lcp(s, W^∞) < |W|` then, on the zero-confined sector, `c_W ≥ 3^{k−1} ≥ 2^{|W|}/3`, so
`S_s(W) < log₂ 3`. The search over "useful periodic roots" is one-parameter.

## 3. The handoff identity (H1)

> **Theorem H1.** Let `m₀ ≥ 1` be an integer with standard parity word `s`, let `ℓ ≥ 1`,
> `W = s[0:ℓ]`, `k = |W|₁`, `d = 2^ℓ − 3^k`, and suppose `x_ℓ := T^ℓ(m₀) ≠ m₀`. Then
>
> 1. `M := m₀ d − c_W = 2^ℓ (m₀ − x_ℓ)` — the EOC aggregate identity `2^{S_n} m_n = 3^n m₀ + C_n`,
>    rearranged;
> 2. `lcp(s, W^∞) = ℓ + v₂(m₀ − x_ℓ)`;
> 3. with `h_eff := |M| / F(W) ∈ (0, m₀]` and `F(W) = |d| + c_W` the proof-native height of
>    `theorems/phase2/ABSTRACT_IRRATIONALITY_CRITERION.md`,
>    ```
>        S_s(W)  =  log₂ h_eff  −  log₂ oddpart(x_ℓ − m₀);
>    ```
> 4. hence **`S_s(W) ≤ log₂ m₀` for every `ℓ`**, strictly when `m₀ > 1`;
> 5. on the zero-confined sector (`d < 0 < c_W`) the archimedean step is an *equality*:
>    `|M| = m₀|d| + c_W`.

Verified exactly at 1 862 zero-confined checkpoints across 15 certified record holders, plus
400 random odd seeds × 130 prefix lengths: 0 failures.

Equivalent quantified form, with `R_n = S_n − n log₂ 3` the EOC drift:

```
    S_s(W)  =  v₂(m₀ − m_n)  − |R_n|  +  O(log n).
```

## 4. Interpretation

**Integer realizability caps the very surplus that this repository's criterion needs to become
unbounded.** `Φ(s) = m₀ ∈ ℤ` means `u = m₀`, `v = 1`, so the criterion's height is `H = m₀` — a
fixed finite number once the orbit is fixed. Theorem T4's hypothesis `limsup_n S_s(W_n) = +∞` is
then not merely unproved on this sector; by H1(4) it is **unsatisfiable**.

More sharply, the bridge does not fail here — it *evaluates*. On the zero-confined sector its
surplus is a two-term function of the aggregate identity alone, and inequality `(‡)` reduces to
`2^{v₂(m₀−m_n)} ≤ |m₀ − m_n|`, a triviality. This is the quantitative form of EOC Revision 7
§5.3/§5.9, which already wrote down the same dichotomy in the accelerated coding and recorded the
branch as vacuous for arbitrary confined words.

## 5. Consequence, and why the gap is circular

The bridge's most general sufficient condition — `theorems/phase1/REPETITION_HEIGHT_CRITERION.md`,
"arbitrarily long initial squares suffice, unconditionally" — contraposes, via the dictionary of
§2 and the elementary growth bound `x_{t+1} ≤ (3x_t+1)/2`, to:

> **Theorem H2a.** If the parity word of an integer `n₀ ≥ 1` begins in a square `WW` with
> `|W| = L` and `T^L(n₀) ≠ n₀`, then `4^L ≤ 3^L (n₀+1)`, i.e.
> `L ≤ log₂(n₀+1)/(2 − log₂ 3) = 2.4094 log₂(n₀+1)`.

So the step under test — "EOC survivor constraints ⟹ arbitrarily long initial squares" — holds
**iff** no zero-confined positive odd integer exists, i.e. iff EOC's open problem (DE) is true.
The middle implication is the conclusion restated.

> **The bridge cannot exclude general EOC survivors by forcing unbounded periodic-approximation
> surplus.** Not because the forcing is hard, but because the surplus it would have to force is
> capped by `log₂ m₀` as an identity, and the repetition it would have to exhibit is capped by
> `2.4094 log₂(n₀+1)` for the same reason.

Corollaries recorded for completeness, neither claimed as new:

* The survivor sector carries topological entropy `H₂(1/α) = 0.949956` bits per standard letter,
  so it does not force low factor complexity. Certified EOC survivor windows sit at 87–100 % of
  the combinatorial complexity ceiling and have longest initial-square half-length 1–8.
* The transported Dubickas rung (`Cor. 9.3`, threshold `1/log₂(3/2) = 1.7095112913514547`) has
  **zero margin** against an integer seed: the hypothesis of Cor. 9.3 is the exact negation of
  the conclusion of Prop. 9.2, with the same constant. The corresponding complexity floor for a
  divergent orbit, `p_s(L) ≥ ⌊(L − 1 − log₂ m₀)/log₂(3/2)⌋ + 1`, is a **specialization of
  Proposition 9.2** with `H₀ = m₀`, not a new theorem.

## 6. Density incompatibility with the headline class

This is the reason the audit's answer is "closed" rather than "partly open".

Zero confinement is exactly `2^ℓ ≤ 3^{k_ℓ}` at every 1-position, i.e. asymptotic one-density
`≥ β = 1/log₂ 3 = 0.6309297535714575`. Complementary symmetric Rote sequences have one-density
**exactly `1/2`** — and that is not incidental: it is `theorems/phase4/REQUIRED_EXPONENT.md`'s
own load-bearing structural fact, the one that drops the required repetition exponent from
`2 log₂ 3 ≈ 3.17` to `2` and makes the bounded-type theorem close.

Since `1/2 < β`, **no CS Rote sequence is zero-confined**, at any slope, either seed, any shift,
and any fixed corridor width `c` (`2^{S_n} ≤ 2^c 3^n`). Measured over 2 000 shifts × both seeds ×
4 slopes: best confined depth 5–13 at `c = 0`, and 317–333 at `c = 64` — widening the corridor by
64 bits buys `~320` letters and then stops, exactly as a constant density mismatch predicts.

> The bridge's new reach past the Dubickas counting threshold is purchased with precisely the
> property that excludes it from the EOC survivor sector. Phases 2–7 are **vacuous** there.

The rungs that *do* meet the sector — eventually periodic words, Sturmian words, sub-threshold
complexity — were already excluded inside the EOC programme itself (its signed marker P1; its
`audits/sturmian_all_words` theorem, `Φ(s) ∉ ℚ` for *every* Sturmian word; and Rev 7's
density exclusion). Net effect of this repository's Phase 2–7 results on the EOC survivor set:
**zero**.

## 7. What remains open, and where it is not

Nothing in this document bears on the 3x+1 Periodicity Conjecture, which remains open, and
nothing here claims the Periodicity Bridge helps prove the Collatz conjecture — it does not.
EOC's (DE) and (PosPC) remain open exactly as before.

The one clean implication found running from EOC into this repository's machinery is:

> **band rigidity ⟹ Sturmian ⟹ irrational.** If a zero-confined orbit's drift stays in a unit
> band `β ≤ R_j < β+1` forever, then (EOC Rev 7 App. A = Rev 5 Thm A.1) its valuation word is a
> Sturmian factor of slope `α − 1`, its standard parity word is the image of a Sturmian word
> under the Sturmian morphism `0 ↦ 1, 1 ↦ 10`, and hence `Φ(s) ∉ ℚ`.

Its hypothesis is "the orbit does not diverge": a divergent orbit has `R_n → −∞` and leaves every
fixed band. Measured unit-band windows on certified survivors are **4–9 accelerated letters**
long. Proved, and empty on the target sector.

## 7b. Cross-program limits, stated plainly

Consolidated 2026-09-29, after two further EOC-side audits (drift/amortization, and the
least-realizer deficit) reached the same kind of closure. For citation purposes:

1. **The Periodicity Bridge remains valid for its proved structured sectors.** Sturmian words,
   the transported counting classes, and bounded-type complementary symmetric Rote sequences are
   unaffected by anything here; `THEOREM_STATUS.md` and `LADDER.md` stand exactly as written.
2. **It does not currently exclude general EOC survivors.** The surplus criterion's hypothesis
   is unsatisfiable on the integer-realizable zero-confined sector (§3–§4), and the headline
   CS Rote class is disjoint from that sector by density (§6).
3. **Integer realizability caps the relevant surplus.** `S_s(W) ≤ log₂ m₀`, an identity, not an
   estimate — verified at 1 862 confined checkpoints with 0 failures.
4. **Zero-confinement words can retain high symbolic complexity.** The confined sector carries
   topological entropy `H₂(1/α) = 0.949956` bits per standard letter; an explicit
   Champernowne-driven confined word has `p(18) = 3 543` and longest initial-square half-length
   `3`. Confinement forces no repetition and no low complexity.
5. **This repository should not be cited as a path to the Collatz conjecture under the presently
   proved EOC constraints.** It is a programme on the Periodicity Conjecture for structured
   symbolic classes; the handoff to divergence exclusion is closed, as recorded here.

None of this is a claim that no conceivable variant of a repetition- or approximation-based idea
could ever work. It is a statement about **this** mechanism under **these** hypotheses.

## 8. Status

```
    ROUTE CLOSED / CIRCULAR
```

for the handoff from this repository's periodic-approximation and arithmetic-height mechanism to
the EOC divergence sector. The mechanism is silent there, correctly, and the audit's control
battery confirms it is silent for the right reasons (it stays silent on rational periodic
controls and on the `3x−1` system's zero-confined positive point `+1`, and it does not falsely
settle `5x+1`, where divergence occurs and the threshold `log₂ 5 > 2` correctly blocks it).

## Audit record

The audit workspace (22 deliverables, 8 exact-arithmetic verification scripts, standard library
only) is not committed to any repository. Its verdict file is `HANDOFF_VERDICT.md`; the
companion route-closure note on the EOC side is
[`notes/PERIODICITY_HANDOFF_ROUTE_CLOSED.md`](https://github.com/innerlightr-wq/eoc-divergence/blob/main/notes/PERIODICITY_HANDOFF_ROUTE_CLOSED.md)
in `eoc-divergence`, and the consolidated index of all three closed pointwise routes — with a
negative-results table — is
[`notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md`](https://github.com/innerlightr-wq/eoc-divergence/blob/main/notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md).

Repository states audited: this repository at `e4708a2`, `eoc-divergence` at `de2fdea`,
`eoc-lean-verification` at `6cb67e7`.
