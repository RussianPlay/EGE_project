def calc(n, lst):
    global k
    if n == 5 and 43 in lst:
        k += 1
    elif n > 5:
        return calc(n - 8, lst + [n - 8]) or calc(n // 2, lst + [n // 2])


k = 0
calc(102, [])
print(k)