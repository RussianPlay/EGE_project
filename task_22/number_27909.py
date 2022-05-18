k = 0
for i in range(-10000, 10000):
    x = i
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    if a == 3 and b == 0:
        k += 1

print(k)
