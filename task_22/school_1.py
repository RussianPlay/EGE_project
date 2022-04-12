def calc():
    for i in range(-1000, 1000):
        s = i
        P = 10
        Q = 8
        K1 = 0
        K2 = 0
        while s <= 100:
            s = s + P
            K1 = K1 + 1

        while s >= Q:
            s = s - Q
            K2 = K2 + 1
        K1 += s
        K2 += s

        if K1 == 10 and K2 == 19:
            return i


print(calc())
