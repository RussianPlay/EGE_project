def calc():
    for i in range(-100000000, 10000):
        x = i
        a = 0; b = 0
        while x > 0:
            a = a + 1
            b = b + (x % 100)
            x = x // 100
        if a == 2 and b == 13:
            return i


print(calc())