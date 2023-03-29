num = 7 * 256 ** 2912 + 5 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8 ** 1980 - 2022

# N_base_8 = ""
# while num != 0:
#     N_base_8 = str(num % 8) + N_base_8
#     num //= 8
# print(N_base_8)
N_base_8 = oct(num)[2:]
print(N_base_8.count("1"))
