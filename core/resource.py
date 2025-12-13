# =======================================================
# File: resource.py
# Mô tả: Khai báo biến dùng chung cho UI: màu sắc, font, kích thước, icon, images
# =======================================================
# Biến cấu hình UI (theo .copilot_instructions)
VERSION = "1.0.0"
LAST_UPDATE = "2025-12-13"  # Ngày cập nhật cuối cùng
HEADER_HEIGHT = "120px"
FOOTER_WEIGHT = "30px"
MAIN_HEIGHT = "calc(100% - HEADER_HEIGHT - FOOTER_WEIGHT)"
HEADER_MAIN_1_HEIGHT = "40px"
HEADER_MAIN_2_HEIGHT = "35px"
HEADER_MAIN_3_HEIGHT = "30px"
HEADER_MAIN_4_HEIGHT = "25px"
MAIN_CONTENT_HEIGHT = "calc(100% - HEADER_MAIN_1_HEIGHT - HEADER_MAIN_2_HEIGHT - HEADER_MAIN_3_HEIGHT - HEADER_MAIN_4_HEIGHT)"
MIN_MAINWINDOW_WIDTH = 960
MIN_MAINWINDOW_HEIGHT = 540
MIN_POPUP_WIDTH = "auto"
MIN_POPUP_HEIGHT = "auto"
COMMON_PADDING = "10px"
COMMON_MARGIN = "10px"
COMMON_PADDING_10_0_10_0 = "10px 0px 10px 0px"
COMMON_MARGIN_10_0_10_0 = "10px 0px 10px 0px"
TABLE_ROW_HEIGHT = "30px"
TITLEBAR_HEIGHT = "40px"
POPUP_TITLE_FONT_SIZE = "18px"
POPUP_1_TITLE_BG_HEIGHT = "40px"
POPUP_2_TITLE_BG_HEIGHT = "50px"
HEADER_BG_COLOR = "#FFFFFF"
MAIN_BG_COLOR = "#FFFFFF"
FOOTER_BG_COLOR = "#a7a9ac"
HEADER_1_BG_COLOR = "#C9B59C"
HEADER_2_BG_COLOR = "#D9CFC7"
HEADER_3_BG_COLOR = "#EFE9E3"
HEADER_4_BG_COLOR = "#F9F8F6"
BOTTOM_BORDER_COLOR = "#a7a9ac"
TITLE_1_COLOR = "#5AB2FF"
TITLE_2_COLOR = "#A0DEFF"
TITLE_3_COLOR = "#CAF4FF"
TITLE_4_COLOR = "#939598"
TITLE_5_COLOR = "#e6e7e8"
BUTTON_1_COLOR = "#0046FF"
BUTTON_2_COLOR = "#DCDCDC"
BUTTON_1_DISABLED_COLOR = "#a7a9ac"
BUTTON_1_HOVER_COLOR = "#0046FF"
BUTTON_2_HOVER_COLOR = "#8CA9FF"
TEXT_1_COLOR = "#000000"
TEXT_2_COLOR = "#BF092F"
TEXT_3_COLOR = "#FFFFFF"
TEXT_4_COLOR = "#0046FF"
UI_FONT = "Segoe UI, Inter, Roboto"
TITLE_FONT = "18px"
CONTENT_FONT = "13px"
BUTTON_FONT = "14px"
TABLE_FONT = "13px"
ROW_SPACING = "6px"
FONT_WEIGHT_NORMAL = 400
FONT_WEIGHT_BOLD = 600
FONT_WEIGHT_SEMIBOLD = 500

# =======================================================
# Đường dẫn icon và ảnh (dùng resource_path)
import os
from typing import Dict


def resource_path(relative_path: str) -> str:
    """
    Mô tả: Trả về đường dẫn tuyệt đối đến tài nguyên, hỗ trợ khi build exe.
    Args:
            relative_path (str): Đường dẫn tương đối đến file tài nguyên.
    Returns:
            str: Đường dẫn tuyệt đối.
    """
    import sys

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", relative_path)


# =============================
# Quản lý icon ứng dụng động
# =============================
_ICON_APP_PATH = resource_path("assets/icons/app_icon.png")


def get_app_icon() -> str:
    """
    Mô tả: Lấy đường dẫn icon ứng dụng hiện tại.
    Returns:
        str: Đường dẫn icon app hiện tại.
    """
    return _ICON_APP_PATH


def set_app_icon(relative_path: str) -> None:
    """
    Mô tả: Cập nhật icon ứng dụng toàn cục.
    Args:
        relative_path (str): Đường dẫn tương đối icon mới.
    Returns:
        None
    """
    global _ICON_APP_PATH
    _ICON_APP_PATH = resource_path(relative_path)


# Backward compatible alias
ICON_APP = get_app_icon()

# =============================
# Quản lý đường dẫn database app.db động
# =============================
_APP_DB_PATH = resource_path("data/app.db")


def get_app_db_path() -> str:
    """
    Mô tả: Lấy đường dẫn file database app.db hiện tại.
    Returns:
        str: Đường dẫn file app.db hiện tại.
    """
    return _APP_DB_PATH


def set_app_db_path(relative_path: str) -> None:
    """
    Mô tả: Cập nhật đường dẫn file database app.db toàn cục.
    Args:
        relative_path (str): Đường dẫn tương đối file app.db mới.
    Returns:
        None
    """
    global _APP_DB_PATH
    _APP_DB_PATH = resource_path(relative_path)


# Backward compatible alias
APP_DB_PATH = get_app_db_path()

# Ảnh/Icons trong assets/images
IMAGES: Dict[str, str] = {
    "absence_restore": resource_path("assets/images/absence_restore.png"),
    "absence_symbol": resource_path("assets/images/absence_symbol.png"),
    "add": resource_path("assets/images/add.png"),
    "arrange_schedule": resource_path("assets/images/arrange_schedule.png"),
    "attendance_symbol": resource_path("assets/images/attendance_symbol.png"),
    "backup": resource_path("assets/images/backup.png"),
    "company": resource_path("assets/images/company.png"),
    "delete": resource_path("assets/images/delete.png"),
    "department": resource_path("assets/images/department.png"),
    "device": resource_path("assets/images/device.png"),
    "download_attendance": resource_path("assets/images/download_attendance.png"),
    "download_staff": resource_path("assets/images/download_staff.png"),
    "dropdown": resource_path("assets/images/dropdown.png"),
    "edit": resource_path("assets/images/Edit.png"),
    "employee": resource_path("assets/images/employee.png"),
    "excel": resource_path("assets/images/excel.png"),
    "exit": resource_path("assets/images/exit.png"),
    "holiday": resource_path("assets/images/holiday.png"),
    "input_staff_name": resource_path("assets/images/input_staff_name.png"),
    "job_title": resource_path("assets/images/job_title.png"),
    "login": resource_path("assets/images/login.png"),
    "logo": resource_path("assets/images/logo.png"),
    "non_shift_attendance": resource_path("assets/images/non_shift_attendance.png"),
    "password": resource_path("assets/images/password.png"),
    "schedule": resource_path("assets/images/schedule.png"),
    "shift": resource_path("assets/images/shift.png"),
    "shift_attendance": resource_path("assets/images/shift_attendance.png"),
    "staff": resource_path("assets/images/staff.png"),
    "total": resource_path("assets/images/total.png"),
    "upload_staff": resource_path("assets/images/upload_staff.png"),
    "weekend": resource_path("assets/images/weekend.png"),
}
