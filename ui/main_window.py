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
        Mô tả: Khởi tạo layout, tách riêng header, main content, footer.
        Returns:
            None
        """
        from core.resource import (
            HEADER_HEIGHT,
            FOOTER_WEIGHT,
            MAIN_HEIGHT,
            HEADER_BG_COLOR,
            FOOTER_BG_COLOR,
        )
        from common.widgets_header import HeaderWidget
        from common.widgets_footer import FooterWidget

        # Widget nền (background)
        bg_widget = QWidget(self)
        bg_layout = QVBoxLayout(bg_widget)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        bg_layout.setSpacing(0)

        # Header
        self.header_widget = HeaderWidget(self)
        self.header_widget.setFixedHeight(int(HEADER_HEIGHT.replace("px", "")))
        self.header_widget.setStyleSheet(f"background-color: {HEADER_BG_COLOR};")
        bg_layout.addWidget(self.header_widget)

        # Main content (tách riêng BG và nội dung)
        from ui.widgets_job_title import WidgetJobTitle

        self.content_widget = QWidget(self)
        self.content_widget.setStyleSheet(f"background-color: {MAIN_BG_COLOR};")
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        bg_layout.addWidget(self.content_widget, 1)

        # Hiển thị widget job title khi click btn "Khai báo chức danh"
        def show_job_title():
            # Xóa widget cũ nếu có
            while self.content_layout.count():
                item = self.content_layout.takeAt(0)
                w = item.widget()
                if w is not None:
                    w.setParent(None)
            # Thêm widget mới
            self.content_layout.addWidget(WidgetJobTitle(self))

        # Kết nối sự kiện click btn "Khai báo chức danh"
        btns = getattr(self.header_widget, "_main_button_groups", {}).get(
            "khai_bao", []
        )
        # Tìm đúng button "Khai báo chức danh" trong header
        for i, (icon_key, text, tooltip) in enumerate(btns):
            if icon_key == "job_title":
                khai_bao_page = self.header_widget.stacked_main.widget(0)
                btn = khai_bao_page.findChildren(type(self.header_widget.btn_khaibao))[
                    i
                ]
                btn.clicked.connect(show_job_title)
                break

        # Footer
        self.footer_widget = FooterWidget(self)
        self.footer_widget.setFixedHeight(int(FOOTER_WEIGHT.replace("px", "")))
        self.footer_widget.setStyleSheet(f"background-color: {FOOTER_BG_COLOR};")
        bg_layout.addWidget(self.footer_widget)

        self.setCentralWidget(bg_widget)
