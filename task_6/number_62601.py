def calc():
    for i in range(-10000, 10000):
        d = i
        n = 3
        s = 57
        tmp = []
        check = 0
        while s <= 1200:
            tmp.append(s)
            s = s + d
            n = n + 4
            if len(tmp) >= 2:
                if tmp[-1] <= tmp[-2]:
                    check = 1
                    break

        if n == 63 and check == 0:
            return i


print(calc())
