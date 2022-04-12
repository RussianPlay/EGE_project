num = "8" * 86

while "1111" in num or "8888" in num:
    if "1111" in num:
        num = num.replace("1111", "8", 1)
    else:
        num = num.replace("8888", "11", 1)

print(num)
