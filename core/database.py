# Quản lý kết nối SQLite, các hàm tạo/mở/đóng database
from typing import Generator
import sqlite3
import logging
from core.resource import DB_PATH

class Database:
	"""
	Lớp quản lý kết nối và thao tác với SQLite database.
	"""
	@staticmethod
	def connect() -> Generator[sqlite3.Connection, None, None]:
		"""
		Mở kết nối tới database với các PRAGMA cần thiết.
		Returns:
			Generator[sqlite3.Connection, None, None]: Kết nối SQLite dùng context manager
		"""
		try:
			conn = sqlite3.connect(DB_PATH)
			conn.row_factory = sqlite3.Row
			conn.execute("PRAGMA journal_mode = WAL")
			conn.execute("PRAGMA foreign_keys = ON")
			yield conn
		except Exception as e:
			logging.error(f"Lỗi khi kết nối database: {e}")
			raise
		finally:
			try:
				conn.close()
			except:
				pass

	@staticmethod
	def create_tables(sql: str) -> None:
		"""
		Tạo bảng mới trong database.
		Args:
			sql (str): Câu lệnh SQL tạo bảng
		"""
		try:
			with Database.connect() as conn:
				conn.execute(sql)
				conn.commit()
		except Exception as e:
			logging.error(f"Lỗi khi tạo bảng: {e}")
			raise
