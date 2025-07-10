from pathlib import Path
from typing import List


def load_paths(dir_path: str | Path, extensions: List[str]) -> List[Path]:
    return [
        path
        for ext in extensions
        for path in Path(dir_path).glob(ext)
        if path.is_file()
    ]
