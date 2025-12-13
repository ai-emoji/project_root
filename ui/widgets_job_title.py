"""
Widget quản lý chức danh (Job Title).
Tuân thủ nghiêm ngặt .copilot_instructions: tách riêng background và nội dung, sử dụng biến resource, không sinh code GUI tự động, comment tiếng Việt, layout sạch, chuẩn production.
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFrame,
    QLabel,
    QHBoxLayout,
    QPushButton,
)
from core.resource import (
    MAIN_BG_COLOR,
    UI_FONT,
    MIN_MAINWINDOW_WIDTH,
    MIN_MAINWINDOW_HEIGHT,
    HEADER_MAIN_1_HEIGHT,
    HEADER_MAIN_2_HEIGHT,
    HEADER_1_BG_COLOR,
    HEADER_2_BG_COLOR,
    IMAGES,
    TEXT_1_COLOR,
    POPUP_TITLE_FONT_SIZE,
    FONT_WEIGHT_BOLD,
    MAIN_CONTENT_HEIGHT,
    BUTTON_1_COLOR,
    BUTTON_FONT,
    BUTTON_1_HOVER_COLOR,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


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
        content_layout = QHBoxLayout(header1_content)
        content_layout.setContentsMargins(16, 0, 0, 0)
        content_layout.setSpacing(2)

        # Ảnh chức danh (icon)
        icon_label = QLabel(header1_content)
        icon_path = IMAGES.get("job_title", "")
        if icon_path:
            pixmap = QPixmap(icon_path).scaled(28, 28, Qt.KeepAspectRatio)
            icon_label.setPixmap(pixmap)
        icon_label.setFixedSize(40, 40)
        icon_label.setStyleSheet("background: transparent;")
        content_layout.addWidget(
            icon_label,
            0,
        )

        # Tiêu đề
        title_label = QLabel("Quản lý chức danh", header1_content)
        title_label.setStyleSheet(
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: {POPUP_TITLE_FONT_SIZE}; font-weight: {FONT_WEIGHT_BOLD}; background: transparent;"
        )
        content_layout.addWidget(
            title_label,
            0,
        )
        content_layout.addStretch(1)

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
        content2_layout = QHBoxLayout(header2_content)
        content2_layout.setContentsMargins(16, 0, 0, 0)  # chỉ cách trái 16px
        content2_layout.setSpacing(10)

        # 3 nút chức năng

        btn_them = QPushButton("Thêm mới", header2_content)
        btn_them.setCursor(Qt.PointingHandCursor)
        btn_them.setIcon(QIcon(IMAGES.get("add", "")))
        btn_them.setIconSize(QSize(20, 20))
        btn_them.setStyleSheet(
            f"QPushButton {{ background: transparent; border: none; color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; padding: 6px 6px; }}"
        )

        btn_sua = QPushButton("Sửa đổi", header2_content)
        btn_sua.setCursor(Qt.PointingHandCursor)
        btn_sua.setIcon(QIcon(IMAGES.get("edit", "")))
        btn_sua.setIconSize(QSize(20, 20))
        btn_sua.setStyleSheet(
            f"QPushButton {{ background: transparent; border: none; color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; padding: 6px 6px; }}"
        )

        btn_xoa = QPushButton("Xóa", header2_content)
        btn_xoa.setCursor(Qt.PointingHandCursor)
        btn_xoa.setIcon(QIcon(IMAGES.get("delete", "")))
        btn_xoa.setIconSize(QSize(20, 20))
        btn_xoa.setStyleSheet(
            f"QPushButton {{ background: transparent; border: none; color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; padding: 6px 6px; }}"
        )

        content2_layout.addWidget(btn_them, 0, Qt.AlignLeft)
        content2_layout.addWidget(btn_sua, 0, Qt.AlignLeft)
        content2_layout.addWidget(btn_xoa, 0, Qt.AlignLeft)
        # Thêm dấu "|" sau nút Xóa
        separator = QLabel("|", header2_content)
        separator.setStyleSheet(
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: 16px; font-weight: {FONT_WEIGHT_BOLD}; background: transparent; padding: 0 8px;"
        )
        content2_layout.addWidget(separator, 0, Qt.AlignLeft)
        # Label tổng số hiển thị ngay sau dấu |
        lbl_total = QLabel("Tổng : 0", header2_content)
        lbl_total.setStyleSheet(
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: 14px; font-weight: {FONT_WEIGHT_BOLD}; background: transparent;"
        )
        content2_layout.addWidget(lbl_total, 0, Qt.AlignLeft)
        content2_layout.addStretch(1)

        header2_layout.addWidget(header2_content)
        main_layout.addWidget(header2_bg)

        # Main content: BG + Content
        main_bg = QFrame(self)
        # Không setFixedHeight cho main_bg để bảng luôn hiển thị đủ
        main_bg.setStyleSheet(f"background: {MAIN_BG_COLOR};")
        main_bg_layout = QVBoxLayout(main_bg)
        main_bg_layout.setContentsMargins(0, 0, 0, 0)
        main_bg_layout.setSpacing(0)
        from PySide6.QtWidgets import QSizePolicy

        main_content = QFrame(main_bg)
        main_content.setStyleSheet("background: transparent;")
        main_content.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Bảng 2 cột: STT | Chức danh
        from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
        from core.resource import (
            TITLEBAR_HEIGHT,
            TABLE_ROW_HEIGHT,
            FONT_WEIGHT_SEMIBOLD,
        )

        table = QTableWidget(0, 2, main_content)
        table.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        table.setHorizontalHeaderLabels(["STT", "Chức danh"])
        table.setStyleSheet(
            f"QTableWidget {{ background: transparent; border: 1px solid #000000; }}"
            f"QHeaderView::section {{ background: transparent; color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-size: 15px; font-weight: {FONT_WEIGHT_SEMIBOLD}; height: {TITLEBAR_HEIGHT}; border: 1px solid #000000; }}"
            f"QTableWidget::item {{ height: {TABLE_ROW_HEIGHT}; border: 1px solid #000000; }}"
        )
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        from PySide6.QtWidgets import QAbstractItemView

        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setShowGrid(True)
        table.setAlternatingRowColors(False)
        table.setColumnWidth(0, 60)
        table.setColumnWidth(1, 300)
        # Bật thanh cuộn dọc
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # Thêm 10 dòng STT từ 1 đến 10, cột Chức danh để trống
        table.setRowCount(50)
        for i in range(50):
            item_stt = QTableWidgetItem(str(i + 1))
            item_stt.setTextAlignment(Qt.AlignCenter)
            table.setItem(i, 0, item_stt)
            table.setItem(i, 1, QTableWidgetItem(""))

        # Thêm bảng vào main_content
        main_content_layout = QVBoxLayout(main_content)
        # Không margin dưới để bảng chiếm tối đa chiều cao
        main_content_layout.setContentsMargins(0, 0, 0, 0)
        main_content_layout.setSpacing(0)
        main_content_layout.addWidget(table)
        main_bg_layout.addWidget(main_content)
        main_layout.addWidget(main_bg, 1)
