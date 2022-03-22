def calc(n, lst):
    global k
    if n == 30 and 20 in lst and 12 not in lst:
        k += 1
    elif n > 30:
        return
    return calc(n + 1, lst + [n + 1]) or calc(n * 2, lst + [n * 2])


k = 0
calc(3, [])
print(k)