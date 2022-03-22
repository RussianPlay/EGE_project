N = 0
R = 0
R_values = []
while True:
    N += 1
    R = bin(N)[2:]
    if N % 2 != 0:
        R = "1" + R + "11"
    else:
        R = "11" + R + "00"
    R = int(R, 2)
    if R < 127:
        R_values.append(R)
    if N == 1000000:
        break

print(max(R_values))