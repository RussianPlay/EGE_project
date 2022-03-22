with open("24-s2_number_55543.txt") as file:
    text = list(map(str.strip, file.readlines()))[0]
    data = {}
    mx = 0
    for i in range(1, len(text) - 1):
        if text[i - 1] == "X" and text[i + 1] == "Z":
            if text[i] not in data.keys():
                data[text[i]] = 1
            else:
                data[text[i]] += 1
    data = dict(reversed(sorted(list(data.items()), key=lambda x: x[1])))
    print(data)
    print("".join(map(str, list(data.items())[0])))
