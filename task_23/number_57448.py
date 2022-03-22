def calculation(n, lst):
    global k
    if n < 65:
        return calculation(n + 1, lst + [n + 1]) or calculation(n * 3, lst + [n * 3])
    elif n == 65 and 20 in lst:
        k += 1


k = 0
n = 1
calculation(n, [])
print(k)