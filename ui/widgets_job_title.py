"""
Widget quản lý chức danh (Job Title).
Tuân thủ nghiêm ngặt .copilot_instructions: tách riêng background và nội dung, sử dụng biến resource, không sinh code GUI tự động, comment tiếng Việt, layout sạch, chuẩn production.
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame
from core.resource import (
    MAIN_BG_COLOR,
    UI_FONT,
    MIN_MAINWINDOW_WIDTH,
    MIN_MAINWINDOW_HEIGHT,
    HEADER_MAIN_1_HEIGHT,
    HEADER_MAIN_2_HEIGHT,
    HEADER_1_BG_COLOR,
    HEADER_2_BG_COLOR,
    MAIN_CONTENT_HEIGHT,
)


class WidgetJobTitle(QWidget):
    """
    Widget quản lý chức danh (Job Title).
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(MIN_MAINWINDOW_WIDTH)
        self.setMinimumHeight(MIN_MAINWINDOW_HEIGHT)
        self.setStyleSheet(
            f"background-color: {MAIN_BG_COLOR}; font-family: {UI_FONT};"
        )
        self._init_ui()

    def _init_ui(self):
        """
        Khởi tạo layout: header 1, header 2, main content. Tách riêng rõ ràng BG và nội dung cho từng phần.
        """
        # Layout tổng
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header 1: BG + Content
        header1_bg = QFrame(self)
        header1_bg.setFixedHeight(int(HEADER_MAIN_1_HEIGHT.replace("px", "")))
        header1_bg.setStyleSheet(f"background: {HEADER_1_BG_COLOR};")
        header1_layout = QVBoxLayout(header1_bg)
        header1_layout.setContentsMargins(0, 0, 0, 0)
        header1_layout.setSpacing(0)
        header1_content = QFrame(header1_bg)
        header1_content.setStyleSheet("background: transparent;")
        # Để trống nội dung header1
        header1_layout.addWidget(header1_content)
        main_layout.addWidget(header1_bg)

        # Header 2: BG + Content
        header2_bg = QFrame(self)
        header2_bg.setFixedHeight(int(HEADER_MAIN_2_HEIGHT.replace("px", "")))
        header2_bg.setStyleSheet(f"background: {HEADER_2_BG_COLOR};")
        header2_layout = QVBoxLayout(header2_bg)
        header2_layout.setContentsMargins(0, 0, 0, 0)
        header2_layout.setSpacing(0)
        header2_content = QFrame(header2_bg)
        header2_content.setStyleSheet("background: transparent;")
        # Để trống nội dung header2
        header2_layout.addWidget(header2_content)
        main_layout.addWidget(header2_bg)

        # Main content: BG + Content
        main_bg = QFrame(self)
        if str(MAIN_CONTENT_HEIGHT).endswith("px"):
            main_bg.setFixedHeight(int(MAIN_CONTENT_HEIGHT.replace("px", "")))
        main_bg.setStyleSheet(f"background: {MAIN_BG_COLOR};")
        main_bg_layout = QVBoxLayout(main_bg)
        main_bg_layout.setContentsMargins(0, 0, 0, 0)
        main_bg_layout.setSpacing(0)
        main_content = QFrame(main_bg)
        main_content.setStyleSheet("background: transparent;")
        # Để trống nội dung main
        main_bg_layout.addWidget(main_content)
        main_layout.addWidget(main_bg, 1)
