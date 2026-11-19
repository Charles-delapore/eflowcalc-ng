# eflowcalc-ng — Refactoring Record

Fork of `ThibHlln/eflowcalc` v0.1.0 (last release 2021-04-26, upstream
inactive since). License: **GPLv3** — the fork stays GPLv3, keeps the
original copyright, author attribution and `LICENCE.rst`, and notes
its modifications here and in `CHANGELOG.md`. Distribution name
changed to `eflowcalc-ng` (PyPI `eflowcalc` is taken); import name
stays `eflowcalc`.

Work follows a three-tier grading: Tier 1 compatibility & stability →
Tier 2 local optimization → Tier 3 underlying logic & system design.
Each tier gets its own section below as it is completed.

---

## Tier 1 — Compatibility & Stability (2026-11-14)

Goal: minimal usable fix. Original test suite passes; numerical
results align with the original reference values.

### Changes (4 commits on top of upstream `ab64178`)

1. **Fork init** (`4fd5d81`): distribution renamed to `eflowcalc-ng`,
   version 0.1.1, README fork note, project URLs pointed at the fork.
   License, copyright and author unchanged.
2. **Test tolerance** (`e55fb2e`): `test_streamflow_characteristics.py`
   now compares all 159 indicators with `assert_allclose(rtol=1e-5,
   atol=1e-8)` instead of `assert_almost_equal` (5e-7 absolute).
3. **float64 computation** (`66a3ced`): `calculator()` promotes the
   input to float64 and returns a float64 array (was float32);
   docstring example outputs updated to the recomputed values.
4. **Compatibility audit** (`9b64788`): `python_requires>=3.9`,
   classifiers 3.9–3.12, CI matrix 3.7–3.9 → 3.10–3.12,
   actions/checkout v2→v4, setup-miniconda v2→v3.

### Why the test tolerance changed

The sample data file (`sample_data/catchment.sim.flow.nc`) stores
flows as **float32**, while the 159 reference values in the test are
**float64**. The rounding noise alone reaches a relative deviation of
**1.37e-6** (worst case, `ma40`) on numpy 1.26 / Python 3.12, and the
old absolute check (5e-7) failed 13 indicators
(`ma12, ma14, ma26, ma30, ma39, ml2, ml12, mh2, mh7, mh8, mh11, mh12,
dh14`). The same 13 fail with float32 input; feeding float64 input
fails a *different* 36 — the reference values themselves carry
~1e-6 relative noise of unknown provenance (they were most likely
generated from a float64 copy of the data, or on an older numpy).
`rtol=1e-5` gives ~7x headroom over the observed noise; any genuine
algorithmic regression would deviate by orders of magnitude more.

### Verification (2026-11-14)

- Environment: shared VM, Python 3.12.3, numpy 1.26.4,
  pandas 2.1.4, netCDF4 1.7.5.1, venv
  `~/workspace/your_files/geography-research/revival/venv2/`
  (reused; only numpy/pandas/netCDF4/pytest installed).
- Full suite (`tests/run_all_tests.py`): **2 tests, OK** — doctests
  for `calculator()` plus `test_each_function` (159 subtests).
- Numerical comparison: all 159 indicators match the reference
  values within rtol=1e-5; max observed relative deviation 1.37e-6
  (`ma40`, float32 input).
- Doctests: 4 example outputs recomputed after the float64 change;
  values differ from the old float32 outputs only in the 7th–8th
  significant digit, and the new values are the more accurate ones
  (e.g. ma1 `26.29431` → `26.29430967`).
- `pip install .` (default build isolation): installs as
  `eflowcalc-ng 0.1.1`, import OK. (`--no-build-isolation` fails only
  when the venv lacks setuptools — an environment quirk, not a repo
  defect.)
- No removed numpy/pandas APIs in use (grep audit clean); the
  `pd.DataFrame(...).groupby(...)` monthly aggregation used by
  `ma12`-style indicators works on pandas 2.x.

### Known issues / leftovers

- Direct calls to individual SFC functions (e.g. `efc.ma12(...)`)
  still compute in the **input dtype** (upstream behaviour
  preserved); only the `calculator()` path promotes to float64.
  Users feeding float32 arrays directly still get float32-precision
  results — acceptable for hydrology, documented here.
- The reference values' ~1e-6 noise provenance is unexplained
  (see above); the test tolerance documents it rather than hiding it.
- CI (GitHub Actions) was not run here — this machine has no runner
  access; the workflow file was updated but its first real run will
  be on GitHub after push.
- Not yet published to PyPI as `eflowcalc-ng`; the PyPI badge in
  `README.rst` will resolve only after the first release.

---

## Tier 2 — Local Optimization (in progress)

- **Ruff lint gate** (2026-11-19): correctness rules `E`/`F` (line length
  ignored), generated Sphinx config excluded, package re-exports marked
  explicitly. CI runs `ruff check .`.

## Tier 3 — Underlying Logic & System Design (pending)

## Maintenance status (2026-11-16)

- CI: Python 3.10-3.13 on Linux, macOS and Windows (pip, no conda).
- PyPI: `eflowcalc-ng` is not published; install from git until the first release.
- Upstream: `ThibHlln/eflowcalc` v0.1.0 (2021-04-26); this fork keeps GPLv3,
  the original copyright and attribution.
