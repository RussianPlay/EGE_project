num = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 2 ** 1050 - 2022
num_base_4 = ""

while num != 0:
    num_base_4 = str(num % 4) + num_base_4
    num //= 4

print(num_base_4.count("3"))