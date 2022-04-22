def calc(n, lst):
    global k
    if n < 14:
        return calc(n + 1, lst + [n + 1]) or calc(n * 2, lst + [n * 2]) or calc(n + 3, lst + [n + 3])
    else:
        if 10 in lst:
            k += 1


k = 0
calc(2, [])
print(k)