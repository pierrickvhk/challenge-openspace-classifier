from pathlib import Path
from typing import List


def read_names_from_txt(path: str | Path) -> List[str]:
    """
    Read names from a .txt file. One name per line.
    Empty lines are ignored.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")
    return [
        line.strip()
        for line in p.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
