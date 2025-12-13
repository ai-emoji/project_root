

"""
Tạo bảng company nếu chưa tồn tại.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
from core.database import Database

def create_company_table():
	"""
	Tạo bảng company nếu chưa có.
	"""
	sql = '''
	CREATE TABLE IF NOT EXISTS company (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		address TEXT,
		phone TEXT
	);
	'''
	try:
		# Database.connect là generator, phải dùng next()
		conn_gen = Database.connect()
		conn = next(conn_gen)
		conn.execute(sql)
		conn.commit()
		try:
			next(conn_gen)
		except StopIteration:
			pass
		logging.info("Đã kiểm tra/tạo bảng company thành công.")
	except Exception as e:
		logging.error(f"Lỗi khi tạo bảng company: {e}")

if __name__ == "__main__":
	create_company_table()
