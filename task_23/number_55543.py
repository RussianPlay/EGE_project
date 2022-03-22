def calc(n, lst):
    global k
    if n == 21 and 8 in lst and 12 not in lst:
        k += 1
    elif n > 21:
        return
    return calc(n + 1, lst + [n]) or calc(n + 3, lst + [n]) or calc(n * 2, lst + [n])


k = 0
calc(3, [])
print(k)
