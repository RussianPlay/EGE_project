with open("24-j1_number_54429.txt", "r") as file:
    text = list(map(lambda x: x.rstrip(), file.readlines()))[0]
    k = 0
    maximum_k = 0
    check_stage = 0
    necessary_word = ["К", "О", "Т"]
    for i in range(len(text)):
        if text[i] == necessary_word[check_stage]:
            check_stage += 1
            if check_stage == 3:
                k += 1
                check_stage = check_stage % 3
        else:
            maximum_k = max(maximum_k, k)
            k = 0
    print(maximum_k)
