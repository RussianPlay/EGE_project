def calc(S, p):
    if S >= 30 and p == 2:
        return True
    if (S < 30 and p == 2) or S >= 30:
        return False
    if p % 2 == 0:
        return calc(S + 2, p + 1) and calc(S + 3, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 2, p + 1) or calc(S + 3, p + 1) or calc(S * 2, p + 1)


lst = []
for b in range(1, 30):
    if calc(b, 0):
        lst.append(b)
print(min(lst))