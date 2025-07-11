from typing import Any, Dict

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ImagePanel(QWidget):
    def __init__(self, config: Dict[str, Any], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._config = config
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)

        cfg = self._config["image_panel"]

        panel_label = QLabel(cfg["label"])

        self.image_label = QLabel()
        self.image_label.setMinimumSize(
            self._config["panel"]["minw"],
            self._config["panel"]["minh"],
        )
        self.image_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_widget = QGroupBox()
        info_layout = QHBoxLayout(info_widget)

        self.name_label = QLabel(cfg["name_null"])
        self.idx_label = QLabel(cfg["idx_null"])

        info_layout.addWidget(self.name_label, 1)
        info_layout.addWidget(self.idx_label)

        layout.addWidget(panel_label)
        layout.addWidget(self.image_label, 1)
        layout.addWidget(info_widget)

    def update_info(self, name: str, idx_str: str) -> None:
        cfg = self._config["image_panel"]

        self.name_label.setText(f"{cfg['name_label']} {name}")
        self.idx_label.setText(f"{cfg['idx_label']} {idx_str}")

    def _clear_info(self) -> None:
        cfg = self._config["image_panel"]

        self.name_label.setText(cfg["name_null"])
        self.idx_label.setText(cfg["idx_null"])

    def _clear_image(self) -> None:
        self.image_label.clear()

    def clear_all(self) -> None:
        self._clear_info()
        self._clear_image()

    def update_image(self, pixmap: QPixmap) -> None:
        self.image_label.setPixmap(
            pixmap.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
