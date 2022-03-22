N = 0
R_mx = 0
while N < 256:
    N += 1
    N_base_2 = bin(N)[2:]
    rev_N_base_2 = N_base_2[::-1]
    R_mx = max(R_mx, int(bin(int(N_base_2, 2) ^ int(rev_N_base_2, 2)), 2))
print(R_mx)