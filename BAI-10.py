lst = ["hello", "hi", "python", "code"]
n = int(input("Nhập n: "))

result = [x for x in lst if len(x) > n]
print(result)