# Audit Report

This report records the minor proof expansions requested for the manuscript
"A Bilinear Twisted Cubic Moment of the Riemann Zeta Function in the
Fixed-Weil Range H^(3/2)K <= T^(1-eta)." The theorem range, fixed l-Poisson
orientation, three main terms, and final error term were not changed.

## VERIFIED

- The completed m_1-weight in the reciprocal-sum argument now retains the
  original Dirichlet weight, dyadic factors, t-integral, coupled V-kernel,
  l-Poisson transform, r=d rho dependence, and every m_1-dependent phase.
  Its support and all fixed-order normalized derivatives satisfy the input
  required by finite completion.
- The parametrization d=(h,km), g=(d,k), d=g delta, k=g k_1,
  m=delta m_1, h=dq is bijective with (q,k_1m_1)=1. The q-sum, k-partition,
  density, Jacobian, frequency counts, and the convergent d-series were
  recomputed without suppressing a power of d.
- The direct/dual and positive/negative rho branches have separate genuine
  absolute-convergence domains. Finite regulators remain in place during
  contour deformation, horizontal sides vanish first, and the limits are
  taken in the order V to infinity, R to infinity, and kappa to 0+. Exact
  branch identities are continued only in the original shift A.
- On the enlarged scaled shift domain, the exact source, complete
  permutation expression, and assembled diagonal boundary satisfy the
  explicit bounds T^(B_0/2+4), T^(B_0/8+4), and T^(B_0/8+3), respectively.
  Hence C_2=B_0/2+5 is valid, with M fixed before the propagation order N.
- The coefficient sums, epsilon bookkeeping, theorem-range consequences,
  fixed derivative orders, contour collars, collision uniformity, order of
  assembly, and final error decomposition passed the D1-D8 adversarial
  checks recorded in the appendix.

## FIXED

- Defined the finite-$R$, finite-$\kappa$, finite-$V$ source and destination
  for each direct/dual and positive/negative branch.  At finite $V$ they now
  satisfy the exact rectangle identity with the two horizontal $s$-edges;
  equality of the complete vertical contours is asserted only after those
  edges vanish as $V\to\infty$.
- Added an $R,\kappa$-independent source majorant uniform on compact subsets
  of the external $A$-strip, and a separate absolute majorant uniform on
  compact subsets of each genuine Tonelli chamber.  Outside the Tonelli
  chambers only source holomorphy and the one-variable identity theorem are
  used.
- Made the recovery order explicit: restore complete contours, take
  $R\to\infty$, remove the Abel factor, evaluate the beta integral, recover
  the $\rho$-series, recover the $m$/gcd-series, and only then apply the zeta
  functional equation and finite Euler identity.

- Rewrote Lemma 5.1 and its application in (5.20) so that the factor
  $(c,q)^{1/2}$ is displayed separately in both terms.  The source already
  factored it globally across the two terms, but the termwise form prevents
  the completed estimate from being misread as omitting the factor from the
  $Xq^{-1/2}$ term.
- Applied the dyadic gcd average (5.5) explicitly and separately to both
  terms before (5.21).  This gives $X_mQ_d^{1/2}$ and $Q_d^{3/2}$, exactly
  as in the prior calculation, so (5.21)--(5.25), Propositions 5.2 and 5.3,
  and the main theorem retain their stated bounds.

- Expanded the formerly compressed smooth-weight verification in the
  fixed-l nonzero-frequency estimate, including the exact completed weight,
  support length, derivative ledger, gcd equivalence, completion terms,
  normalization, and both d-series.
- Replaced the compressed regulator/Tonelli bridge with a four-branch
  proposition that separates finite- and post-limit singularities, proves
  horizontal decay, fixes the order of limits, and states the one-variable
  identity-theorem step precisely.
- Added a global polynomial majorant with fixed scaled domains, separate
  source/permutation/boundary estimates, collision-safe Cauchy bounds, and an
  acyclic parameter order.
- Repaired the final permutation left-line estimate at beta+gamma=0: the
  complete holomorphic permutation sum is now retained before taking
  absolute values, and the collision tube is controlled by a scaled
  one-variable maximum/Cauchy argument.
- Added a publication-facing D1-D8 audit ledger and release-integrity checks.

This is an internal line-by-line consistency audit, not a formal proof
certificate or an external peer-review report.

## REMAINING GAP

No unresolved dependency was found in this audit.
