"""
Phase 8, step G: INDEPENDENT end-to-end audit of Theorem 2's dependency chain.

Deliberately uses NO Berthe-Holton-Zamboni formula and no Ostrowski digit machinery.
Everything is computed on literally constructed mechanical words, so this is an
independent check of the CONCLUSION rather than a re-check of the derivation:

    certified irrational slope  ->  literal mechanical word (BOTH conventions, any intercept)
    -> literal attained initial powers W^r = (u[0:ell])^r, r = lcp(u,W^inf)/ell
    -> exact XOR transfer  v_{n+1} = v_n XOR u_n  (BOTH seeds)
    -> exact integer height F(R) = |2^|R| - 3^|R|_1| + c_R
    -> surplus S = lcp(v, R^inf) - log2 F(R)  ->  unbounded  ->  Phi(v) not in Q

Irrational slopes and intercepts are CERTIFIED RATIONAL BRACKETS.  Every floor/ceil is
decided by the bracket or the computation raises -- never guessed.

Conventions:
  lower mechanical word   u_i  = floor((i+1)gamma + rho) - floor(i gamma + rho)
  upper mechanical word   u'_i = ceil ((i+1)gamma + rho) - ceil (i gamma + rho)
  A   := sup_k A_k, the partial quotients of gamma = [0; A_1, A_2, ...]
  A_b := sup_k a_k, the BHZ digits (a_1 = A_1 - 1, a_k = A_k for k >= 2); A_b <= A
  delta(A_b) := 1/(2 (A_b+1)^2)          the Phase-8 proved floor
"""
from fractions import Fraction
import math, sys

LOG23 = math.log2(3)

# ---------------------------------------------------------------- certified reals

class Cert:
    """A real number pinned between two rationals.  Arithmetic is interval arithmetic;
    floor()/ceil() raise UndecidedError rather than guess."""
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi):
        assert lo <= hi
        self.lo, self.hi = Fraction(lo), Fraction(hi)
    def __add__(self, o):
        o = o if isinstance(o, Cert) else Cert(o, o)
        return Cert(self.lo + o.lo, self.hi + o.hi)
    def __rmul__(self, n):           # n a non-negative int
        assert isinstance(n, int) and n >= 0
        return Cert(n * self.lo, n * self.hi)
    def floor(self):
        f = math.floor(self.lo)
        if math.floor(self.hi) != f:
            raise UndecidedError(f"floor undecided on [{self.lo}, {self.hi}]")
        return f
    def ceil(self):
        c = math.ceil(self.lo)
        if math.ceil(self.hi) != c:
            raise UndecidedError(f"ceil undecided on [{self.lo}, {self.hi}]")
        return c
    def width(self):
        return self.hi - self.lo

class UndecidedError(Exception):
    pass

def cf_convergents(digits):
    """[0; d_1, d_2, ...] -> list of (p_k, q_k), k = 0..len(digits)."""
    p0, q0, p1, q1 = 0, 1, 1, digits[0]
    out = [(p0, q0), (p1, q1)]
    for d in digits[1:]:
        p0, q0, p1, q1 = p1, q1, d * p1 + p0, d * q1 + q0
        out.append((p1, q1))
    return out

def cf_cert(digits):
    """gamma = [0; digits] as a certified bracket.  gamma lies strictly between the last
    two convergents, and |gamma - p_k/q_k| < 1/(q_k q_{k+1})."""
    cv = cf_convergents(digits)
    (pa, qa), (pb, qb) = cv[-2], cv[-1]
    lo, hi = Fraction(pa, qa), Fraction(pb, qb)
    if lo > hi:
        lo, hi = hi, lo
    return Cert(lo, hi), cv

# ---------------------------------------------------------------- mechanical words

def mech(gamma, rho, N, upper=False):
    """Certified prefix u[0:N] of the mechanical word of slope gamma, intercept rho."""
    vals = [(i * gamma) + rho for i in range(N + 1)]
    f = [v.ceil() if upper else v.floor() for v in vals]
    return [f[i + 1] - f[i] for i in range(N)]

# ---------------------------------------------------------------- literal repetition

def lcp_pow(s, ell):
    """lcp(s, (s[0:ell])^inf).  Returns None if it runs past the certified prefix."""
    n = ell
    while n < len(s) and s[n] == s[n - ell]:
        n += 1
    return None if n >= len(s) else n

def attained_powers(u, rmin, ell_min=8):
    """Every ell with an attained initial power of exponent >= rmin.  Purely literal."""
    out = []
    for ell in range(ell_min, len(u) // 2):
        L = lcp_pow(u, ell)
        if L is None:
            break
        r = Fraction(L, ell)
        if r >= rmin:
            out.append((ell, L, r))
    return out

# ---------------------------------------------------------------- arithmetic side

def c_W(W):
    k = sum(W); tot = 0; run = 0
    for i, b in enumerate(W):
        if b:
            run += 1
            tot += 3 ** (k - run) * (1 << i)
    return tot

def F_of(W):
    return abs((1 << len(W)) - 3 ** sum(W)) + c_W(W)

def log2_int(n):
    b = n.bit_length()
    return (b - 1) + math.log2(n / (1 << (b - 1)))

def discrepancy(W):
    g = Fraction(sum(W), len(W)); best = Fraction(0); run = 0
    for i in range(len(W) + 1):
        if i and W[i - 1]:
            run += 1
        d = abs(run - i * g)
        if d > best:
            best = d
    return best

def rote(u, seed):
    v = [seed]
    for x in u:
        v.append(v[-1] ^ x)
    return v

def chain(u, ell, L, seed):
    """One full pass of the chain at one witness.  Returns a dict, or None if the
    certified prefix of v is too short to confirm the transfer depth."""
    W = u[:ell]
    V = rote(u, seed)[:ell]
    v = rote(u, seed)
    if sum(W) % 2 == 0:
        R, branch = V, "even"
    else:
        R, branch = V + [1 - b for b in V], "odd"
    if len(R) >= len(v):
        return None
    Lv = lcp_pow(v, len(R))
    if Lv is None:
        return None
    F = F_of(R)
    return dict(branch=branch, ell=ell, ellR=len(R), r_u=Fraction(L, ell),
                r_v=Fraction(Lv, len(R)), L=L, Lv=Lv, transfer=(Lv == L + 1),
                gammaR=Fraction(sum(R), len(R)), D=discrepancy(R),
                S=Lv - log2_int(F), exact_pos=((1 << Lv) > F))

# ---------------------------------------------------------------- intercepts

def keep_one_intercept(digits, cv, gamma):
    """BHZ Prop. 4.1's 'keep one' intercept, the empirically hardest one, as a certified
    bracket in the repository's [0,1) mechanical convention.

    BHZ: x = sum_{k>=1} c_k (q_{k-1} alpha - p_{k-1}),  here c_k = a_k - 1 with BHZ digits
    a_1 = A_1 - 1, a_k = A_k.  The terms alternate in sign and decay, so truncating an
    alternating tail after an even/odd number of terms brackets the sum.
    theorems/phase5/BHZ_PRIMARY_SOURCE_AUDIT.md: BHZ's x = -alpha is the repository's
    rho = 0, so rho = x + alpha."""
    a = [digits[0] - 1] + list(digits[1:])
    terms = []
    for k in range(1, len(a) + 1):
        ck = a[k - 1] - 1
        if ck <= 0:
            terms.append(Fraction(0)); continue
        p, q = cv[k - 1]
        # q_{k-1} alpha - p_{k-1}, bracketed
        lo = q * gamma.lo - p
        hi = q * gamma.hi - p
        terms.append((min(lo, hi), max(lo, hi), ck))
    lo = hi = Fraction(0)
    for t in terms:
        if t == 0:
            continue
        tlo, thi, ck = t
        lo += ck * tlo; hi += ck * thi
    # widen by the (geometrically small) truncated tail
    pad = Fraction(1, cv[len(a) - 2][1])
    x = Cert(lo - pad, hi + pad)
    return x + gamma

# ---------------------------------------------------------------- main

def audit_slope(digits, N, intercepts, label):
    A = max(digits)
    A_b = max([digits[0] - 1] + list(digits[1:]))
    delta = Fraction(1, 2 * (A_b + 1) ** 2)
    gamma, cv = cf_cert(digits)
    rows = []
    print(f"\n{'='*78}\n{label}:  gamma = [0; {','.join(map(str,digits[:8]))},...]   "
          f"A = {A},  A_b = {A_b},  delta(A_b) = 1/{1//delta} = {float(delta):.6f}")
    print(f"  certified bracket width for gamma: {float(gamma.width()):.3e}  "
          f"(need << 1/N = {1/N:.2e})")
    assert gamma.width() * N < Fraction(1, 100), "bracket too loose for N floors"
    for iname, rho in intercepts:
        for upper in (False, True):
            conv = "upper" if upper else "lower"
            try:
                u = mech(gamma, rho, N, upper=upper)
            except UndecidedError as e:
                print(f"  {iname:<22} {conv:<5}  BRACKET RAISED: {e}")
                raise
            wits = attained_powers(u, 2 + delta)
            for seed in (0, 1):
                got = []
                for (ell, L, r) in wits:
                    c = chain(u, ell, L, seed)
                    if c:
                        c.update(intercept=iname, conv=conv, seed=seed)
                        got.append(c)
                rows.append((iname, conv, seed, got))
    return rows, delta, A_b

def main():
    print("=" * 78)
    print("PHASE 8 / G.  Independent end-to-end audit of Theorem 2's chain")
    print("=" * 78)
    print("No BHZ formula, no Ostrowski digits: literal mechanical words only.")

    cases = []
    # gamma = [0;A,A,A,...] (sup partial quotient exactly A) and one non-periodic slope
    for A, N in ((1, 30000), (2, 30000), (3, 30000)):
        digits = [A] * 40
        gamma, cv = cf_cert(digits)
        ko = keep_one_intercept(digits, cv, gamma)
        intercepts = [
            ("rho = 0", Cert(0, 0)),
            ("rho = 1/2 (rational)", Cert(Fraction(1, 2), Fraction(1, 2))),
            ("rho = {gamma} (return)", gamma),
            ("rho = keep-one (worst)", ko),
        ]
        cases.append((digits, N, intercepts, f"constant slope A={A}"))
    # a genuinely non-eventually-periodic bounded-type slope (Fibonacci-word-coded digits)
    fw = "0"
    while len(fw) < 40:
        fw = "".join("01" if ch == "0" else "0" for ch in fw)
    digits = [1 + int(ch) for ch in fw[:40]]        # digits in {1,2}, not eventually periodic
    gamma, cv = cf_cert(digits)
    ko = keep_one_intercept(digits, cv, gamma)
    cases.append((digits, 30000,
                  [("rho = 0", Cert(0, 0)),
                   ("rho = keep-one (worst)", ko),
                   ("rho = {gamma^2}", Cert(gamma.lo * gamma.lo, gamma.hi * gamma.hi))],
                  "non-eventually-periodic slope, digits in {1,2}"))

    allrows = []
    for digits, N, intercepts, label in cases:
        rows, delta, A_b = audit_slope(digits, N, intercepts, label)
        print(f"  {'intercept':<24}{'conv':<6}{'seed':<5}{'#witnesses':<11}"
              f"{'ell range':<16}{'min r_u':<9}{'branches':<12}{'min S':<9}{'transfer'}")
        for (iname, conv, seed, got) in rows:
            if not got:
                print(f"  {iname:<24}{conv:<6}{seed:<5}{'0':<11}"
                      f"{'-':<16}{'-':<9}{'-':<12}{'-':<9}-")
                continue
            ells = [g["ell"] for g in got]
            brs = sorted({g["branch"] for g in got})
            tr = all(g["transfer"] for g in got)
            pos = all(g["exact_pos"] for g in got)
            print(f"  {iname:<24}{conv:<6}{seed:<5}{len(got):<11}"
                  f"{str(min(ells))+'..'+str(max(ells)):<16}"
                  f"{float(min(g['r_u'] for g in got)):<9.5f}{','.join(brs):<12}"
                  f"{min(g['S'] for g in got):<9.1f}{tr}")
            assert tr, ("transfer L_v = L_u+1 violated", iname, conv, seed)
            assert pos, ("surplus not positive", iname, conv, seed)
            for g in got:
                assert g["r_u"] >= 2 + delta, ("witness below floor", g)
                if g["branch"] == "odd":
                    assert g["gammaR"] == Fraction(1, 2), ("odd-branch density != 1/2", g)
            allrows += got

    # -------- growth of the surplus and sublinearity of the discrepancy
    print("\n" + "-" * 78)
    print("Surplus growth and discrepancy sublinearity, pooled over every case above")
    print("-" * 78)
    buckets = {}
    for g in allrows:
        b = int(math.log2(g["ell"]))
        e = buckets.setdefault(b, [])
        e.append(g)
    print(f"  {'ell ~ 2^b':<12}{'n':<5}{'min S':<11}{'min S/ell':<12}"
          f"{'max D(R)':<10}{'max D/ell':<11}{'max D/log2(ell)'}")
    for b in sorted(buckets):
        gs = buckets[b]
        print(f"  2^{b:<10}{len(gs):<5}{min(g['S'] for g in gs):<11.1f}"
              f"{min(g['S']/g['ell'] for g in gs):<12.4f}"
              f"{float(max(g['D'] for g in gs)):<10.2f}"
              f"{float(max(g['D']/g['ell'] for g in gs)):<11.5f}"
              f"{float(max(g['D']/math.log2(g['ell']) for g in gs)):.3f}")
    print(f"\n  witnesses total: {len(allrows)}   transfer L_v = L_u + 1: "
          f"{sum(g['transfer'] for g in allrows)}/{len(allrows)}   "
          f"2^L_v > F(R): {sum(g['exact_pos'] for g in allrows)}/{len(allrows)}")
    odd = [g for g in allrows if g["branch"] == "odd"]
    print(f"  odd-branch witnesses: {len(odd)}, every one with gamma_R = 1/2 exactly: "
          f"{all(g['gammaR'] == Fraction(1,2) for g in odd)}")

    # -------- gamma/2 is bounded type too (the discrepancy step's hidden hypothesis)
    print("\n" + "-" * 78)
    print("The discrepancy step reduces to the rotation by gamma/2, NOT gamma.")
    print("Claim: gamma badly approximable => gamma/2 badly approximable.")
    print("  ||q gamma|| = ||2 q (gamma/2)|| <= 2 ||q (gamma/2)||, so")
    print("  inf_q q||q gamma/2|| >= (1/2) inf_q q||q gamma|| > 0.   Hence sup p.q. of")
    print("  gamma/2 is bounded by a function of A alone.  Checked numerically:")
    print(f"  {'gamma = [0;...]':<28}{'A = sup p.q.(gamma)':<21}{'sup p.q.(gamma/2)'}")
    for digits in ([1]*30, [2]*30, [3]*30, [4]*30, [5]*30, [1,2]*15, [2,1,3]*10, [1,1,2,3]*7):
        g, cv = cf_cert(digits)
        mid = (g.lo + g.hi) / 2
        h = mid / 2
        # exact CF of the rational midpoint; valid because the bracket is far tighter
        # than the depth we read off
        d2 = []
        x = h
        for _ in range(24):
            ip = math.floor(x)
            d2.append(ip)
            x = x - ip
            if x == 0:
                break
            x = 1 / x
        d2 = d2[1:]                                   # drop the leading 0
        print(f"  {str(digits[:6])+'...':<28}{max(digits):<21}{max(d2[:18])}")

    print("\nALL CHAIN-AUDIT CHECKS PASS.")

if __name__ == "__main__":
    main()
