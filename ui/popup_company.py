from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSizePolicy, QSpacerItem
from PySide6.QtGui import QIcon, QPixmap
from core.resource import UI_FONT, COLOR_TEXT, COLOR_BACKGROUND, APP_ICON_PATH, CONTENT_FONT_SIZE, FONT_BOLD, BUTTON_COLOR
from data.company_repository import upsert_company, get_company


class PopupCompany(QDialog):
    def change_avatar(self):
        """Thay đổi ảnh đại diện và đồng bộ ngay lập tức"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Chọn ảnh đại diện", 
            "", 
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        
        print(f"[DEBUG] Chọn file: {file_path}")
        
        if not file_path:
            return
            
        pixmap = QPixmap(file_path)
        print(f"[DEBUG] pixmap.isNull(): {pixmap.isNull()}")
        
        if pixmap.isNull():
            print("[ERROR] Không thể load ảnh từ file đã chọn")
            return
        
        # 1. Cập nhật preview trong dialog
        self.avatar_label.setPixmap(pixmap.scaled(
            80, 80, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        ))
        self.selected_avatar_path = file_path
        
        # 2. Lưu vào DB ngay lập tức
        name = self.edit_name.text().strip()
        address = self.edit_address.text().strip()
        phone = self.edit_phone.text().strip()
        tax_code = ''
        
        upsert_company(name, address, phone, tax_code, file_path)
        print(f"[INFO] Đã lưu avatar mới vào DB: {file_path}")
        
        # 3. Cập nhật biến toàn cục
        from core.resource import set_app_icon_path
        set_app_icon_path(file_path)
        print(f"[INFO] APP_ICON_PATH đã được cập nhật: {file_path}")
        
        # 4. Đồng bộ icon cho tất cả cửa sổ trong ứng dụng
        self._sync_app_icon(file_path)

    def _sync_app_icon(self, icon_path: str):
        """Đồng bộ icon cho toàn bộ ứng dụng"""
        from PySide6.QtWidgets import QApplication
        
        new_icon = QIcon(icon_path)
        
        # Cập nhật icon cho QApplication (áp dụng cho tất cả cửa sổ mới)
        app = QApplication.instance()
        if app:
            app.setWindowIcon(new_icon)
            print(f"[INFO] QApplication icon đã được cập nhật")
        
        # Cập nhật icon cho dialog hiện tại
        self.setWindowIcon(new_icon)
        
        # Cập nhật icon cho cửa sổ cha (MainWindow) nếu có
        if self.parent():
            self.parent().setWindowIcon(new_icon)
            print(f"[INFO] Parent window icon đã được cập nhật")
        
        # Cập nhật tất cả top-level windows
        if app:
            for window in app.topLevelWindows():
                # window có thể là QWindow, cần lấy widget tương ứng
                widget = QWidget.find(window.winId())
                if widget:
                    widget.setWindowIcon(new_icon)
            print(f"[INFO] Tất cả top-level windows đã được cập nhật icon")

    def save_and_exit(self):
        """Lưu thông tin và đóng dialog"""
        name = self.edit_name.text().strip()
        address = self.edit_address.text().strip()
        phone = self.edit_phone.text().strip()
        avatar = getattr(self, 'selected_avatar_path', None)
        
        # Nếu không có avatar mới, giữ nguyên avatar cũ từ DB
        if not avatar:
            company = get_company()
            avatar = company.get("image_path") if company else APP_ICON_PATH
        
        tax_code = ''
        
        # Lưu vào DB
        upsert_company(name, address, phone, tax_code, avatar)
        print(f"[INFO] Đã lưu thông tin công ty")
        print(f"  - Tên: {name}")
        print(f"  - Địa chỉ: {address}")
        print(f"  - SĐT: {phone}")
        print(f"  - Avatar: {avatar}")
        
        # Đồng bộ icon (trường hợp người dùng chỉ sửa thông tin không sửa ảnh)
        from core.resource import set_app_icon_path
        set_app_icon_path(avatar)
        self._sync_app_icon(avatar)
        
        self.accept()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thông tin công ty")
        self.setFixedSize(500, 400)
        self.setStyleSheet(
            f"background: {COLOR_BACKGROUND}; "
            f"color: {COLOR_TEXT}; "
            f"font-family: {UI_FONT};"
        )
        self.setWindowIcon(QIcon(APP_ICON_PATH))

        # Đảm bảo popup nằm giữa main_window nếu có parent
        if parent is not None:
            parent_geom = parent.geometry()  # geometry() lấy vị trí thực tế trên màn hình
            self_geom = self.geometry()
            x = parent_geom.x() + (parent_geom.width() - self.width()) // 2
            y = parent_geom.y() + (parent_geom.height() - self.height()) // 2
            self.move(x, y)

        # Lưu đường dẫn avatar đã chọn (nếu có)
        self.selected_avatar_path = None

        # Lấy dữ liệu từ DB
        company = get_company() or {}

        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignTop)

        # --- Nhóm Tên công ty ---
        name_group = self._create_input_group(
            "Tên công ty",
            "Nhập tên công ty...",
            company.get("name", "")
        )
        self.edit_name = name_group['input']
        layout.addWidget(name_group['widget'])

        # --- Nhóm Địa chỉ ---
        address_group = self._create_input_group(
            "Địa chỉ",
            "Nhập địa chỉ...",
            company.get("address", "")
        )
        self.edit_address = address_group['input']
        layout.addWidget(address_group['widget'])

        # --- Nhóm Số điện thoại ---
        phone_group = self._create_input_group(
            "Số điện thoại",
            "Nhập số điện thoại...",
            company.get("phone", "")
        )
        self.edit_phone = phone_group['input']
        layout.addWidget(phone_group['widget'])

        # --- Nhóm Avatar & Buttons ---
        extra_group = self._create_avatar_section(company)
        layout.addWidget(extra_group)
    
    def _create_input_group(self, label_text: str, placeholder: str, default_value: str) -> dict:
        """Tạo nhóm input với label và textbox"""
        group = QWidget()
        group.setFixedHeight(70)
        group_layout = QHBoxLayout(group)
        group_layout.setContentsMargins(0, 0, 0, 0)
        group_layout.setSpacing(0)
        
        inner = QWidget()
        inner_layout = QVBoxLayout(inner)
        inner_layout.setSpacing(5)
        inner_layout.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel(label_text)
        label.setStyleSheet(
            f"font-size: {CONTENT_FONT_SIZE}px; "
            f"font-weight: {FONT_BOLD}; "
            f"color: {COLOR_TEXT}; "
            f"font-family: {UI_FONT};"
        )
        inner_layout.addWidget(label)
        
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setText(default_value)
        input_field.setStyleSheet(
            f"font-size: {CONTENT_FONT_SIZE}px; "
            f"color: {COLOR_TEXT}; "
            f"font-family: {UI_FONT}; "
            f"padding: 8px 12px;"
        )
        inner_layout.addWidget(input_field)
        
        group_layout.addWidget(inner, stretch=1)
        
        return {'widget': group, 'input': input_field}
    
    def _create_avatar_section(self, company: dict) -> QWidget:
        """Tạo section hiển thị avatar và các nút điều khiển"""
        extra_group = QWidget()
        extra_group.setMinimumWidth(400)
        extra_group.setFixedHeight(120)
        extra_group_layout = QHBoxLayout(extra_group)
        extra_group_layout.setContentsMargins(0, 0, 0, 0)
        extra_group_layout.setSpacing(12)
        
        # Avatar label
        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(100, 100)
        self.avatar_label.setStyleSheet(
            "background: #e0e0e0; "
            "border: 1px solid #ccc; "
            "border-radius: 4px;"
        )
        self.avatar_label.setAlignment(Qt.AlignCenter)
        
        # Load avatar từ DB hoặc dùng icon mặc định
        image_path = company.get("image_path")
        if image_path:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.avatar_label.setPixmap(pixmap.scaled(
                    80, 80, 
                    Qt.KeepAspectRatio, 
                    Qt.SmoothTransformation
                ))
                self.selected_avatar_path = image_path
        
        # Fallback to default icon
        if not hasattr(self, 'selected_avatar_path') or not self.selected_avatar_path:
            pixmap = QPixmap(APP_ICON_PATH)
            if not pixmap.isNull():
                self.avatar_label.setPixmap(pixmap.scaled(
                    80, 80, 
                    Qt.KeepAspectRatio, 
                    Qt.SmoothTransformation
                ))
        
        extra_group_layout.addWidget(self.avatar_label)
        
        # Right column với buttons
        right_col = QWidget()
        right_col_layout = QVBoxLayout(right_col)
        right_col_layout.setContentsMargins(0, 10, 0, 10)
        right_col_layout.setSpacing(8)
        right_col_layout.setAlignment(Qt.AlignVCenter)
        
        # Nút thay đổi ảnh
        self.btn_change_image = QPushButton("Thay đổi ảnh")
        self.btn_change_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_change_image.setFixedHeight(40)
        self.btn_change_image.setStyleSheet(
            f"background: {BUTTON_COLOR}; "
            f"color: white; "
            f"border-radius: 4px;"
        )
        self.btn_change_image.setCursor(Qt.PointingHandCursor)
        self.btn_change_image.clicked.connect(self.change_avatar)
        right_col_layout.addWidget(self.btn_change_image)
        
        # Spacer
        right_col_layout.addItem(QSpacerItem(
            20, 10, 
            QSizePolicy.Minimum, 
            QSizePolicy.Expanding
        ))
        
        # Nút lưu & thoát
        self.btn_save_exit = QPushButton("Lưu & Thoát")
        self.btn_save_exit.setFixedHeight(40)
        self.btn_save_exit.setStyleSheet(
            f"background: {BUTTON_COLOR}; "
            f"color: white; "
            f"border-radius: 4px;"
        )
        self.btn_save_exit.setCursor(Qt.PointingHandCursor)
        self.btn_save_exit.clicked.connect(self.save_and_exit)
        right_col_layout.addWidget(self.btn_save_exit)
        
        extra_group_layout.addWidget(right_col, stretch=1)
        
        return extra_group