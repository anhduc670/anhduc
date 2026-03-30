import time

# Nhập năm sinh từ bàn phím
nam_sinh = int(input("Nhập năm sinh của bạn: "))

# Lấy năm hiện tại theo gợi ý của đề bài
x = time.localtime()
year = x[0]

# Tính tuổi
tuoi = year - nam_sinh

# In ra kết quả
print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")