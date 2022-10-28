with open("24_fipi_demo_2023.txt", "r") as file:
    text = list(map(str.strip, file.readlines()))[0]
vowels = ("A", "O")
consonants = ("B", "C", "D", "F")
mx_pair_length = -1
pair_length = 0
for i in range(0, len(text), 2):
    if text[i] in consonants and text[i + 1] in vowels:
        pair_length += 1

    else:
        mx_pair_length = max(mx_pair_length, pair_length)
        pair_length = 0

print(mx_pair_length)
