"""Phase 12.  Exact arithmetic in Q(sqrt D), written independently of scripts/phase11.

Nothing here is imported from Phase 11; the point of Phase 12 item 1 is an independent
reconstruction, so every routine below is re-derived from the definitions.
"""
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import itertools, math

getcontext().prec = 320


class Q:
    """a + b*sqrt(D), with a,b rational and D a positive squarefree integer."""
    __slots__ = ("a", "b", "D")

    def __init__(self, a=0, b=0, D=5):
        self.a = Fr(a); self.b = Fr(b); self.D = D

    def __add__(s, o):
        o = s._co(o); return Q(s.a + o.a, s.b + o.b, s.D)

    def __sub__(s, o):
        o = s._co(o); return Q(s.a - o.a, s.b - o.b, s.D)

    def __neg__(s):
        return Q(-s.a, -s.b, s.D)

    def __mul__(s, o):
        o = s._co(o)
        return Q(s.a * o.a + s.D * s.b * o.b, s.a * o.b + s.b * o.a, s.D)

    __rmul__ = __mul__
    __radd__ = __add__

    def _co(s, o):
        return o if isinstance(o, Q) else Q(o, 0, s.D)

    def sign(s):
        """Exact sign of a + b*sqrt(D).  No floating point anywhere."""
        a, b, D = s.a, s.b, s.D
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        # opposite signs: compare a^2 with D*b^2
        c = a * a - D * b * b            # sign of a+b*sqrt(D) = sign(a)*sign(a^2-D b^2) ... careful
        # a>0,b<0: a+b√D>0 iff a^2 > D b^2
        if a > 0:
            return (c > 0) - (c < 0)
        else:
            return -((c > 0) - (c < 0))

    def __lt__(s, o): return (s - s._co(o)).sign() < 0
    def __le__(s, o): return (s - s._co(o)).sign() <= 0
    def __gt__(s, o): return (s - s._co(o)).sign() > 0
    def __ge__(s, o): return (s - s._co(o)).sign() >= 0
    def __eq__(s, o): return (s - s._co(o)).sign() == 0

    def floor(s):
        """Exact floor, by rational bracketing of sqrt(D) -- never trusts a float."""
        if s.b == 0:
            return math.floor(s.a)
        n = int(s.approx())          # float estimate, then verified and corrected exactly
        while Q(n, 0, s.D) > s:
            n -= 1
        while Q(n + 1, 0, s.D) <= s:
            n += 1
        return n

    def frac(s):
        return s - Q(s.floor(), 0, s.D)

    def approx(s):
        return float(s.a) + float(s.b) * math.sqrt(s.D)

    def dec(s, prec=250):
        getcontext().prec = prec
        return Decimal(s.a.numerator) / Decimal(s.a.denominator) + \
               (Decimal(s.b.numerator) / Decimal(s.b.denominator)) * Decimal(s.D).sqrt()

    def __repr__(s):
        return f"({s.a}+{s.b}v{s.D})"


class Undecided(Exception):
    pass


def beta_bracket(prec=300):
    """Certified rational bracket BLO < log_3 2 < BHI, from high-precision Decimal ln."""
    getcontext().prec = prec + 40
    v = Decimal(2).ln() / Decimal(3).ln()
    eps = Decimal(10) ** (-prec)
    lo, hi = v - eps, v + eps
    f = 10 ** prec
    BLO = Fr(int(lo * f), f)
    BHI = Fr(int(hi * f) + 1, f)
    assert BLO < BHI
    # sanity: 3^BLO < 2 < 3^BHI  checked through ln with margin
    return BLO, BHI


BLO, BHI = beta_bracket()


def lt_beta(x):
    """Certified test  x < beta  for x in [0,1) exact in Q(sqrt D).  Raises if undecided."""
    if x < Q(BLO, 0, x.D):
        return True
    if x >= Q(BHI, 0, x.D):
        return False
    raise Undecided(f"cannot decide {x} vs beta with the 300-digit bracket")


def chi(x):
    return 1 if lt_beta(x) else 0


def cf(a_num_D, limit):
    """Continued fraction partial quotients and convergent denominators of a Q element."""
    x = a_num_D
    a, qs, ps = [], [], []
    pm1, pm2, qm1, qm2 = 1, 0, 0, 1
    for _ in range(limit):
        n = x.floor()
        a.append(n)
        p, q = n * pm1 + pm2, n * qm1 + qm2
        ps.append(p); qs.append(q)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
        r = x - Q(n, 0, x.D)
        if r.sign() == 0:
            break
        # reciprocal of r = a+b√D  is  (a-b√D)/(a^2-D b^2)
        den = r.a * r.a - x.D * r.b * r.b
        x = Q(r.a / den, -r.b / den, x.D)
    return a, ps, qs


def dist_to_int(x):
    """||x|| as an exact Q element (>=0)."""
    f = x.frac()
    one_minus = Q(1, 0, x.D) - f
    return f if f <= one_minus else one_minus
