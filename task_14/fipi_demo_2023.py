lst_nums_base_15 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E"]
for x_base_15 in lst_nums_base_15:

    num_base_10 = int(f"123{x_base_15}5", 15) + int(f"1{x_base_15}233", 15)
    if num_base_10 % 14 == 0:
        print(num_base_10 / 14)
        break
