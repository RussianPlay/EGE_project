num = "3" + "6" * 115 + "3"

while "63" in num or "664" in num or "6665" in num:
    if "63" in num:
        num = num.replace("63", "4", 1)
    elif "664" in num:
        num = num.replace("664", "65", 1)
    elif "6665" in num:
        num = num.replace("6665", "63", 1)

print(num)
