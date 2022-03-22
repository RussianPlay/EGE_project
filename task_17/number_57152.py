with open("17-1_number_57152.txt", "r") as file:
    numbers = list(map(lambda x: int(x.strip()),
                       file.readlines()))
    k = 0
    arithmetic_mean = sum(numbers) / len(numbers)
    current_amount_pairs = []
    for i in range(len(numbers) - 1):
        if numbers[i] > arithmetic_mean > numbers[i + 1] or \
                numbers[i + 1] > arithmetic_mean > numbers[i]:
            k += 1
            current_amount_pairs.append(numbers[i] +
                                        numbers[i + 1])
    print(k)
    print(max(current_amount_pairs))
