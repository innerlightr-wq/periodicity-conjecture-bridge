# ROTATION_CODING_AUDIT.md

*(Literature-dependent claims below are marked; the structural/mathematical framing is derived independently of the pending literature search and stable regardless of its outcome.)*

## What generalizing the coding means, precisely

The Sturmian mechanical words `1c_γ, 0c_γ` are codings of the rotation `x ↦ x+γ` by the **specific** two-interval partition `\{[0,1-γ), [1-γ,1)\}` (equivalently, by `⌈(j+1)γ⌉-⌈jγ⌉`). A general two-interval coding replaces this with an **arbitrary** partition `\{[a,a+γ), [a+γ,a+1)\}` (any base point `a`, not tied to the rotation angle's own fractional structure) — i.e. `s(j) = 1` if `\{jγ+a\} ∈ [0,γ)` else `0`, for arbitrary `γ,a`.

**Key structural fact** (standard three-distance-theorem territory, re-derivable from the source paper's own machinery, not requiring new citation): for **any** two-interval coding of an irrational rotation, the orbit `\{jγ+a \mod 1\}` partitions `[0,1)` into at most 3 distinct gap lengths at any finite stage (the three-distance theorem), and the coding's factor complexity is `p_s(L) ≤ 2L` generically (matching the `2L` figure the source paper flags at Section 12, Open Problem (4)), with equality typically unless the interval endpoints are chosen to coincide with orbit points of the rotation itself (in which case complexity can drop back to the Sturmian `L+1`, recovering the special case). **This is why two-interval codings and Rote sequences are the natural "next rung": both sit at the `2L` complexity level the source paper's own counting route (`Corollary 9.3`) cannot reach.**

## Applying `CERTIFICATE_DEPENDENCY_MAP.md`'s sharpened requirement

Per this audit's central simplification, the *only* question that matters is: **do two-interval rotation codings possess arbitrarily long initial powers of exponent `>log₂3≈1.585`?** Discrepancy/balance is no longer a separate concern (it is automatically controlled, per `DISCREPANCY_HEIGHT_THEOREM.md`'s unconditional cap, for *any* word, rotation-coded or not).

## Convergents and prefix agreement — does the Sturmian mechanism transfer?

The source paper's depth law (Theorem 5.3/8.3) is proved using **two exact identities specific to the intercept-0 mechanical word** (`m_{p_{n+1}} = p_n-1` and the convergent-difference identity, `CURRENT_BRIDGE.md` Classification F) — these do **not** transfer to a general intercept `a`, exactly as the source paper's own Remark 8.9 / Section 12 Open Problem (1) already states for the *Sturmian* case at nonzero intercept. A fortiori, they should not be expected to transfer automatically to a general two-interval coding either. **However**, per the certificate map, the depth-law route is not what is needed here — only the *initial-squares* route is, which needs no continued-fraction identity at all (`CURRENT_BRIDGE.md` Classification F, confirmed the Section 10 route is continued-fraction-free).

## What would need to be true (pending literature confirmation)

1. **[Literature-dependent]** A published or derivable guarantee that general two-interval rotation codings contain initial powers of exponent `≥2` (or any fixed threshold `>log₂3`), analogous to Theorem 10.2 for the Sturmian case.
2. **[Not literature-dependent, already established]** If (1) holds for a specific coding with any density/arrangement, irrationality of `Φ(s)` follows immediately and unconditionally, with no further combinatorial input.

This sharply reduces the open question for this rung to a single, well-posed combinatorial fact about initial repetitions of two-interval codings — see `ROTE_LITERATURE_AUDIT.md` for the closely related (per the literature search) question about Rote sequences specifically, since the two classes are reported in the literature to be closely connected.

## Computational test (Part 9, resolved for one concrete instance)

`scripts/rotation_coding_test.py` builds the coding `s_n = 1` iff `{nγ+ρ}∈[0,δ)` for `γ` = golden ratio conjugate (exact high-precision `Fraction` continued-fraction convergent — **a reciprocal bug in the CF evaluator was caught and fixed mid-session**, see `ROTE_COMPUTATIONAL_AUDIT.md`'s disclosure; this script was re-run after the fix), `δ=1/3` (deliberately mismatched from `γ`), `ρ=0`.

**Complexity confirmed exactly `2n`** for `n` up to 30 (e.g. `p_s(30)=60`), genuinely exceeding the Sturmian `n+1` bound — a real, verified non-Sturmian instance, not assumed.

**Initial squares found, with exact positive surplus**:
- `ℓ=233, r≈2.412, S=316` (exact integer lower bound, `bridge_surplus_exact`)
- `ℓ=89, r≈2.079, S=86`

**Verdict for this instance: the bridge reaches this non-Sturmian two-interval rotation coding**, exactly and unconditionally at these two depths (both `r>2`, both certified per `REPETITION_HEIGHT_CRITERION.md`'s unconditional theorem, confirmed directly via exact surplus computation). This is one concrete instance, not a general theorem over all `(γ,δ,ρ)` — but it is the first confirmed non-Sturmian rotation-coding member of Rung C (`PERIODICITY_LADDER.md`).
