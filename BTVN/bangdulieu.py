import sqlite3

def setup_db():
    conn = sqlite3.connect('quan_ly_ban_hang.db')
    cursor = conn.cursor()
    # Tạo bảng Mặt hàng
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MatHang (
            MaMH TEXT PRIMARY KEY,
            TenMH TEXT,
            NguonGoc TEXT,
            DonGia REAL
        )
    ''')
    conn.commit()
    conn.close()

setup_db()