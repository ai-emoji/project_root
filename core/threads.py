# Các lớp/hàm hỗ trợ chạy đa luồng, xử lý tác vụ nền an toàn
from PySide6.QtCore import QObject, Signal, QRunnable, QThreadPool, QThread
import traceback

class WorkerSignals(QObject):
	"""
	Tín hiệu cho worker thread: trả về kết quả, lỗi, trạng thái hoàn thành.
	"""
	finished = Signal()
	error = Signal(str)
	result = Signal(object)

class Worker(QRunnable):
	"""
	Worker chạy tác vụ nền trong QThreadPool.
	Args:
		fn (callable): Hàm cần thực thi
		*args, **kwargs: Tham số cho hàm
	"""
	def __init__(self, fn, *args, **kwargs):
		super().__init__()
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()

	def run(self):
		try:
			result = self.fn(*self.args, **self.kwargs)
			self.signals.result.emit(result)
		except Exception as e:
			tb = traceback.format_exc()
			self.signals.error.emit(tb)
		finally:
			self.signals.finished.emit()

def run_in_threadpool(fn, *args, **kwargs):
	"""
	Hàm tiện ích để chạy hàm trong QThreadPool.
	Args:
		fn (callable): Hàm cần thực thi
		*args, **kwargs: Tham số cho hàm
	Returns:
		Worker: Đối tượng worker đã submit vào threadpool
	"""
	worker = Worker(fn, *args, **kwargs)
	QThreadPool.globalInstance().start(worker)
	return worker
