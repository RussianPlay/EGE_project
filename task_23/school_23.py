def calc(n, lst):
    global k
    if n == 36 and 18 in lst:
        k += 1
    elif n < 36:
        return calc(n + 3, lst + [n + 3]) or calc(n + 2, lst + [n + 2]) or calc(n * 2, lst + [n * 2])


k = 0
calc(10, [10])
print(k)
