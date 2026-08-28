import math


def smooth_bump(t):
    """A normalized C-infinity bump on (0, 1)."""
    if not 0.0 < t < 1.0:
        return 0.0
    return math.exp(4.0 - 1.0 / (t * (1.0 - t)))


def prime_c_equals_q_case(q):
    """Test c=q and X=q^2, where the reciprocal phase is identically one."""
    x_length = q * q
    lhs = sum(
        smooth_bump(u / (x_length + 1.0))
        for u in range(1, x_length + 1)
        if u % q
    )
    gcd_factor = math.sqrt(q)
    missing_factor_bound = x_length / math.sqrt(q) + math.sqrt(q) * gcd_factor
    corrected_bound = (
        x_length / math.sqrt(q) * gcd_factor
        + math.sqrt(q) * gcd_factor
    )
    return lhs, missing_factor_bound, corrected_bound


print("counterexample_scaling: c=q, X=q^2")
scaled_ratios = []
corrected_ratios = []
for prime in (31, 61, 127, 251):
    lhs, missing, corrected = prime_c_equals_q_case(prime)
    ratio_missing = lhs / missing
    ratio_corrected = lhs / corrected
    scaled_ratios.append(ratio_missing / math.sqrt(prime))
    corrected_ratios.append(ratio_corrected)
    print(
        f"q={prime} lhs={lhs:.6e} "
        f"lhs/missing={ratio_missing:.6f} "
        f"lhs/corrected={ratio_corrected:.6f}"
    )

# The omitted-factor ratio grows on the sqrt(q) scale, whereas the corrected
# ratio remains bounded.  These are finite sanity checks; the paper's
# counterexample is the corresponding asymptotic family.
assert min(scaled_ratios) > 0.25
assert max(scaled_ratios) / min(scaled_ratios) < 1.25
assert max(corrected_ratios) < 0.5


def check_two_term_modulus_average(c, q_start, x_length):
    """Check the elementary majorization used before applying (5.5)."""
    moduli = range(q_start, 2 * q_start)
    gcd_sum = sum(math.sqrt(math.gcd(c, q)) for q in moduli)
    exact_first = sum(
        x_length * q ** -0.5 * math.sqrt(math.gcd(c, q)) for q in moduli
    )
    exact_second = sum(
        q ** 0.5 * math.sqrt(math.gcd(c, q)) for q in moduli
    )
    first_majorant = x_length * q_start ** -0.5 * gcd_sum
    second_majorant = (2 * q_start) ** 0.5 * gcd_sum
    assert exact_first <= first_majorant * (1.0 + 1e-12)
    assert exact_second <= second_majorant * (1.0 + 1e-12)
    return exact_first, first_majorant, exact_second, second_majorant


first, first_bound, second, second_bound = check_two_term_modulus_average(
    c=2**4 * 3**3 * 5, q_start=128, x_length=400
)
print(
    "two_term_average "
    f"first={first:.6e}<={first_bound:.6e} "
    f"second={second:.6e}<={second_bound:.6e}"
)
print("status=PASS")
