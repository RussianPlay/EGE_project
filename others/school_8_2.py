with open("ФайлB_school_8.txt", "r") as file:
    total = list(map(int, file.readlines()))
    N = total[0]
    numbers = total[1:]

k = 0
amount = 0
mx_amount = -1
for num in numbers:
    if num % 2 == 0:
        amount += num
        k += 1
    else:
        if k % 3 == 0:
            mx_amount = max(mx_amount, amount)
        amount = 0
        k = 0

print(mx_amount)