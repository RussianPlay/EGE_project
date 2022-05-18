num = 3 * 125 ** 6 + 2 * 25 ** 9 + 5 ** 12 - 625
num_base_5 = ""
while num != 0:
    num_base_5 = num_base_5 + str(num % 5)
    num //= 5

sign_zeros = 0
while num_base_5 and num_base_5[0] == "0":
    sign_zeros += 1
    num_base_5 = num_base_5[1:]

print(sign_zeros)
