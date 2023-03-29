for x in range(1, 10000):
    num = 27 ** 7 - 3 ** 11 + 36 - x
    num_base_3 = ""
    while num != 0:
        num_base_3 = str(num % 3) + num_base_3
        num //= 3
    if sum(map(int, num_base_3)) == 22:
        print(x)
        break