with open("17_home_1.txt", "r") as file:
    numbers = list(map(int, file.readlines()))


k = 0
mx_amount = -1
mn_num = min(numbers)
for i in range(len(numbers) - 1):
    if numbers[i] % 117 == mn_num or numbers[i + 1] % 117 == mn_num:
        k += 1
        mx_amount = max(mx_amount, numbers[i] + numbers[i + 1])
print(k, mx_amount)