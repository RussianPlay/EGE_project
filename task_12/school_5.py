# import itertools
#
# for i in range(6, 51):
#     combinations = itertools.permutations("2" * i + "1" * i)
#     print(combinations)
#     for comb in combinations:
#         num = "0" + "".join(comb) + "0"
#         while "00" not in num:
#             num = num.replace("011", "20")
#             num = num.replace("022", "10")
#             num = num.replace("01", "220")
#             num = num.replace("02", "110")
#         if num.count("1") == 40 and num.count("2") > 50:
#             print(num.count("2"))
#             break
#     print(i)

for k1 in range(51):
    for k2 in range(51):
        for k3 in range(51):
            for k4 in range(51):
                if (2 * k1 + k3) == (2 * k2 + k4) and k2 + 2 * k4 == 40 and k4 + 2 * k3 == 51:
                    print(k1, k2, k3, k4)