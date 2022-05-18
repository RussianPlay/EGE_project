def calc(S, p):
    if S >= 34 and p == 2:
        return True
    if (S < 34 and p == 2) or S >= 34:
        return False
    if p % 2 == 0:
        return calc(S + 1, p + 1) and calc(S + 2, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 1, p + 1) or calc(S + 2, p + 1) or calc(S * 2, p + 1)


for b in range(1, 33 + 1):
    if calc(b, 0):
        print(b)
