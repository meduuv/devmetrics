from devmetrics import summarize


def test_summary():
    result = summarize({"src/app.py": 120, "tests/test_app.py": 80})
    assert result == {"files": 2, "lines": 200, "source_lines": 120, "test_lines": 80, "test_ratio": 0.4}


def test_empty():
    assert summarize({})["test_ratio"] == 0.0
