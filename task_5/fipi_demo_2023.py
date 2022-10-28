N = 0
R = -1
while R <= 40:
    N += 1
    N_base_2 = bin(N)[2:]
    amount_num_N_base_2 = sum(map(int, list(N_base_2)))
    if amount_num_N_base_2 % 2 == 0:
        N_base_2 = N_base_2 + "0"
        N_base_2 = "10" + N_base_2[2:]
    elif amount_num_N_base_2 % 2 != 0:
        N_base_2 = N_base_2 + "1"
        N_base_2 = "11" + N_base_2[2:]
    R = int(N_base_2, 2)
print(N)

