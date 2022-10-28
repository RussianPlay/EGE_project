def calc(n, lst):
    global k
    if n < 39:
        return calc(n + 1, lst + [n + 1]) or calc(n * 2, lst + [n * 2])
    if n == 39 and 7 in lst and 16 in lst:
        k += 1


k = 0
calc(2, [])
print(k)