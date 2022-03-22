def F(n):
    if n < 2:
        return 1
    elif n >= 2 and n % 3 == 0:
        return F(n // 3) - 1
    elif n >= 2 and n % 3 != 3:
        return F(n - 1) + 7


k = 0
for i in range(1, 100001):
    if F(i) == 35:
        k += 1
print(k)
