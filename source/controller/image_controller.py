from typing import Any, Dict

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

from source.model.image_manager import ImageManager
from source.view.main_window import MainWindow


class ImageController:
    def __init__(
        self,
        main_view: MainWindow,
        image_manager: ImageManager,
        config: Dict[str, Any],
    ) -> None:
        self._view = main_view
        self._image = image_manager
        self._config = config

        self._image_panel = self._view.image_panel
        self._chart_panel = self._view.chart_panel
        self._control_panel = self._view.control_panel

        self._connect_signals()

    def _connect_signals(self) -> None:
        self._control_panel.load_image_btn.clicked.connect(self._load_images)
        self._control_panel.prev_btn.clicked.connect(self._show_prev_image)
        self._control_panel.next_btn.clicked.connect(self._show_next_image)

        self._view.resized.connect(self._update_image_display)
        self._view.stateChanged.connect(self._update_image_display)

    def _load_images(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(self._view)

        if not dir_path:
            return

        self._image.load_images_from_dir(dir_path)
        self._update_image_panel()

    def _show_next_image(self) -> None:
        if self._image.next_image:
            self._update_image_panel()

    def _show_prev_image(self) -> None:
        if self._image.prev_image:
            self._update_image_panel()

    def _update_image_display(self) -> None:
        if self._image.current_path:
            self._image_panel.update_image(QPixmap(self._image.current_path))

    def _update_image_panel(self) -> None:
        self._image_panel.clear_all()
        self._chart_panel.clear_all()

        self._update_image_display()
        name, idx_str = self._image.current_status
        self._image_panel.update_info(name, idx_str)
