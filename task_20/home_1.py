def calc(S, p):
    if S >= 26 and p == 3:
        return True
    if S >= 26 or (S < 26 and p == 3):
        return False

    if S % 2 != 0:
        if p % 2 != 0 or p == 1:
            return calc(S + 1, p + 1) and calc(S + 2, p + 1) and calc(S * 2, p + 1)
        else:
            return calc(S * 2, p + 1) or calc(S + 1, p + 1) or calc(S + 2, p + 1)
    else:
        if p % 2 != 0:
            return calc(S + 1, p + 1) and calc(S + 2, p + 1)
        else:
            return calc(S + 1, p + 1) or calc(S + 2, p + 1)


for i in range(1, 26):
    if calc(i, 0):
        print(i)
