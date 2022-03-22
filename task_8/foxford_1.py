def finder():
    lst = sorted(["Л", "О", "Т", "К", "И"])
    k = 0
    for ltr1 in lst:
        for ltr2 in lst:
            for ltr3 in lst:
                for ltr4 in lst:
                    k += 1
                    new_word = ltr1 + ltr2 + ltr3 + ltr4
                    if new_word[0] == "О":
                        return k


print(finder())
