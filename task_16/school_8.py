def F(n):
    if n == 1:
        return 2
    elif n % 2 == 0:
        return 2 * n + F(n - 3)
    elif n > 1 and n % 2 != 0:
        return 2 * F(n + 1)


print(F(21))
