N = -1
R = -1
while R <= 228:
    N += 1
    N_base = bin(N)[2:]
    if N % 2 != 0:
        N_base = N_base + "0"
    elif N % 2 == 0:
        N_base = "1" + N_base
    if N_base.count("1") % 2 == 0:
        N_base = N_base + "1"
    elif N_base.count("1") % 2 != 0:
        N_base = N_base + "0"
    R = int(N_base, 2)
print(N)