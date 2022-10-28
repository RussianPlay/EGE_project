words = list(sorted("ПРВДА"))
vowel = "А"
k = 1


def calc():
    global k
    for l1 in words:
        for l2 in words:
            for l3 in words:
                for l4 in words:
                    new_word = l1 + l2 + l3 + l4
                    print(new_word)
                    if vowel not in new_word and len(set(new_word)) == len(new_word):
                        return k
                    else:
                        k += 1


print(calc())
