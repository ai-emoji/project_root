"""
Mô tả:
        Chứa các hàm truy vấn SQL trực tiếp với bảng "item".
        Chỉ chứa truy vấn SQL thô, không chứa logic nghiệp vụ.
        Mọi truy vấn đều dùng context manager, query parameter, không nối chuỗi.
"""

from typing import List, Dict, Any, Optional
from core.database import connect


def insert_item(data: Dict[str, Any]) -> int:
    """
    Mô tả: Thêm mới một bản ghi vào bảng item.
    Args:
            data (dict): Dữ liệu item (key: tên cột, value: giá trị).
    Returns:
            int: ID bản ghi vừa thêm.
    """
    with connect() as conn:
        cursor = conn.execute(
            """
			INSERT INTO item (name, description, created_at)
			VALUES (?, ?, ?)
			""",
            (data["name"], data["description"], data["created_at"]),
        )
        return cursor.lastrowid


def update_item(item_id: int, data: Dict[str, Any]) -> int:
    """
    Mô tả: Cập nhật bản ghi item theo ID.
    Args:
            item_id (int): ID item.
            data (dict): Dữ liệu cập nhật.
    Returns:
            int: Số dòng bị ảnh hưởng.
    """
    with connect() as conn:
        cursor = conn.execute(
            """
			UPDATE item SET name = ?, description = ?, created_at = ?
			WHERE id = ?
			""",
            (data["name"], data["description"], data["created_at"], item_id),
        )
        return cursor.rowcount


def delete_item(item_id: int) -> int:
    """
    Mô tả: Xóa bản ghi item theo ID.
    Args:
            item_id (int): ID item.
    Returns:
            int: Số dòng bị xóa.
    """
    with connect() as conn:
        cursor = conn.execute("DELETE FROM item WHERE id = ?", (item_id,))
        return cursor.rowcount


def get_item_by_id(item_id: int) -> Optional[Dict[str, Any]]:
    """
    Mô tả: Lấy thông tin item theo ID.
    Args:
            item_id (int): ID item.
    Returns:
            dict | None: Thông tin item hoặc None nếu không tồn tại.
    """
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM item WHERE id = ?", (item_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def get_all_items() -> List[Dict[str, Any]]:
    """
    Mô tả: Lấy toàn bộ danh sách item.
    Returns:
            list[dict]: Danh sách item.
    """
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM item ORDER BY id DESC")
        return [dict(row) for row in cursor.fetchall()]


def search_items(keyword: str) -> List[Dict[str, Any]]:
    """
    Mô tả: Tìm kiếm item theo tên hoặc mô tả.
    Args:
            keyword (str): Từ khóa tìm kiếm.
    Returns:
            list[dict]: Danh sách item phù hợp.
    """
    with connect() as conn:
        cursor = conn.execute(
            "SELECT * FROM item WHERE name LIKE ? OR description LIKE ? ORDER BY id DESC",
            (f"%{keyword}%", f"%{keyword}%"),
        )
        return [dict(row) for row in cursor.fetchall()]
