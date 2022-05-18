mx_num = -1
for i in range(48427574, 10 ** 10):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x % 9
        a *= d
        if d < 5:
            b += d
        x //= 9
    if a == 10:
        print(a, b)

    if a == 10 and b == 9:
        mx_num = max(mx_num, i)
        print(i)

print(mx_num)
