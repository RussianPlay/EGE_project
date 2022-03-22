def F(n):
    if n < 2:
        return n
    elif n % 2 == 0 and n >= 2:
        return F(n / 2) + 1
    elif n % 2 != 0 and n >= 2:
        return F(n * 3 + 1) + 1

k = 0
for i in range(1, 101):
    if F(i) > 100:
        k += 1
print(k)