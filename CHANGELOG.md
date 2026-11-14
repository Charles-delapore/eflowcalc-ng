# Changelog

All notable changes to this fork are documented here. The original
project is `ThibHlln/eflowcalc <https://github.com/ThibHlln/eflowcalc>`_
(v0.1.0, 2021-04-26); see `REFACTORING.md` for the full record.

## 0.1.1 (2026-11-14) — eflowcalc-ng fork, Tier 1 (compatibility & stability)

- Fork renamed to `eflowcalc-ng` (PyPI name `eflowcalc` is taken);
  import name stays `eflowcalc`. License stays GPLv3, original
  copyright and author attribution retained.
- Tests: all 159 streamflow characteristics now compared with a
  relative tolerance (`assert_allclose`, rtol=1e-5, atol=1e-8).
  The old absolute check (5e-7) failed 13 indicators because the
  sample data ships float32 flows while the reference values are
  float64 (observed max relative deviation 1.37e-6).
- `calculator()` now computes and returns float64 (was float32):
  results are no longer silently truncated to ~7 significant digits.
  Docstring example outputs updated to the recomputed values.
- Declared support for Python 3.9–3.12 (`python_requires>=3.9`);
  CI matrix updated from 3.7–3.9 to 3.10–3.12.
- Verification: full suite passes on Python 3.12.3 / numpy 1.26.4 /
  pandas 2.1.4 / netCDF4 1.7.5; `pip install .` installs as
  `eflowcalc-ng 0.1.1`.
