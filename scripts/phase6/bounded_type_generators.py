"""
Phase 6: generators for genuinely non-eventually-periodic, bounded-partial-
quotient continued fractions, used as adversarial controls against any
reasoning/code that silently assumes a repeating CF tail.

All partial quotients lie in {1,2} (so A=2 for every sequence here,
directly comparable to the audited "A+1" margin formula) but are produced
by aperiodic rules:

  - thue_morse_pq(n):   a_i = 1 + t_i, t = Thue-Morse sequence (0/1),
                        provably not eventually periodic.
  - fibonacci_pq(n):    a_i = 1 + f_i, f = the Fibonacci word (image of the
                        Fibonacci morphism 0->01, 1->0), provably not
                        eventually periodic, and NOT purely/eventually
                        periodic as a digit sequence either (it is a fixed
                        point of a substitution, low-complexity but
                        genuinely aperiodic).
  - random_bounded_pq(n, seed): i.i.d. uniform in {1,2}, for a purely
                        statistical (non-structured) bounded-type control.

Periodicity of each generated digit sequence is checked directly (not
assumed) before use.
"""
import random


def thue_morse_bits(n):
    t = [0]
    while len(t) < n:
        t = t + [1 - x for x in t]
    return t[:n]


def thue_morse_pq(n):
    t = thue_morse_bits(n)
    return [1 + x for x in t]  # values in {1,2}


def fibonacci_word_bits(n):
    """Fixed point of 0->01, 1->0, starting from 0."""
    w = [0]
    while len(w) < n:
        nw = []
        for b in w:
            nw.extend([0, 1] if b == 0 else [0])
        w = nw
    return w[:n]


def fibonacci_pq(n):
    f = fibonacci_word_bits(n)
    return [1 + x for x in f]  # values in {1,2}


def random_bounded_pq(n, seed=0):
    rng = random.Random(seed)
    return [rng.randint(1, 2) for _ in range(n)]


def is_eventually_periodic(seq, max_period=None, min_repeats=4):
    """Brute-force check: is seq eventually periodic within what's given?
    Returns (is_periodic, preperiod_len, period_len) or (False, None, None)."""
    n = len(seq)
    max_period = max_period or n // (min_repeats + 1)
    for start in range(0, n // 2):
        tail = seq[start:]
        m = len(tail)
        for period in range(1, min(max_period, m // min_repeats) + 1):
            if m < period * min_repeats:
                continue
            root = tail[:period]
            reps = m // period
            if root * reps == tail[:period * reps]:
                return True, start, period
    return False, None, None


if __name__ == "__main__":
    for name, gen in [("Thue-Morse", thue_morse_pq), ("Fibonacci", fibonacci_pq),
                       ("random(seed=7)", lambda n: random_bounded_pq(n, seed=7))]:
        seq = gen(4000)
        periodic, start, period = is_eventually_periodic(seq, max_period=200)
        print(f"{name}: first 40 terms = {seq[:40]}")
        print(f"  max value = {max(seq)}  (A = {max(seq)})")
        print(f"  eventually periodic (checked up to period 200, min 4 repeats)? {periodic}"
              + (f"  (start={start}, period={period})" if periodic else ""))
        print()
