print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = (not a and not b) or (b == c) or d
                if int(F) == 0:
                    print(a, b, c, d)