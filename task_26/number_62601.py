with open("26-48_number_62601.txt", "r") as file:
    total = list(map(lambda x: int(x.rstrip()), file.readlines()))
    N = total[0]
    cur_averages = []
    K = 5
    numbers = total[1:]
    num_pairs = 0
    pairs = []
    for num1 in numbers:
        print(1)
        for num2 in numbers:
            if num1 != num2 and (num1, num2) not in pairs and (num2, num1) not in pairs:
                pairs.append((num1, num2))
                # if (num1 + num2) % 2 == 0:
                #     average = (num2 + num1) // 2
                #     if K == average - num1 or K == average - num2:
                #         cur_averages.append(average)

    pairs = list(set(pairs))
    print(len(pairs))




