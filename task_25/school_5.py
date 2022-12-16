for num in range(0, 10 ** 10, 2023):
    num = str(num)
    if num[0] == "1" and num[2:5] == "493" and num[-2:] == "41":
        print(num)