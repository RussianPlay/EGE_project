mx_cur_s = -1
for i in range(-1000, 10000):
    s = i
    n = 5
    while s > 5:
        s = s // 2
        n = n + 4

    if n == 29:
        mx_cur_s = max(mx_cur_s, i)

print(mx_cur_s)