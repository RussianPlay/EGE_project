def tcalc(S, p):
    if S >= 82 and (p == 3 or p == 1):
        return True
    if p == 4 or (S >= 82 and p == 2):
        return False

    return tcalc(S + 10, p + 1) or tcalc(S * 2, p + 1)


for i in range(1, 82):
    if tcalc(i, 0):
        print(i)

