with open("number_1_2023.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
max_sum = 0
k = 0


def func(x):
    if str(x)[-1] == "9" and x > 0:
        return True
    return False


for i in range(0, len(numbers) - 2):
    if not func(numbers[i]) and func(numbers[i + 1]) and not func(numbers[i + 2]):
        k += 1
        max_sum = max(max_sum, sum(numbers[i:i+3]))

print(k)
print(max_sum)
