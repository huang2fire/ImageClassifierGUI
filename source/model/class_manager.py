import json
from typing import Dict


class ClassManager:
    def __init__(self) -> None:
        self.classes: Dict[str, str] = {}

    def load_classes(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            self.classes = json.load(f)

    def get_class_name(self, class_id: str) -> str | None:
        return self.classes.get(class_id)

    @property
    def count(self) -> int:
        return len(self.classes)
