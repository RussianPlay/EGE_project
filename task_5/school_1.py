N = 0
R = -1

while R <= 516:
    N_base_2 = bin(N)[2:]
    if N % 2 == 0:
        N_base_2 = N_base_2 + "10"
    else:
        N_base_2 = "1" + N_base_2 + "01"
    R = int(N_base_2, 2)
    N += 1

print(N)
