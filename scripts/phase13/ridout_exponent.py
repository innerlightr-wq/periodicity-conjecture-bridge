"""Phase 13 / item 2.  How far are the witnesses from Ridout's p-adic Roth threshold?

Bugeaud-Kekec, "On Mahler's classification of p-adic numbers", Theorem 1.3 (= Ridout 1958):
if there are rationals x_n/y_n, gcd = 1, with heights 2 <= |x_1,y_1| < |x_2,y_2| < ... and
0 < |xi - x_n/y_n|_p < |x_n,y_n|^{-2-eps}, then xi is TRANSCENDENTAL.

Our approximants are c_W/delta_W with |Phi(s) - c_W/delta_W|_2 = 2^{-L}.  So the exponent is
    E(ell) := L(ell) / log2( height of the REDUCED c_W/delta_W ) ,
and Ridout needs E > 2 + eps for infinitely many, with heights increasing.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "phase12"))
from fractions import Fraction as Fr
from qfield import Q, cf, chi, dist_to_int

D = 5
ALPHA = Q(Fr(-1, 2), Fr(1, 2), D)
RHO = Q(Fr(1, 7), 0, D)
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

W_ = []
def sym(m):
    return chi((Q(m, 0, D) * ALPHA + RHO).frac())
def word(n):
    while len(W_) < n:
        W_.append(sym(len(W_)))
    return W_
def L_exact(ell):
    i = ell
    while True:
        word(i + 400)
        if W_[i] != W_[i % ell]:
            return i
        i += 1
def c_of(Wd):
    k = sum(Wd); c = 0; run = 0
    for i, b in enumerate(Wd):
        if b:
            run += 1; c += 3 ** (k - run) * 2 ** i
    return c, k

P("=" * 96)
P("PHASE 13 / item 2.  The Ridout exponent of the periodic approximants (named Phase 11 word)")
P("=" * 96)
P("")
P("  ell     k      L        log2 H_red   E = L/log2(H_red)   > 2 ?   m*/ell")
qs = cf(ALPHA, 40)[2]
rows = []
best = 0.0
for q in qs[3:]:
    if q > 30000:
        break
    word(q + 10)
    Wd = W_[:q]; c, k = c_of(Wd); den = 2 ** q - 3 ** k
    g = math.gcd(c, abs(den))
    cr, dr = c // g, abs(den) // g
    Hred = max(cr, dr)
    L = L_exact(q)
    lgH = math.log2(Hred) if Hred > 1 else 1.0
    E = L / lgH
    best = max(best, E)
    rows.append((q, k, L, lgH, E, (L - q) / q, g))
    P(f"  {q:<7} {k:<6} {L:<8} {lgH:<12.2f} {E:<19.6f} {str(E>2):<7} {(L-q)/q:.4f}")
P("")
P(f"  max exponent observed: E = {best:.6f}   (Ridout needs E > 2 + eps for INFINITELY many)")
P(f"  gcd(c_W, delta_W) was {'always 1' if all(r[6]==1 for r in rows) else 'sometimes > 1'}")
above = [r for r in rows if r[4] > 2]
P(f"  convergents with E > 2 : {len(above)} of {len(rows)}  -> ell = {[r[0] for r in above]}")
P("")
P("  READING.  E > 2 happens, repeatedly, but NOT along the constructed witness family: the")
P("  construction takes ell(M) with L - ell >= M and ell(M) >= 49M, so E -> 1 there.  Whether")
P("  E > 2 + eps for INFINITELY many convergents is exactly the statement  m*(ell)/ell > 1 + eps")
P("  infinitely often, which is open.  If it held, Ridout would give TRANSCENDENCE of Phi(s),")
P("  answering the foundation paper's open problem (3) for this word.  It is NOT claimed here.")
P("")
P("  Empirical distribution of m*(ell)/ell over the convergents above:")
r = sorted(x[5] for x in rows)
P(f"    min {r[0]:.4f}   median {r[len(r)//2]:.4f}   max {r[-1]:.4f}   fraction > 1: {sum(1 for x in r if x>1)}/{len(r)}")
P("")
P("ALL PHASE-13 RIDOUT-EXPONENT COMPUTATIONS COMPLETE (no assertion: this is a measurement).")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
     "data", "phase13", "ridout_exponent_output.txt"), "w").write("\n".join(out) + "\n")
