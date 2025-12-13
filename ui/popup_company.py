from PySide6.QtCore import Qt
# popup_company.py
# Popup thông tin công ty - Cửa sổ trống, setup chuẩn resource.py
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from core.resource import UI_FONT, COLOR_TEXT, COLOR_BACKGROUND, APP_ICON_PATH

class PopupCompany(QDialog):

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Thông tin công ty")
		self.setMinimumWidth(400)
		self.setMinimumHeight(300)
		self.setStyleSheet(f"background: {COLOR_BACKGROUND}; color: {COLOR_TEXT}; font-family: {UI_FONT};")
		self.setWindowIcon(QIcon(APP_ICON_PATH))

		# Chỉ còn một trường duy nhất: Tên công ty
		from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit
		from core.resource import CONTENT_FONT_SIZE, FONT_BOLD, BUTTON_COLOR
		layout = QVBoxLayout(self)
		layout.setContentsMargins(20 , 20, 20, 20)
		layout.setSpacing(12)
		layout.setAlignment(Qt.AlignTop)  # Đảm bảo các group hiển thị từ trên xuống

		# Nhóm label và input thành 1 khối
		from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
		# --- Nhóm Tên công ty ---
		name_group = QWidget()
		name_group.setFixedHeight(70)
		name_group_layout = QHBoxLayout(name_group)
		name_group_layout.setContentsMargins(0, 0, 0, 0)
		name_group_layout.setSpacing(0)

		name_inner = QWidget()
		name_layout = QVBoxLayout(name_inner)
		name_layout.setSpacing(5)
		name_layout.setContentsMargins(0, 0, 0, 0)

		label_name = QLabel("Tên công ty")
		label_name.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; font-weight: {FONT_BOLD}; color: {COLOR_TEXT}; font-family: {UI_FONT};")
		name_layout.addWidget(label_name)
		self.edit_name = QLineEdit()
		self.edit_name.setPlaceholderText("Nhập tên công ty...")
		self.edit_name.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; color: {COLOR_TEXT}; font-family: {UI_FONT}; padding: 8px 12px;")
		self.edit_name.setMaximumWidth(16777215)
		self.edit_name.setMinimumWidth(0)
		name_layout.addWidget(self.edit_name)
		name_layout.setContentsMargins(0, 0, 0, 0)
		name_group_layout.addWidget(name_inner, stretch=1)
		layout.addWidget(name_group)

		# --- Nhóm Địa chỉ ---
		address_group = QWidget()
		address_group.setFixedHeight(70)
		address_group_layout = QHBoxLayout(address_group)
		address_group_layout.setContentsMargins(0, 0, 0, 0)
		address_group_layout.setSpacing(0)

		address_inner = QWidget()
		address_layout = QVBoxLayout(address_inner)
		address_layout.setSpacing(5)
		address_layout.setContentsMargins(0, 0, 0, 0)

		label_address = QLabel("Địa chỉ")
		label_address.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; font-weight: {FONT_BOLD}; color: {COLOR_TEXT}; font-family: {UI_FONT};")
		address_layout.addWidget(label_address)
		self.edit_address = QLineEdit()
		self.edit_address.setPlaceholderText("Nhập địa chỉ...")
		self.edit_address.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; color: {COLOR_TEXT}; font-family: {UI_FONT}; padding: 8px 12px;")
		self.edit_address.setMaximumWidth(16777215)
		self.edit_address.setMinimumWidth(0)
		address_layout.addWidget(self.edit_address)
		address_layout.setContentsMargins(0, 0, 0, 0)
		address_group_layout.addWidget(address_inner, stretch=1)
		layout.addWidget(address_group)

		# --- Nhóm Số điện thoại ---
		phone_group = QWidget()
		phone_group.setFixedHeight(70)
		phone_group_layout = QHBoxLayout(phone_group)
		phone_group_layout.setContentsMargins(0, 0, 0, 0)
		phone_group_layout.setSpacing(0)

		phone_inner = QWidget()
		phone_layout = QVBoxLayout(phone_inner)
		phone_layout.setSpacing(5)
		phone_layout.setContentsMargins(0, 0, 0, 0)

		label_phone = QLabel("Số điện thoại")
		label_phone.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; font-weight: {FONT_BOLD}; color: {COLOR_TEXT}; font-family: {UI_FONT};")
		phone_layout.addWidget(label_phone)
		self.edit_phone = QLineEdit()
		self.edit_phone.setPlaceholderText("Nhập số điện thoại...")
		self.edit_phone.setStyleSheet(f"font-size: {CONTENT_FONT_SIZE}px; color: {COLOR_TEXT}; font-family: {UI_FONT}; padding: 8px 12px;")
		self.edit_phone.setMaximumWidth(16777215)
		self.edit_phone.setMinimumWidth(0)
		phone_layout.addWidget(self.edit_phone)
		phone_layout.setContentsMargins(0, 0, 0, 0)
		phone_group_layout.addWidget(phone_inner, stretch=1)
		layout.addWidget(phone_group)
		# --- Nhóm mới bên dưới các input ---
		from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem
		extra_group = QWidget()
		extra_group.setMinimumWidth(400)
		extra_group.setFixedHeight(120)
		extra_group_layout = QHBoxLayout(extra_group)
		extra_group_layout.setContentsMargins(0, 0, 0, 0)
		extra_group_layout.setSpacing(12)

		# Bên trái: ô vuông 100x100
		self.avatar_label = QLabel()
		self.avatar_label.setFixedSize(100, 100)
		self.avatar_label.setStyleSheet("background: #e0e0e0; border: 1px solid #ccc; border-radius: 4px;")
		self.avatar_label.setAlignment(Qt.AlignCenter)
		extra_group_layout.addWidget(self.avatar_label)

		# Bên phải: cột dọc chứa nút thay đổi ảnh ở trên, 2 nút lưu/thoát bên dưới
		right_col = QWidget()
		right_col_layout = QVBoxLayout(right_col)
		right_col_layout.setContentsMargins(0, 10, 0, 10)
		right_col_layout.setSpacing(8)
		right_col_layout.setAlignment(Qt.AlignVCenter)

		self.btn_change_image = QPushButton("Thay đổi ảnh")
		self.btn_change_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		self.btn_change_image.setFixedHeight(40)
		self.btn_change_image.setStyleSheet(f"background: {BUTTON_COLOR}; color: white; border-radius: 4px; cursor: pointer;")
		right_col_layout.addWidget(self.btn_change_image)

		right_col_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

		self.btn_save_exit = QPushButton("Lưu & Thoát")
		self.btn_save_exit.setFixedHeight(40)
		self.btn_save_exit.setStyleSheet(f"background: {BUTTON_COLOR}; color: white; border-radius: 4px; cursor: pointer;")
		right_col_layout.addWidget(self.btn_save_exit)

		extra_group_layout.addWidget(right_col, stretch=1)
		layout.addWidget(extra_group)
