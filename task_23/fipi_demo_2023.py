def F(n, lst):
    global k
    if n < 35:
        return F(n + 1, lst + [n + 1]) or F(n * 2, lst + [n * 2])
    elif n == 35 and 10 in lst and 17 not in lst:
        k += 1


k = 0
F(1, [1])
print(k)