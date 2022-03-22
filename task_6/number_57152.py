def calc():
    k = 0
    for i in range(-100000, 10000):
        x = i
        s = 5 * (x // 10)
        n = 1
        while s < 300:
            s = s + 28
            n = n * 3
        if n == 243:
            k += 1
    return k


print(calc())