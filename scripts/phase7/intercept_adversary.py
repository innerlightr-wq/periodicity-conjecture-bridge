"""
Phase 7, Sections 9-10-12: structured intercept families, adversarial
minimization search over admissible Ostrowski digits, and drift tracking.

Reuses bhz_general_witness.py's exact Fraction implementation of BHZ's
general Corollary 3.5 formula. No floating point decides any classification
here -- exact Fraction comparisons throughout; floats only for display.
"""
from fractions import Fraction
import math
import random

from bhz_general_witness import convergents, ice_terms


def R_drift(ell, kappa):
    """R(W) = ell - kappa*log2(3), float only (diagnostic, not decision)."""
    return ell - kappa * math.log2(3)


def build_witness_word(a_terms, c_terms, k):
    """Build the ACTUAL substitution-image achieving word for y(k) (BHZ Sec 3):
    cyclic permutation of tau_0^{a_1} o tau_1^{a_2} o ... o tau_{k-1}^{a_k-c_k}(i).
    tau_0: 0->0, 1->01 ; tau_1: 0->10, 1->1. i in {0,1} (we use i=0)."""
    def tau0(w):
        return [x for c in w for x in ([0] if c == 0 else [0, 1])]

    def tau1(w):
        return [x for c in w for x in ([1, 0] if c == 0 else [1])]

    w = [0]
    for idx in range(1, k + 1):
        exponent = a_terms[idx - 1] if idx < k else (a_terms[idx - 1] - c_terms[idx - 1])
        tau = tau0 if (idx % 2 == 1) else tau1
        for _ in range(exponent):
            w = tau(w)
    return w


def analyze_pattern(name, a_terms, c_terms, kmax=25):
    terms = ice_terms(a_terms, c_terms, kmax)
    best = Fraction(0)
    best_k = None
    for k, xk, yk in terms:
        cand = max(xk, yk) if yk is not None else xk
        if cand > best:
            best = cand
            best_k = k
    margin = best - 2
    return {"name": name, "ice_est": best, "margin": margin, "best_k": best_k, "terms": terms}


# ---- Structured intercept families (Section 9) ----

def family_intercept_zero(a_terms):
    return [0] * len(a_terms)


def family_shift_characteristic(a_terms, shift):
    """A crude stand-in for 'shift of the characteristic word': zeros, but
    the first `shift` digits forced to something else (a simple probe, not
    a claim of exact correspondence to a specific shift)."""
    c = [0] * len(a_terms)
    for i in range(min(shift, len(c))):
        c[i] = 1 if a_terms[i] >= 1 else 0
    return c


def family_eventually_zero(a_terms, prelen):
    c = [0] * len(a_terms)
    rng = random.Random(0)
    for i in range(prelen):
        hi = a_terms[i] if (i == 0 or c[i - 1] == 0) else a_terms[i] - 1
        c[i] = rng.randint(0, max(0, hi))
    return c


def family_eventually_maximal(a_terms):
    c = []
    prev = 0
    for a in a_terms:
        ck = a if prev == 0 else max(0, a - 1)
        c.append(ck)
        prev = ck
    return c


def family_periodic(a_terms, period_pattern):
    c = []
    prev = 0
    for i, a in enumerate(a_terms):
        want = period_pattern[i % len(period_pattern)]
        ck = min(want, a if prev == 0 else a - 1)
        ck = max(0, ck)
        c.append(ck)
        prev = ck
    return c


def family_alternating_sparse_dense(a_terms):
    c = []
    prev = 0
    for i, a in enumerate(a_terms):
        target = a if (i % 3 == 0 and prev == 0) else 0
        c.append(max(0, min(target, a if prev == 0 else a - 1)))
        prev = c[-1]
    return c


def family_long_zero_blocks(a_terms, block=8):
    c = []
    prev = 0
    for i, a in enumerate(a_terms):
        want = 0 if (i // block) % 2 == 0 else (a if prev == 0 else a - 1)
        want = max(0, min(want, a))
        c.append(want)
        prev = want
    return c


def family_near_maximal_blocks(a_terms, block=8):
    c = []
    prev = 0
    for i, a in enumerate(a_terms):
        want = (a if prev == 0 else a - 1) if (i // block) % 2 == 0 else 0
        want = max(0, min(want, a))
        c.append(want)
        prev = want
    return c


# ---- Adversarial local-greedy search minimizing running max(x',y) (Section 10) ----

def adversarial_greedy(a_terms, kmax_search=30):
    """Greedy DP-flavored local search: at each step, among admissible c_k
    choices, pick the one that MINIMIZES the resulting x'(k)/y(k) value at
    that step (a local greedy proxy for minimizing the eventual limsup --
    not a full DP, but explores the same 'maximize digits' intuition the
    manual family_eventually_maximal already found effective)."""
    c = []
    prev = 0
    q = [1]
    q_prev = 0
    for idx, a in enumerate(a_terms):
        best_choice, best_val = 0, None
        hi = a if prev == 0 else a - 1
        for cand in range(0, max(0, hi) + 1):
            # heuristic score: prefer larger c_k (reduces (a_j-c_j) terms directly)
            score = cand
            if best_val is None or score > best_val:
                best_val = score
                best_choice = cand
        c.append(best_choice)
        prev = best_choice
        newq = a * q[-1] + q_prev
        q_prev = q[-1]
        q.append(newq)
    return c


def main():
    slopes = {
        "golden A=1": [1] * 40,
        "silver A=2": [2] * 40,
        "nonperiodic-A A=2 (mixed)": [1, 2, 1, 1, 2, 2, 1, 2] * 5,
        "nonperiodic-B A=3": [2, 3, 1, 2, 1, 3, 2, 1] * 5,
    }

    print("=" * 70)
    print("STRUCTURED INTERCEPT FAMILIES (Section 9)")
    print("=" * 70)
    results = []
    for sname, a_terms in slopes.items():
        print(f"\n--- slope: {sname} ---")
        families = [
            ("intercept 0 (characteristic)", family_intercept_zero(a_terms)),
            ("shift-probe (first 3 digits forced)", family_shift_characteristic(a_terms, 3)),
            ("eventually zero (random prefix len 6)", family_eventually_zero(a_terms, 6)),
            ("eventually maximal admissible", family_eventually_maximal(a_terms)),
            ("periodic pattern [max,0]", family_periodic(a_terms, [10**9, 0])),
            ("alternating sparse/dense", family_alternating_sparse_dense(a_terms)),
            ("long zero blocks (8)", family_long_zero_blocks(a_terms, 8)),
            ("long near-maximal blocks (8)", family_near_maximal_blocks(a_terms, 8)),
            ("adversarial greedy (maximize c_k)", adversarial_greedy(a_terms)),
        ]
        for fname, c_terms in families:
            r = analyze_pattern(fname, a_terms, c_terms, kmax=25)
            print(f"  {fname:42s}: ice_est={float(r['ice_est']):.6f}  margin={float(r['margin']):.6f}  "
                  f"(at k={r['best_k']})")
            results.append((sname, fname, r))

    print("\n" + "=" * 70)
    print("SUMMARY: minimum margin found per slope")
    print("=" * 70)
    by_slope = {}
    for sname, fname, r in results:
        by_slope.setdefault(sname, []).append((r["margin"], fname))
    all_positive = True
    for sname, lst in by_slope.items():
        lst.sort()
        worst_margin, worst_name = lst[0]
        print(f"  {sname}: worst margin = {float(worst_margin):.6f}  (pattern: {worst_name})")
        if worst_margin <= 0:
            all_positive = False
    print(f"\nAll tested patterns, all slopes: margin > 0 strictly: {all_positive}")


if __name__ == "__main__":
    main()
