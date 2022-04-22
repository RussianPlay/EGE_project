A = list(range(100000))
P = list(range(4, 16))
Q = list(range(12, 21))
res_length = 0
mn_length = 10000
for x in range(10000):
    F = ((x in P) and (x in Q)) <= (x in A)
    if F:
        res_length += 1
    else:
        if res_length:
            mn_length = min(mn_length, res_length)
            res_length = 0

print(mn_length)