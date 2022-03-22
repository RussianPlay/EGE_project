with open("foxford_1.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    text = total[0]

mx_length = 0
length = 0
for ltr in text:
    if ltr == "S":
        length += 1
    else:
        mx_length = max(mx_length, length)
        length = 0
print(mx_length)
