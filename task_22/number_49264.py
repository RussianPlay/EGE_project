mx_num = 0

for i in range(1, 1000):
    x = i
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    if a == 2 and b == 6 and len(str(i)) == 3:
        mx_num = max(mx_num, i)

print(mx_num)
