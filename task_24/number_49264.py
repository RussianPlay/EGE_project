with open("24-j5_number_49264.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    ttext = total[0]
    text = ttext


k = 0
while text.find("OCK") != -1:
    ind = text.find("OCK")
    if ind - 2 >= 0:
        if text[ind - 2: ind + 3] != "STOCK":
            k += 1
    else:
        k += 1
    text = text.replace("OCK", "***", 1)
print(k)