s = 81 ** 11 + 27 ** 6 - 9
s_base_3 = ""
while s > 0:
    s_base_3 = str(s % 3) + s_base_3
    s = s // 3
print(s_base_3.count("2"))