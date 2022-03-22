def calc(S, p):
    if S >= 30 and p == 3:
        return True
    if (S < 30 and p == 3) or S >= 30:
        return False
    if p % 2 == 1:
        return calc(S + 2, p + 1) and calc(S + 3, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 2, p + 1) or calc(S + 3, p + 1) or calc(S * 2, p + 1)

k = 0
for b in range(1, 30):
    if calc(b, 0):
        k += 1
print(k)