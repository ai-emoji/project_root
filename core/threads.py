"""
Mô tả:
        Cung cấp các lớp/hàm hỗ trợ chạy đa luồng, xử lý tác vụ nền an toàn với PySide6.
        Đảm bảo không update UI trực tiếp từ thread nền, chỉ emit signal về UI thread.
"""

from PySide6.QtCore import QThread, Signal, QObject


class WorkerSignals(QObject):
    """
    Mô tả: Định nghĩa các signal cho worker thread.
    """

    finished = Signal()
    error = Signal(str)
    result = Signal(object)


class DatabaseWorker(QThread):
    """
    Mô tả: QThread chạy truy vấn database nặng ở background, trả kết quả qua signal.
    Args:
            func (callable): Hàm thực thi tác vụ nền.
            *args, **kwargs: Tham số truyền vào hàm.
    Signals:
            result(object): Kết quả trả về.
            error(str): Lỗi nếu có.
            finished(): Kết thúc tác vụ.
    """

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self):
        try:
            res = self.func(*self.args, **self.kwargs)
            self.signals.result.emit(res)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()
