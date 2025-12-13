# Tạo bảng SQLite cho module company
# Tuân thủ chuẩn Clean Architecture, comment tiếng Việt, không sinh code GUI tự động
import os
import sys
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.resource import APP_DB_PATH


def create_company_table():
    """
    Tạo bảng company nếu chưa tồn tại.
    Các trường:
            - id: INTEGER PRIMARY KEY AUTOINCREMENT
            - name: TEXT (tên công ty)
            - address: TEXT (địa chỉ)
            - phone: TEXT (số điện thoại)
            - tax_code: TEXT (mã số thuế)
            - image_path: TEXT (đường dẫn ảnh/logo)
    """
    with sqlite3.connect(APP_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
			CREATE TABLE IF NOT EXISTS company (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				address TEXT,
				phone TEXT,
				tax_code TEXT,
				image_path TEXT
			)
		"""
        )
        conn.commit()


# Tự động tạo bảng khi chạy trực tiếp file này
if __name__ == "__main__":
    create_company_table()
    print("Đã tạo bảng company (nếu chưa tồn tại)")
