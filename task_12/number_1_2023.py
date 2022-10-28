word = "4" * 5 + "42" * 5 + "32" * 15
while "42" in word or "32" in word:
    if "42" in word:
        word = word.replace("42", "51", 1)
    else:
        word = word.replace("32", "61", 1)

print(sum(map(int, word)))
