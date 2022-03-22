maximum = 0
k = 0
with open("17-4_number_57448.txt") as file:
    numbers = list(map(lambda x: int(x.rstrip()), file.readlines()))
    for num in numbers:
        if list(str(num)).count("0") >= 2 and num % 7 == 0:
            maximum = max(maximum, num)
            k += 1

print(maximum)
print(k)