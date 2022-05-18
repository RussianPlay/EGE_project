def calc(n, lst):
    global k
    if n == 15 and 8 in lst:
        k += 1
    elif n < 15:
        return calc(n + 1, lst + [n + 1]) or calc(n + 2, lst + [n + 2]) or calc(n * 3, lst + [n * 3])


k = 0
calc(1, [])
print(k)
