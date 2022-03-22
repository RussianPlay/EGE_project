N = 0
R = 0
while N <= 100 or R != 7:
    N += 1
    R = list(bin(N)[2:])
    R = R[::-1]
    while R and R[0] == "0":
        R.pop(0)
    if R:
        R = int("".join(R), 2)
print(N)

