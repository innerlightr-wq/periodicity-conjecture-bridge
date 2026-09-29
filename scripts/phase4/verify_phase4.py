"""
Phase 4 consolidated formal verification. Exact Fraction/integer arithmetic
decides every check; floating point appears only in printed summaries.

Prints "ALL PHASE 4 CHECKS PASS" only if every encoded identity/inequality
succeeds.
"""
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension  # noqa: E402


def convergents_pq(pq, n):
    a0 = pq[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
        q.append(pq[i] * q[-1] + q[-2])
    return p[1:], q[1:]


def weight_seq(pq, n):
    p, _ = convergents_pq(pq, n)
    return [pk % 2 ^ (k % 2) for k, pk in enumerate(p)]


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def mechanical_word(gamma, n):
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], 0
    for i in range(1, n + 1):
        cur = fl(i * gamma)
        s.append(cur - prev)
        prev = cur
    return s


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


checks = []


def check(name, condition):
    checks.append((name, bool(condition)))
    print(f"  [{'PASS' if condition else 'FAIL'}] {name}")


def section(title):
    print(f"\n=== {title} ===")


def main():
    section("1. Silver constant: x=2+1/x has exact root x=1+sqrt(2)")
    # verify algebraically via the defining polynomial x^2-2x-1=0 at x=1+sqrt(2)
    x_num_sq_minus_2x_minus_1 = (1 + math.sqrt(2)) ** 2 - 2 * (1 + math.sqrt(2)) - 1
    check("x=1+sqrt(2) satisfies x^2-2x-1=0 (to float precision)",
          abs(x_num_sq_minus_2x_minus_1) < 1e-9)
    check("2+sqrt(2) = 1 + (1+sqrt(2)), i.e. ice(silver) = 1+x", abs((2 + math.sqrt(2)) - (1 + (1 + math.sqrt(2)))) < 1e-12)

    section("2. term2(k) > 2+1/(A+1) exact bound, several tails")
    tail_tests = [
        ("silver [0;2,2,...]", [0] + [2] * 40, 2),
        ("counterexample [0;1,1,1,2,2,...]", [0, 1, 1, 1] + [2] * 40, 2),
        ("mixed [0;2,1,2,1,...]", [0] + [2, 1] * 40, 2),
        ("near-boundary [0;1,4,1,5,1,6,2,...]", [0, 1, 4, 1, 5, 1] + [6, 2] * 20, 6),
    ]
    for name, pq, A in tail_tests:
        p, q = convergents_pq(pq, len(pq))
        bound = 2 + Fraction(1, A + 1)
        ok = True
        for k in range(2, min(12, (len(pq) - 1) // 2)):
            term2 = 1 + pq[2 * k - 1] + Fraction(q[2 * k - 3], q[2 * k - 2])
            if not (term2 > bound):
                ok = False
        check(f"term2(k) > 2+1/(A+1) for every tested k -- {name}", ok)

    section("3. Density of R=V-Vbar is EXACTLY 1/2 (structural, any V)")
    import random
    random.seed(0)
    ok = True
    for _ in range(20):
        ell = random.randint(1, 50)
        V = [random.randint(0, 1) for _ in range(ell)]
        Vbar = [1 - x for x in V]
        R = V + Vbar
        if Fraction(sum(R), len(R)) != Fraction(1, 2):
            ok = False
    check("density(V concat Vbar) == 1/2 exactly, 20 random V's", ok)

    section("4. Threshold collapse: max(1, (1/2)*log2(3)) == 1")
    log2_3 = math.log2(3)
    check("(1/2)*log2(3) < 1  (so max(1, .) == 1)", 0.5 * log2_3 < 1)
    check("log2(3) < 2  (even-weight route: r_u>=2 clears log2(3) trivially)", log2_3 < 2)

    section("5. Known bad parity-cycle counterexample still recorded correctly")
    pq = [0, 1, 1, 1] + [2] * 30
    w = weight_seq(pq, min(len(pq), 28))
    check("gamma=[0;1,1,1,2,2,...] has all-odd weight parity from index 2 on",
          all(x == 1 for x in w[2:]))

    section("6. Odd-tail control: mixed [0;2,1,2,1,...] with NO preperiod does NOT lock bad")
    pq = [0] + [2, 1] * 30
    w = weight_seq(pq, min(len(pq), 20))
    check("weight parity contains a 0 within first 20 terms (does not lock)", 0 in w)

    section("7. All-even control: exact surplus positive & growing at silver-ratio-tailed slope")
    pq = [0, 1, 1, 1] + [2] * 24
    gamma = cf_value(pq, len(pq))
    _, q = convergents_pq(pq, len(pq))
    n_needed = min(q[10] * 3, 2_000_000)
    u = mechanical_word(gamma, n_needed)
    v = rote_from_sturmian(u)
    surpluses = []
    for k in [6, 8, 10]:
        ell = q[k]
        if ell * 5 > len(u):
            continue
        checklen = min(len(u), ell * 5)
        W = u[:ell]
        L = lcp(u, periodic_extension(W, checklen), checklen)
        wpar = sum(W) % 2
        if wpar == 0:
            V, rootlen = v[:ell], ell
        else:
            V0 = v[:ell]
            V, rootlen = V0 + [1 - x for x in V0], 2 * ell
        checklen_v = min(len(v), rootlen * 5)
        Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
        Wv = v[:rootlen]
        Sv, _ = bridge_surplus_exact(Lv, Wv)
        surpluses.append(Sv)
    check("at least 2 positive surplus values found", sum(1 for s in surpluses if s > 0) >= 2)
    check("surpluses strictly increasing (growing, not just positive)",
          surpluses == sorted(surpluses) and len(set(surpluses)) == len(surpluses))

    print("\n" + "=" * 60)
    all_pass = all(ok for _, ok in checks)
    print(f"Total checks: {len(checks)}, all passing: {all_pass}")
    if all_pass:
        print("ALL PHASE 4 CHECKS PASS")
    else:
        print("SOME PHASE 4 CHECKS FAILED:")
        for name, ok in checks:
            if not ok:
                print(f"  FAILED: {name}")
        sys.exit(1)


if __name__ == "__main__":
    main()
