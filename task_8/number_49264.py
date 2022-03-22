lst = ["К", "А", "Л", "И", "Й"]
k = 0

for l1 in lst:
    for l2 in lst:
        for l3 in lst:
            for l4 in lst:
                for l5 in lst:
                    for l6 in lst:
                        new_word = l1 + l2 + l3 + l4 + l5 + l6
                        check = 0
                        if new_word[0] == "Й" or new_word[-1] == "Й" or new_word.count("Й") > 1:
                            check = 1
                        for i in range(1, len(new_word) - 1):
                            if new_word[i] == "Й" and (new_word[i - 1] == "И" or new_word[i + 1] == "И"):
                                check = 1

                        if not check:
                            k += 1

print(k)
