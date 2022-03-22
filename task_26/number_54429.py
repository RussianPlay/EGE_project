with open("26-s1_number_54429.txt", "r") as file:
    numbers = list(sorted(map(lambda x: int(x.rstrip()), file.readlines()[1:])))
    start_ind = sum([1 if numbers[i] <= 150 else 0 for i in range(len(numbers))])
    changing_numbers = numbers[start_ind:]
    quantity_discount_products = len(changing_numbers) // 2
    res_quantity_discount_products = quantity_discount_products
    amount = sum(numbers[:start_ind])
    for i in range(len(changing_numbers)):
        if res_quantity_discount_products != 0:
            res_quantity_discount_products -= 1
            amount += changing_numbers[i] * 0.8
        else:
            amount += changing_numbers[i]

    print(round(amount), changing_numbers[quantity_discount_products - 1])

