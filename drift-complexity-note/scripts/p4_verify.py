"""Phase 4 publication-readiness verification (new code; standard library only; exact integers/Fractions).
Checks the statements EXACTLY as they will appear in the note:

 V1  Lemma 2 (factor => congruence): v[i:i+L] == v[j:j+L]  implies  a_i == a_j (mod 2^L)   [only direction used]
 V2  Lemma 4 (finite counting, sharp form, NO aperiodicity needed):
        p_v(L) >= #{ distinct values a_i in [c, c+2^L) }   for every integer c   (whole orbit known)
     and the equality p_v(L) = #{a_i mod 2^L} (whole orbit).
 V3  Off-by-one audit: the CLOSED symmetric interval [-2^{L-1}, 2^{L-1}] can contain p_v(L)+1 distinct values
     (so half-open is necessary) -- search for an explicit instance.
 V4  Lemma 3 envelope |a_n| <= 2^{Omega_n}(|a| + b k_n/2), b normalised > 0, negative a included.
 V5  Theorem finite core: with J* = max{J : Omega*_J + log2(|a| + b J/2) + 1 < L} (exact test:
        2^{Omega*_J} * (|a| + bJ/2) * 2 < 2^L),  if a_0..a_{J*} distinct then the factors at 0..J* are distinct.
 V6  Lemma 5 shift inequalities (exact).
 V7  Carry identity a_n = 2^{rho_n} Lambda - b K(s^n v) on supercritical rational cycles, and Lambda = 0 there.
Random sampling is used for parameters; every decision is exact.
"""
import random
from fractions import Fraction
from math import gcd

random.seed(4040)
S = {}


def rec(k, ok):
    s = S.setdefault(k, [0, 0]); s[0] += 1; s[1] += (not ok)


def T(a, b):
    return a // 2 if a % 2 == 0 else (3 * a + b) // 2


def full_orbit(a, b, cap=100000):
    orb = [a]; pos = {a: 0}
    while len(orb) < cap:
        y = T(orb[-1], b)
        if y in pos:
            return orb, pos[y]
        pos[y] = len(orb); orb.append(y)
    return None, None


def word_from(orb, pre, n):
    per = len(orb) - pre
    return [(orb[i] if i < len(orb) else orb[pre + (i - pre) % per]) & 1 for i in range(n)]


closed_violations = []
for trial in range(3000):
    b = random.choice([1, 3, 5, 7, 11, 13, 17, 31, 101])
    a = random.randint(-5000, 5000)
    if a == 0 or gcd(a, b) != 1:
        continue
    orb, pre = full_orbit(a, b)
    if orb is None:
        continue
    npos = len(orb)
    for L in range(1, 11):
        w = word_from(orb, pre, npos + L + 1)
        facs = {tuple(w[i:i + L]) for i in range(npos)}  # all factors of the one-sided infinite word
        res = {x % (1 << L) for x in orb}
        rec("V2 p(L) = #{a_i mod 2^L} (whole orbit)", len(facs) == len(res))
        vals = set(orb)
        for c in random.sample(range(-3 * (1 << L), 3 * (1 << L)), 6) + [-(1 << (L - 1))]:
            cnt = sum(1 for x in vals if c <= x < c + (1 << L))
            rec("V2 p(L) >= #{distinct a_i in [c, c+2^L)}", len(facs) >= cnt)
        cc = sum(1 for x in vals if -(1 << (L - 1)) <= x <= (1 << (L - 1)))
        if cc > len(facs):
            closed_violations.append((a, b, L, cc, len(facs)))
    # V1 on pairs
    w = word_from(orb, pre, npos + 40)
    for _ in range(20):
        i, j = random.randrange(npos), random.randrange(npos)
        L = random.randint(1, 12)
        ai = orb[i]; aj = orb[j]
        if w[i:i + L] == w[j:j + L]:
            rec("V1 equal factors => congruent mod 2^L", (ai - aj) % (1 << L) == 0)
    # V4 envelope along the first 60 steps (sign of a arbitrary, b>0)
    ks = [0]
    for t in range(60):
        ks.append(ks[-1] + w[t] if t < len(w) else ks[-1])
    for n in range(1, min(60, len(w))):
        G = max(Fraction(3 ** (ks[n] - ks[t]), 2 ** (n - t)) for t in range(n + 1))
        an = orb[n] if n < len(orb) else orb[pre + (n - pre) % (len(orb) - pre)]
        rec("V4 envelope |a_n| <= 2^Omega_n (|a| + b k_n/2)", abs(an) <= G * (abs(a) + Fraction(b * ks[n], 2)))
    # V5 finite core on the distinct prefix a_0..a_{npos-1}
    rises = [Fraction(1)]; cur = Fraction(1); best = Fraction(1)
    for t in range(npos):
        cur = max(Fraction(1), cur * Fraction(3 if w[t] else 1, 2)); best = max(best, cur); rises.append(best)
    for L in range(2, 40):
        Js = [J for J in range(npos) if 2 * rises[J] * (abs(a) + Fraction(b * J, 2)) < (1 << L)]
        if not Js:
            continue
        Jstar = max(Js)
        if Js != list(range(Jstar + 1)):
            rec("V5 J-set is an initial segment (monotonicity)", False); continue
        rec("V5 J-set is an initial segment (monotonicity)", True)
        ww = word_from(orb, pre, Jstar + L + 1)
        rec("V5 all factors at positions 0..J* distinct", len({tuple(ww[i:i + L]) for i in range(Jstar + 1)}) == Jstar + 1)

# V6 shift inequalities
def omega_star_factor(v):
    best = cur = Fraction(1)
    for x in v:
        cur = max(Fraction(1), cur * Fraction(3 if x else 1, 2)); best = max(best, cur)
    return best
for _ in range(2000):
    v = [random.randint(0, 1) for _ in range(random.randint(1, 150))]
    r = random.randint(0, len(v) - 1)
    A = omega_star_factor(v); B = omega_star_factor(v[r:])
    rec("V6 Omega*_N(s^r v) <= Omega*_{N+r}(v)", B <= A)
    rec("V6 Omega*_{N+r}(v) <= Omega*_N(s^r v) + r log2(3/2)", A <= B * Fraction(3, 2) ** r)

# V7 carry identity on supercritical cycles
def K_periodic(V):
    p, q = Fraction(1), Fraction(0)
    for x in reversed(V):
        p, q = (Fraction(2, 3) * p, Fraction(1, 3) + Fraction(2, 3) * q) if x else (2 * p, 2 * q)
    return q / (1 - p)
def K_ep(U, V):
    x = K_periodic(V)
    for y in reversed(U):
        x = Fraction(1, 3) + Fraction(2, 3) * x if y else 2 * x
    return x
ncyc = 0
for trial in range(3000):
    b = random.choice([1, 5, 7, 11, 13, 17, 19, 23]); a = random.randint(-2000, 2000)
    if a == 0 or gcd(a, b) != 1: continue
    orb, pre = full_orbit(a, b)
    if orb is None: continue
    U = [x & 1 for x in orb[:pre]]; V = [x & 1 for x in orb[pre:]]
    if 3 ** sum(V) <= 2 ** len(V): continue
    ncyc += 1
    Lam = a + b * K_ep(U, V)
    rec("V7 Lambda == 0 on supercritical (eventually periodic) rational points", Lam == 0)
    w = U + V * 3; k = 0
    for n in range(len(U) + len(V)):
        Kn = K_ep(U[n:], V) if n < len(U) else K_periodic(V[(n - len(U)):] + V[:(n - len(U))])
        rec("V7 a_n = 2^rho_n Lambda - b K(s^n v)", Fraction(orb[n]) == Fraction(3 ** k, 2 ** n) * Lam - b * Kn)
        k += w[n]

for k_ in sorted(S): print(f"{k_:72s} {S[k_][0]:8d} fail {S[k_][1]}")
print("TOTAL", sum(s[0] for s in S.values()), "FAILURES", sum(s[1] for s in S.values()))
print("supercritical cycles tested:", ncyc)
print("V3 closed-interval off-by-one instances found (a, b, L, #values in closed interval, p(L)):", len(closed_violations))
for x in closed_violations[:5]: print("   ", x)
