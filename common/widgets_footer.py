"""
Mô tả:
        Widget footer dùng chung, hiển thị ngày giờ realtime, thông tin phần mềm, tách riêng background và nội dung.
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import QTimer, QDateTime, Qt
from core.resource import (
    FOOTER_BG_COLOR,
    TEXT_1_COLOR,
    UI_FONT,
    VERSION,
    LAST_UPDATE,
    FONT_WEIGHT_BOLD,
)


class FooterWidget(QWidget):
    """
    Mô tả: Footer hiển thị ngày giờ realtime và thông tin phần mềm.
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._init_ui()
        self._init_timer()

    def _init_ui(self) -> None:
        """
        Mô tả: Khởi tạo layout, tách riêng background và nội dung.
        Returns:
                None
        """
        # Widget nền (background)
        bg = QFrame(self)
        bg.setStyleSheet(f"background-color: {FOOTER_BG_COLOR};")
        layout = QHBoxLayout(bg)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(10)

        # Label ngày giờ realtime
        self.datetime_label = QLabel()
        self.datetime_label.setStyleSheet(
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-weight: {FONT_WEIGHT_BOLD};"
        )
        self.datetime_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.datetime_label, 1)

        # Label thông tin phần mềm
        self.info_label = QLabel(f"Phiên bản: {VERSION} | Cập nhật: {LAST_UPDATE}")
        self.info_label.setStyleSheet(
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-weight: {FONT_WEIGHT_BOLD};"
        )
        self.info_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(self.info_label, 0)

        # Layout tổng
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(bg)

    def _init_timer(self) -> None:
        """
        Mô tả: Khởi tạo timer cập nhật ngày giờ realtime.
        Returns:
                None
        """
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()

    def _update_datetime(self) -> None:
        """
        Mô tả: Cập nhật label ngày giờ theo thời gian thực (thứ tiếng Việt).
        Returns:
            None
        """
        now = QDateTime.currentDateTime()
        # Chuyển thứ sang tiếng Việt
        weekday_map = {
            "Monday": "Thứ Hai",
            "Tuesday": "Thứ Ba",
            "Wednesday": "Thứ Tư",
            "Thursday": "Thứ Năm",
            "Friday": "Thứ Sáu",
            "Saturday": "Thứ Bảy",
            "Sunday": "Chủ Nhật",
        }
        weekday_en = now.toString("dddd")
        weekday_vi = weekday_map.get(weekday_en, weekday_en)
        text = f"{weekday_vi}, Ngày : {now.toString('dd/MM/yyyy - Giờ : HH:mm:ss')}"
        self.datetime_label.setText(text)
