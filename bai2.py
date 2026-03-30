# Nhập vào 3 số nguyên dương
_a = int(input("Nhập số nguyên dương _a: "))
_b = int(input("Nhập số nguyên dương _b: "))
_c = int(input("Nhập số nguyên dương _c: "))

# Kiểm tra điều kiện bất đẳng thức tam giác
if (_a + _b > _c) and (_a + _c > _b) and (_b + _c > _a):
    print("Độ dài ba canh tam giác")
else:
    print("Đây không phải độ dài ba canh tam giác")