"""
Widget quản lý chức danh (Job Title).
Tuân thủ nghiêm ngặt .copilot_instructions: tách riêng background và nội dung, sử dụng biến resource, không sinh code GUI tự động, comment tiếng Việt, layout sạch, chuẩn production.
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame

from core.resource import (
    JOB_TITLE_MIN_WIDTH,
    JOB_TITLE_MIN_HEIGHT,
    JOB_TITLE_MIN_HEIGHT_1,
    JOB_TITLE_MIN_HEIGHT_2,
    JOB_TITLE_MIN_HEIGHT_3,
    JOB_TITLE_BG_1,
    JOB_TITLE_BG_2,
    JOB_TITLE_BG_3,
)


class WidgetJobTitle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Thiết lập kích thước tối thiểu cho cửa sổ chức danh
        self.setMinimumWidth(JOB_TITLE_MIN_WIDTH)
        self.setMinimumHeight(JOB_TITLE_MIN_HEIGHT)
        # Layout tổng chia 3 phần riêng biệt

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Phần 1

        # Phần 1: BG + Content
        part1_bg = QFrame(self)
        part1_bg.setFixedHeight(JOB_TITLE_MIN_HEIGHT_1)
        part1_bg.setStyleSheet(f"background: {JOB_TITLE_BG_1};")
        part1_layout = QVBoxLayout(part1_bg)
        part1_layout.setContentsMargins(0, 0, 0, 0)
        part1_layout.setSpacing(0)
        part1_content = QFrame(part1_bg)
        part1_content.setStyleSheet("background: transparent;")
        part1_layout.addWidget(part1_content)
        main_layout.addWidget(part1_bg)

        # Phần 2: BG + Content
        part2_bg = QFrame(self)
        part2_bg.setFixedHeight(JOB_TITLE_MIN_HEIGHT_2)
        part2_bg.setStyleSheet(f"background: {JOB_TITLE_BG_2};")
        part2_layout = QVBoxLayout(part2_bg)
        part2_layout.setContentsMargins(0, 0, 0, 0)
        part2_layout.setSpacing(0)
        part2_content = QFrame(part2_bg)
        part2_content.setStyleSheet("background: transparent;")
        part2_layout.addWidget(part2_content)
        main_layout.addWidget(part2_bg)

        # Phần 3: BG + Content
        part3_bg = QFrame(self)
        part3_bg.setMinimumHeight(JOB_TITLE_MIN_HEIGHT_3)
        part3_bg.setMaximumHeight(JOB_TITLE_MIN_HEIGHT_3)
        part3_bg.setStyleSheet(f"background: {JOB_TITLE_BG_3};")
        part3_layout = QVBoxLayout(part3_bg)
        part3_layout.setContentsMargins(0, 0, 0, 0)
        part3_layout.setSpacing(0)
        part3_content = QFrame(part3_bg)
        part3_content.setStyleSheet("background: transparent;")
        part3_layout.addWidget(part3_content)
        main_layout.addWidget(part3_bg)
