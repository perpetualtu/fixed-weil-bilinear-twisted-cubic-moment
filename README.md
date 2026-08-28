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
D1--D9 consistency audit. It also states the limits of that audit.
`REVISION_NOTES.md` records the August 28 focused Lemma 5.1 re-audit.

The current proof status is **candidate complete resolution** after a
fresh-context, three-route internal cross-audit. This is not formal
verification and should not be described as independent human peer review.

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

The focused Lemma 5.1 regression check is

    python verification/check_reciprocal_lemma.py

It records the $c=q$, $X=q^2$ omitted-factor scaling and checks that the two
terms in the corrected estimate are both majorized by the same dyadic gcd
average. It is a finite regression test, not a proof of the analytic lemma.

The focused Proposition 6.4 beta-branch check is

    python verification/check_regulator_bridge.py

It samples points strictly inside all four Tonelli chambers, numerically
checks the four displayed beta identities, and checks the integrable endpoint
pullback model, corrected mesh-supremum scale, and worst endpoint-corner
exponent used in the repaired source domination. The compact-uniform
domination and ordered-limit arguments remain analytic parts of Proposition
6.4.

## Baseline manifest

A legacy `MANIFEST.sha256`, when retained with an imported baseline, records
only that baseline. It is not required in the revised proof package and is not
used by the proof or the verification scripts.
