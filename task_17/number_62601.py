with open("17-243_number_62601.txt", "r") as file:
    numbers = list(map(lambda x: int(x.rstrip()), file.readlines()))
    k = 0
    cur_max_num = max(numbers, key=lambda x: x % 111 == 0)
    amount_pairs = []
    for i in range(len(numbers) - 1):
        pair = (numbers[i], numbers[i + 1])
        if (pair[0] > cur_max_num and str(pair[1])[-1] == "7") or (pair[1] > cur_max_num and str(pair[0])[-1] == "7"):
            amount_pairs.append(pair[0] + pair[1])
            k += 1
    print(k)
