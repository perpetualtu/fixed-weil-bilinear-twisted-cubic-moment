"""Finite regression checks for the four beta branches in Proposition 6.4.

This script verifies representative points strictly inside all four Tonelli
chambers and the integrability of the model endpoint pullback used when the
source regulator is removed.  These are finite numerical checks, not a
substitute for compact-uniform domination and limiting arguments.
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

# The repaired source argument integrates through the endpoint in the
# physical variable.  It never takes the divergent supremum of
# n^(-a) |log n|^(-J).  Under n=exp(-x), the relevant model integral is
# exp(-(1-a)x)(1+x)^(-J) dx and is uniformly integrable for a<1.
endpoint_exponent = mp.mpf("0.43")
endpoint_log_order = 4


def endpoint_pullback(cutoff):
    upper = mp.log(cutoff)
    return mp.quad(
        lambda x: mp.exp(-(1 - endpoint_exponent) * x)
        * mp.power(1 + x, -endpoint_log_order),
        [0, upper],
    )


endpoint_limit = mp.quad(
    lambda x: mp.exp(-(1 - endpoint_exponent) * x)
    * mp.power(1 + x, -endpoint_log_order),
    [0, mp.inf],
)
endpoint_values = [endpoint_pullback(mp.mpf(10) ** exponent) for exponent in (2, 4, 8)]
assert endpoint_values == sorted(endpoint_values), "endpoint truncations are not monotone"
assert endpoint_values[-1] < endpoint_limit
assert endpoint_limit - endpoint_values[-1] < mp.mpf("1e-7")
print(
    "source_endpoint_model="
    f"{mp.nstr(endpoint_values[-1], 10)} limit={mp.nstr(endpoint_limit, 10)}"
)

# The mesh-supremum term in (6.13) has scale T^(1/2-b), not log T.  A
# truncated regression at fourfold scales checks that normalization.  The
# cutoff 40*T is ample for Q=8; this remains a finite test, not an asymptotic
# proof.
mesh_b = 0.07
mesh_q = 8
mesh_scales = (200, 800, 3200)
mesh_normalized = []
for scale in mesh_scales:
    raw = sum(
        m ** (-0.5 - mesh_b) * (1 + m / scale) ** (-mesh_q)
        for m in range(1, 40 * scale + 1)
    )
    mesh_normalized.append(raw / scale ** (0.5 - mesh_b))
assert max(mesh_normalized) / min(mesh_normalized) < 1.25
print(
    "mesh_supremum_normalized="
    + ",".join(f"{value:.8f}" for value in mesh_normalized)
)

# At the genuine l=0 crossing the worst corner exponent is exactly
# -1-2*delta_A-delta_g, hence is strictly summable.
a_plus = mp.mpf("0.30")
b_minus = mp.mpf("0.12")
c_plus = mp.mpf("-0.08")
delta_a = HALF - a_plus
delta_g = b_minus - c_plus
corner_exponent = -2 + 2 * a_plus - b_minus + c_plus
assert mp.almosteq(corner_exponent, -1 - 2 * delta_a - delta_g)
assert corner_exponent < -1
print(
    "l_endpoint_corner_exponent="
    f"{mp.nstr(corner_exponent, 8)}"
)
print("status=PASS")
