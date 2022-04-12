from itertools import product

word = "ПАРУС"
k = 0
for new_word in product(word, repeat=len(word)):
    new_word = "".join(new_word)
    if new_word[0] == "У" and "АА" not in new_word:
        print(k)
        break
    else:
        k += 1
