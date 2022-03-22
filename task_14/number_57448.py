for x in range(2, 36):
    if int("101", x) + 13 == int("101", x + 1):
        print(x)