"""
Phase 7: direct, fully-trustworthy exact verification at NONZERO intercepts,
sidestepping the unverified BHZ word-reconstruction (verify_phase7.py
Section 2's disclosed gap) entirely.

Builds the ACTUAL general-intercept mechanical word
    u_n = floor((n+1)*gamma + rho) - floor(n*gamma + rho)
directly (rho != 0), then runs the EXACT SAME already-verified pipeline
used throughout Phases 4-6: direct lcp search for initial powers (no
formula trusted), exact XOR transfer, exact surplus via bridge_toolkit.

Exact Fraction/integer arithmetic throughout; no floating point decides
any result.
"""
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension  # noqa: E402


def cf_value(pq_terms, n):
    num, den = 1, 0
    for a in reversed(pq_terms[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def convergents_q(pq_terms, n):
    q = [1, pq_terms[0] if False else 0]  # placeholder unused path; real calc below
    return q


def convergents(pq_terms, n):
    q0, q1 = 1, pq_terms[0]
    qs = [q0, q1]
    for i in range(1, n):
        qs.append(pq_terms[i] * qs[-1] + qs[-2])
    return qs


def mechanical_word_intercept(gamma, rho, n):
    """u_n = floor((n+1)*gamma+rho) - floor(n*gamma+rho), n=0..n_terms-1."""
    def fl(x):
        return x.numerator // x.denominator
    s, prev = [], fl(rho)
    for i in range(1, n + 1):
        cur = fl(i * gamma + rho)
        s.append(cur - prev)
        prev = cur
    return s


def rote_from_sturmian(u, v0=0):
    v = [v0]
    for b in u:
        v.append(v[-1] ^ b)
    return v[:-1]


def scan_slope(name, gamma, rho, max_ell=3000, n_reps=8):
    print(f"=== {name}: gamma={float(gamma):.6f} rho={float(rho):.6f} ===")
    n_needed = min(max_ell * n_reps, 400_000)
    u = mechanical_word_intercept(gamma, rho, n_needed)
    v = rote_from_sturmian(u)

    certifying = []
    for ell in range(2, max_ell):
        if ell * n_reps > len(u):
            break
        W = u[:ell]
        prim = True
        for d in range(1, ell):
            if ell % d == 0 and all(W[i] == W[i % d] for i in range(ell)):
                prim = False
                break
        if not prim:
            continue
        checklen = min(len(u), ell * n_reps)
        L_u = lcp(u, periodic_extension(W, checklen), checklen)
        if L_u < 2 * ell:
            continue  # require a genuine SQUARE (r>=2) as the base witness, per Theorem 10.2
        wpar = sum(W) % 2
        if wpar == 0:
            V, rootlen = v[:ell], ell
        else:
            V0 = v[:ell]
            V, rootlen = V0 + [1 - x for x in V0], 2 * ell
        checklen_v = min(len(v), rootlen * n_reps)
        Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
        S, _ = bridge_surplus_exact(Lv, V)
        if S > 0:
            certifying.append((ell, wpar, S))

    print(f"  squares (r>=2) tested: found {len(certifying)} certifying (S>0) witnesses")
    for ell, wpar, S in certifying[-6:]:
        print(f"    ell={ell:6d} weight_parity={wpar}  S={S}")
    return certifying


def main():
    prec = 60
    # golden ratio slope, several nonzero rational and irrational intercepts
    golden_pq = [0] + [1] * prec
    golden = cf_value(golden_pq, len(golden_pq))
    silver_pq = [0] + [2] * prec
    silver = cf_value(silver_pq, len(silver_pq))

    results = {}
    results["golden, rho=1/3"] = scan_slope("golden, rho=1/3", golden, Fraction(1, 3))
    results["golden, rho=golden^2 mod 1"] = scan_slope(
        "golden, rho=golden^2 (irrational)", golden, (golden * golden) - int(golden * golden))
    results["silver, rho=2/5"] = scan_slope("silver, rho=2/5", silver, Fraction(2, 5))
    results["silver, rho=1-golden (irrational, cross-slope)"] = scan_slope(
        "silver, rho=1-golden", silver, 1 - golden)

    print("\n" + "=" * 60)
    print("SUMMARY")
    all_certify = True
    for name, certs in results.items():
        ok = len(certs) >= 2
        all_certify &= ok
        print(f"  {name}: {len(certs)} certifying witnesses found, >=2: {ok}")
    print(f"\nAll tested nonzero intercepts certify via the exact, already-verified pipeline: {all_certify}")


if __name__ == "__main__":
    main()
