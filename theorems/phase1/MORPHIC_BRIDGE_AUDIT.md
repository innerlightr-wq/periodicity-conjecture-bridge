# MORPHIC_BRIDGE_AUDIT.md

Kept deliberately bounded, per the task's instruction — this is a scoping note, not a research program.

## Thue–Morse: the negative control, already established

The source paper's own Appendix A control (cited, not reproduced) establishes: the Thue–Morse word has **no square at all below half-length 2048**. Thue–Morse is overlap-free (a classical fact, Thue 1912/1906) but it is **not** square-free — it does contain squares (e.g. `00`, `1010`), just apparently none as an *initial* factor at the tested scale. This is the critical distinction the task asks to keep sharp:

- **Failure of this particular bridge** (no long *initial* power found, hence `REPETITION_HEIGHT_CRITERION.md`'s hypothesis is simply not verified at tested scales for Thue–Morse): confirmed.
- **Irrationality of `Φ(s)` for Thue–Morse**: not addressed by this bridge either way. Separately, Thue–Morse has complexity `p(L) = O(L)` (in fact known exactly, e.g. via de Luca–Varricchio-type results in the automatic-sequences literature — not independently re-verified here), and if that linear constant is below `1.70951...`, Corollary 9.3's counting route would settle irrationality of `Φ(s)` **without any repetition argument at all** — a claim not checked in this audit and flagged as a natural, easy follow-up rather than asserted.
- **The actual Periodicity/Collatz status of Thue–Morse's orbit**: entirely untouched by anything here, exactly as `FULL_PERIODICITY_GAP.md` insists.

## Primitive morphic words in general: scope only, no research program

A primitive morphic word is the image, under a coding, of a fixed point of a primitive substitution. Whether such a word begins in arbitrarily long initial powers of exponent `>log₂3` is a substitution-by-substitution combinatorial question (the *initial* critical exponent of a fixed point of a given substitution is, in general, computable from the substitution's incidence structure by known methods in the combinatorics-on-words literature — e.g. the kind of Ostrowski/return-word machinery already cited for Sturmian words in Berthé–Holton–Zamboni), but **no general theorem covering the whole class is asserted or sought here**. This matches `FALSIFICATION_REPORT.md`'s verdict on C5 ("unknown, and likely too broad") and `FULL_PERIODICITY_GAP.md`'s Q3/Q4: some primitive morphic words will fall in Rung B (if they happen to have long initial powers `>log₂3` — the *height* side is now unconditional, so only the *repetition* side needs checking, substitution by substitution), others in Rung D (no useful initial power, like Thue–Morse), and the boundary is not mapped out here.

## Deliberate stopping point

Per the task's explicit instruction ("Keep this section bounded; do not let it become a separate research project"), this document stops here. A genuine morphic-words research program — computing initial critical exponents across a taxonomy of primitive substitutions — is exactly the kind of follow-up `BRIDGE_VERDICT.md`'s final question ("what should the next paper/project be") should assess as a *candidate*, not attempt in this pass.
