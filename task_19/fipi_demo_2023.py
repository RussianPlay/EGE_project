def calc(S, p):
    if S >= 129 and p == 2:
        return True
    if S >= 129 or (S < 129 and p == 2):
        return False
    if p % 2 == 0:
        return calc(S + 1, p + 1) and calc(S * 2, p + 1)
    return calc(S + 1, p + 1) or calc(S * 2, p + 1)


lst = []
for i in range(1, 129):
    if calc(i, 0):
        print(i)