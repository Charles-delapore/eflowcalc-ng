# Security policy

## Supported versions

| Version | Supported |
|---|---|
| 0.1.x | yes |

## Reporting a vulnerability

Use GitHub's private vulnerability reporting on this repository
(**Security → Report a vulnerability**). Do not open a public issue for a
security problem.

Include the affected function, the input file or array that triggers it, and
the expected impact. The package reads streamflow time series; malformed
netCDF or array input is the most plausible attack surface.

## Upstream

This is a fork of `ThibHlln/eflowcalc`. Security fixes that also affect the
upstream project will be reported there as well, with attribution.

## Response

We aim to acknowledge within 7 days and to publish a patched release with a
note in `CHANGELOG.md`.
