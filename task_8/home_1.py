k = 0
for n in range(1, 1000000):
    num = n
    N_base_9 = ""
    while num != 0:
        N_base_9 = str(num % 9) + N_base_9
        num //= 9
    if len(N_base_9) == 5:
        if int(N_base_9[0]) % 2 == 0 and N_base_9[-1] not in ("1", "8") and N_base_9.count("3") <= 1:
            k += 1
    elif len(N_base_9) > 5:
        print(k)
        break