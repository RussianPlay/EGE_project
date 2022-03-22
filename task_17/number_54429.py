with open("17-1_number_54429.txt", "r") as file:
    numbers = list(map(lambda x: int(x.rstrip()), file.readlines()))
    arithmetic_middle = sum(numbers)/ len(
        numbers)
    amount_current_pairs = []
    for i in range(len(numbers) - 1):
        if (numbers[i] > arithmetic_middle or numbers[i + 1] > arithmetic_middle) and \
                (str(numbers[i + 1])[-1] == "3" or str(numbers[i])[-1] == "3"):
            amount_current_pairs.append(numbers[i] + numbers[i + 1])
    print(len(amount_current_pairs))
    print(max(amount_current_pairs))

