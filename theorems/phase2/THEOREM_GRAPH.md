# THEOREM_GRAPH.md

```mermaid
graph TD
    A["Phi isometry (Prop 2.2)<br/>SOURCE-PAPER RESULT"]
    B["periodic-value formula (Prop 4.1)<br/>SOURCE-PAPER RESULT"]
    C["abstract surplus theorem<br/>ABSTRACT_IRRATIONALITY_CRITERION.md<br/>NEWLY PROVED HERE (Phase 2 re-derivation;<br/>content = Phase 1 ABSTRACT_BRIDGE_THEOREM.md)"]
    D["surplus dual theorem (uniform bound<br/>under rationality)<br/>SURPLUS_THEOREM.md<br/>NEWLY PROVED HERE"]
    E["discrepancy-height theorem<br/>DISCREPANCY_HEIGHT_PROOF.md<br/>NEWLY PROVED HERE (re-derivation of<br/>Phase 1 DISCREPANCY_HEIGHT_THEOREM.md,<br/>+ explicit weakest-condition ladder)"]
    F["repetition-surplus theorem<br/>(density-free, r > log2 3)<br/>REPETITION_SURPLUS_THEOREM.md<br/>NEWLY PROVED HERE"]
    G["square + sublinear-discrepancy<br/>corollary S<br/>SQUARE_DISCREPANCY_COROLLARY.md<br/>NEWLY PROVED HERE, adversarially checked"]
    H["Rote-Sturmian transfer<br/>(exact depth L+1)<br/>ROTE_TRANSFER_THEOREM.md<br/>NEWLY PROVED HERE (Phase 1 version was<br/>COMPUTATIONALLY VERIFIED only)"]
    I["Sturmian initial squares<br/>(Theorem 10.2 / ADQZ 2001)<br/>KNOWN (cited, not re-proved)"]
    J["Rote root discrepancy = O(log ell)<br/>ROTE_ROOT_DISCREPANCY.md<br/>PROVED for bounded-partial-quotient<br/>slopes; OPEN beyond that"]
    K["weight-parity eventual periodicity<br/>+ 'cycle contains 0' check<br/>ROTE_IRRATIONALITY_THEOREM.md<br/>PROVED (periodicity, general);<br/>COMPUTATIONALLY VERIFIED (contains-0,<br/>5 explicit slopes); OPEN (all quadratic<br/>irrationals)"]
    L["ROTE IRRATIONALITY THEOREM<br/>Phi(v) not in Q, 5 explicit slopes<br/>ROTE_IRRATIONALITY_THEOREM.md<br/>PROVED - NONTRIVIAL SUBCLASS"]
    M["rotation-coding discrepancy<br/>(same 3-distance mechanism)<br/>ROTATION_EXAMPLE_THEOREM.md<br/>PROVED"]
    N["rotation-coding initial powers<br/>(analogue of Theorem 10.2, mismatched delta)<br/>OPEN - no citation found"]
    O["rotation-coding irrationality<br/>ROTATION_EXAMPLE_THEOREM.md<br/>PARTIALLY PROVED"]

    A --> C
    B --> C
    C --> D
    C --> F
    E --> F
    F --> G
    I --> H
    H --> J
    E --> J
    J --> K
    K --> L
    G --> L
    F --> L
    H --> L
    I --> N
    E --> M
    M --> O
    N -.->|"missing"| O
```

## Bottleneck, made explicit by the graph

Every arrow into **L (the main theorem)** is solid — `PROVED` or `KNOWN` (cited) — **except** the arrow from **K**, which is itself `PROVED` in its general mechanism (eventual periodicity) but only `COMPUTATIONALLY VERIFIED` in its specific decisive content (cycle contains `0`) for five explicit slopes, not proved for all quadratic irrationals. **This is the single precise bottleneck of the entire graph**, isolated exactly as `ROTE_IRRATIONALITY_THEOREM.md`'s "PRECISE MISSING LEMMA" section states it.

The **rotation-coding branch (M–O)** has a genuinely dashed (missing) edge at **N `\to` O**: no citation or proof supplies the rotation-coding analogue of Theorem 10.2 at all — a strictly more open bottleneck than the Rote branch's, consistent with `ROTATION_EXAMPLE_THEOREM.md`'s weaker `PARTIALLY PROVED` classification versus `L`'s `PROVED — NONTRIVIAL SUBCLASS`.

## Legend

- **KNOWN / SOURCE-PAPER RESULT**: cited from the source paper or standard literature, not re-derived here.
- **NEWLY PROVED HERE**: a complete, original proof in this phase (Phase 2).
- **COMPUTATIONALLY VERIFIED**: checked by exact-arithmetic script for specific instances, not proved as a general theorem.
- **OPEN**: identified, precisely stated, not resolved.
