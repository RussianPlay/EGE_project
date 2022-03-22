def calc(n, lst):
    global k
    if n < 20:
        return calc(n * 3, lst + [n * 3]) or calc(n + 1, lst + [n + 1])
    elif n == 20:
        k += 1


k = 0
calc(3, [])
print(k)
