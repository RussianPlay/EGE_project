def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1 and n % 2 == 0:
        return F(n - 1) - F(n - 2) + 3 * n
    if n > 1 and n % 2 != 0:
        return F(n - 2) - F(n - 3) + 2 * n


print(F(40))