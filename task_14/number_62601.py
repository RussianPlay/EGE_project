num = 4 ** 2016 + 2 ** 2018 - 8 ** 600 + 6
num_base_2 = bin(num)[2:]
print(num_base_2.count("1"))