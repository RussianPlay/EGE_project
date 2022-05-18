with open("24_school_3.txt", "r") as file:
    text = list(map(str.strip, file.readlines()))[0]

mx_length = -1
res_symbols = text[0]

for i in range(len(text) - 1):
    if (res_symbols.count("C") + res_symbols.count("D")) < 3:
        res_symbols += text[i]
    else:
        mx_length = max(mx_length, len(res_symbols))
        res_length = ""

print(mx_length)