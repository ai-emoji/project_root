# Khai báo biến dùng chung cho UI: màu sắc, font, kích thước, icon, images
# Tất cả comment, docstring đều bằng tiếng Việt

# =============================
# Thông số UI bắt buộc
# =============================
MIN_MAINWINDOW_WIDTH: int = 960
MIN_MAINWINDOW_HEIGHT: int = 540
HEADER_HEIGHT: int = 140
MAIN_HEIGHT: int = 370
FOOTER_HEIGHT: int = 30


# wedget header
WIDGETS_HEADER_WIDTH: int = 960
WIDGETS_HEADER_HEIGHT: int = 30
WIDGETS_MAIN_HEIGHT: int = 110
WIDGETS_HEADER_BG: str = "#EEEEEE"
WIDGETS_MAIN_BG: str = "#EEEEEE"
WIDTH_FUNCTION_HEADER: int = 100
HEIGHT_FUNCTION_HEADER: int = 30
WIDTH_FUNCTION_MAIN: int = 100
HEIGHT_FUNCTION_MAIN: int = 110

# wedget job title
JOB_TITLE_MIN_WIDTH: int = 960
JOB_TITLE_MIN_HEIGHT: int = 370
JOB_TITLE_MIN_HEIGHT_1: int = 40
JOB_TITLE_MIN_HEIGHT_2: int = 40
JOB_TITLE_MIN_HEIGHT_3: int = 290
JOB_TITLE_BG_1: str = "#FFFFFF"
JOB_TITLE_BG_2: str = "#F5F5F5"
JOB_TITLE_BG_3: str = "#FFFFFF"


# Font
UI_FONT: str = "Segoe UI, Inter, Roboto"
TITLE_FONT_SIZE: int = 18
CONTENT_FONT_SIZE: int = 13
BUTTON_FONT_SIZE: int = 14
TABLE_FONT_SIZE: int = 13
ROW_SPACING: int = 6
FONT_NORMAL: int = 400
FONT_BOLD: int = 600
FONT_SEMIBOLD: int = 500

# Màu sắc (ví dụ, có thể chỉnh sửa lại cho phù hợp dự án)
COLOR_PRIMARY: str = "#1976D2"
COLOR_SECONDARY: str = "#424242"
COLOR_BACKGROUND: str = "#F5F5F5"
COLOR_TEXT: str = "#000000"
COLOR_1_TEXT: str = "#FFFFFF"
COLOR_ERROR: str = "#D32F2F"
FOOTER_BG: str = "#CBCBCB"
HEADER_BG: str = "#EEEEEE"
BUTTON_COLOR: str = "#1976D2"
# =============================
HOVER_COLOR: str = "#1976D2"
ACTIVE_COLOR: str = "#1976D2"

# Đường dẫn icon, ảnh (dùng resource_path để load)
import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Lấy đường dẫn tuyệt đối đến tài nguyên (icon, ảnh, db,...) tương thích khi build exe.
    Args:
            relative_path (str): Đường dẫn tương đối đến file tài nguyên
    Returns:
            str: Đường dẫn tuyệt đối
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Đường dẫn mẫu
ICON_PATH: str = resource_path("assets/icons/")
IMAGE_PATH: str = resource_path("assets/images/")

# Đường dẫn database, cho phép thay đổi khi người dùng cập nhật

# Đường dẫn database, cho phép thay đổi khi người dùng cập nhật
DB_PATH: str = resource_path("data/app.db")


def set_db_path(new_path: str) -> None:
    """
    Cập nhật đường dẫn database động khi người dùng chọn file khác.
    Args:
            new_path (str): Đường dẫn tuyệt đối hoặc tương đối tới file database mới
    """
    global DB_PATH
    DB_PATH = new_path


# Đường dẫn icon ứng dụng, cho phép thay đổi khi người dùng cập nhật

# Đường dẫn icon ứng dụng, cho phép thay đổi khi người dùng cập nhật
APP_ICON_PATH: str = resource_path("assets/icons/app_icon.png")


def set_app_icon_path(new_path: str) -> None:
    """
    Cập nhật đường dẫn icon ứng dụng động khi người dùng chọn file khác.
    Args:
        new_path (str): Đường dẫn tuyệt đối hoặc tương đối tới file icon mới
    """
    global APP_ICON_PATH
    APP_ICON_PATH = new_path


# Đường dẫn ảnh trong assets/images
IMG_ABSENCE_RESTORE = resource_path("assets/images/absence_restore.png")
IMG_ABSENCE_SYMBOL = resource_path("assets/images/absence_symbol.png")
IMG_ADD = resource_path("assets/images/add.png")
IMG_ARRANGE_SCHEDULE = resource_path("assets/images/arrange_schedule.png")
IMG_ATTENDANCE_SYMBOL = resource_path("assets/images/attendance_symbol.png")
IMG_BACKUP = resource_path("assets/images/backup.png")
IMG_COMPANY = resource_path("assets/images/company.png")
IMG_DELETE = resource_path("assets/images/delete.png")
IMG_DEPARTMENT = resource_path("assets/images/department.png")
IMG_DEVICE = resource_path("assets/images/device.png")
IMG_DOWNLOAD_ATTENDANCE = resource_path("assets/images/download_attendance.png")
IMG_DOWNLOAD_STAFF = resource_path("assets/images/download_staff.png")
IMG_DROPDOWN = resource_path("assets/images/dropdown.png")
IMG_EDIT = resource_path("assets/images/Edit.png")
IMG_EMPLOYEE = resource_path("assets/images/employee.png")
IMG_EXCEL = resource_path("assets/images/excel.png")
IMG_EXIT = resource_path("assets/images/exit.png")
IMG_HOLIDAY = resource_path("assets/images/holiday.png")
IMG_INPUT_STAFF_NAME = resource_path("assets/images/input_staff_name.png")
IMG_JOB_TITLE = resource_path("assets/images/job_title.png")
IMG_LOGIN = resource_path("assets/images/login.png")
IMG_LOGO = resource_path("assets/images/logo.png")
IMG_NON_SHIFT_ATTENDANCE = resource_path("assets/images/non_shift_attendance.png")
IMG_PASSWORD = resource_path("assets/images/password.png")
IMG_SCHEDULE = resource_path("assets/images/schedule.png")
IMG_SHIFT = resource_path("assets/images/shift.png")
IMG_SHIFT_ATTENDANCE = resource_path("assets/images/shift_attendance.png")
IMG_STAFF = resource_path("assets/images/staff.png")
IMG_TOTAL = resource_path("assets/images/total.png")
IMG_UPLOAD_STAFF = resource_path("assets/images/upload_staff.png")
IMG_WEEKEND = resource_path("assets/images/weekend.png")
