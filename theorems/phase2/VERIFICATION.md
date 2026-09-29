# VERIFICATION.md

All scripts in `phase2/scripts/`, outputs in `phase2/data/`. Exact integer/`Fraction` arithmetic decides every pass/fail; floating point appears only in display lines (ratios, log-scale summaries), never in a verification decision.

| Script | Verifies | Result |
|---|---|---|
| `verify_core_identities.py` | (1) `v_2(M_n)=\text{lcp}(s,W^\infty)` exactly, 4 cases | **PASS** |
| | (2) `c_W\le\ell\cdot3^{\lceil D\rceil}\cdot\max(2^\ell,3^k)`, exhaustive, every nonzero word `\ell\le14` (32,752 words) | **PASS, 0 failures** |
| | (4) rational control: eventually-periodic `s`, surplus against lengthening periods of the true period `\to-\infty$ | **PASS** (qualitative; see limitation below) |
| `verify_rote_transfer.py` | `L_v=L+1` exactly, 11 diverse `W` `\times` 4 period counts (44 cases: even/odd weight, even/odd `\ell`, `\ell=2` to `9`, all-ones roots) | **PASS, 44/44** |
| `verify_rote_root_discrepancy.py` | `D(V_n)=O(\log\ell_n)` for golden/silver ratio Rote roots, `\ell` to `8000`; unbounded-PQ contrast | **Consistent with `O(\log\ell)`** (not a formal proof-checker — corroboration of the analytic bound) |
| `verify_weight_parity.py` | weight formula `\text{weight}(u[0{:}q_k])=p_k-[k\text{ odd}]` exact; eventual-cycle-contains-`0` for 5 quadratic irrationals | **PASS, formula exact on 88 total convergent points across 5 slopes; all 5 cycles contain `0`** |

## Bugs caught and fixed in this phase (disclosed, not hidden)

1. **`find_cycle` false-positive periods** (`verify_weight_parity.py`): an early version matched only a 3-symbol local window, reporting a spurious period-`1` cycle inside a genuine period-`6` pattern (three consecutive equal symbols occur naturally inside the real cycle). Caught by the script's own downstream assertion failing unexpectedly (`bronze ratio` initially reported `contains 0 = None` due to insufficient data, and `golden`/`bronze`/`[0;1,3,...]` reported `False` from the false period). Fixed by requiring the candidate period to explain the **entire** remaining tail of the sequence, not a short local match; re-verified with more continued-fraction terms.
2. Phase 1's CF-evaluator reciprocal bug (`PHASE1_FREEZE.md` §5) — not re-encountered in this phase's own CF code (`verify_weight_parity.py`, `verify_rote_root_discrepancy.py` both use a freshly written, independently-checked `cf_convergent`, cross-validated by the `weight(u[0{:}q_k])=p_k-[k\text{ odd}]` **exact** identity holding on every one of 88 tested points — a strong internal consistency check that would have failed loudly had the CF evaluator been wrong again).

## Known limitation, disclosed

`verify_core_identities.py`'s "rational control" test (Test 4) is qualitatively but not deeply illustrative: the chosen eventually-periodic `s` and candidate periodic root happen to mismatch at position `0` (`L=0` throughout), so the test confirms surplus `\to-\infty` as powers lengthen but does not exercise a scenario with substantial initial agreement (`L>0`) before the preperiod forces divergence. A more elaborate rational control (matching `SURPLUS_THEOREM.md`'s uniform-bound theorem against a genuinely deep partial match) was not built in this phase — the **theorem** (`SURPLUS_THEOREM.md` §8) is proved independently of this specific script, so this is a disclosed gap in *computational* corroboration depth, not in the proof itself.

## What was not re-verified

Every Phase 1 computational claim (`PHASE1_FREEZE.md`, checksummed) is taken as given, not re-run in this phase — this phase's scripts test only the **new** identities introduced here (exact `L+1` transfer, weight-parity cycles, the `O(\log\ell)` discrepancy behavior), consistent with the instruction to freeze Phase 1 rather than re-litigate it.
