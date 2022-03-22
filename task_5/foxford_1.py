N = 0
R = -1
while R <= 73:
    N += 1
    base2_N = bin(N)[2:]
    if N % 2 == 0:
        base2_N = base2_N + "01"
    else:
        base2_N = base2_N + "10"
    R = int(base2_N, 2)

print(N)