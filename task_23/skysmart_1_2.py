def calc(n, lst):
    global k
    if n < 17:
        return calc(n * 2, lst + [n * 2]) or calc(n + 1, lst + [n + 1]) or calc(n + 4, lst + [n + 4])
    elif n == 17 and 9 in lst and 13 in lst:
        k += 1


k = 0
calc(2, [])
print(k)
