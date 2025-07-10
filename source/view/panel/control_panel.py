from typing import Any, Dict

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ControlPanel(QGroupBox):
    def __init__(self, config: Dict[str, Any], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._config = config
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QHBoxLayout(self)

        load_panel = self._create_load_panel()
        nav_panel = self._create_nav_panel()
        model_panel = self._create_model_panel()

        layout.addWidget(load_panel)
        layout.addWidget(nav_panel)
        layout.addWidget(model_panel)

    def _create_load_panel(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout(widget)

        cfg = self._config["load_panel"]

        panel_label = QLabel(cfg["label"])
        self.load_class_btn = QPushButton(cfg["cls_btn"])
        self.load_class_btn.setIcon(QIcon.fromTheme("document-new"))
        self.load_image_btn = QPushButton(cfg["image_btn"])
        self.load_image_btn.setIcon(QIcon.fromTheme("folder-new"))
        self.load_model_btn = QPushButton(cfg["model_btn"])
        self.load_model_btn.setIcon(QIcon.fromTheme("folder-new"))

        layout.addWidget(panel_label, 0, 0, 1, 2)
        layout.addWidget(self.load_class_btn, 1, 0, 2, 1)
        layout.addWidget(self.load_image_btn, 1, 1)
        layout.addWidget(self.load_model_btn, 2, 1)

        return widget

    def _create_nav_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        cfg = self._config["nav_panel"]

        panel_label = QLabel(cfg["label"])
        self.prev_btn = QPushButton(cfg["prev_btn"])
        self.prev_btn.setIcon(QIcon.fromTheme("go-previous"))
        self.next_btn = QPushButton(cfg["next_btn"])
        self.next_btn.setIcon(QIcon.fromTheme("go-next"))

        layout.addWidget(panel_label)
        layout.addWidget(self.prev_btn)
        layout.addWidget(self.next_btn)

        return widget

    def _create_model_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        cfg = self._config["model_panel"]

        panel_label = QLabel(cfg["label"])
        self.model_combobox = QComboBox()
        self.model_combobox.addItem(cfg["box_null"])
        self.pred_btn = QPushButton(cfg["pred_btn"])
        self.pred_btn.setIcon(QIcon.fromTheme("media-playback-start"))

        layout.addWidget(panel_label)
        layout.addWidget(self.model_combobox)
        layout.addWidget(self.pred_btn)

        return widget
