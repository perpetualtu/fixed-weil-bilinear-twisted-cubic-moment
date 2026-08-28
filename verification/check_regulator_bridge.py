"""Finite regression checks for the four beta branches in Proposition 6.4.

This script verifies representative points strictly inside all four Tonelli
chambers.  It is a numerical check of (6.41)--(6.44), not a substitute for
the compact-uniform domination and limiting arguments in the proof.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor" / "mpmath-1.3.0.zip"))

import mpmath as mp


mp.mp.dps = 70

HALF = mp.mpf("0.5")
B = mp.mpf("0.30")
C = mp.mpf("-0.25")
T = mp.mpf("1.75")
R = mp.mpf("2.30")


def relative_error(lhs, rhs):
    return abs(lhs - rhs) / max(mp.mpf(1), abs(lhs), abs(rhs))


def integral(power_zero, power_shifted):
    # Compactify x=R*u/(1-u), then grade both endpoints.  With p=16 the
    # smallest sampled Tonelli margin becomes a positive power at t=0,1.
    p = 16

    def kernel(t):
        if t == 0 or t == 1:
            return mp.mpc(0)
        x = R * mp.power(t / (1 - t), p)
        dx = x * p / (t * (1 - t))
        return mp.power(x, power_zero) * mp.power(x + R, power_shifted) * dx

    return mp.quadts(kernel, [0, 1])


def gamma_quotient(z, numerator, denominator):
    return mp.power(R, -z) * mp.gamma(numerator) * mp.gamma(z) / mp.gamma(denominator)


cases = [
    {
        "name": "direct_plus",
        "lam": mp.mpf("0.20"),
        "s": mp.mpf("1.20"),
        "z": lambda lam, s: lam + C + s,
        "nu": lambda lam, s: 1 - lam + B + s,
        "zero_margin": lambda lam, s: HALF - lam,
        "lhs": lambda lam, s: integral(-HALF - lam - 1j * T, -HALF - C + 1j * T - s),
        "rhs": lambda lam, s, z: gamma_quotient(z, HALF - lam - 1j * T, HALF + C - 1j * T + s),
    },
    {
        "name": "direct_minus",
        "lam": mp.mpf("0.775"),
        "s": mp.mpf("0.6125"),
        "z": lambda lam, s: lam + C + s,
        "nu": lambda lam, s: 1 - lam + B + s,
        "zero_margin": lambda lam, s: HALF - C - s,
        "lhs": lambda lam, s: integral(-HALF - C + 1j * T - s, -HALF - lam - 1j * T),
        "rhs": lambda lam, s, z: gamma_quotient(z, HALF - C + 1j * T - s, HALF + lam + 1j * T),
    },
    {
        "name": "dual_plus",
        "lam": mp.mpf("0.20"),
        "s": mp.mpf("1.30"),
        "z": lambda lam, s: lam - B + s,
        "nu": lambda lam, s: 1 - lam - C + s,
        "zero_margin": lambda lam, s: HALF - lam,
        "lhs": lambda lam, s: integral(-HALF - lam - 1j * T, -HALF + B + 1j * T - s),
        "rhs": lambda lam, s, z: gamma_quotient(z, HALF - lam - 1j * T, HALF - B - 1j * T + s),
    },
    {
        "name": "dual_minus",
        "lam": mp.mpf("0.775"),
        "s": mp.mpf("0.6625"),
        "z": lambda lam, s: lam - B + s,
        "nu": lambda lam, s: 1 - lam - C + s,
        "zero_margin": lambda lam, s: HALF + B - s,
        "lhs": lambda lam, s: integral(-HALF + B + 1j * T - s, -HALF - lam - 1j * T),
        "rhs": lambda lam, s, z: gamma_quotient(z, HALF + B + 1j * T - s, HALF + lam + 1j * T),
    },
]


errors = []
for case in cases:
    lam = case["lam"]
    s = case["s"]
    z = case["z"](lam, s)
    nu = case["nu"](lam, s)
    margins = (z - 1, nu - 1, case["zero_margin"](lam, s))
    assert min(margins) > 0, f"{case['name']}: sample is not strictly inside its Tonelli chamber"

    lhs = case["lhs"](lam, s)
    rhs = case["rhs"](lam, s, z)
    error = relative_error(lhs, rhs)
    errors.append(error)
    print(
        f"branch={case['name']} min_margin={mp.nstr(min(margins), 6)} "
        f"beta_relerr={mp.nstr(error, 8)}"
    )

assert max(errors) < mp.mpf("1e-35"), "a beta identity exceeded the regression threshold"
print("status=PASS")
