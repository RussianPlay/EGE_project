N = 1
R = 0
max_N = -1
while N < 90:
    N += 1
    N_base_2 = bin(N)[2:]
    for _ in range(3):
        numbers = N_base_2.count("1")
        zeros = N_base_2.count("0")
        if numbers == zeros:
            N_base_2 = N_base_2 + N_base_2[-1]
        elif numbers < zeros:
            N_base_2 = N_base_2 + "1"
        elif zeros < numbers:
            N_base_2 = N_base_2 + "0"
    R = int(N_base_2, 2)
    if R % 4 == 0:
        max_N = max(max_N, N)

print(max_N)