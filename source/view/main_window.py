from typing import Any, Dict

from PySide6.QtCore import QEvent, Signal
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from source.view.panel.chart_panel import ChartPanel
from source.view.panel.control_panel import ControlPanel
from source.view.panel.image_panel import ImagePanel
from source.view.status_bar import StatusBar


class MainWindow(QMainWindow):
    resized = Signal()
    stateChanged = Signal()

    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self.config = config

        self.setWindowTitle(self.config["app"]["title"])
        self.setGeometry(100, 100, 1200, 800)

        self._init_ui()

    def _init_ui(self) -> None:
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 20, 20, 20)

        view_panels = self._create_view_panels()
        self.control_panel = ControlPanel(self.config)
        self.status_bar = StatusBar(self.config)
        self.setStatusBar(self.status_bar)

        layout.addWidget(view_panels, 1)
        layout.addWidget(self.control_panel)

    def _create_view_panels(self) -> QWidget:
        panels_group = QGroupBox()
        panels_layout = QHBoxLayout(panels_group)

        self.image_panel = ImagePanel(self.config)
        self.chart_panel = ChartPanel(self.config)

        panels_layout.addWidget(self.image_panel, 1)
        panels_layout.addWidget(self.chart_panel, 1)

        return panels_group

    def changeEvent(self, event: QEvent) -> None:
        if event.type() in [QEvent.Type.WindowStateChange, QEvent.Type.Resize]:
            if event.type() == QEvent.Type.WindowStateChange:
                self.stateChanged.emit()
            self.resized.emit()

        super().changeEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        cfg = self.config["question"]

        reply = QMessageBox.question(
            self,
            cfg["title"],
            cfg["text"],
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
