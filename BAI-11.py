lst = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
count = 0

for x in lst:
    if len(x) >= 4 and x[0] == x[-1]:
        count += 1

print(count)