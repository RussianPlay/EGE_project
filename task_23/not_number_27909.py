def F(n, k):
    global lst
    if n < 227:
        return F(n + 1, k + 1) or F(n + 5, k + 1) or F(n * 3, k + 1)
    elif n == 227:
        print(k)
        lst.append(k)
    return


lst = [0]
F(1, 0)
print(lst)