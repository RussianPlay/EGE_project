N = 0
R = -1
while R != 999:
    N += 1
    N_base_2 = bin(N)[2:]
    N_changed_base_2 = "".join(list(map(lambda x: str(int(not int(x))), N_base_2)))
    while N_changed_base_2 and N_changed_base_2[0] == "0":
        N_changed_base_2 = N_changed_base_2[1:]
    if N_changed_base_2:
        N_new_base_10 = int(N_changed_base_2, 2)
        R = N - N_new_base_10
        if R == 999:
            print(N)


