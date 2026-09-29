# BASELINE_FREEZE.md

## Public baseline at audit start

```
HEAD:   4b0862a7632cc502085e206cd633a78eb7b08981
branch: main, tracking origin/main, up to date (pushed)
status: clean
```

All files under `theorems/phase{1,2,3,4}/`, `scripts/`, `data/`, `reference/` checksummed directly from the working tree — 90 entries, `theorems/phase5/PHASE5_BASELINE_CHECKSUMS.txt`. This is the authoritative record; Phase 1–4 files are read-only for the remainder of this audit, and any apparent inconsistency found is reported in a Phase 5 file, never silently patched into an earlier phase's files.

## Audit posture

This audit treats the Phase 4 claim as **unproven until re-derived independently**. Where this document or later Phase 5 files state a fact that happens to match a Phase 4 file, that match is reported as a match *after* independent derivation, not assumed from having written Phase 4 in an earlier session. Genuine mismatches, gaps, or unjustified steps are reported as such, not smoothed over.
