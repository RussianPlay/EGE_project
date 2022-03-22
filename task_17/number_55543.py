with open("17-1_number_55543.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
    minimum = 100001
    k = 0
    for i in range(len(numbers) - 1):
        pair = [numbers[i], numbers[i + 1]]
        cur_pair = list(filter(lambda x: str(x)[-1] == "6" and x % 3 == 0, pair))
        if cur_pair:
            k += 1
            for num in cur_pair:
                minimum = min(minimum, num)
    print(k, minimum)
