with open("24-5_number_57448.txt", "r") as file:
    text = list(map(lambda x: x.rstrip(), file.readlines()))[0]
    max_lenght = 0
    line_lenght = 0
    for letter in text:
        if letter == "(":
            line_lenght += 1
        else:
            max_lenght = max(max_lenght, line_lenght)
            line_lenght = 0
    print(max_lenght)