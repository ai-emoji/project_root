from functools import partial

"""
Mô tả:
    Widget header dùng chung, chia 2 phần: header (HEADER_MAIN_1_HEIGHT, có border dưới), main (MAIN_CONTENT_HEIGHT), tách bg và nội dung.
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton,
    QStackedWidget,
)
from PySide6.QtCore import Qt, QSize
from core.resource import (
    HEADER_MAIN_1_HEIGHT,
    MAIN_CONTENT_HEIGHT,
    BOTTOM_BORDER_COLOR,
    HEADER_BG_COLOR,
    UI_FONT,
    FUNCTION_HEDER_WIDTH,
    TEXT_1_COLOR,
    FONT_WEIGHT_SEMIBOLD,
    FONT_WEIGHT_BOLD,
    FONT_SIZE_ACTIVE,
    FUNCTION_MAIN_HEIGHT,
    FUNCTION_MAIN_WIDTH,
    IMAGES,
)

from PySide6.QtGui import QIcon


class HeaderWidget(QWidget):
    """
    Mô tả: Header chia 2 phần: header (HEADER_MAIN_1_HEIGHT, có border dưới), main (MAIN_CONTENT_HEIGHT), tách bg và nội dung.
    """

    def _show_company_popup(self):
        from ui.popup_company import PopupCompany

        parent = self.window() if hasattr(self, "window") else self
        # Giữ reference để tránh bị GC
        self._popup_company_ref = PopupCompany(parent)
        self._popup_company_ref.setWindowModality(Qt.ApplicationModal)
        # Cho phép chuyển đổi giữa exec/show để debug
        USE_EXEC = False  # Đổi sang False để thử show() nếu exec() không hiển thị
        if USE_EXEC:
            result = self._popup_company_ref.exec()
        else:
            self._popup_company_ref.show()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Mô tả: Khởi tạo layout header chia 2 phần, tách bg và nội dung.
        Returns:
            None
        """
        # Layout tổng
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Phần header (HEADER_MAIN_1_HEIGHT, có border dưới)
        self.header_bg = QFrame(self)
        self.header_bg.setFixedHeight(int(HEADER_MAIN_1_HEIGHT.replace("px", "")))
        self.header_bg.setStyleSheet(
            f"background-color: {HEADER_BG_COLOR}; border-bottom: 1px solid {BOTTOM_BORDER_COLOR};"
        )
        header_layout = QHBoxLayout(self.header_bg)
        header_layout.setContentsMargins(0, 0, 10, 0)
        header_layout.setSpacing(10)

        # Widget chứa 4 phím chức năng, sát trái, trên nền bg
        self.button_bar = QWidget(self.header_bg)
        button_bar_layout = QHBoxLayout(self.button_bar)
        button_bar_layout.setContentsMargins(0, 0, 0, 0)
        button_bar_layout.setSpacing(0)

        # Đảm bảo FUNCTION_HEDER_WIDTH là chuỗi px
        width_px = (
            f"{FUNCTION_HEDER_WIDTH}px"
            if isinstance(FUNCTION_HEDER_WIDTH, int)
            else FUNCTION_HEDER_WIDTH
        )
        from core.resource import BUTTON_1_HOVER_COLOR, TEXT_3_COLOR

        button_style = (
            f"min-width: {width_px}; max-width: {width_px}; min-height: {HEADER_MAIN_1_HEIGHT}; max-height: {HEADER_MAIN_1_HEIGHT}; "
            f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-weight: {FONT_WEIGHT_SEMIBOLD}; border-radius: 0px; background: transparent;"
        )

        # Set QSS cho toàn bộ button_bar để enable hover/active đúng chuẩn Qt
        self.button_bar.setStyleSheet(
            f"QPushButton {{ {button_style} }}"
            f"QPushButton:hover, QPushButton:checked {{ background: {BUTTON_1_HOVER_COLOR}; color: {TEXT_3_COLOR}; font-weight: {FONT_WEIGHT_BOLD}; font-size: {FONT_SIZE_ACTIVE}; }}"
        )

        def create_text_button(text, tooltip, hover_active=True):
            btn = QPushButton(text)
            btn.setToolTip(tooltip)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setCheckable(hover_active)
            return btn

        self.btn_khaibao = create_text_button("Khai báo", "Khai báo", True)
        self.btn_ketnoi = create_text_button("Kết nối", "Kết nối", True)
        self.btn_chamcong = create_text_button("Chấm công", "Chấm công", True)
        self.btn_congcu = create_text_button("Công cụ", "Công cụ", True)

        button_bar_layout.addWidget(self.btn_khaibao)
        button_bar_layout.addWidget(self.btn_ketnoi)
        button_bar_layout.addWidget(self.btn_chamcong)
        button_bar_layout.addWidget(self.btn_congcu)

        # Đảm bảo chỉ 1 button được checked cùng lúc
        self._button_group = [
            self.btn_khaibao,
            self.btn_ketnoi,
            self.btn_chamcong,
            self.btn_congcu,
        ]

        def make_exclusive(btn, others):
            def handler():
                if btn.isChecked():
                    for b in others:
                        b.setChecked(False)

            return handler

        for i, btn in enumerate(self._button_group):
            others = self._button_group[:i] + self._button_group[i + 1 :]
            btn.clicked.connect(make_exclusive(btn, others))

        header_layout.addWidget(self.button_bar, 0, Qt.AlignLeft)

        # Phần main (MAIN_CONTENT_HEIGHT)

        # Tạo QFrame làm nền có border-bottom
        self.main_content_bg = QFrame(self)
        if MAIN_CONTENT_HEIGHT.endswith("px"):
            self.main_content_bg.setFixedHeight(
                int(MAIN_CONTENT_HEIGHT.replace("px", ""))
            )
        self.main_content_bg.setStyleSheet(
            f"background-color: {HEADER_BG_COLOR}; border-bottom: 1px solid {BOTTOM_BORDER_COLOR};"
        )
        main_content_bg_layout = QVBoxLayout(self.main_content_bg)
        main_content_bg_layout.setContentsMargins(0, 0, 0, 0)
        main_content_bg_layout.setSpacing(0)

        # QFrame chứa nội dung thực sự, không border
        self.main_content = QFrame(self.main_content_bg)
        self.main_content.setStyleSheet("background: transparent; border: none;")
        main_content_layout = QHBoxLayout(self.main_content)
        main_content_layout.setContentsMargins(0, 0, 0, 0)
        main_content_layout.setSpacing(8)

        # Định nghĩa các nhóm chức năng cho từng tab header
        # Định nghĩa các nhóm chức năng cho từng tab header, tránh lặp lại tooltip nếu giống text
        def btn(text, tooltip=None):
            return (text, tooltip or text)

        self._main_button_groups = {
            "khai_bao": [
                ("company", *btn("Thông tin công ty")),
                ("job_title", *btn("Khai báo chức danh")),
                ("department", *btn("Khai báo phòng ban")),
                ("employee", *btn("Thông tin nhân viên")),
                ("holiday", *btn("Khai báo ngày lễ")),
                ("password", *btn("Đổi mật khẩu")),
                ("exit", *btn("Thoát ứng dụng")),
            ],
            "ket_noi": [
                ("device", *btn("Máy chấm công")),
                ("download_attendance", *btn("Tải máy chấm công")),
                ("download_staff", *btn("Tải nhân viên về máy tính")),
                ("upload_staff", *btn("Tải nhân viên lên máy chấm công")),
            ],
            "cham_cong": [
                ("arrange_schedule", *btn("Sắp xếp lịch làm việc")),
                ("attendance_symbol", *btn("Các ký hiệu chấm công")),
                ("absence_symbol", *btn("Ký hiệu các loại vắng")),
                ("weekend", *btn("Chọn ngày cuối tuần")),
            ],
            "cong_cu": [
                ("backup", *btn("Sao lưu dữ liệu")),
                ("absence_restore", *btn("Khôi phục dữ liệu")),
            ],
        }

        def create_main_button(icon_key, text, tooltip):
            btn = QPushButton()
            # Không setToolTip để không có chú thích khi hover
            btn.setMinimumWidth(FUNCTION_MAIN_WIDTH)
            btn.setMaximumWidth(FUNCTION_MAIN_WIDTH)
            btn.setMinimumHeight(FUNCTION_MAIN_HEIGHT)
            btn.setMaximumHeight(FUNCTION_MAIN_HEIGHT)
            btn.setStyleSheet(
                f"QPushButton {{"
                f"  color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-weight: {FONT_WEIGHT_SEMIBOLD}; background: transparent; border-radius: 12px;"
                f"  text-align: center;"
                f"}}"
                f"QPushButton:hover {{ background: {BUTTON_1_HOVER_COLOR}; color: {TEXT_3_COLOR}; border-radius: 0px; }}"
            )
            btn.setCursor(Qt.PointingHandCursor)

            # Tạo widget dọc: icon trên, text dưới với chiều cao cố định
            from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget

            vlayout = QVBoxLayout(btn)
            vlayout.setContentsMargins(0, 12, 0, 8)
            vlayout.setSpacing(4)

            # Container cho icon với chiều cao cố định
            icon_container = QWidget()
            icon_container.setFixedHeight(43)  # tăng chiều cao icon
            icon_layout = QVBoxLayout(icon_container)
            icon_layout.setContentsMargins(0, 0, 0, 0)
            icon_layout.setAlignment(Qt.AlignCenter)

            icon_label = QLabel()
            icon_label.setPixmap(
                QIcon(IMAGES.get(icon_key, "")).pixmap(36, 36)
            )  # tăng icon
            icon_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            icon_layout.addWidget(icon_label)

            # Container cho text với chiều cao cố định
            text_container = QWidget()
            text_container.setFixedHeight(40)  # tăng chiều cao text
            text_layout = QVBoxLayout(text_container)
            text_layout.setContentsMargins(0, 2, 0, 2)  # thêm padding trên/dưới
            text_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

            text_label = QLabel(text)
            text_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
            text_label.setWordWrap(True)
            text_label.setFixedWidth(110)
            text_label.setStyleSheet(
                f"color: {TEXT_1_COLOR}; font-family: {UI_FONT}; font-weight: {FONT_WEIGHT_SEMIBOLD}; font-size: 13px; background: transparent;"
            )
            text_layout.addWidget(text_label)

            vlayout.addWidget(icon_container, alignment=Qt.AlignHCenter)
            vlayout.addWidget(text_container, alignment=Qt.AlignHCenter)
            vlayout.setSpacing(6)  # tăng spacing giữa icon và text
            vlayout.addStretch(1)

            return btn

        # Tạo QStackedWidget để chuyển đổi nhóm chức năng
        self.stacked_main = QStackedWidget(self.main_content)
        self._main_pages = {}
        from PySide6.QtWidgets import QApplication

        for key, btns in self._main_button_groups.items():
            page = QWidget()
            layout = QHBoxLayout(page)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(8)
            layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            for icon_key, text, tooltip in btns:
                btn = create_main_button(icon_key, text, tooltip)
                if icon_key == "exit":
                    btn.clicked.connect(QApplication.quit)
                elif icon_key == "company":
                    btn.clicked.connect(partial(HeaderWidget._show_company_popup, self))
                layout.addWidget(btn)
            layout.addStretch(1)
            self.stacked_main.addWidget(page)
            self._main_pages[key] = page
        main_content_layout.addWidget(self.stacked_main)
        main_content_layout.addStretch(1)
        main_content_bg_layout.addWidget(self.main_content)

        # Hàm chuyển trang chức năng
        def show_main_group(key):
            idx = list(self._main_pages.keys()).index(key)
            self.stacked_main.setCurrentIndex(idx)

        # Gán sự kiện cho các nút header
        self.btn_khaibao.clicked.connect(lambda: show_main_group("khai_bao"))
        self.btn_ketnoi.clicked.connect(lambda: show_main_group("ket_noi"))
        self.btn_chamcong.clicked.connect(lambda: show_main_group("cham_cong"))
        self.btn_congcu.clicked.connect(lambda: show_main_group("cong_cu"))

        # Hiển thị mặc định nhóm khai báo
        show_main_group("khai_bao")

        main_layout.addWidget(self.header_bg)
        main_layout.addWidget(self.main_content_bg)
