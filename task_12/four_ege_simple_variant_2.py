min_length = 101
min_cur_num = int("3" * 101)
for n in range(101, 20000):
    num = "3" * n
    while "111" in num or "333" in num:
        if "111" in num:
            num = num.replace("111", "3", 1)
        else:
            num = num.replace("333", "1")

    if int(num) < min_cur_num:
        min_cur_num = int(num)
        min_length = n

print(min_length, min_cur_num)