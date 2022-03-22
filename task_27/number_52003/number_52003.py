with open("27-46a.txt", "r") as file:
    total = list(map(lambda x: x.strip(), file.readlines()))
    n = int(total[0])
    min_amount = 0
    max_amount = 0
    for i in range(1, n + 1):
        x, y = map(int, total[i].split())
        min_amount += min(x, y)
        max_amount += max(x, y)
    remainder = min_amount % 7
    waste_num = 10000000001
    for i in range(1, n + 1):
        x, y = map(int, total[i].split())
        if abs(x - y) % 7 == remainder:
            waste_num = min(waste_num, abs(x - y))
    if max_amount % 7 == remainder:
        print(max_amount)
    else:
        print(max_amount - waste_num)


