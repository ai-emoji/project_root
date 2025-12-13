# File main.py
# Điểm khởi động ứng dụng

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys

if __name__ == "__main__":
	# Khởi tạo ứng dụng PySide6
	app = QApplication(sys.argv)
	# Tạo cửa sổ chính
	window = MainWindow()
	window.show()
	# Chạy vòng lặp sự kiện
	sys.exit(app.exec())
