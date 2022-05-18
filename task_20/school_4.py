def calc(S, p):
    if S >= 34 and p == 3:
        return True
    if (S < 34 and p == 3) or S >= 34:
        return False
    if p % 2 != 0:
        return calc(S + 1, p + 1) and calc(S + 2, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 1, p + 1) or calc(S + 2, p + 1) or calc(S * 2, p + 1)


lst_b = []
for b in range(1, 33 + 1):
    if calc(b, 0):
        lst_b.append(b)

print(min(lst_b), max(lst_b))
