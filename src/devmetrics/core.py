from collections.abc import Mapping


def summarize(files: Mapping[str, int]) -> dict[str, int | float]:
    total = sum(files.values())
    source = sum(lines for path, lines in files.items() if not path.lower().startswith(("test/", "tests/")))
    tests = total - source
    return {
        "files": len(files),
        "lines": total,
        "source_lines": source,
        "test_lines": tests,
        "test_ratio": round(tests / total, 4) if total else 0.0,
    }
