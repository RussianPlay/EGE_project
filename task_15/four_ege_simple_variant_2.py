data = list(range(-1000, 1000))
P = list(range(43, 49 + 1))
Q = list(range(44, 53 + 1))
lst_values = []
mx_length = 0
for x in range(-100, 100):
    F = ((x in data) <= (x in P)) or (x in Q)
    if F:
        lst_values.append(x)
    else:
        if len(lst_values) >= 2:
            cur_length = lst_values[-1] - lst_values[0]
            mx_length = max(mx_length, cur_length)
        lst_values = []

print(mx_length)