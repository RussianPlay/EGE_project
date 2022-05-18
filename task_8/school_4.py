from itertools import product

k = 0
word = "СВЕТЛАНА"

for new_word in product(word, repeat=8):
    new_word = "".join(new_word)
    check_1 = 0
    check_2 = 0
    for i in range(len(new_word) - 1):
        if new_word[i] == new_word[i + 1]:
            check_1 = 1
            break
    if list(sorted(new_word)) == list(sorted(word)):
        check_2 = 1
    if check_1 and check_2:
        k += 1

print(k)
