P = list(range(19, 84 + 1))
Q = list(range(4, 51 + 1))
data = list(range(-10000, 10000))
A_length = 0
for x in range(-1000, 1000):
    f = (x in Q) <= (not(x in P) <= (not((x in Q) and not(x in data))))
    if int(f) == 1:
        A_length += 1
    else:
        print(A_length)
        break
