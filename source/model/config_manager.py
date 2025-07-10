import tomllib
from pathlib import Path
from typing import Any, Dict


class ConfigManager:
    _config: Dict[str, Any] | None = None

    @classmethod
    def load_config(cls, path: Path) -> None:
        if not path.is_file():
            raise FileNotFoundError(f"Configuration file not found at: {path}")
        with open(path, "rb") as f:
            cls._config = tomllib.load(f)

    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        if cls._config is None:
            raise ValueError("Config has not been loaded. Call load_config() first.")
        return cls._config
