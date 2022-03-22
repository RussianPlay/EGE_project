num = 81 ** 18 - (81 ** 8 - 1) * ((8 + 1) ** 8 + 1) // 8 - 8
new_num = ""
while num != 0:
    new_num += str(num % 3)
    num //= 3
new_num = new_num[::-1]
print(new_num.count("1"))

