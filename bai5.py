import math

# Nhập 3 hệ số a, b, c (sử dụng float để có thể nhập số thập phân)
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Nếu a = 0, bài toán trở thành giải phương trình bậc nhất bx + c = 0
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Vì a = 0 nên đây là phương trình bậc 1. Nghiệm là: x = {x}")
else:
    # Tính Delta
    delta = b**2 - 4*a*c
    
    # Biện luận theo Delta
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = {x}")
    else:
        # Sử dụng math.sqrt() để tính căn bậc 2 của delta
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")