def F(n, com_k):
    global lst
    if com_k < 13:
        return F(n + 3, com_k + 1) or F(n * 2 + 1, com_k + 1)
    elif com_k == 13:
        lst.append(n)
        return


lst = []
F(2, 0)
print(len(set(lst)))
