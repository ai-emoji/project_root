"""
Popup hiển thị/thay đổi thông tin công ty.
Tuân thủ nghiêm ngặt .copilot_instructions: tách riêng BG và nội dung, dùng biến resource, không sinh code GUI tự động, comment tiếng Việt, layout sạch, chuẩn production.
"""

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
)
from PySide6.QtCore import Qt
from core.resource import (
    POPUP_TITLE_FONT_SIZE,
    POPUP_1_TITLE_BG_HEIGHT,
    TITLE_1_COLOR,
    UI_FONT,
    BUTTON_1_COLOR,
    BUTTON_1_HOVER_COLOR,
    BUTTON_FONT,
    FONT_WEIGHT_BOLD,
    COMMON_PADDING,
    COMMON_MARGIN,
    TEXT_1_COLOR,
    MAIN_BG_COLOR,
)


class PopupCompany(QDialog):
    """
    Popup hiển thị và chỉnh sửa thông tin công ty.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thông tin công ty")
        self.setModal(True)
        self.setFixedWidth(600)
        self._init_ui()
        self._load_company_data()
        self.show()

    def _init_ui(self):
        # Layout tổng, tách riêng BG và nội dung
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # BG title
        title_bg = QFrame(self)
        title_bg.setFixedHeight(int(POPUP_1_TITLE_BG_HEIGHT.replace("px", "")))
        title_bg.setStyleSheet(f"background: {MAIN_BG_COLOR};")
        title_layout = QHBoxLayout(title_bg)
        title_layout.setContentsMargins(24, 0, 24, 0)
        title_layout.setSpacing(0)

        # Tiêu đề
        title_label = QLabel("Thông tin công ty", title_bg)
        title_label.setStyleSheet(
            f"color: {TITLE_1_COLOR}; font-family: {UI_FONT}; font-size: {POPUP_TITLE_FONT_SIZE}; font-weight: {FONT_WEIGHT_BOLD};"
        )
        title_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        title_layout.addWidget(title_label)

        # BG nội dung
        content_bg = QFrame(self)
        content_bg.setStyleSheet(f"background: {MAIN_BG_COLOR};")
        content_layout = QVBoxLayout(content_bg)
        content_layout.setContentsMargins(24, 24, 24, 24)
        content_layout.setSpacing(20)

        # Phần ảnh công ty ở trên cùng, căn giữa
        img_container = QFrame()
        img_container.setStyleSheet("background: transparent;")
        img_layout = QVBoxLayout(img_container)
        img_layout.setContentsMargins(0, 0, 0, 0)
        img_layout.setSpacing(12)
        img_layout.setAlignment(Qt.AlignHCenter)

        from core.resource import ICON_APP
        from PySide6.QtGui import QPixmap

        self.label_image = QLabel()
        self.label_image.setFixedSize(120, 120)
        self.label_image.setStyleSheet(
            "border: 2px solid #e0e0e0; background: #ffffff; border-radius: 8px;"
        )
        self.label_image.setAlignment(Qt.AlignCenter)
        # Hiển thị ảnh mặc định từ ICON_APP
        pixmap = QPixmap(ICON_APP).scaled(
            116, 116, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.label_image.setPixmap(pixmap)
        img_layout.addWidget(self.label_image, alignment=Qt.AlignHCenter)

        btn_change_img = QPushButton("Thay đổi logo công ty")
        btn_change_img.setCursor(Qt.PointingHandCursor)
        btn_change_img.setFixedWidth(180)
        btn_change_img.setStyleSheet(
            f"QPushButton {{ background: {BUTTON_1_COLOR}; color: white; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; border-radius: 6px; padding: 8px 20px; }}"
            f"QPushButton:hover {{ background: {BUTTON_1_HOVER_COLOR}; }}"
        )
        btn_change_img.clicked.connect(self._on_change_image)
        img_layout.addWidget(btn_change_img, alignment=Qt.AlignHCenter)

        content_layout.addWidget(img_container)

        # Đường phân cách
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background: #e0e0e0; max-height: 1px;")
        content_layout.addWidget(separator)

        # Form nhập liệu với styling đồng nhất
        form_layout = QVBoxLayout()
        form_layout.setSpacing(16)

        # Helper function để tạo field
        def create_field(label_text, placeholder=""):
            field_layout = QVBoxLayout()
            field_layout.setSpacing(6)

            label = QLabel(label_text)
            label.setStyleSheet(
                f"font-family: {UI_FONT}; font-size: 14px; color: {TEXT_1_COLOR}; font-weight: {FONT_WEIGHT_BOLD};"
            )
            field_layout.addWidget(label)

            line_edit = QLineEdit()
            line_edit.setPlaceholderText(placeholder)
            line_edit.setFixedHeight(38)
            line_edit.setStyleSheet(
                f"QLineEdit {{"
                f"  font-family: {UI_FONT}; font-size: 14px; color: {TEXT_1_COLOR};"
                f"  background: #ffffff; border: 1px solid #d0d0d0; border-radius: 6px;"
                f"  padding: 0 12px;"
                f"}}"
                f"QLineEdit:focus {{"
                f"  border: 2px solid {BUTTON_1_COLOR};"
                f"}}"
            )
            field_layout.addWidget(line_edit)

            return field_layout, line_edit

        # Tên công ty
        name_layout, self.edit_name = create_field("Tên công ty", "Nhập tên công ty")
        form_layout.addLayout(name_layout)

        # Địa chỉ
        address_layout, self.edit_address = create_field(
            "Địa chỉ", "Nhập địa chỉ công ty"
        )
        form_layout.addLayout(address_layout)

        # Layout 2 cột cho Phone và Tax
        row_layout = QHBoxLayout()
        row_layout.setSpacing(16)

        # Số điện thoại
        phone_layout, self.edit_phone = create_field(
            "Số điện thoại", "Nhập số điện thoại"
        )
        row_layout.addLayout(phone_layout, 1)

        # Mã số thuế
        tax_layout, self.edit_tax = create_field("Mã số thuế", "Nhập mã số thuế")
        row_layout.addLayout(tax_layout, 1)

        form_layout.addLayout(row_layout)
        content_layout.addLayout(form_layout)

        # Spacer để đẩy nút xuống dưới
        content_layout.addStretch(1)

        # Đường phân cách trước nút
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setFrameShadow(QFrame.Sunken)
        separator2.setStyleSheet("background: #e0e0e0; max-height: 1px;")
        content_layout.addWidget(separator2)

        # Nút lưu và thoát với layout đẹp hơn
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        button_layout.addStretch(1)

        btn_cancel = QPushButton("Hủy")
        btn_cancel.setCursor(Qt.PointingHandCursor)
        btn_cancel.setFixedWidth(120)
        btn_cancel.setStyleSheet(
            f"QPushButton {{ background: #e0e0e0; color: #333333; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; border-radius: 6px; padding: 10px 24px; }}"
            f"QPushButton:hover {{ background: #d0d0d0; }}"
        )
        btn_cancel.clicked.connect(self.reject)
        button_layout.addWidget(btn_cancel)

        btn_save = QPushButton("Lưu thông tin")
        btn_save.setCursor(Qt.PointingHandCursor)
        btn_save.setFixedWidth(140)
        btn_save.setStyleSheet(
            f"QPushButton {{ background: {BUTTON_1_COLOR}; color: white; font-family: {UI_FONT}; font-size: {BUTTON_FONT}; font-weight: {FONT_WEIGHT_BOLD}; border-radius: 6px; padding: 10px 24px; }}"
            f"QPushButton:hover {{ background: {BUTTON_1_HOVER_COLOR}; }}"
        )
        btn_save.clicked.connect(self._on_save_and_close)
        button_layout.addWidget(btn_save)

        content_layout.addLayout(button_layout)

        # Gắn các widget vào layout tổng
        main_layout.addWidget(title_bg)
        main_layout.addWidget(content_bg)
        self.setLayout(main_layout)

    def _load_company_data(self):
        """
        Đọc dữ liệu công ty từ DB và hiển thị realtime lên popup.
        """
        try:
            from data.company_repository import get_company
            from PySide6.QtGui import QPixmap

            data = get_company()
            if data:
                self.edit_name.setText(data.get("name") or "")
                self.edit_address.setText(data.get("address") or "")
                self.edit_phone.setText(data.get("phone") or "")
                self.edit_tax.setText(data.get("tax_code") or "")
                img_path = data.get("image_path")
                if img_path:
                    pixmap = QPixmap(img_path).scaled(
                        116, 116, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                    self.label_image.setPixmap(pixmap)
        except Exception as e:
            print("Lỗi load dữ liệu công ty:", e)

    def _on_save_and_close(self):
        """
        Lưu dữ liệu công ty vào DB và đóng popup.
        """
        try:
            from data.company_repository import upsert_company

            name = self.edit_name.text().strip()
            address = self.edit_address.text().strip()
            phone = self.edit_phone.text().strip()
            tax_code = self.edit_tax.text().strip()
            # Lấy đường dẫn ảnh hiện tại nếu có
            img_path = None
            pixmap = self.label_image.pixmap()
            if pixmap and hasattr(self, "_last_image_path"):
                img_path = self._last_image_path
            from core.resource import ICON_APP

            if not img_path:
                img_path = ICON_APP
            upsert_company(name, address, phone, tax_code, img_path)
        except Exception as e:
            print("Lỗi lưu dữ liệu công ty:", e)
        self.accept()

    def _on_change_image(self):
        """
        Xử lý chọn và hiển thị ảnh công ty, đồng thời lưu đường dẫn ảnh để cập nhật DB.
        Nếu chọn ảnh mới, cập nhật luôn app icon toàn cục để đồng bộ logo trên toàn app.
        """
        from PySide6.QtWidgets import QFileDialog

        file, _ = QFileDialog.getOpenFileName(
            self, "Chọn ảnh công ty", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file:
            from PySide6.QtGui import QPixmap, QIcon
            from core.resource import set_app_icon
            from PySide6.QtWidgets import QApplication

            pixmap = QPixmap(file).scaled(
                116, 116, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.label_image.setPixmap(pixmap)
            self._last_image_path = file
            # Cập nhật icon app toàn cục
            set_app_icon(file)
            # Đổi icon cho QApplication và MainWindow nếu có
            app = QApplication.instance()
            if app:
                app.setWindowIcon(QIcon(file))
            mw = self.parent()
            if mw:
                mw.setWindowIcon(QIcon(file))
