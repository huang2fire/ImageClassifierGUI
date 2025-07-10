from typing import Any, Dict

from PySide6.QtWidgets import QLabel, QStatusBar


class StatusBar(QStatusBar):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self._config = config
        self._init_ui()

    def _init_ui(self) -> None:
        cfg = self._config["status_bar"]

        self.status_label = QLabel(cfg["null"])
        version_label = QLabel(cfg["version"])

        self.addPermanentWidget(self.status_label, 1)
        self.addPermanentWidget(version_label)

    def update_status(
        self,
        class_count: int,
        image_count: int,
        model_count: int,
    ) -> None:
        cfg = self._config["status_bar"]

        if class_count > 0 or image_count > 0 or model_count > 0:
            status_text = (
                f"{cfg['label']} "
                f"{class_count} {cfg['cls']} | "
                f"{image_count} {cfg['image']} | "
                f"{model_count} {cfg['model']}"
            )
            self.status_label.setText(status_text)
        else:
            self.status_label.setText(cfg["null"])
