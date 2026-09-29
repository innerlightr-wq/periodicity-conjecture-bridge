# FLEXIBLE_MARGIN_BOUNDARY.md

Task's `r_k=2+\epsilon_k` (`\epsilon_k\equiv E_k` in this phase's other notation). Sufficient criterion, re-derived in `INTERCEPT_EXCESS.md`: `\epsilon_k\cdot\ell_k\gg\log\ell_k`, equivalently `\epsilon_k\ell_k/\log\ell_k\to\infty`.

| `\epsilon_k` | `\epsilon_k\ell_k` | vs. `\log\ell_k` | Sufficient? |
|---|---|---|---|
| `\sim\text{const}` | `\sim\ell_k` | `\ell_k\gg\log\ell_k` | **Yes** (Phases 4–6's actual regime) |
| `\sim1/\log\ell_k` | `\sim\ell_k/\log\ell_k` | `\ell_k/\log\ell_k\gg\log\ell_k\iff\ell_k\gg(\log\ell_k)^2` | **Yes** (polynomial beats any power of log) |
| `\sim1/\sqrt{\ell_k}` | `\sim\sqrt{\ell_k}` | `\sqrt{\ell_k}\gg\log\ell_k` | **Yes** |
| `\sim\log\ell_k/\ell_k` | `\sim\log\ell_k` | `\log\ell_k\gg\log\ell_k` | **No** — exactly borderline, same order, criterion fails as stated (would need a diverging *constant* multiple, not just this rate) |
| `\sim1/\ell_k` | `\sim1` | `1\gg\log\ell_k`? No | **No** |

## The true asymptotic boundary

```
epsilon_k = omega(log(ell_k)/ell_k)      -- i.e. epsilon_k * ell_k / log(ell_k) -> infinity
```
is the exact boundary: anything decaying **strictly slower** than `\log\ell_k/\ell_k` suffices (including `1/\log\ell_k`, `1/\sqrt{\ell_k}`, or any fixed positive constant); anything decaying **at the rate of or faster than** `\log\ell_k/\ell_k` does not (as stated — a large enough *constant multiple* of `\log\ell_k/\ell_k`, i.e. `\epsilon_k=M\log\ell_k/\ell_k$ for fixed `M`, gives `\epsilon_k\ell_k=M\log\ell_k`, still only `\Theta(\log\ell_k)`, not `\gg\log\ell_k$, so this entire rate-class fails regardless of the constant).

## Relevance to Phase 7's actual findings

**Not needed in practice.** Every tested Ostrowski digit pattern (`theorems/phase7/OSTROWSKI_PATTERN_CLASSIFICATION.md`, including the adversarial "maximal-digit" family) gave `\epsilon_k$ bounded below by a **fixed positive constant** depending only on `A` (empirically `\sim1/A^2`, comfortably better than the conservative `1/(A+1)` bound re-derived from BHZ) — i.e. every case found lands in the *first, easiest* row of this table. **The flexible-margin machinery is recorded here because the task asked for the true boundary of the method, not because any found witness family actually needed it.** If a future adversarial search finds a pattern with genuinely vanishing `\epsilon_k`, this table is where to check whether it still certifies.
