with open("number_1_2023.txt", "r") as file:
    text = file.readline().strip()

data_cur_letters = {"C": 0, "D": 0, "E": 0}
k = 0
for i in range(len(text) - 4):
    if text[i:i+2] == "CB" and text[i + 2] not in ("A", "B", "F") and text[i + 3: i + 5] == "BC":
        k += 1
        data_cur_letters[text[i + 2]] += 1

print(list(sorted(data_cur_letters.items(), key=lambda x: x[1], reverse=True))[0][0] + str(k))

