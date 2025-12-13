# Repository thao tác dữ liệu bảng company
# Tuân thủ Clean Architecture, comment tiếng Việt
import sqlite3
from core.resource import DB_PATH


def get_company():
    """
    Lấy thông tin công ty (bản ghi đầu tiên).
    Returns: dict hoặc None
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, address, phone, tax_code, image_path FROM company LIMIT 1"
        )
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "name": row[1],
                "address": row[2],
                "phone": row[3],
                "tax_code": row[4],
                "image_path": row[5],
            }
        return None


def upsert_company(name, address, phone, tax_code, image_path):
    """
    Cập nhật hoặc thêm mới thông tin công ty (chỉ 1 bản ghi duy nhất).
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Kiểm tra đã có bản ghi chưa
        cursor.execute("SELECT id FROM company LIMIT 1")
        row = cursor.fetchone()
        if row:
            cursor.execute(
                """
                UPDATE company SET name=?, address=?, phone=?, tax_code=?, image_path=? WHERE id=?
                """,
                (name, address, phone, tax_code, image_path, row[0]),
            )
        else:
            cursor.execute(
                """
                INSERT INTO company (name, address, phone, tax_code, image_path) VALUES (?, ?, ?, ?, ?)
                """,
                (name, address, phone, tax_code, image_path),
            )
        conn.commit()
