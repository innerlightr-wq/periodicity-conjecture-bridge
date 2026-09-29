"""
Phase 5, Section 14: random quadratic stress test. NOT a proof -- a search
for mismatches between the theorem's assumptions and what actually happens:
missing witnesses, wrong root density, discrepancy-bound failures,
persistently nonpositive surplus, seed/shift anomalies.

Exact integer/Fraction arithmetic decides every flag; floats for display.
"""
from fractions import Fraction
import random
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "phase1"))
from bridge_toolkit import bridge_surplus_exact, lcp, periodic_extension  # noqa: E402


def cf_value(pq, n):
    num, den = 1, 0
    for a in reversed(pq[:n]):
        num, den = a * num + den, num
    return Fraction(num, den)


def convergents_pq(pq, n):
    a0 = pq[0]
    p, q = [1, a0], [0, 1]
    for i in range(1, n):
        p.append(pq[i] * p[-1] + p[-2])
        q.append(pq[i] * q[-1] + q[-2])
    return p[1:], q[1:]


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


def random_quadratic(rng, max_prelen=4, max_period=3, max_val=8):
    prelen = rng.randint(0, max_prelen)
    period_len = rng.randint(1, max_period)
    pre = [rng.randint(1, max_val) for _ in range(prelen)]
    period = [rng.randint(1, max_val) for _ in range(period_len)]
    return pre, period


def analyze(pre, period, max_ell=8000, reps=60):
    pq = [0] + pre + period * reps
    gamma = cf_value(pq, len(pq))
    _, q = convergents_pq(pq, len(pq))
    q_small = [x for x in q if 2 <= x <= max_ell]
    if not q_small:
        return {"flag": "NO_WITNESS_IN_RANGE", "pre": pre, "period": period}

    n_needed = min(max(q_small) * 6, 400_000)
    u = mechanical_word(gamma, n_needed)
    v0 = rote_from_sturmian(u, 0)
    v1 = rote_from_sturmian(u, 1)

    flags = []
    best_S = {"seed0": None, "seed1": None}
    for ell in q_small:
        if ell * 6 > len(u):
            continue
        W = u[:ell]
        wpar = sum(W) % 2
        checklen = min(len(u), ell * 6)
        L_u = lcp(u, periodic_extension(W, checklen), checklen)
        for label, v in [("seed0", v0), ("seed1", v1)]:
            if wpar == 0:
                V, rootlen = v[:ell], ell
            else:
                V0 = v[:ell]
                V, rootlen = V0 + [1 - x for x in V0], 2 * ell
                dens = Fraction(sum(V), rootlen)
                if dens != Fraction(1, 2):
                    flags.append(f"DENSITY_NOT_HALF at ell={ell} {label}: {dens}")
            checklen_v = min(len(v), rootlen * 6)
            Lv = lcp(v, periodic_extension(V, checklen_v), checklen_v)
            S, _ = bridge_surplus_exact(Lv, V)
            if best_S[label] is None or S > best_S[label]:
                best_S[label] = S

    result = {"pre": pre, "period": period, "gamma": float(gamma),
              "n_witnesses": len(q_small), "best_S_seed0": best_S["seed0"],
              "best_S_seed1": best_S["seed1"], "flags": flags}
    if best_S["seed0"] is None or (best_S["seed0"] <= 0 and best_S["seed1"] is not None and best_S["seed1"] <= 0):
        result["flags"].append("PERSISTENTLY_NONPOSITIVE_SURPLUS")
    if (best_S["seed0"] is None) != (best_S["seed1"] is None):
        result["flags"].append("SEED_ASYMMETRY")
    return result


def main():
    rng = random.Random(42)
    n_samples = 25
    anomalies = 0
    print(f"Testing {n_samples} random quadratic irrationals (preperiod<=4, period<=3, digits 1-8)...\n")
    for i in range(n_samples):
        pre, period = random_quadratic(rng)
        r = analyze(pre, period)
        flag_str = f"  FLAGS: {r['flags']}" if r.get("flags") else ""
        if r.get("flag") == "NO_WITNESS_IN_RANGE":
            print(f"[{i:2d}] pre={pre} period={period}: NO WITNESS FOUND IN RANGE (flagged)")
            anomalies += 1
            continue
        print(f"[{i:2d}] pre={pre} period={period} gamma={r['gamma']:.6f} "
              f"witnesses={r['n_witnesses']} best_S(seed0)={r['best_S_seed0']} "
              f"best_S(seed1)={r['best_S_seed1']}{flag_str}")
        if r["flags"]:
            anomalies += 1

    print(f"\n{n_samples} slopes tested, {anomalies} with flagged anomalies.")


if __name__ == "__main__":
    main()
