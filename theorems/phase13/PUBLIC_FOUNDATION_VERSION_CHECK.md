**THE LOCAL COPY IS BYTE-IDENTICAL TO THE DEPOSITED FILE — NO DIFFERENCES**

# PUBLIC_FOUNDATION_VERSION_CHECK.md

Phase 13 / preliminary. The foundation paper is now public; this file verifies it before it is used
as the authoritative reference.

## 1. Metadata, from the Zenodo REST API

```
record id        23019799
version DOI      10.5281/zenodo.23019799
concept DOI      10.5281/zenodo.22920055
title            The 3x+1 Conjugacy Map Sends Every Sturmian Word to an Irrational 2-adic Integer
creator          De Jesus, Elias   (ORCID 0009-0007-0190-9143)
resource type    publication / preprint
publication date 2026-09-28
license          CC BY 4.0
access            open
created          2026-09-28T16:04:18Z      modified  2026-09-29T14:24:59Z
file             Sturmian_v2_revision_draft3.pdf   467 315 bytes
                 md5:54732e14b939c39f74c118097a069f30
```

## 2. Integrity: the local copy needs no update

| file | bytes | md5 |
|---|---|---|
| Zenodo `Sturmian_v2_revision_draft3.pdf` (per API) | 467 315 | `54732e14b939c39f74c118097a069f30` |
| `~/Downloads/Sturmian_v2_revision_draft3.pdf` (and the two duplicates) | 467 315 | `54732e14b939c39f74c118097a069f30` |
| **`reference/sturmian-conjugacy-map-irrational-2adic-integer.pdf`** (in this repository since Phase 1) | **467 315** | **`54732e14b939c39f74c118097a069f30`** |

> **The local reference copy is byte-identical to the deposited file.** There are **no differences**
> to record: every theorem number, statement and open problem cited in Phases 1–12 was already
> cited from the same bytes that are now public. No prior citation needs revising on this account.

## 3. Version history of the concept record

| record | DOI | date | access | title |
|---|---|---|---|---|
| 23019799 | `…23019799` | 2026-09-28 | **open** | *…Every Sturmian Word…* |
| 22968196 | `…22968196` | 2026-09-25 | restricted | *…Every Sturmian Word…* |
| 22921024 | `…22921024` | 2026-09-23 | restricted | *…the Critical Sturmian Word…* |
| 22920056 | `…22920056` | 2026-09-23 | restricted | *…the Critical Sturmian Word…* |

Exactly the latest version is open; the three earlier ones remain restricted, and the title changed
from "the Critical Sturmian Word" to "Every Sturmian Word" between v2 and v3. **The standing note
that the concept DOI `10.5281/zenodo.22920055` must not be reused, and that the earlier versions are
under review hold, is unaffected** — only v4 is public, and it is the one cited from here on.

## 4. Contents verified before use

22 pages. Section structure: 1 Introduction · 2 The conjugacy map · 3 The critical Sturmian word ·
4 Periodic values and their heights · 5 The approximation depth · 6 Irrationality · 7 Consequences ·
8 All irrational slopes · 9 A counting bound, after Dubickas · 10 All Sturmian words · 11 Why the
2-adic place · 12 Open problems · Appendix A Verification · References [1]–[18].

Every label this research program has cited was located in the public file:

| cited as | present |
|---|---|
| Prop. 2.2 (isometry), Prop. 4.1 (periodic-value formula) | ✓ |
| Cor. 6.2, Thm 8.5, Cor. 8.7 (height floors, effective Liouville route) | ✓ |
| Cor. 9.3 / Cor. 9.4 (Dubickas transport, threshold `1/log₂(3/2) = 1.70951…`) | ✓ |
| Thm 10.1, Thm 10.2, Thm 10.3, Lemma 10.4, Cor. 10.5 (all Sturmian) | ✓ |
| §12 open problems (1) depth law at general intercept, (2) irrationality measure, (3) transcendence, (4) complexity up to `2L` | ✓ |

**Authorship note, now on the public record.** The "foundation paper" is by **Elias De Jesús** — the
author of this research program. It is a preprint, not refereed. Every use of it below is flagged as
a self-citation, and its own citation of `[17] M. Sharpe` as "not refereed" is matched by the same
caveat applied to itself.

## 5. Two passages relied on in Phases 12–13, quoted from the public file

**§12 problem (1)** — the mechanism this program executes:

> "The natural replacement is the first entry time of the orbit `{jγ+ρ}` into an interval of length
> `jD_n` at the partition endpoint, which the three-distance theorem and the Ostrowski expansion of
> `ρ` compute."

**§12 problem (4)** — the target:

> "Corollary 9.3 reaches every `s` with `liminf_L p_s(L)/L < 1/log₂(3/2) = 1.70951…`; Rote words and
> binary codings of rotations with two intervals sit at `p_s(L) = 2L`, out of reach of counting alone
> (Remark 9.5). Is `Φ(s) ∉ ℚ` for every non-eventually-periodic `s` with `p_s(L) ≤ 2L` for all large
> `L` — in particular for Rote words? The repetition method of Sections 6–10 needs, in place of
> Theorem 10.2 and Theorem 10.3, some substitute initial repetition and height bound valid on this
> wider class; **none is known to the author.** This is the natural next target for either method."

**§12, closing scope sentence**, which this program adopts verbatim:

> "None of these … bears on divergent orbits of positive integers, on the Periodicity Conjecture in
> general, or on the Collatz conjecture."
