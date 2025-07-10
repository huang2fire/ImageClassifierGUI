from typing import Any, Dict

from PySide6.QtWidgets import QFileDialog

from source.model.class_manager import ClassManager
from source.view.main_window import MainWindow


class ClassController:
    def __init__(
        self,
        main_view: MainWindow,
        class_manager: ClassManager,
        config: Dict[str, Any],
    ) -> None:
        self._view = main_view
        self._class = class_manager
        self._config = config

        self._control_panel = self._view.control_panel

        self._connect_signals()

    def _connect_signals(self) -> None:
        self._control_panel.load_class_btn.clicked.connect(self._load_classes)

    def _load_classes(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self._view, "", "", self._config["load"]["cls_filter"]
        )

        if not file_path:
            return

        self._class.load_classes(file_path)
