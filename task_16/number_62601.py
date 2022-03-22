def F(n):
    if n == 0:
        return 0
    if n % 2 == 0 and 0 < n < 1000:
        return F(n // 2) - 1
    if n % 2 != 0 and 0 < n < 1000:
        return 2 + F(n - 1)


k = 0
for i in range(-100000, 100000):
    if F(i) == 3:
        k += 1
print(k)
