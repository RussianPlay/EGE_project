N = 2
R = 0
k = 0
while True:
    R = bin(N)[2:]
    if "0" not in R:
        N += 1
        continue
    else:
        first_part = R[:2]
        ind = R.rindex("0")
        R = list(R)
        R[ind] = first_part
        R = "".join(R)
    R = R[::-1]
    R = int(R, 2)
    if R == 127:
        k += 1
    N += 1
    print(k)
