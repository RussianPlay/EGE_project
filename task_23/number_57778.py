lst = [1]
for i in range(4):
    n = len(lst)
    for j in range(n):
        lst.append(lst[0] + 1)
        lst.append(lst[0] + 5)
        lst.append(lst[0] * 3)
        lst.remove(lst[0])

print(len(set(lst)))