import sys
from pathlib import Path

from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QMessageBox

from source.controller.app_controller import ApplicationController
from source.model.config_manager import ConfigManager


def main() -> None:
    app = QApplication(sys.argv)

    try:
        config_manager = ConfigManager()
        config_manager.load_config(Path("./config/app.toml"))
    except FileNotFoundError as e:
        QMessageBox.critical(None, "Error", f"{e}")
        sys.exit(1)

    config = config_manager.get_config()

    app.setStyle(config["app"]["style"])
    app.setFont(QFont(config["app"]["font"]))
    app.setWindowIcon(QIcon(str(config["app"]["icon"])))

    with open("./style/app.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    controller = ApplicationController(config)
    controller.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
