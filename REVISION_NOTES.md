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
    << X_m Q_d^(1/2) (a rho)^eps,

Q_d^(1/2) sum_{q~Q_d} (a rho,q)^(1/2)
    << Q_d^(3/2) (a rho)^eps.
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
- `python verification/check_zero_identities.py`: PASS. Existing gamma and
  collision regression checks remain unchanged.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error
  fixed_weil_twisted_cubic.tex`: PASS with no final LaTeX, package, box,
  citation, or reference warnings.
- The complete affected pages 9--14, title page, and updated proof-ledger page
  were rendered and visually inspected.

## Result class

Rigorous focused correction audit.
