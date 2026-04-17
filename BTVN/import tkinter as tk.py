import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Mặt hàng")
        self.root.geometry("800x500")

        # --- Khung nhập liệu ---
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Mã MH:").grid(row=0, column=0)
        self.ent_ma = tk.Entry(frame_input)
        self.ent_ma.grid(row=0, column=1)

        tk.Label(frame_input, text="Tên MH:").grid(row=0, column=2)
        self.ent_ten = tk.Entry(frame_input)
        self.ent_ten.grid(row=0, column=3)

        tk.Label(frame_input, text="Nguồn gốc:").grid(row=1, column=0)
        self.ent_nguon = tk.Entry(frame_input)
        self.ent_nguon.grid(row=1, column=1)

        # --- Các nút chức năng ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Thêm", command=self.add_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Xóa", command=self.delete_item).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Làm mới", command=self.load_data).pack(side=tk.LEFT, padx=5)

        # --- Bảng hiển thị danh sách (Treeview) ---
        self.tree = ttk.Treeview(self.root, columns=("Ma", "Ten", "Nguon", "Gia"), show='headings')
        self.tree.heading("Ma", text="Mã Mặt Hàng")
        self.tree.heading("Ten", text="Tên Mặt Hàng")
        self.tree.heading("Nguon", text="Nguồn Gốc")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_data()

    def load_data(self):
        """Hiển thị danh sách mặt hàng lên bảng"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM MatHang")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
        conn.close()

    def add_item(self):
        """Thêm mặt hàng mới"""
        ma = self.ent_ma.get()
        ten = self.ent_ten.get()
        nguon = self.ent_nguon.get()

        if ma and ten:
            try:
                conn = sqlite3.connect('quan_ly_ban_hang.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO MatHang (MaMH, TenMH, NguonGoc) VALUES (?, ?, ?)", (ma, ten, nguon))
                conn.commit()
                conn.close()
                self.load_data()
                messagebox.showinfo("Thành công", "Đã thêm mặt hàng!")
            except:
                messagebox.showerror("Lỗi", "Mã mặt hàng đã tồn tại!")
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đủ thông tin!")

    def delete_item(self):
        """Xóa mặt hàng đang chọn"""
        selected = self.tree.selection()
        if not selected:
            return
        
        item_id = self.tree.item(selected)['values'][0]
        conn = sqlite3.connect('quan_ly_ban_hang.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM MatHang WHERE MaMH=?", (item_id,))
        conn.commit()
        conn.close()
        self.load_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()