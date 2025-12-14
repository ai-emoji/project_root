# Giao diện chính, quản lý signal/slot, gọi service

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from core.resource import (
    MIN_MAINWINDOW_WIDTH,
    MIN_MAINWINDOW_HEIGHT,
    HEADER_HEIGHT,
    MAIN_HEIGHT,
    APP_ICON_PATH,
)
from PySide6.QtGui import QIcon
from common.widgets_header import HeaderWidget
from common.widgets_footer import FooterWidget


class MainWindow(QMainWindow):
    """
    Cửa sổ chính của ứng dụng, quản lý giao diện và các signal/slot.
    """

    def __init__(self):
        super().__init__()
        # Thiết lập kích thước tối thiểu cho cửa sổ chính
        self.setMinimumSize(MIN_MAINWINDOW_WIDTH, MIN_MAINWINDOW_HEIGHT)
        # Lưu lại kích thước tối thiểu để popup có thể truy cập nếu cần
        self.min_width = MIN_MAINWINDOW_WIDTH
        self.min_height = MIN_MAINWINDOW_HEIGHT

        self.setWindowTitle("Quản lý dữ liệu")
        # Thiết lập icon ứng dụng, có thể thay đổi động qua APP_ICON_PATH
        # Lấy icon mới nhất từ DB (nếu có)
        from data.company_repository import get_company

        company = get_company()
        icon_path = (
            company["image_path"]
            if company and company.get("image_path")
            else APP_ICON_PATH
        )
        self.setWindowIcon(QIcon(icon_path))

        # Widget nền tổng
        central_widget = QWidget(self)
        central_widget.setStyleSheet(f"background: none;")
        self.setCentralWidget(central_widget)

        # Layout tổng chia header, main, footer
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header luôn ở trên cùng
        self.header = HeaderWidget()
        layout.addWidget(self.header, stretch=0)

        # Main content chiếm toàn bộ phần còn lại
        self.main_content = QWidget()
        self.main_content.setStyleSheet("background: transparent;")
        layout.addWidget(self.main_content, stretch=1)

        # Footer luôn ở cuối
        self.footer = FooterWidget()
        layout.addWidget(self.footer, stretch=0)
