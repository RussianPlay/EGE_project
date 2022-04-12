with open("17_school_1.txt", "r") as file:
    numbers = list(map(lambda x: int(x.rstrip()), file.readlines()))
    k = 0
    max_pair_amount = 0
    min_cur_num = min(list(filter(lambda x: x % 17 == 0, numbers)))
    for i in range(0, len(numbers) - 1, 2):
        if numbers[i] % min_cur_num == 0 or numbers[i + 1] % min_cur_num == 0:
            k += 1
            max_pair_amount = max(max_pair_amount, numbers[i] + numbers[i + 1])

    print(k)
    print(max_pair_amount)
