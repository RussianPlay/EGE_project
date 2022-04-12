with open("24_school_1.txt", "r") as file:
    text = file.readlines()[0].strip()
    num_of_pairs = 0
    max_num_of_pairs = 0

    for i in range(0, len(text) - 1):
        if text[i] == "A" and (text[i + 1] == "B" or text[i + 1] == "C"):
            num_of_pairs += 1
        else:
            max_num_of_pairs = max(max_num_of_pairs, num_of_pairs)
            num_of_pairs = 0

    for i in range(1, len(text) - 1, 2):
        if text[i] == "A" and (text[i + 1] == "B" or text[i + 1] == "C"):
            num_of_pairs += 1
        else:
            max_num_of_pairs = max(max_num_of_pairs, num_of_pairs)
            num_of_pairs = 0

    print(max_num_of_pairs)