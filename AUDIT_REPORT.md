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
  assembly, and final error decomposition passed the D1-D9 adversarial
  checks recorded in the appendix.

## FIXED

- Defined the finite-$R$, finite-$\kappa$, finite-$V$ source and destination
  for each direct/dual and positive/negative branch.  At finite $V$ they now
  satisfy the exact rectangle identity with the two horizontal $s$-edges;
  equality of the complete vertical contours is asserted only after those
  edges vanish as $V\to\infty$.
- Removed the false assertion that a half-mesh controls every nonnegative
  measurable function by a planar integral plus one supremum.  The repaired
  source proof works in the physical measure `sum_(m,rho) dv`, using the bulk
  mesh estimate only away from zero and integrating the endpoint
  `n^(-a)|log n|^(-J)` singularity directly.  This supplies an
  $R,\kappa$-independent pullback majorant uniform on compact subsets of the
  external $A$-strip.
- Strengthened that repair after a fresh adversarial review: the parameter
  supremum is now bounded pointwise, before integration or summation, by the
  eight endpoint corners of the compact $(A,B,C_1)$ box.  The true $n=0$
  and $l=0$ crossings, both noncrossing endpoint pieces, and all fixed
  $A$-derivatives are summed separately.  The $m$-dependent gcd is cancelled
  before the remaining $m$-sum is taken.
- Corrected the mesh-supremum residual series from the false $O(\log T)$
  description to its actual $O(T^{1/2-\Re B})$ scale.  This remains only a
  fixed polynomial majorant and does not change the sharp theorem error.
- Defined the good patch as a two-variable $(B,C_1)$ domain and kept the
  external $A$-strip separate, removing the former type ambiguity.
- Kept a separate destination majorant on compact subsets of each genuine
  Tonelli chamber.  Outside those chambers only source holomorphy and the
  one-variable identity theorem are used.
- Made the recovery order explicit: restore complete contours, take
  $R\to\infty$, remove the Abel factor, evaluate the beta integral, recover
  the $\rho$-series, recover the $m$/gcd-series, and only then apply the zeta
  functional equation and finite Euler identity.
- Expanded the common-contour recovery lemma to identify the target
  $A$-compact set, branchwise paths, compact-uniform contour margins, complete
  $u$-tails, moving remote $u$-poles, and the aggregate arbitrary-power-small
  remainder after the outer coefficient sum.
- Replaced the overstrong full-$s$-line pointwise Gamma-ratio estimate by a
  central Stirling region and a complementary Gaussian region.  The product
  bound is also stated locally uniformly on the external $A$-compact sets
  used in Section 6.
- Split every common-contour deformation into finitely many pole-free
  subpaths.  Remote crossings are handled by indentation and successive
  residues, the final line is required to avoid all remote divisors, and the
  uniform exponential bounds are stated as $e^{-cT}$ and $e^{-cT^2}$.
- Proved the exact-to-power Stirling replacement on the complete replacement
  difference.  Three-divisor division first removes all collision poles; a
  scaled-polydisc maximum-principle estimate then retains the pointwise
  $T^{-1}$ saving uniformly at pairwise and triple collisions.
- Defined the endpoint error symbol before use and expanded the residue-to-
  ideal-divisibility step in the local analytic ring.

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
- Moved the three-divisor lemma and algebraic collision-removability
  proposition before the quantitative continuation that uses them.  The
  resulting order is Lemma 8.2, Propositions 8.3--8.5, so no forward
  Section 9 dependency or apparent cycle remains.
- Standardized the meaning of every harmless `T^epsilon`: auxiliary small
  exponents are chosen below the final epsilon, intermediate constants may
  depend on the fixed smoothing order and explicitly listed finite weight
  seminorms, and no fixed positive power depending on `M` is hidden. The
  separate coarse power used in Section 8 is only a continuation majorant.
- Repaired the final permutation left-line estimate at beta+gamma=0: the
  complete holomorphic permutation sum is now retained before taking
  absolute values, and the collision tube is controlled by a scaled
  one-variable maximum/Cauchy argument.
- Added a publication-facing D1-D8 audit ledger and release-integrity checks.

This is an internal line-by-line consistency audit, not a formal proof
certificate or an external peer-review report.

## REMAINING STATUS

No unresolved dependency was found after a fresh-context, three-route
cross-audit of the revised source domination, contour bridge, dependency
order, and collision-safe Stirling replacement.  The result class is
**candidate complete resolution**: this is still an AI-assisted internal
proof audit, not formal verification or independent human peer review.
