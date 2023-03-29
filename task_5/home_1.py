N = 1
while True:
    N_base_2 = bin(N)[2:]
    if N % 2 == 0:
        N_base_2 = "1" + N_base_2 + "0"
    else:
        N_base_2 = "11" + N_base_2 + "10"
    R = int(N_base_2, 2)
    R_num_amount = sum(map(int, list(str(R))))
    if R_num_amount > 17:
        print(bin(R_num_amount)[2:])
        break
    N += 1
