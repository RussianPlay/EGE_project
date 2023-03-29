with open("17_school_8.txt", "r") as file:
    numbers = list(map(int, file.readlines()))

mn_pair_amount = 10 ** 100
k = 0
for i in range(len(numbers) - 1):
    num_1 = numbers[i]
    num_2 = numbers[i + 1]
    if (str(num_1)[-1] == "7" or str(num_2)[-1] == "7") and (num_1 + num_2) % 2 == 0:
        k += 1
        mn_pair_amount = min(mn_pair_amount, num_1 + num_2)

print(k)
print(mn_pair_amount)