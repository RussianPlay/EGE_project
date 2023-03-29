k = 0
for n in range(1, 10000000):
    num = n
    N_base_7 = ""
    while num != 0:
        N_base_7 = str(num % 7) + N_base_7
        num //= 7
    if len(N_base_7) == 5:
        check = 0
        for i in range(len(N_base_7) - 1):
            if (int(N_base_7[i]) % 2 == 0 and int(N_base_7[i + 1]) % 2 == 0) or \
                    (int(N_base_7[i]) % 2 != 0 and int(N_base_7[i + 1]) % 2 != 0):
                check = 1
        if len(N_base_7) == len(set(N_base_7)) and not check:
            k += 1
    elif len(N_base_7) > 5:
        print(k)
        break
