with open("17-199_number_49264.txt", "r") as file:
    numbers = list(map(lambda x: int(x.rstrip()), file.readlines()))

three_quantity = 0
mx_amount = 0
for i in range(1, len(numbers) - 1):
    if len(str(numbers[i])) == 2 and numbers[i] >= 0 and numbers[i] % 2 != 0:
        three_quantity += 1
        mx_amount = max(mx_amount, sum(numbers[i - 1:i + 2]))

print(three_quantity)
print(mx_amount)