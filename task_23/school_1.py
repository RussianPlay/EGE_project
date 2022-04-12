def calc(n, lst):
    global k
    if n < 52:
        return calc(n + 2, lst + [n + 2]) or calc(n * 2, lst + [n * 2])
    elif n == 52:
        k += 1


k = 0
calc(1, [])

print(k)
