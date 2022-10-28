num = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
num_base_64 = ""
while num != 0:
    num_base_64 = num_base_64 + str(num % 64)
    num = num // 64
num_base_64 = num_base_64[::-1]
while num_base_64[0] == "0" and num_base_64:
    num_base_64 = num_base_64[1:]
print(num_base_64.count("0"))