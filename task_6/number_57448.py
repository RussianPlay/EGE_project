def calculation():
    for i in range(1, 100):
        x = i
        res = []
        is_inf = False
        while x < 100:
            if x % 2 < 1:
                x = x // 2
            else:
                x = 3*x + 1
            res.append(x)
            for num in res:
                if res.count(num) >= 2:
                    is_inf = True
            if is_inf:
                break
        if not is_inf:
            print(i)


print(calculation())