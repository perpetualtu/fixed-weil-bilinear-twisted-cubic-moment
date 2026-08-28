# Fixed-Weil Bilinear Twisted Cubic Moment

This release contains the paper

> A Bilinear Twisted Cubic Moment of the Riemann Zeta Function in the
> Fixed-Weil Range \(H^{3/2}K \leq T^{1-\eta}\).

The main theorem gives the three shifted permutation terms with error

\[
O_{\eta,C,\varepsilon}\!\left(
T^\varepsilon\{KH^{3/2}+T^{1/2}(HK)^{1/2}\}\right)
\]

for two independent divisor-bounded coefficient sequences. The result covers
compact subregions of \(\frac32\theta_1+\theta_3<1\). It does not include the
limiting Bui corner \((4/7,1/4)\), and it does not assert a sixth-moment
asymptotic.

`AUDIT_REPORT.md` summarizes the requested proof expansions and the final
D1--D8 consistency audit. It also states the limits of that audit.

## Build

The audited build uses TeX Live 2024 and latexmk 4.83:

    latexmk -pdf -interaction=nonstopmode -halt-on-error fixed_weil_twisted_cubic.tex

## Numerical checks

The verification script carries its mpmath 1.3.0 dependency in
verification/vendor/:

    python verification/check_zero_identities.py

A successful run ends with status=PASS. These finite checks cover two gamma
identities and collision limits. The analytic contour and continuation
arguments are proved in the paper.

## Integrity

MANIFEST.sha256 covers every distributed payload file except the manifest
itself. Paths are relative to the archive root.
