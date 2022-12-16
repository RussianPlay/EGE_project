def F(n, lst):
    global k
    if n == 40 and 3 not in lst:
        k += 1
    if n < 40:
        return F(n + 1, lst + [n + 1]) or F(n * 2, lst + [n * 2])


k = 0
F(1, [])
print(k)