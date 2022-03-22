letters = "ПСКАЛЬ"
k = 0
for w1 in letters:
    for w2 in letters:
        for w3 in letters:
            for w4 in letters:
                new_word = w1 + w2 + w3 + w4
                check = 0
                for i in range(1, len(new_word) - 1):
                    if new_word[i] == "Ь" and (new_word[i - 1] == "Ь" or new_word[i + 1] == "Ь"):
                        check += 1
                if new_word[0] != "Ь" and not check:
                    k += 1
print(k)