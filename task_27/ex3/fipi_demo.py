with open("27_B demo2022.txt") as file:
    total = list(map(lambda x: int(x.rstrip()), file.readlines()))
    N = total[0]
    numbers = total[1:]
    length = 0
    amount = 0
    res = []
    mx_amount = -1
    mx_length = -1
    r = []
    for i in range(N):
        amount += numbers[i]
        if amount % 43 == 0:
            length += 1
        else:
            r.append(length)
            if amount > mx_amount:
                mx_amount = amount
                mx_length = length
            elif amount == mx_amount and mx_length != -1 and length < mx_length:
                mx_amount = max(mx_amount, amount)
                mx_length = max(mx_length, length)
            amount = 0
            length = 0
    print(mx_length)
