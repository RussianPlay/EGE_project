def finding():
    for i in range(1, 10000):
        x = i
        a = 0
        b = 1
        while x > 0:
            if x % 2 > 0:
                a += x % 8
            else:
                b *= x % 8
            x = x // 8
        if a == 2 and b == 24:
            return i

print(finding())