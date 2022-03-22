def F(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return F(n // 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(n - 3) + 3


for i in range(0, 1000000):
    if F(i) == 31:
        print(i)
        break
