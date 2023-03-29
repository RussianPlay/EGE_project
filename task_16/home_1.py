def F(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 == 0:
        return 2 * F(n - 1) - F(n - 2)
    elif n > 2 and n % 2 != 0:
        return F(n - 1) - 2 * F(n - 2) - 3


print(F(15))
