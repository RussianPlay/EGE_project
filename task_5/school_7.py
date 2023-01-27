N = 0
lst_R = []

for i in range(0, 100000):
    N = i
    N_base_2 = bin(N)[2:]
    N = N - str(N_base_2).count("0")
    if N >= 0:
        N_base_2 = bin(N)[2:]
        N_base_2 = N_base_2[-3:] + N_base_2
        R = int(N_base_2, 2)
        if R > 224:
            lst_R.append(R)
print(min(lst_R))