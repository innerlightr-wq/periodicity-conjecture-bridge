"""
Phase 7: implements BHZ's GENERAL Corollary 3.5 formula for arbitrary
admissible Ostrowski digit sequences (c_k), not merely the characteristic
(c_k=0) or omega(-alpha)-specific pattern used in Phases 4-6.

BHZ admissibility condition (1), read from the primary source (Sec. 1,
p.2): a_k >= c_k >= 0 for all k, a_k>=1 for k>=2, and if c_k=a_k then
c_{k-1}=0.

Corollary 3.5 (exact quote, p.16-17):
  x'(k) = [ sum_{j=1}^{k+1} (a_j-c_j) q_{j-1} ] / q_k
  y(k)  = 1 + [ sum_{j=1}^{k} (a_j-c_j) q_{j-1} ] / (q_k - c_k*q_{k-1})
  ice(omega) = limsup_k max(x'(k), y(k))

Exact Fraction arithmetic throughout; floats only for display.
"""
from fractions import Fraction
import random


def convergents(a_terms):
    """a_terms: [a_1, a_2, ...] (1-indexed conceptually, 0-indexed list).
    Returns q_0=1, q_1, q_2, ... as a list q with q[0]=q_0."""
    q = [1]  # q_0 = 1
    q_prev = 0  # q_{-1} = 0
    for a in a_terms:
        q.append(a * q[-1] + q_prev)
        q_prev = q[-2]
    return q  # q[0]=q_0, q[1]=q_1, ...


def random_admissible_c(a_terms, rng, style="random"):
    """Generates an admissible (c_k) sequence for the given (a_k), 1-indexed
    conceptually (c[0] corresponds to c_1, etc.), respecting: 0<=c_k<=a_k,
    and if c_k=a_k then c_{k-1}=0 (c_0 taken as 0, i.e. no constraint at k=1
    beyond 0<=c_1<=a_1)."""
    c = []
    prev_c = 0
    for a in a_terms:
        if style == "zero":
            ck = 0
        elif style == "max_when_allowed":
            # try to set c_k = a_k whenever admissible (prev c must be 0)
            ck = a if prev_c == 0 else a - 1 if a >= 1 else 0
            ck = max(0, min(ck, a))
        elif style == "random":
            hi = a if prev_c == 0 else a - 1
            hi = max(0, hi)
            ck = rng.randint(0, hi)
        else:
            raise ValueError(style)
        c.append(ck)
        prev_c = ck
    return c


def ice_terms(a_terms, c_terms, kmax):
    """Returns list of (k, x'(k), y(k)) for k=1..kmax (using 1-indexed
    convention matching BHZ: a_terms[j-1]=a_j, c_terms[j-1]=c_j, q[j]=q_j)."""
    q = convergents(a_terms)
    results = []
    for k in range(1, min(kmax, len(a_terms) - 1, len(q) - 1) + 1):
        # x'(k) needs sum up to j=k+1, and a_{k+1}, c_{k+1}
        if k + 1 > len(a_terms):
            break
        s_kplus1 = sum((a_terms[j - 1] - c_terms[j - 1]) * q[j - 1] for j in range(1, k + 2))
        xk = Fraction(s_kplus1, q[k])

        s_k = sum((a_terms[j - 1] - c_terms[j - 1]) * q[j - 1] for j in range(1, k + 1))
        denom = q[k] - c_terms[k - 1] * q[k - 1]
        if denom == 0:
            yk = None
        else:
            yk = 1 + Fraction(s_k, denom)
        results.append((k, xk, yk))
    return results


def ice_estimate(a_terms, c_terms, kmax):
    terms = ice_terms(a_terms, c_terms, kmax)
    best = Fraction(0)
    for k, xk, yk in terms:
        if xk > best:
            best = xk
        if yk is not None and yk > best:
            best = yk
    return best, terms


def characteristic_ice_formula(a_terms, kmax):
    """Known closed form: ice(characteristic) = 1 + limsup [a_k;a_{k-1},...,a_1]
    (reversed CF value). Cross-check for the c_k=0 case."""
    best = Fraction(0)
    for k in range(1, min(kmax, len(a_terms)) + 1):
        # compute [a_k; a_{k-1}, ..., a_1]
        val = Fraction(a_terms[0])
        for j in range(1, k):
            val = a_terms[j] + Fraction(1, val)
        if val > best:
            best = val
    return 1 + best


if __name__ == "__main__":
    rng = random.Random(1)
    a_terms = [2] * 40  # silver ratio, A=2
    print("=== Validation: characteristic (c_k=0) vs known closed form, silver ratio ===")
    c_zero = random_admissible_c(a_terms, rng, style="zero")
    val, _ = ice_estimate(a_terms, c_zero, kmax=30)
    known = characteristic_ice_formula(a_terms, kmax=30)
    print(f"  ice estimate (general formula, c=0) = {float(val):.6f}")
    print(f"  known closed form (1+limsup reversed CF) = {float(known):.6f}")
    print(f"  match: {val == known}")
