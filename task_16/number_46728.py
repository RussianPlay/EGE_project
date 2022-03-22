def F(n):
    if n <= 1:
        return 2
    else:
        return F(n - 1) + F(n - 2) + 4 * n


print(F(24))