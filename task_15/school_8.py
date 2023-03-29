P = list(range(25, 50 + 1))
Q = list(range(55, 95 + 1))
data = list(range(-1000, 1000))
cur_lst = []
mx_length = -1
for x in range(-1000, 1000):
    check = ((not(x in data)) <= (not(x in P))) <= ((x in data) <= (x in Q))
    if check:
        cur_lst.append(x)
    else:
        if cur_lst:
            mx_length = max(mx_length, cur_lst[-1] - cur_lst[0])
            cur_lst = []
print(mx_length)