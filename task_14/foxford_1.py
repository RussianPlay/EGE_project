number = 49 ** 20 - 7 ** 19 + 95
base7_number = ""
while number != 0:
    base7_number = base7_number + str(number % 7)
    number //= 7

base7_number = base7_number[::-1]
print(base7_number.count("6"))
