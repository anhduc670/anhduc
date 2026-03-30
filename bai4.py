# Nhập một số nguyên dương từ bàn phím
n = int(input("Nhập vào một số nguyên dương: "))

# Kiểm tra các trường hợp chia hết
if n % 2 == 0 and n % 3 == 0:
    print(f"Số {n} chia hết cho cả 2 và 3.")
elif n % 2 == 0:
    print(f"Số {n} chia hết cho 2 nhưng không chia hết cho 3.")
elif n % 3 == 0:
    print(f"Số {n} chia hết cho 3 nhưng không chia hết cho 2.")
else:
    print(f"Số {n} không chia hết cho 2 và cũng không chia hết cho 3.")