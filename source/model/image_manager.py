from pathlib import Path
from typing import List, Tuple

from source.utils.folder_util import load_paths


class ImageManager:
    def __init__(self, extensions: List[str]) -> None:
        self.image_paths: List[Path] = []
        self.current_index: int = -1
        self._extensions = extensions

    def load_images_from_dir(self, dir_path: str) -> bool:
        self.image_paths = load_paths(dir_path, self._extensions)

        if self.image_paths:
            self.current_index = 0

            return True

        return False

    def next_image(self) -> bool:
        if 0 <= self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            return True

        return False

    def prev_image(self) -> bool:
        if self.current_index > 0:
            self.current_index -= 1
            return True

        return False

    @property
    def has_images(self) -> bool:
        return bool(self.image_paths)

    @property
    def count(self) -> int:
        return len(self.image_paths)

    @property
    def current_path(self) -> Path | None:
        if 0 <= self.current_index < len(self.image_paths):
            return self.image_paths[self.current_index]

        return None

    def get_current_status(self) -> Tuple[str, str]:
        path = self.current_path

        if not path:
            return "-", "-/-"

        name = path.name
        idx_str = f"{self.current_index + 1}/{self.count}"

        return name, idx_str
