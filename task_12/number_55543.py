num = "687" * 143
while "68" in num or "7777" in num:
    num = num.replace("68", "7", 1)
    num = num.replace("7777", "7", 1)

print(num)
