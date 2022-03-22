num = 81 ** 15 + 3 ** 22 - 27
num_base_9 = ""
num_base_10 = num
while num_base_10 != 0:
    num_base_9 = num_base_9 + str(num_base_10 % 9)
    num_base_10 //= 9
num_base_9 = num_base_9[::-1]

print(num_base_9.count("8"))