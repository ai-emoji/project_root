from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from core.resource import (
    COLOR_1_TEXT, HEADER_HEIGHT, HEADER_BG, COLOR_TEXT, FONT_BOLD, 
    WIDGETS_HEADER_HEIGHT, WIDGETS_MAIN_HEIGHT, WIDTH_FUNCTION_HEADER, 
    HEIGHT_FUNCTION_HEADER, WIDGETS_HEADER_WIDTH, HOVER_COLOR,
    IMG_COMPANY, IMG_JOB_TITLE, IMG_DEPARTMENT, IMG_EMPLOYEE, IMG_HOLIDAY, 
    IMG_PASSWORD, IMG_EXIT, IMG_DEVICE, IMG_DOWNLOAD_ATTENDANCE, 
    IMG_DOWNLOAD_STAFF, IMG_UPLOAD_STAFF, IMG_ARRANGE_SCHEDULE, 
    IMG_ATTENDANCE_SYMBOL, IMG_ABSENCE_SYMBOL, IMG_WEEKEND, 
    IMG_BACKUP, IMG_ABSENCE_RESTORE
)

class HeaderWidget(QWidget):
    """
    Widget header dùng chung cho toàn bộ ứng dụng.
    Chia làm 2 phần: phần trên (WIDGETS_HEADER_HEIGHT) và phần dưới (WIDGETS_MAIN_HEIGHT).
    Tách riêng background và nội dung.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Thiết lập kích thước cố định cho header tổng
        self.setFixedHeight(HEADER_HEIGHT)
        # Không setFixedWidth để header tự co giãn theo cửa sổ chính
        
        # Layout dọc cho 2 phần
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Phần trên: Header nhỏ (4 nút chức năng chính)
        top_container = QWidget(self)
        top_container_layout = QVBoxLayout(top_container)
        top_container_layout.setContentsMargins(0, 0, 0, 0)
        top_container_layout.setSpacing(0)
        
        self.header_top = QWidget()
        self.header_top.setFixedHeight(WIDGETS_HEADER_HEIGHT)
        self.header_top.setStyleSheet(f"background: {HEADER_BG};")
        top_layout = QHBoxLayout(self.header_top)
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)
        
        # 4 phím chức năng bên trái: Khai báo, Kết nối, Chấm công, Công cụ
        button_names = ["Khai báo", "Kết nối", "Chấm công", "Công cụ"]
        button_keys = ["khai_bao", "ket_noi", "cham_cong", "cong_cu"]
        self.function_buttons = []
        self.active_button_key = None
        
        for idx, (name, key) in enumerate(zip(button_names, button_keys)):
            btn = QPushButton(name)
            btn.setFixedSize(WIDTH_FUNCTION_HEADER, HEIGHT_FUNCTION_HEADER)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setProperty("button_key", key)
            
            # Style mặc định + hover + active
            btn.setStyleSheet(
                f"QPushButton {{ font-weight: {FONT_BOLD}; color: {COLOR_TEXT}; background: transparent; border: none; }}"
                f"QPushButton:hover {{ background: {HOVER_COLOR}; color: {COLOR_1_TEXT}; }}"
                f"QPushButton[active='true'] {{ background: {HOVER_COLOR}; color: {COLOR_1_TEXT}; }}"
            )
            
            # Kết nối sự kiện click
            btn.clicked.connect(lambda checked, k=key: self._on_function_button_clicked(k))
            
            top_layout.addWidget(btn)
            self.function_buttons.append(btn)
        
        # Spacer để đẩy các phím chức năng sang trái
        top_layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Border line cho phần trên
        top_border = QWidget()
        top_border.setFixedHeight(1)
        top_border.setStyleSheet("background: #444;")
        
        top_container_layout.addWidget(self.header_top)
        top_container_layout.addWidget(top_border)
        main_layout.addWidget(top_container)
        
        # Phần dưới: Header main (hiển thị các nút chức năng chi tiết)
        bottom_container = QWidget(self)
        bottom_container_layout = QVBoxLayout(bottom_container)
        bottom_container_layout.setContentsMargins(0, 0, 0, 0)
        bottom_container_layout.setSpacing(0)
        
        self.header_bottom = QWidget()
        self.header_bottom.setFixedHeight(WIDGETS_MAIN_HEIGHT)
        self.header_bottom.setStyleSheet(f"background: transparent;")
        self.bottom_layout = QHBoxLayout(self.header_bottom)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.addStretch()
        
        # Border line cho phần dưới
        bottom_border = QWidget()
        bottom_border.setFixedHeight(1)
        bottom_border.setStyleSheet("background: #444;")
        
        bottom_container_layout.addWidget(self.header_bottom)
        bottom_container_layout.addWidget(bottom_border)
        main_layout.addWidget(bottom_container)
        
        # Hiển thị nhóm đầu tiên mặc định
        self._on_function_button_clicked("khai_bao")
    
    def _on_function_button_clicked(self, button_key):
        """Xử lý khi click vào một trong 4 nút chức năng chính"""
        # Cập nhật trạng thái active cho các nút
        for btn in self.function_buttons:
            if btn.property("button_key") == button_key:
                btn.setProperty("active", "true")
            else:
                btn.setProperty("active", "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)
        
        self.active_button_key = button_key
        
        # Xóa các nút cũ trong phần dưới
        self._clear_bottom_layout()
        
        # Hiển thị nhóm nút tương ứng
        if button_key in self._main_button_groups:
            self._display_button_group(button_key)
    
    def _clear_bottom_layout(self):
        """Xóa tất cả widget trong bottom layout"""
        while self.bottom_layout.count():
            item = self.bottom_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                pass
            
        # Hàm tạo tuple (text, tooltip)
        def btn(text, tooltip=None):
            return (text, tooltip if tooltip else text)
        
        # Khai báo các nhóm nút chức năng cho phần dưới
        self._main_button_groups = {
            "khai_bao": [
                ("company", IMG_COMPANY, *btn("Thông tin công ty")),
                ("job_title", IMG_JOB_TITLE, *btn("Khai báo chức danh")),
                ("department", IMG_DEPARTMENT, *btn("Khai báo phòng ban")),
                ("employee", IMG_EMPLOYEE, *btn("Thông tin nhân viên")),
                ("holiday", IMG_HOLIDAY, *btn("Khai báo ngày lễ")),
                ("password", IMG_PASSWORD, *btn("Đổi mật khẩu", "Đổi mật khẩu đăng nhập")),
                ("exit", IMG_EXIT, *btn("Thoát ứng dụng")),
            ],
            "ket_noi": [
                ("device", IMG_DEVICE, *btn("Máy chấm công", "Quản lý máy chấm công")),
                ("download_attendance", IMG_DOWNLOAD_ATTENDANCE, *btn("Tải máy chấm công", "Tải dữ liệu từ máy chấm công")),
                ("download_staff", IMG_DOWNLOAD_STAFF, *btn("Tải nhân viên về máy tính", "Tải nhân viên từ máy chấm công về máy tính")),
                ("upload_staff", IMG_UPLOAD_STAFF, *btn("Tải nhân viên lên máy chấm công")),
            ],
            "cham_cong": [
                ("arrange_schedule", IMG_ARRANGE_SCHEDULE, *btn("Sắp xếp lịch làm việc")),
                ("attendance_symbol", IMG_ATTENDANCE_SYMBOL, *btn("Các ký hiệu chấm công")),
                ("absence_symbol", IMG_ABSENCE_SYMBOL, *btn("Ký hiệu các loại vắng")),
                ("weekend", IMG_WEEKEND, *btn("Chọn ngày cuối tuần")),
            ],
            "cong_cu": [
                ("backup", IMG_BACKUP, *btn("Sao lưu dữ liệu")),
                ("absence_restore", IMG_ABSENCE_RESTORE, *btn("Khôi phục dữ liệu")),
            ],
        }
        
    def _display_button_group(self, group_key):
        """Hiển thị nhóm nút chức năng trong phần dưới"""
        buttons_data = self._main_button_groups[group_key]
        
        for btn_data in buttons_data:
            btn_id, img_path, text, tooltip = btn_data
            
            # Tạo widget container cho mỗi nút
            btn_container = QWidget()
            btn_container.setFixedSize(100, 110)
            btn_container.setCursor(Qt.PointingHandCursor)
            btn_container.setToolTip(tooltip)
            btn_container.setStyleSheet(
                f"QWidget {{ background: transparent; }}"
                f"QWidget:hover {{ background: {HOVER_COLOR}; }}"
            )
            btn_container.setProperty("btn_id", btn_id)
            
            # Kết nối sự kiện click cho tất cả nút
            btn_container.mousePressEvent = lambda event, bid=btn_id: self._on_button_clicked(bid)
            
            # Layout dọc cho icon và text
            btn_layout = QVBoxLayout(btn_container)
            btn_layout.setContentsMargins(0, 20, 0, 10)
            btn_layout.setSpacing(5)
            btn_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            
            # Icon - container cố định
            icon_container = QWidget()
            icon_container.setFixedHeight(45)
            icon_container.setStyleSheet("background: transparent;")
            icon_layout = QVBoxLayout(icon_container)
            icon_layout.setContentsMargins(0, 0, 0, 0)
            icon_layout.setSpacing(0)
            icon_layout.setAlignment(Qt.AlignCenter)
            
            icon_label = QLabel()
            pixmap = QPixmap(img_path)
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_label.setPixmap(scaled_pixmap)
            icon_label.setAlignment(Qt.AlignCenter)
            icon_label.setStyleSheet("background: transparent;")
            icon_layout.addWidget(icon_label)
            
            btn_layout.addWidget(icon_container)
            
            # Text container - cố định chiều cao và căn text từ trên xuống
            text_container = QWidget()
            text_container.setFixedSize(90, 45)
            text_container.setStyleSheet("background: transparent;")
            text_layout = QVBoxLayout(text_container)
            text_layout.setContentsMargins(0, 0, 0, 0)
            text_layout.setSpacing(0)
            text_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            
            text_label = QLabel(text)
            text_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            text_label.setWordWrap(True)
            text_label.setStyleSheet(f"""
                QLabel {{
                    color: {COLOR_TEXT}; 
                    font-size: 11px; 
                    background: transparent;
                    qproperty-alignment: 'AlignTop | AlignHCenter';
                }}
            """)
            text_label.setFixedWidth(90)
            text_layout.addWidget(text_label)
            text_layout.addStretch()
            
            btn_layout.addWidget(text_container)
            
            self.bottom_layout.addWidget(btn_container)
        
        # Thêm spacer cuối
        self.bottom_layout.addStretch()
    
    def _on_button_clicked(self, btn_id):
        """Xử lý khi click vào các nút trong phần dưới"""
        if btn_id == "exit":
            QApplication.quit()
        elif btn_id == "company":
            try:
                from ui.popup_company import PopupCompany
            except ImportError:
                return
            parent_window = self.window()
            popup = PopupCompany(parent=parent_window)
            # Đặt popup ra giữa cửa sổ chính
            if parent_window:
                geo = parent_window.geometry()
                popup.move(
                    geo.x() + (geo.width() - popup.width()) // 2,
                    geo.y() + (geo.height() - popup.height()) // 2
                )
            popup.exec()
    
    def resizeEvent(self, event):
        """Không cần xử lý bg vì đã chia widget riêng biệt"""
        super().resizeEvent(event)