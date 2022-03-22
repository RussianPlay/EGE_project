def F(n):
    if n > 25:
        return 2 * n * n * n + 1
    elif n <= 25:
        return F(n + 2) + 2 * F(n + 3)


k = 0
for i in range(1, 1001):
    if F(i) % 11 == 0:
        k += 1
print(k)