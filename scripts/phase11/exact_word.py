"""
Phase 11: exact machinery for the named word

    alpha = (sqrt5 - 1)/2 ,   rho = 1/7 ,   beta = ln2/ln3 ,
    s_n = 1  <=>  {n*alpha + rho} in [0, beta) .

alpha-arithmetic is EXACT in Q(sqrt5) -- no bracket, no rounding.  Only comparisons against the
transcendental beta use a certified bracket, refined until the comparison is decided or the code
raises.  So every symbol of s is certified.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
import math

getcontext().prec = 400

class Q5:
    """a + b*sqrt(5), a,b in Q.  Exact ordered field arithmetic."""
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = Fraction(a); self.b = Fraction(b)
    def __add__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(s.a + o.a, s.b + o.b)
    def __sub__(s, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(s.a - o.a, s.b - o.b)
    def __rmul__(s, n):
        return Q5(s.a * n, s.b * n)
    def sign(s):
        a, b = s.a, s.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        # mixed signs: compare a^2 with 5 b^2
        d = a * a - 5 * b * b
        if a > 0:                      # b < 0 : positive iff a^2 > 5b^2
            return 1 if d > 0 else (-1 if d < 0 else 0)
        else:                          # a < 0, b > 0 : positive iff 5b^2 > a^2
            return -1 if d > 0 else (1 if d < 0 else 0)
    def __float__(s):
        return float(s.a) + float(s.b) * math.sqrt(5)
    def floor(s):
        n = math.floor(float(s))
        for cand in (n - 2, n - 1, n, n + 1, n + 2):
            if (s - Q5(cand)).sign() >= 0 and (s - Q5(cand + 1)).sign() < 0:
                return cand
        raise AssertionError("floor failed")
    def frac(s):
        return s - Q5(s.floor())

ALPHA = Q5(Fraction(-1, 2), Fraction(1, 2))       # (sqrt5 - 1)/2
RHO   = Q5(Fraction(1, 7))

def beta_bracket(prec_digits=300):
    b = Decimal(2).ln() / Decimal(3).ln()
    scale = 10 ** prec_digits
    lo = Fraction(int(b * Decimal(scale)), scale)
    return lo, lo + Fraction(1, scale)

BLO, BHI = beta_bracket()

class Undecided(Exception):
    pass

def lt_beta(x):
    """Is the Q5 value x (assumed in [0,1)) < beta?  Certified."""
    if (x - Q5(BHI)).sign() < 0 and (x - Q5(BLO)).sign() < 0:
        return True
    if (x - Q5(BLO)).sign() >= 0 and (x - Q5(BHI)).sign() >= 0:
        return False
    raise Undecided(f"x within the beta bracket: {float(x)}")

def orbit(n):
    """{n*alpha + rho} exactly."""
    return (n * ALPHA + RHO).frac()

def word(N):
    return [1 if lt_beta(orbit(n)) else 0 for n in range(N)]

def delta(ell):
    """signed ell*alpha - nearest integer, exactly."""
    x = ell * ALPHA
    n = x.floor()
    f = x - Q5(n)
    return f if (f - Q5(Fraction(1, 2))).sign() < 0 else f - Q5(1)

def norm(x):
    """||x|| = distance from x to the nearest integer, as a Q5 (non-negative)."""
    n = x.floor()
    f = x - Q5(n)
    return f if (f - Q5(Fraction(1, 2))).sign() < 0 else Q5(1) - f

def in_mismatch(x, d):
    """Is x in the mismatch set of [0,beta) under translation by d?
    d>0: [-d,0) u [beta-d, beta);  d<0: [0,|d|) u [beta, beta+|d|).   x in [0,1)."""
    sgn = d.sign()
    if sgn == 0:
        return False
    if sgn > 0:
        # x in [1-d, 1)  or  x in [beta-d, beta)
        if (x - (Q5(1) - d)).sign() >= 0:
            return True
        return (not lt_beta(x)) is False and (x - (Q5(BHI) - d)).sign() >= 0 and lt_beta(x)
    else:
        ad = Q5(0) - d
        if x.sign() >= 0 and (x - ad).sign() < 0:
            return True
        return (not lt_beta(x)) and (x - (Q5(BLO) + ad)).sign() < 0

def convergents(n=45):
    p0, q0, p1, q1 = 0, 1, 1, 1
    out = [(p1, q1)]
    for _ in range(n):
        p0, q0, p1, q1 = p1, q1, p1 + p0, q1 + q0
        out.append((p1, q1))
    return out
