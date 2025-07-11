from typing import Any, Dict

import numpy as np
from PySide6.QtCharts import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QChartView,
    QValueAxis,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ChartPanel(QWidget):
    def __init__(self, config: Dict[str, Any], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._config = config
        self._init_ui()

    def _init_ui(self) -> None:
        layout = QVBoxLayout(self)

        cfg = self._config["chart_panel"]

        panel_label = QLabel(cfg["label"])

        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.legend().setVisible(False)

        chart_view = QChartView(self.chart)
        chart_view.setMinimumSize(
            self._config["panel"]["minw"],
            self._config["panel"]["minh"],
        )

        info_widget = QGroupBox()
        info_layout = QHBoxLayout(info_widget)

        self.name_label = QLabel(cfg["name_null"])
        self.conf_label = QLabel(cfg["conf_null"])

        info_layout.addWidget(self.name_label, 1)
        info_layout.addWidget(self.conf_label)

        layout.addWidget(panel_label)
        layout.addWidget(chart_view, 1)
        layout.addWidget(info_widget)

    def update_info(self, name: str, confidence: float) -> None:
        cfg = self._config["chart_panel"]

        self.name_label.setText(f"{cfg['name_label']} {name}")
        self.conf_label.setText(f"{cfg['conf_label']} {confidence:.2f}%")

    def clear_info(self) -> None:
        cfg = self._config["chart_panel"]

        self.name_label.setText(cfg["name_null"])
        self.conf_label.setText(cfg["conf_null"])

    def clear_chart(self) -> None:
        self.chart.removeAllSeries()
        for axis in self.chart.axes():
            self.chart.removeAxis(axis)

    def clear_all(self) -> None:
        self.clear_info()
        self.clear_chart()

    def plot_barchart(self, probs: np.ndarray, classes: Dict[str, str]) -> None:
        cfg = self._config["plot"]

        top_n = min(self._config["plot"]["top_n"], len(classes))
        probs = probs * 100

        # 获取 top_n 置信度最高的索引，按 ID 排序
        topn_indices = sorted(np.argsort(probs)[-top_n:].tolist())

        # 绘图数据
        categories = [classes[str(idx)] for idx in topn_indices]
        values = [float(probs[idx]) for idx in topn_indices]

        # 清理旧图表
        self.clear_chart()

        # 数据系列
        bar_set = QBarSet("")
        bar_set.append(values)
        series = QBarSeries()
        series.append(bar_set)
        self.chart.addSeries(series)

        # X 轴
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText(cfg["xlabel"])
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        # Y 轴
        axis_y = QValueAxis()
        axis_y.setTitleText(cfg["ylabel"])
        axis_y.setRange(0, 100)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)
