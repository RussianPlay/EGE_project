def tcalc(S, p):
    if S >= 34 and (p == 2 or p == 4):
        return True
    if (S < 34 and p == 4) or S >= 34:
        return False
    if p % 2 == 0:
        return tcalc(S + 1, p + 1) and tcalc(S + 2, p + 1) and tcalc(S * 2, p + 1)
    else:
        return tcalc(S + 1, p + 1) or tcalc(S + 2, p + 1) or tcalc(S * 2, p + 1)


def calc1(S, p):
    if S >= 34 and p == 2:
        return True
    if (S < 34 and p == 2) or S >= 34:
        return False
    if p % 2 == 0:
        return calc1(S + 1, p + 1) and calc1(S + 2, p + 1) and calc1(S * 2, p + 1)
    else:
        return calc1(S + 1, p + 1) or calc1(S + 2, p + 1) or calc1(S * 2, p + 1)


def calc2(S, p):
    if S >= 34 and p == 4:
        return True
    if (S < 34 and p == 4) or S >= 34:
        return False
    if p % 2 == 0:
        return calc2(S + 1, p + 1) and calc2(S + 2, p + 1) and calc2(S * 2, p + 1)
    else:
        return calc2(S + 1, p + 1) or calc2(S + 2, p + 1) or calc2(S * 2, p + 1)


for b in range(1, 33 + 1):
    if tcalc(b, 0):
        print(b)
print("---------------------")
for b in range(1, 33 + 1):
    if calc1(b, 0):
        print(b)
print("---------------------")
for b in range(1, 33 + 1):
    if calc2(b, 0):
        print(b)
