N = 1
while True:
    N_base_2 = bin(N)[2:]
    if N_base_2.count("1") % 2 == 0:
        N_base_2 = "1" + N_base_2 + "10"
    else:
        N_base_2 = "11" + N_base_2
    R = int(N_base_2, 2)
    if R >= 635:
        print(N)
        break
    N += 1