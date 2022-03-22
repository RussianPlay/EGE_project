N = 0
k = 0
while True:
    N += 1
    R = list(bin(N)[2:])
    R = R + ["0" if R.count("1") > R.count("0") else "1"]
    if len(R) % 2 == 0:
        first_mid_index = len(R) // 2 - 1
        R.pop(first_mid_index)
        R.pop(first_mid_index)
    else:
        first_mid_index = (len(R) - 1) // 2 - 1
        R.pop(first_mid_index)
        R.pop(first_mid_index)
        R.pop(first_mid_index)
    if R:
        R = int("".join(R), 2)
        if R == 58:
            k += 1
        print(k)