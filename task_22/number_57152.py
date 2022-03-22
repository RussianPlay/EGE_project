def calc():
    for i in range(-100000, 1000):
        x = i
        m = 0
        s = 0
        while x > 0:
            d = x % 6
            s += d
            if d > m: m = d
            x = x // 6
        if m == 3 and s == 10:
            return i


print(calc())