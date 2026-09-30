"""Phase 13.  Exact arithmetic in a number field Q(theta), for ALGEBRAIC intercepts.

Written from scratch (no sympy/mpmath available).  Elements are Fraction vectors in the power
basis 1, theta, ..., theta^{D-1}.  Sign decisions are RIGOROUS: an element is zero iff its
coefficient vector is zero, and for a non-zero element the characteristic polynomial supplies an
a priori separation bound  |x| >= (1 + H)^{-D},  so a numeric evaluation carried to more than
D*log10(1+H) digits decides the sign with certainty.
"""
from fractions import Fraction as Fr
from decimal import Decimal, getcontext, localcontext
import math

WORK = 220                      # working digits for ordinary sign decisions
getcontext().prec = WORK + 60


class Undecided(Exception):
    pass


def _dec(fr, prec):
    with localcontext() as c:
        c.prec = prec
        return Decimal(fr.numerator) / Decimal(fr.denominator)


class NumField:
    """Q(theta) with theta a root of the monic integer polynomial f (list of ints, low->high)."""

    def __init__(self, f, root_approx, name="theta"):
        assert f[-1] == 1
        self.f = [Fr(c) for c in f]
        self.D = len(f) - 1
        self.name = name
        self.root = self._refine(Decimal(root_approx), WORK + 40)
        self.powers = self._theta_powers(WORK + 40)

    # ---- numerics -------------------------------------------------------
    def _fval(self, x, prec):
        with localcontext() as c:
            c.prec = prec
            s = Decimal(0)
            for co in reversed(self.f):
                s = s * x + _dec(co, prec)
            return s

    def _dfval(self, x, prec):
        with localcontext() as c:
            c.prec = prec
            s = Decimal(0)
            for i in range(self.D, 0, -1):
                s = s * x + _dec(self.f[i] * i, prec)
            return s

    def _refine(self, x, prec):
        with localcontext() as c:
            c.prec = prec + 20
            for _ in range(200):
                d = self._dfval(x, prec + 20)
                if d == 0:
                    break
                nx = x - self._fval(x, prec + 20) / d
                if nx == x:
                    break
                x = nx
            return +x

    def _theta_powers(self, prec):
        with localcontext() as c:
            c.prec = prec
            p = [Decimal(1)]
            for _ in range(self.D - 1):
                p.append(p[-1] * self.root)
            return p

    # ---- element algebra ------------------------------------------------
    def el(self, *coeffs):
        v = [Fr(0)] * self.D
        for i, c in enumerate(coeffs):
            v[i] = Fr(c)
        return El(self, v)

    def rat(self, q):
        return self.el(q)

    def reduce(self, v):
        """reduce a list of Fractions of any length modulo f, in place semantics."""
        v = list(v)
        while len(v) > self.D:
            top = v.pop()
            if top:
                k = len(v) - self.D            # theta^{len(v)} = -sum f_i theta^{i+k}
                for i in range(self.D):
                    v[i + k] -= top * self.f[i]
        while len(v) < self.D:
            v.append(Fr(0))
        return v


class El:
    __slots__ = ("K", "v")

    def __init__(self, K, v):
        self.K = K
        self.v = list(v)

    def _co(self, o):
        return o if isinstance(o, El) else self.K.rat(o)

    def __add__(s, o):
        o = s._co(o); return El(s.K, [a + b for a, b in zip(s.v, o.v)])
    __radd__ = __add__

    def __neg__(s):
        return El(s.K, [-a for a in s.v])

    def __sub__(s, o):
        return s + (-s._co(o))

    def __rsub__(s, o):
        return s._co(o) + (-s)

    def __mul__(s, o):
        o = s._co(o)
        D = s.K.D
        w = [Fr(0)] * (2 * D - 1)
        for i, a in enumerate(s.v):
            if a:
                for j, b in enumerate(o.v):
                    if b:
                        w[i + j] += a * b
        return El(s.K, s.K.reduce(w))
    __rmul__ = __mul__

    def is_zero(s):
        return all(a == 0 for a in s.v)

    # ---- multiplication matrix, characteristic polynomial, height -------
    def mat(s):
        D = s.K.D
        cols = []
        e = s.K.el(1)
        for j in range(D):
            cols.append((s * e).v)
            e = e * s.K.el(0, 1)
        return [[cols[j][i] for j in range(D)] for i in range(D)]

    def charpoly(s):
        """integer coefficients (primitive), low->high, of the char. poly of multiplication by s."""
        D = s.K.D
        M = s.mat()
        # traces of powers
        P = [[Fr(1) if i == j else Fr(0) for j in range(D)] for i in range(D)]
        tr = []
        for _ in range(D):
            P = [[sum(P[i][k] * M[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
            tr.append(sum(P[i][i] for i in range(D)))
        # Newton's identities: e_1 = p_1 ; k e_k = sum_{i=1..k} (-1)^{i-1} e_{k-i} p_i
        e = [Fr(1)]
        for k in range(1, D + 1):
            acc = Fr(0)
            for i in range(1, k + 1):
                acc += (-1) ** (i - 1) * e[k - i] * tr[i - 1]
            e.append(acc / k)
        # char poly = sum_{k} (-1)^k e_k t^{D-k}
        co = [(-1) ** (D - i) * e[D - i] for i in range(D + 1)]
        den = 1
        for c in co:
            den = den * c.denominator // math.gcd(den, c.denominator)
        ico = [int(c * den) for c in co]
        g = 0
        for c in ico:
            g = math.gcd(g, abs(c))
        if g:
            ico = [c // g for c in ico]
        return ico

    def height(s):
        return max(abs(c) for c in s.charpoly())

    def sep_bound_digits(s):
        """d such that |s| >= 10^{-d}, from Liouville via the characteristic polynomial."""
        H = s.height()
        return int(s.K.D * (math.log10(H + 1) + 1)) + 2

    # ---- certified numerics --------------------------------------------
    def approx(s, prec=None):
        prec = prec or WORK
        with localcontext() as c:
            c.prec = prec
            tot = Decimal(0)
            for i, a in enumerate(s.v):
                if a:
                    tot += _dec(a, prec) * s.K.powers[i]
            return +tot

    def sign(s):
        if s.is_zero():
            return 0
        val = s.approx(WORK)
        guard = Decimal(10) ** (-(WORK - 40))
        if abs(val) > guard:
            return 1 if val > 0 else -1
        d = s.sep_bound_digits()
        prec = d + 60
        with localcontext() as c:
            c.prec = prec + 40
            K = s.K
            root = K._refine(K.root, prec + 40)
            p = [Decimal(1)]
            for _ in range(K.D - 1):
                p.append(p[-1] * root)
            tot = Decimal(0)
            for i, a in enumerate(s.v):
                if a:
                    tot += _dec(a, prec + 40) * p[i]
        if abs(tot) <= Decimal(10) ** (-d - 1):
            raise Undecided("separation bound violated -- bug")
        return 1 if tot > 0 else -1

    def __lt__(s, o): return (s - s._co(o)).sign() < 0
    def __le__(s, o): return (s - s._co(o)).sign() <= 0
    def __gt__(s, o): return (s - s._co(o)).sign() > 0
    def __ge__(s, o): return (s - s._co(o)).sign() >= 0
    def __eq__(s, o): return (s - s._co(o)).is_zero()

    def floor(s):
        n = int(s.approx(60))
        while s.K.rat(n) > s:
            n -= 1
        while s.K.rat(n + 1) <= s:
            n += 1
        return n

    def frac(s):
        return s - s.K.rat(s.floor())

    def nearest_int(s):
        n = s.floor()
        return n if (s - s.K.rat(n)) <= s.K.rat(Fr(1, 2)) else n + 1

    def dist_int(s):
        f = s.frac()
        one_m = s.K.rat(1) - f
        return f if f <= one_m else one_m

    def inverse(s):
        """1/s by solving M_s y = e_0 over Q (D <= 6, exact Gaussian elimination)."""
        assert not s.is_zero()
        D = s.K.D
        A = [row[:] + [Fr(1) if i == 0 else Fr(0)] for i, row in enumerate(s.mat())]
        for c in range(D):
            piv = next(r for r in range(c, D) if A[r][c] != 0)
            A[c], A[piv] = A[piv], A[c]
            pv = A[c][c]
            A[c] = [x / pv for x in A[c]]
            for r in range(D):
                if r != c and A[r][c] != 0:
                    f = A[r][c]
                    A[r] = [x - f * y for x, y in zip(A[r], A[c])]
        return El(s.K, [A[i][D] for i in range(D)])

    def __repr__(s):
        return "+".join(f"{a}*{s.K.name}^{i}" for i, a in enumerate(s.v) if a) or "0"


def beta_bracket(prec=300):
    with localcontext() as c:
        c.prec = prec + 40
        v = Decimal(2).ln() / Decimal(3).ln()
        eps = Decimal(10) ** (-prec)
        f = 10 ** prec
        return Fr(int((v - eps) * f), f), Fr(int((v + eps) * f) + 1, f)


BLO, BHI = beta_bracket()
BETA_F = float(Decimal(2).ln() / Decimal(3).ln())


def lt_beta(x):
    """certified test x < beta for x in a number field; raises if the 300-digit bracket fails."""
    if x < x.K.rat(BLO):
        return True
    if x >= x.K.rat(BHI):
        return False
    raise Undecided("cannot separate from beta with 300 digits")


def chi(x):
    return 1 if lt_beta(x) else 0


def cf(x, limit):
    """partial quotients and convergent denominators of x, exactly."""
    a, ps, qs = [], [], []
    pm1, pm2, qm1, qm2 = 1, 0, 0, 1
    for _ in range(limit):
        n = x.floor()
        a.append(n)
        p, q = n * pm1 + pm2, n * qm1 + qm2
        ps.append(p); qs.append(q)
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
        r = x - x.K.rat(n)
        if r.is_zero():
            break
        x = r.inverse()
    return a, ps, qs
