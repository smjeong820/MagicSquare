import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).parent / "golden"


def assert_matches_golden(actual: str, relative_path: str) -> None:
    golden_path = GOLDEN_DIR / relative_path
    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual, encoding="utf-8")
        return
    if not golden_path.exists():
        raise AssertionError(f"Golden file missing: {golden_path}")
    expected = golden_path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(
            f"Golden mismatch for {relative_path}\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )
