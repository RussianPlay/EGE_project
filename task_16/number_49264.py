def F(n):
    global lst
    lst.append(n)
    if n > 0:
        d = n % 10 + F(n // 10)
        lst.append(d)
        return d
    else:
        return 0


for i in range(-10000000, 100000000):
    lst = []
    result = F(i)
    if lst[-1] > 32:
        print(i, result)
        break
