with open("24-153_number_46529.txt", "r") as file:
    text = list(map(lambda x: x.rstrip(), file.readlines()))[0]
    AF_line = ["A", "B", "C", "D", "E", "F"]
    ind = 0
    line_length = 0
    word = ""
    line_lengths = []
    for i in range(len(text)):
        if text[i] in AF_line[ind]:
            line_length += 1
            word += AF_line[ind]
        else:
            ind += 1
            if ind < len(AF_line) and text[i] in AF_line[ind:]:
                line_length += 1
                word += AF_line[ind]

            if word[0] == "A" and word[-1] == "F":
                line_lengths.append(line_length)
                print(word)
                ind = 0
                line_length = 0
                word = ""
            if text[i] not in AF_line[ind:]:
                ind = 0
                line_length = 0
                word = ""
    print(min(line_lengths))