import numpy as np

from source.model.class_manager import ClassManager
from source.model.image_manager import ImageManager
from source.model.model_manager import ModelManager
from source.view.main_window import MainWindow


class PredictionController:
    def __init__(
        self,
        main_view: MainWindow,
        class_manager: ClassManager,
        image_manager: ImageManager,
        model_manager: ModelManager,
    ) -> None:
        self._view = main_view
        self._class = class_manager
        self._image = image_manager
        self._model = model_manager

        self._chart_panel = self._view.chart_panel
        self._control_panel = self._view.control_panel

        self._connect_signals()

    def _connect_signals(self) -> None:
        self._control_panel.pred_btn.clicked.connect(self._run_pred)

    def _run_pred(self) -> None:
        image_path = self._image.current_path
        if not (self._model.is_loaded and image_path):
            return

        probs = self._model.predict(image_path)

        if probs is not None and self._class.count > 0:
            self._update_chart_panel(probs)

    def _update_chart_panel(self, probs: np.ndarray) -> None:
        top_idx = np.argmax(probs)
        top_class_name = self._class.get_class_name(str(top_idx))
        top_confidence = probs[top_idx] * 100

        if top_class_name:
            self._chart_panel.update_info(top_class_name, top_confidence)

        self._chart_panel.plot_barchart(probs, self._class.classes)
