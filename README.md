# DevMetrics

> Small, dependency-free helpers for summarizing development metrics.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

DevMetrics turns simple project file statistics into structured summaries for developer tooling and automation.

## Features

- Line and file counts
- Test-to-source ratios
- Aggregate project summaries
- JSON-friendly output
- Dependency-free runtime

## Installation

```bash
pip install devmetrics
```

## Example

```python
from devmetrics import summarize

result = summarize({
    "src/app.py": 120,
    "tests/test_app.py": 80,
})

print(result)
```

## What it is for

DevMetrics is intended as a **small data layer**, not a full analytics platform. It can be embedded into scripts, CI jobs, project dashboards and repository analysis tools.

```text
project statistics
       ↓
   aggregation
       ↓
 structured metrics
       ↓
 reports / automation
```

## Development

```bash
python -m pytest
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
