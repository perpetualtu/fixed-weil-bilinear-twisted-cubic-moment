# Lemma 5.1 focused revision (August 28, 2026)

## Source provenance

The manuscript source was recovered from
`Fixed-Weil_Bilinear_Twisted_Cubic_Moment_Source.zip`. Its SHA-256 is
`FA0CD4BFD651035224CC9A8941BE9327E78A41278401B39E63D3BD6B8BB0ED81`,
matching the desktop checksum manifest. The PDF inside that archive has
SHA-256
`4F6F9B60B4BBC830565014540DAB3459F39F287F48505947D4A114855115A630`,
identical to the manuscript PDF supplied for revision.

## Focused mathematical change

The August 24 source already placed `(c,q)^(1/2)` outside the parentheses in
(5.4), so it mathematically multiplied both terms. The revision expands the
factor termwise:

```text
Z q^eps { X q^(-1/2) (c,q)^(1/2)
          + q^(1/2) (c,q)^(1/2) }.
```

The same termwise form is used in (5.20). The proof now states explicitly
that `(c,n,q)^(1/2) <= (c,q)^(1/2)` for every completed frequency `n`.

For `X_m=M_0g/d` and `Q_d=H_0/d`, (5.5) is then applied separately:

```text
X_m Q_d^(-1/2) sum_{q~Q_d} (a rho,q)^(1/2)
    << X_m Q_d^(1/2) |a rho|^eps,

Q_d^(1/2) sum_{q~Q_d} (a rho,q)^(1/2)
    << Q_d^(3/2) |a rho|^eps.
```

These are exactly the two contributions already present in (5.21). Thus the
subsequent `d`-series in (5.25) remain `sum d^(-5/2)` and
`sum d^(-3/2)`.

## Downstream result

The focused audit finds no change to Proposition 5.2, Proposition 5.3, the
nonzero-frequency error `T^eps K H^(3/2)`, the theorem range, or the main
theorem. This conclusion is conditional on the rest of the manuscript; the
revision is not a new independent audit of every other section.

## Verification

- `python verification/check_reciprocal_lemma.py`: PASS. It records the
  `c=q`, `X=q^2` omitted-factor scaling and checks the two termwise modulus
  majorizations.
- `python verification/check_zero_identities.py`: PASS. The collision
  regression now checks all three collision divisors and their common triple
  intersection.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error
  fixed_weil_twisted_cubic.tex`: PASS with no final LaTeX, package, box,
  citation, or reference warnings.
- The complete affected pages 9--14, title page, and updated proof-ledger page
  were rendered and visually inspected.

## Result class

Rigorous focused correction audit.

## August 29 regulator and dependency revision

- Independent review found that the initially inserted source pushforward
  inequality was false for a general nonnegative measurable function.  It has
  been deleted.  Proposition 6.4 now removes the regulators directly in the
  physical measure `sum_(m,rho) dv`, splitting the source into a bounded bulk
  part and an integrable endpoint part.  The latter uses the estimates already
  proved in (6.17)--(6.25), so no divergent `sup_n` is taken.
- Lemma 7.4 recovers the four branchwise Tonelli destinations on a common
  `s`-contour by branchwise paths moving the external `A` variable and contour
  together.  Its target compact set, uniform margins, complete `u`-tail, and
  remote `u`-pole remainder are now explicit.
- The three-divisor lemma and joint collision proposition have been moved
  before the quantitative continuation that uses them. They are now Lemma
  8.2 and Proposition 8.3; the collision-safe Stirling replacement is
  Proposition 8.4 and the full-kernel continuation is Proposition 8.5.
- The replacement of exact gamma ratios by Bui's power factors is now proved
  on the complete two-term replacement difference.  Three-divisor division
  establishes joint removability first, and a scaled-polydisc maximum
  principle then preserves the `T^(-1)` Stirling saving at collisions.
- The endpoint error symbol is explicitly defined, and the local-ring meaning
  of the three residue divisibilities is stated.

Result class: candidate-complete proof repair pending a fresh independent
review of the revised regulator bridge and collision-safe Stirling lemma.

## August 29 post-review closure

- A fresh source-bridge audit rejected the inference from normal convergence
  to a `sum integral sup` dominator.  The manuscript now places the compact
  parameter supremum inside an explicit pointwise eight-corner majorant
  before any $m,\rho,v$ summation or integration.
- The bulk, genuine $n=0$, genuine $l=0$, and two noncrossing endpoint pieces
  are treated separately.  The $m$-dependent gcd is cancelled before the
  final $m$-sum, and fixed $A$-derivatives are controlled through powers of
  $\log l$.
- The residual mesh-supremum series in the earlier normality estimate is now
  recorded with its correct $T^{1/2-\Re B}$ scale rather than $O(\log T)$.
- The complete-$s$-line Gamma estimate is divided into a uniform central
  Stirling region and a Gaussian complementary region.  Its product bound is
  stated on the external $A$-compact sets used by Proposition 6.4.
- Common-contour recovery now uses finitely many pole-free deformation
  segments.  Remote crossings are indented and evaluated by successive or
  iterated residues; the terminal contours avoid the remote divisors.
- Three fresh-context specialist audits then checked the repaired source
  majorant, contour/Gamma bridge, and global dependency graph.  No remaining
  invalid inference or cycle was found in that scope.

Result class: candidate complete resolution after independent internal
cross-audit; not a formal proof certificate or external human review.
