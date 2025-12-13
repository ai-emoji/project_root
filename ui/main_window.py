"""
Mô tả:
        Giao diện chính của ứng dụng, quản lý signal/slot, gọi service, tách riêng background và nội dung.
"""

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from core.resource import (
    MIN_MAINWINDOW_WIDTH,
    MIN_MAINWINDOW_HEIGHT,
    MAIN_BG_COLOR,
    UI_FONT,
)


class MainWindow(QMainWindow):
    """
    Mô tả: Cửa sổ chính của ứng dụng.
    """

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Quản lý Item ")
        self.setMinimumWidth(MIN_MAINWINDOW_WIDTH)
        self.setMinimumHeight(MIN_MAINWINDOW_HEIGHT)
        self.setStyleSheet(
            f"background-color: {MAIN_BG_COLOR}; font-family: {UI_FONT};"
        )
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Mô tả: Khởi tạo layout, tách riêng background và nội dung.
        Returns:
                None
        """
        # Widget nền (background)
        bg_widget = QWidget(self)
        bg_layout = QVBoxLayout(bg_widget)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        bg_layout.setSpacing(0)

        # Widget nội dung (content)
        self.content_widget = QWidget(self)
        content_layout = QVBoxLayout(self.content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        # ... Thêm các widget nội dung tại đây ...

        bg_layout.addWidget(self.content_widget)
        self.setCentralWidget(bg_widget)
