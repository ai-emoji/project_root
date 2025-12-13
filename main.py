"""
Mô tả:
        Điểm khởi động ứng dụng PySide6, thiết lập icon, khởi tạo MainWindow.
"""

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import sys
from core.resource import get_app_icon
from ui.main_window import MainWindow


def main() -> None:
    """
    Mô tả: Hàm main khởi động ứng dụng.
    Returns:
            None
    """
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(get_app_icon()))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
