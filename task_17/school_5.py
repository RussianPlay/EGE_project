with open("17_school_5.txt", "r") as file:
    numbers = list(map(lambda x: int(x.strip()), file.readlines()))
mn_number = min(filter(lambda x: str(x)[-1] == "7", numbers))

k = 0
for i in range(len(numbers) - 1):
    num_1, num_2 = numbers[i], numbers[i + 1]
    if ((str(num_1)[-1] == "7" and str(num_2)[-1] != "7") or (str(num_1)[-1] != "7" and str(num_2)[-1] == "7")) and \
            (num_1 + num_2) ** 2 < mn_number ** 2:
        k += 1
print(k)