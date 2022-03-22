N = -1
k = 0
while True:
    N += 1
    check = 0
    N_base_16 = hex(N)[2:]
    if len(N_base_16) <= 3:
        if len(N_base_16) == 3:
            for i in range(len(str(N)) - 1):
                if (int(str(N)[i]) % 2 == 0 and int(str(N)[i + 1]) % 2 == 0) or (int(str(N)[i]) % 2 != 0 and int(str(N)[i + 1]) % 2 != 0):
                    check += 1
            for i in range(1, len(str(N)) - 1):
                if (int(str(N)[i]) % 2 == 0 and int(str(N)[i + 1]) % 2 == 0) or (int(str(N)[i]) % 2 != 0 and int(str(N)[i + 1]) % 2 != 0):
                    check += 1
            if len(str(N)) != len(list(set(str(N)))):
                check += 1
            if check == 0:
                k += 1
    else:
        break

print(k)