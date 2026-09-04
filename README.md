# DevMetrics

Small, dependency-free helpers for summarizing development metrics.

## Features

- Line and file counts
- Test-to-source ratios
- Aggregate project summaries
- Simple JSON-friendly output

```python
from devmetrics import summarize

print(summarize({"src/app.py": 120, "tests/test_app.py": 80}))
```

Development: `python -m pytest`

MIT licensed. Built by meduuv. https://guns.lol/meduu
