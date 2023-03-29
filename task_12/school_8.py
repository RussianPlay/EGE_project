num = "2" * 80
while "222" in num or "333" in num:
    if "222" in num:
        num = num.replace("222", "33", 1)
    else:
        num = num.replace("333", "22", 1)

print(num)