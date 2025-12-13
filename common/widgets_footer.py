
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import QTimer, QDateTime
from core.resource import FOOTER_HEIGHT, FOOTER_BG, COLOR_TEXT, FONT_BOLD

class FooterWidget(QWidget):
	"""
	Widget footer dùng chung cho toàn bộ ứng dụng.
	Tách riêng background và nội dung.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		# Thiết lập chiều cao cố định cho footer
		self.setFixedHeight(FOOTER_HEIGHT)

		# Widget nền (background)
		self.bg = QWidget(self)
		self.bg.setStyleSheet(f"background: {FOOTER_BG};")
		self.bg.setGeometry(0, 0, self.width(), self.height())
		self.bg.lower()  # Đảm bảo bg nằm dưới nội dung

		# Layout cho nội dung footer
		layout = QHBoxLayout(self)
		layout.setContentsMargins(20, 0, 20, 0)
		layout.setSpacing(0)


		# Label thời gian thực (bên trái)
		self.time_label = QLabel()
		self.time_label.setStyleSheet(f"color: {COLOR_TEXT}; font-size: 12px; font-weight: {FONT_BOLD};")
		layout.addWidget(self.time_label)

		# Spacer để đẩy label bản quyền sang phải
		from PySide6.QtWidgets import QSpacerItem, QSizePolicy
		layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))

		# Label bản quyền (bên phải)
		self.label = QLabel("© 2025 Công ty ABC")
		self.label.setStyleSheet(f"color: {COLOR_TEXT}; font-size: 12px; font-weight: {FONT_BOLD};")
		layout.addWidget(self.label)

		# Timer cập nhật thời gian mỗi giây
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_time)
		self.timer.start(1000)
		self.update_time()

	def update_time(self):
		"""
		Cập nhật label thời gian thực với thứ, ngày, tháng, năm, giờ, phút, giây (thứ tiếng Việt)
		"""
		thu_vn = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]
		now = QDateTime.currentDateTime()
		weekday = thu_vn[now.date().dayOfWeek() % 7]
		time_str = now.toString("dd/MM/yyyy Giờ: HH:mm:ss")
		self.time_label.setText(f"{weekday}, {time_str}")

	def resizeEvent(self, event):
		# Đảm bảo bg luôn phủ kín khi resize
		self.bg.setGeometry(0, 0, self.width(), self.height())
		super().resizeEvent(event)
