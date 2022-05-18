mx_last_length = -1
for i in range(201, 1000):
    num = "1" * i
    while "1111" in num:
        num = num.replace("1111", "22", 1)
        num = num.replace("222", "1", 1)
    mx_last_length = max(mx_last_length, num.count("1"))

for i in range(201, 1000):
    num = "1" * i
    while "1111" in num:
        num = num.replace("1111", "22", 1)
        num = num.replace("222", "1", 1)
    if num.count("1") == mx_last_length:
        print(i)
        break

