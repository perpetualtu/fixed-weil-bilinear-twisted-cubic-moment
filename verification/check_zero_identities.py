import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor" / "mpmath-1.3.0.zip"))

import mpmath as mp


mp.mp.dps = 80


def chi(z):
    return mp.power(mp.pi, z - mp.mpf("0.5")) * mp.gamma((1 - z) / 2) / mp.gamma(z / 2)


def x_factor(a, c, t):
    half = mp.mpf("0.5")
    return (
        mp.power(mp.pi, a + c)
        * mp.gamma((half - a - 1j * t) / 2)
        * mp.gamma((half - c + 1j * t) / 2)
        / mp.gamma((half + a + 1j * t) / 2)
        / mp.gamma((half + c - 1j * t) / 2)
    )


def g_factor(b, c, z, t):
    half = mp.mpf("0.5")
    return (
        mp.power(mp.pi, -z)
        * mp.gamma((half + b + z + 1j * t) / 2)
        * mp.gamma((half + c + z - 1j * t) / 2)
        / mp.gamma((half + b + 1j * t) / 2)
        / mp.gamma((half + c - 1j * t) / 2)
    )


def mathfrak_x(a, b, c, z, t):
    half = mp.mpf("0.5")
    beta_sum = (
        mp.gamma(half - a - 1j * t) / mp.gamma(half + c - 1j * t + z)
        + mp.gamma(half - c + 1j * t - z) / mp.gamma(half + a + 1j * t)
    )
    return (
        chi(a + c + z)
        * mp.gamma(a + c + z)
        * g_factor(b, c, z, t)
        * beta_sum
    )


def relative_error(lhs, rhs):
    return abs(lhs - rhs) / max(mp.mpf(1), abs(lhs), abs(rhs))


def b_factor(nu, prime, q_shift, u_shift):
    x = mp.power(prime, -q_shift)
    y = mp.power(prime, -u_shift)
    total = mp.power(x, nu)
    for i in range(nu):
        total += (1 - x) * mp.power(x, i) * mp.power(y, nu - i)
    return total


def factor_integer(value):
    factors = []
    prime = 2
    remaining = value
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
        prime += 1
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def z_factor(a, b, c, h, k):
    common = math.gcd(h, k)
    h_zero = h // common
    k_zero = k // common
    result = (
        mp.power(h_zero, mp.mpf("0.5") + c)
        * mp.power(k_zero, -mp.mpf("0.5") - c)
        * mp.zeta(1 + a + c)
        * mp.zeta(1 + b + c)
    )
    for prime, exponent in factor_integer(h_zero):
        result *= b_factor(exponent, prime, 1 + a + c, 1 + b + c)
    return result


def permutation_sum(a, b, c, h, k, t):
    return (
        z_factor(a, b, c, h, k)
        + x_factor(a, c, t) * z_factor(-c, b, -a, h, k)
        + x_factor(b, c, t) * z_factor(a, -c, -b, h, k)
    )


cases = [
    (mp.mpc("0.013", "0.004"), mp.mpc("-0.009", "0.002"), mp.mpc("0.017", "-0.003"), mp.mpc("0.021", "0.007"), mp.mpf("37.25")),
    (mp.mpc("-0.027", "0.011"), mp.mpc("0.019", "-0.008"), mp.mpc("0.031", "0.005"), mp.mpc("-0.018", "0.013"), mp.mpf("103.75")),
]

gamma_errors = []
for index, (a, b, c, z, t) in enumerate(cases, start=1):
    identity_one = relative_error(mathfrak_x(a, b, c, 0, t), x_factor(a, c, t))
    identity_two = relative_error(
        x_factor(b, c, t) * mathfrak_x(a, -c, -b, z, t),
        mathfrak_x(a, b, c, -z, t),
    )
    gamma_errors.extend((identity_one, identity_two))
    print(f"case={index} identity_5.8d_relerr={mp.nstr(identity_one, 8)}")
    print(f"case={index} identity_5.8e_relerr={mp.nstr(identity_two, 8)}")


collision_data = [
    ("a_plus_c", lambda eps: (-mp.mpc("0.031", "0.005") + eps, mp.mpc("0.019", "-0.008"), mp.mpc("0.031", "0.005"))),
    ("a_minus_b", lambda eps: (mp.mpc("0.019", "-0.008") + eps, mp.mpc("0.019", "-0.008"), mp.mpc("0.031", "0.005"))),
]

for label, shifts in collision_data:
    previous = None
    differences = []
    for exponent in (8, 12, 16, 20):
        epsilon = mp.power(10, -exponent)
        a, b, c = shifts(epsilon)
        current = permutation_sum(a, b, c, 12, 35, mp.mpf("103.75"))
        if previous is not None:
            difference = abs(current - previous)
            differences.append(difference)
            print(
                f"collision={label} eps=1e-{exponent} successive_diff="
                f"{mp.nstr(difference, 8)}"
            )
        previous = current

    assert all(
        mp.mpf("0.5e-4") < right / left < mp.mpf("2e-4")
        for left, right in zip(differences, differences[1:])
    ), f"{label}: collision differences do not decrease linearly"
    assert differences[-1] < mp.mpf("1e-15"), (
        f"{label}: collision test did not reach the expected scale"
    )

assert max(gamma_errors) < mp.mpf("1e-40"), (
    "gamma identity relative error exceeds the release threshold"
)
print("status=PASS")
