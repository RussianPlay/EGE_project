with open("24_school_6.txt", "r") as file:
    text = file.readline()

amount_cur_chars = 0
mx_amount_cur_chars = 0
always_right_chars = 2
for i in range(1, len(text) - 1):
    char_1 = text[i - 1]
    t_char = text[i]
    char_3 = text[i + 1]
    if t_char != char_1 and t_char != char_3:
        amount_cur_chars += 1
    else:
        mx_amount_cur_chars = max(mx_amount_cur_chars, amount_cur_chars)
        amount_cur_chars = 0

print(mx_amount_cur_chars + always_right_chars)