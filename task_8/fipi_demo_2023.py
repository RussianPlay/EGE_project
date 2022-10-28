k = 0
for N in range(99999):
    N_base_8 = oct(N)[2:]
    if len(N_base_8) > 5:
        break
    else:
        num_6_ind = N_base_8.find("6")
        if len(N_base_8) == 5 and num_6_ind != -1:
            check_1 = ((num_6_ind - 1) >= 0 and int(N_base_8[num_6_ind - 1]) % 2 == 0) or ((num_6_ind - 1) < 0)
            check_2 = ((num_6_ind + 1) < len(N_base_8) and int(N_base_8[num_6_ind + 1]) % 2 == 0) or \
                      ((num_6_ind + 1) >= len(N_base_8))

            if check_1 and check_2:
                k += 1
print(k)