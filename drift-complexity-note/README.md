# Drift-sensitive complexity note — verification files

Companion files for *A Drift-Sensitive Complexity Bound for Rational Points of the 3x+1 Conjugacy Map* (E. De Jesús, Revision 1).

- `note.tex`, `note.pdf` — the technical note.
- `scripts/p4_verify.py` — exact-arithmetic checks of the finite statements (the finite lemmas of Sections 2–5, Proposition 10 and Lemma 19 of the note); 535,509 checks, 0 failures (`data/p4_verify_output.txt`).
- `scripts/closed_window_search.py` — exhaustive search showing why the counting window must be half-open (`data/closed_window_search_output.txt`).

Standard library only: `python3 scripts/p4_verify.py`. These scripts verify finite instances; they are not part of any proof. No rational aperiodic parity vector is known, and none was tested.
