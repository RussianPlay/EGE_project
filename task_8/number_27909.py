letts = list("ЛОГАРИФМ")
cosn = "ЛГРФМ"
vowls = "ОАИ"
amount_cur_words = 0
for l1 in letts:
    for l2 in letts:
        for l3 in letts:
            for l4 in letts:
                for l5 in letts:
                    new_word = l1 + l2 + l3 + l4 + l5
                    check1_1 = all([(new_word[i] in cosn and new_word[i+1] in cosn) or
                                    (new_word[i] in vowls and new_word[i+1] in vowls)
                                    for i in range(len(new_word) - 1)])
                    check1_2 = all([(new_word[i] in cosn and new_word[i+1] in cosn) or
                                    (new_word[i] in vowls and new_word[i+1] in vowls)
                                    for i in range(1, len(new_word) - 1)])

                    check2 = len(new_word) == len(set(new_word))
                    if (check1_1 or check1_2) and check2:
                        amount_cur_words += 1

print(amount_cur_words)
