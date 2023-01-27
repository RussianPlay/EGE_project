def calc(S, p):
    if S >= 82 and p == 2:
        return True
    if p == 3:
        return False

    if p % 2 != 0:
        return calc(S + 10, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 10, p + 1) or calc(S * 2, p + 1)


for i in range(1, 82):
    if calc(i, 0):
        print(i)