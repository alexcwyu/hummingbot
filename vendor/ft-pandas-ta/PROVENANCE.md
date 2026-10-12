# ft-pandas-ta compatibility source

Source: PyPI `ft-pandas-ta` 0.3.16, the latest resolved release on 2026-10-12, from its installed wheel. The package preserves the upstream `pandas_ta` namespace and MIT license.

The Python 3.15 compiler treats previously warned invalid string escapes as errors. Compatibility edits escape only the offending backslashes or use raw regex strings when equivalent; numerical algorithms, formulas and API behavior remain unchanged. See the source diff for exact literal repairs. Current Pandas/NumPy dependencies remain resolved through the host uv lock.

Exact edits in `utils/_core.py`: the regex replacement is a raw string with the same backslash/group value; `is_datetime_ordered` returns its unchanged predicate after the try/except instead of inside `finally`, which Python 3.15 diagnoses as suppressing exceptions. All package source files compile with `python -W error -m compileall`; no warning filter is added.
