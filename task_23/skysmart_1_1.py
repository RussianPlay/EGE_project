def calc(n, lst):
    global k
    if n < 20:
        return calc(n * 2, lst + [n * 2]) or calc(n + 1, lst + [n + 1])
    elif n == 20 and 9 in lst:
        k += 1


k = 0
calc(3, [])
print(k)
