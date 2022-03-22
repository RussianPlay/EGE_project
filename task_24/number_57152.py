with open("24-153_number_57152.txt", "r") as file:
    text = list(map(str.strip, file.readlines()))[0]
    minimum_lenght = len(text)
    for i in range(len(text)):
        res_text = text[i:]
        ind_start = res_text.find("A")
        ind_end = res_text.find("F")
        text_slice = text[ind_start:
                          ind_end]
        if len(text_slice) >= 5:
            minimum_lenght = min(minimum_lenght,
                                 len(text_slice) + 1)
print(minimum_lenght)