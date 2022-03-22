P = list(range(10, 15 + 1))
Q = list(range(14, 40 + 1))
data = list(range(10000))
res_A = []
total_A = []
for x in range(15, 10000):
    F = not(not(x in P) or not(x in Q)) and not(x in data)
    if not F:
        res_A.append(x)
    else:
        print(1)
        total_A = max(total_A, res_A, key=len)
        res_A = []

print(total_A)
