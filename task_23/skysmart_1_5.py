def calc(n, com_k):
    global cur_lst
    if com_k != 3:
        return calc(n * 2, com_k + 1) or calc(n + 3, com_k + 1)
    else:
        cur_lst.append(n)


cur_lst = []
calc(2, 0)
print(len(set(cur_lst)))
