A = []
P = list(range(5, 21))
Q = list(range(25, 39))
data = list(range(100000))
maximum_length = 0
for x in range(10000):
    check = (((x in data) <= (x in P)) or (x in Q))
    if check:
        A.append(x)
    else:
        maximum_length = max(maximum_length, len(A))
        A = []
print(maximum_length)