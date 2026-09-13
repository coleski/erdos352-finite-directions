"""Bounded phase search followed by exact rational interval verification.

This certifies a finite horizontal-base-avoidance construction, NOT an
unrestricted unit-area-triangle avoiding set. No floating-point value is
used as the final certificate for any phase inequality.
"""

from fractions import Fraction as F
from math import floor, isqrt, sqrt


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
SCALE = 10**30
ROOT_INTERVALS = [
    (F(isqrt(p * SCALE**2), SCALE), F(isqrt(p * SCALE**2) + 1, SCALE))
    for p in PRIMES
]


def reciprocal_gap_interval(i, j):
    ilo, ihi = ROOT_INTERVALS[i]
    jlo, jhi = ROOT_INTERVALS[j]
    lo, hi = jlo - ihi, jhi - ilo
    assert lo * hi > 0
    return F(2) / hi, F(2) / lo


def verify_phase(i, frequency):
    phases = []
    for j in range(len(PRIMES)):
        if j == i:
            continue
        lo, hi = reciprocal_gap_interval(i, j)
        lo *= frequency
        hi *= frequency
        integer = floor(lo)
        assert integer == floor(hi)
        assert F(3, 8) < lo - integer <= hi - integer < F(5, 8)
        phases.append((float(lo - integer), float(hi - integer)))
    return phases


def main():
    frequencies = []
    for i, p in enumerate(PRIMES):
        gaps = [2 / (sqrt(q) - sqrt(p)) for q in PRIMES if q != p]
        for frequency in range(1, 1_000_001):
            if all(0.38 < (frequency * d) % 1 < 0.62 for d in gaps):
                phases = verify_phase(i, frequency)
                frequencies.append(frequency)
                print(i, p, frequency, "phase range", min(a for a, _ in phases), max(b for _, b in phases))
                break
        else:
            raise RuntimeError(f"bounded search did not find row {i}")

    eta = min(
        ROOT_INTERVALS[j][0] - ROOT_INTERVALS[i][1]
        for i in range(len(PRIMES)) for j in range(i + 1, len(PRIMES))
    )
    epsilon = min(eta / 4, eta**2 / (128 * max(frequencies)), F(1, 128))
    assert epsilon > 0
    assert epsilon <= eta / 2
    assert 4 * max(frequencies) * epsilon / eta**2 <= F(1, 16)
    assert 1 / epsilon >= 32
    print("frequencies", frequencies)
    print("epsilon", float(epsilon), "length", float(1 / epsilon))
    print("Exact phase and perturbation certificate passed; area >=", F(len(PRIMES), 16))
    print("No claim of avoidance for nonhorizontal bases.")


if __name__ == "__main__":
    main()
