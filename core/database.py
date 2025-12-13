"""
Mô tả:
        Quản lý kết nối SQLite, các hàm tạo/mở/đóng database, đảm bảo tuân thủ Clean Architecture.
        Sử dụng context manager, bật WAL, foreign_keys, không giữ connection lâu.
"""

import sqlite3
import logging
from contextlib import contextmanager
from core.resource import get_app_db_path


def get_connection() -> sqlite3.Connection:
    """
    Mô tả: Tạo kết nối SQLite với các PRAGMA cần thiết.
    Returns:
            sqlite3.Connection: Đối tượng kết nối SQLite.
    """
    db_path = get_app_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
    except Exception as e:
        logging.error(f"Lỗi khi thiết lập PRAGMA: {e}")
    return conn


@contextmanager
def connect():
    """
    Mô tả: Context manager để mở/đóng kết nối SQLite an toàn.
    Yêu cầu: Không giữ connection lâu, tự động đóng sau khi dùng.
    Yields:
            sqlite3.Connection: Đối tượng kết nối SQLite.
    """
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(f"Lỗi truy vấn DB: {e}")
        raise
    finally:
        conn.close()
