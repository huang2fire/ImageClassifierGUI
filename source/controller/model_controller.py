from typing import Any, Dict

from PySide6.QtWidgets import QFileDialog

from source.model.model_manager import ModelManager
from source.view.main_window import MainWindow


class ModelController:
    def __init__(
        self,
        main_view: MainWindow,
        model_manager: ModelManager,
        config: Dict[str, Any],
    ) -> None:
        self._view = main_view
        self._model = model_manager
        self._config = config

        self._chart_panel = self._view.chart_panel
        self._control_panel = self._view.control_panel

        self._connect_signals()

    def _connect_signals(self) -> None:
        self._control_panel.load_model_btn.clicked.connect(self._load_models)
        self._control_panel.model_combobox.currentIndexChanged.connect(
            self._select_model
        )

    def _load_models(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(self._view)

        if not dir_path:
            return

        self._model.load_models_from_dir(dir_path)
        self._update_model_combobox()

    def _select_model(self, index: int) -> None:
        model_index = index - 1

        if model_index >= 0:
            self._model.set_active(model_index)
            self._chart_panel.clear_all()

    def _update_model_combobox(self) -> None:
        combobox = self._control_panel.model_combobox

        combobox.clear()
        combobox.addItem(self._config["model_panel"]["box_item"])
        combobox.addItems(self._model.model_names)
