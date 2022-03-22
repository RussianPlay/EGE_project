with open("24-j5_number_62601.txt", "r") as file:
    text = file.read().rstrip()
    counter = 0
    mx_length = 0
    check_timer = 0
    for i in range(len(text) - 2):
        if not check_timer:
            if text[i:i + 3] == "KOT":
                counter += 1
                check_timer = 2
            else:
                mx_length = max(mx_length, counter)
                counter = 0
        else:
            check_timer -= 1
    mx_length = max(mx_length, counter)
    print(mx_length)