def F(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif n <= 30 and n % 2 == 0:
        return F(n + 1) + 3 * F(n + 4)
    elif n <= 30 and n % 2 != 0:
        return 2 * F(n + 2) + F(n + 5)


k = 0
for i in range(1, 1001):
    if sum(map(int, str(F(i)))) == 27:
        k += 1
print(k)