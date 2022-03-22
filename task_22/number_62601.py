def calc():
    for i in range(1, 1000000):
        x = i
        a = 0
        b = 1
        while x > 0:
            if x % 2 > 0:
                a = a + x % 13
            else:
                b = b * (x % 13)
            x = x // 13
        if a == 3 and b == 12:
            return i


print(calc())
