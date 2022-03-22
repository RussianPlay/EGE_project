def set_to_base_6(num):
    num_base_6 = ""
    while num != 0:
        num_base_6 = num_base_6 + str(num % 6)
        num //= 6
    return num_base_6[::-1]


k = 0
N = 0
num_base_6 = set_to_base_6(N)
while len(num_base_6) <= 5:
    if len(num_base_6) == 5:
        is_wrong = 0
        for i in range(len(num_base_6) - 1):
            if (int(num_base_6[i]) % 2 == 0 and int(num_base_6[i + 1]) % 2 == 0) or \
                    (int(num_base_6[i]) % 2 != 0 and int(num_base_6[i + 1]) % 2 != 0):
                is_wrong = 1
        if not is_wrong:
            k += 1
    N += 1
    num_base_6 = set_to_base_6(N)
print(k)

