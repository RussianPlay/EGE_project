N = 100
R = 0
while R != 9:
    N += 1
    R = list(bin(N)[2:])
    R = R[::-1]
    while R[0] == "0" and "1" in R:
        R.pop(0)
    R = int("".join(R), 2)
print(N)
