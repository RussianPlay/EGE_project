data = list(range(-1000, 1000))
res_lst = []
P = list(range(10, 29 + 1))
Q = list(range(13, 18 + 1))
max_length = 0
for x in range(-1000, 1000):
    F = ((x in data) <= (x in P)) or (x in Q)
    if int(F) == 1:
        res_lst.append(x)
    else:
        if len(res_lst) > 0:
            res_length = max(res_lst) - min(res_lst)
        else:
            res_length = 0
        if res_length == 19:
            print(res_lst)
        max_length = max(max_length, res_length)
        res_lst = []

print(max_length)
