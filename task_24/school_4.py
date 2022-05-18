with open("24_school_4.txt", "r") as file:
    text = list(map(str.strip, file.readlines()))[0]


res = ""
mx_length = -1
for lt in text:
    if lt != "A":
        res += lt
    elif res.count("E") >= 3:
        mx_length = max(mx_length, len(res))
        res = ""
    else:
        res = ""

print(mx_length)
