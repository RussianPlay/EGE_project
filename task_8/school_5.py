nums_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
odd_nums = ["1", "3", "5", "7", "9"]
k = 0
for n1 in nums_base_10:
    for n2 in nums_base_10:
        for n3 in nums_base_10:
            for n4 in nums_base_10:
                for n5 in nums_base_10:
                    for n6 in nums_base_10:
                        for n7 in nums_base_10:
                            new_num = n1 + n2 + n3 + n4 + n5 + n6 + n7
                            if new_num.count("6") == 1 and len(list(filter(lambda x: x in odd_nums, new_num))) == 2:
                                k += 1
print(k)