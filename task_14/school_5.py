nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
for x in nums:
    new_num = int(f"1{x}BAD", 16) + int(f"2C{x}FE", 16)
    if new_num % 15 == 0:
        print(new_num)