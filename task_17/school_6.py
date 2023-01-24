with open("17_school_6.txt", "r") as file:
    numbers = list(map(int, file.readlines()))

lst_sums = []
for i in range(len(numbers) - 1):
    num_1 = numbers[i]
    num_2 = numbers[i + 1]
    if (num_1 + num_2) % 3 == 0 and (num_1 + num_2) % 6 != 0:
        lst_sums.append(num_1 + num_2)

print(len(lst_sums), max(lst_sums))
