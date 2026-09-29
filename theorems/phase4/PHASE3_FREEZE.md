# PHASE3_FREEZE.md

## Repository state at Phase 4 start

```
HEAD:   f9ccf93f103da18601ee72f56aa4decc58289798
branch: main, tracking origin/main, up to date
status: clean (nothing to commit)
```

All 70 pre-existing tracked files (37 `theorems/phase{1,2,3}`, 15 `scripts/phase{1,2,3}`, 10 `data/phase{1,2,3}`, 1 `reference/*.pdf`, 7 top-level metadata files) checksummed exactly as they stand at this commit — full list in `theorems/phase4/PHASE4_CHECKSUMS.txt`, generated directly from the working tree, not retyped.

## What Phase 3 established (restated for reference, not modified)

1. The finite 8-node weight-parity automaton is exhaustively searched: exactly one bad (all-odd-weight-sustaining) cycle exists, `(A,0)\leftrightarrow(C,1)`.
2. A genuine counterexample was found: `\gamma=[0;1,1,1,\overline2]` has weight parity `0,0,1,1,1,1,1,\ldots` — all odd from index 2 onward, forever. **The universal "every quadratic slope has an even-weight witness" claim is false.**
3. Direct computation at this counterexample's standard-word witnesses (`q_k=1,1,2,3,8,19,46,111,268,\ldots`) showed the odd-weight halved-exponent route still certifies: at alternating `k`, `r_u\to2+\sqrt2\approx3.41421`, giving `r_v=r_u/2\to1.70711>\log_23\approx1.58496`, with exact surplus `S` growing `5\to55\to365\to2191\to12852\to75014\to437340` as `\ell` grows through `8,46,268,1562,9104,53062,309268`.
4. Four other all-even (or mixed-even) tails were spot-tested (`\overline4\to\ge5.23`, `\overline{2,4}\to\ge3.22`, `\overline6\to\ge7.16`), all clearing `2\log_23\approx3.16993`.
5. **Not closed**: no general proof that every all-even-tail quadratic irrational has `r_u\to\ge2+\sqrt2` (or any threshold `>2\log_23`). This is the exact Phase 4 target.

## Discipline for this phase

Phase 1–3 files are read-only from here. All new work lives under `theorems/phase4/`, `scripts/phase4/`, `data/phase4/`. No claim in this phase overwrites or silently reinterprets a Phase 1–3 statement — any apparent tension is reconciled explicitly, by reference, in the relevant Phase 4 file.
