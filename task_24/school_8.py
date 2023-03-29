with open('24_school_8.txt', "r") as file:
    text = list(map(str.strip, file.readlines()))[0]

mx_length = -1
res_length = 0
for i in range(0, len(text) - 1, 2):
    if text[i] == "O" and text[i + 1] == "N":
        res_length += 1
    else:
        mx_length = max(mx_length, res_length)
        res_length = 0

res_length = 0

for i in range(1, len(text) - 1, 2):
    if text[i] == "O" and text[i + 1] == "N":
        res_length += 1
    else:
        mx_length = max(mx_length, res_length)
        res_length = 0

print(mx_length)