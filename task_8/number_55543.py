word = "ДЕЙКСТРА"
consonants = "ДКСТР"
k = 0
for lt1 in word:
    for lt2 in word:
        for lt3 in word:
            for lt4 in word:
                for lt5 in word:
                    for lt6 in word:
                        for lt7 in word:
                            for lt8 in word:
                                total_check = 0
                                word_check = 0
                                new_word = lt1 + lt2 + lt3 +lt4 +lt5 +lt6 +lt7 +lt8
                                if len(set(new_word)) == len(new_word):
                                    total_check += 1
                                if "Й" in new_word and new_word.count("Й") == 1:
                                    total_check += 1
                                if "Й" in new_word and list(new_word).index("Й") != len(new_word) - 1 and new_word[list(new_word).index("Й") + 1] in consonants:
                                    total_check += 1
                                if total_check == 3:
                                    k += 1

print(k)
