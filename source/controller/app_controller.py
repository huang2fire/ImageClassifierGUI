from typing import Any, Dict

from PySide6.QtCore import QObject, QTimer

from source.controller.class_controller import ClassController
from source.controller.image_controller import ImageController
from source.controller.model_controller import ModelController
from source.controller.prediction_controller import PredictionController
from source.model.class_manager import ClassManager
from source.model.image_manager import ImageManager
from source.model.model_manager import ModelManager
from source.view.main_window import MainWindow


class ApplicationController(QObject):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()
        self._config = config

        # 1. 初始化 Models
        self.class_manager = ClassManager()
        self.image_manager = ImageManager(self._config["load"]["image_extensions"])
        self.model_manager = ModelManager(self._config["load"]["model_extensions"])

        # 2. 初始化 View
        self.main_view = MainWindow(self._config)

        # 3. 初始化 Controllers
        self.class_controller = ClassController(
            self.main_view, self.class_manager, self._config
        )
        self.image_controller = ImageController(
            self.main_view, self.image_manager, self._config
        )
        self.model_controller = ModelController(
            self.main_view, self.model_manager, self._config
        )
        self.prediction_controller = PredictionController(
            self.main_view, self.class_manager, self.image_manager, self.model_manager
        )

        # 4. 设置定时器以持续更新UI状态
        self.ui_update_timer = QTimer(self)
        self.ui_update_timer.timeout.connect(self._update_ui_state)
        self.ui_update_timer.start(100)

    def run(self) -> None:
        self.main_view.show()

    def _update_ui_state(self) -> None:
        total_images = self.image_manager.count
        current_index = self.image_manager.current_index

        self._update_nav_buttons_state(total_images, current_index)
        self._update_model_related_state()

        self.main_view.status_bar.update_status(
            self.class_manager.count,
            self.image_manager.count,
            self.model_manager.count,
        )

    def _update_nav_buttons_state(self, total: int, index: int) -> None:
        controls = self.main_view.control_panel

        if total <= 1:
            controls.prev_btn.setEnabled(False)
            controls.next_btn.setEnabled(False)
        else:
            controls.prev_btn.setEnabled(index > 0)
            controls.next_btn.setEnabled(index < total - 1)

    def _update_model_related_state(self) -> None:
        controls = self.main_view.control_panel

        controls.model_combobox.setEnabled(self.model_manager.count > 0)

        can_predict = (
            self.model_manager.is_loaded
            and self.image_manager.has_images
            and self.class_manager.count > 0
        )
        controls.pred_btn.setEnabled(can_predict)
