with open("26-j8_number_57448.txt", "r") as file:

    total = list(map(lambda x: int(x.rstrip()), file.readlines()))
    n = total[0]
    numbers = total[1:]
    numbers = list(sorted(numbers))
    amount_1 = 0
    amount_2 = 0
    part1_1 = int(n / 100 * 70)
    part1_2 = n // 2
    max1 = 0
    max2 = 0
    for i in range(len(numbers)):
        if i <= (part1_1 - 1):
            amount_1 = amount_1 + numbers[i] * 0.7
        else:
            amount_1 = amount_1 + numbers[i] * 0.6
            max1 = max(max1, numbers[i] * 0.6)

    for i in range(len(numbers)):
        if i <= (part1_2 - 1):
            amount_2 = amount_2 + numbers[i] * 0.6
        else:
            amount_2 = amount_2 + numbers[i] * 0.65
            max2 = max(max2, numbers[i] * 0.65)
    if amount_1 > amount_2:
        print(int(abs(amount_1 - amount_2)), int(max1))
    elif amount_1 < amount_2:
        print(int(abs(amount_1 - amount_2)), int(max2))
