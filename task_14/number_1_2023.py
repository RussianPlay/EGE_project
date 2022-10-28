num = (64 ** 25 + 4 ** 10) - (16 ** 20 + 32 ** 3)
num_base_4 = ""
while num != 0:
    num_base_4 = num_base_4 + str(num % 4)
    num //= 4

print(num_base_4.find("2"))