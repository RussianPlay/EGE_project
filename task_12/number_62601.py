num = "7" * 86

while "4444" in num or "7777" in num:
    if "4444" in num:
        num = num.replace("4444", "77", 1)
    else:
        num = num.replace("7777", "44", 1)

print(num)
