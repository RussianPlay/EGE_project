k = 0
for i in range(-10000, 10000000):
    s = i
    n = 1
    print(s)
    while s < 45:
        s = s + 8
        n = n * 3
    if n == 243:
        k += 1

print(k)