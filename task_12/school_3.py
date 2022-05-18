num = 17 * 1728 ** 6 + 7 * 144 ** 9 + 10 * 12 ** 10 + 22
num_base_12 = ""
while num != 0:
    num_base_12 = num_base_12 + str(num % 12)
    num //= 12

num_base_12 = num_base_12[::-1]
while num and num[0] == "0":
    num = num[1:]
print(num_base_12.count("0"))
