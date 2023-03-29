def tcalc(S, p):
    if S >= 26 and (p == 5 or p == 3 or p == 1):
        return True
    elif S >= 26 or (S < 26 and p == 5):
        return False

    if S % 2 != 0:
        if p % 2 != 0:
            return tcalc(S + 1, p + 1) and tcalc(S + 2, p + 1) and tcalc(S * 2, p + 1)
        else:
            return tcalc(S + 1, p + 1) or tcalc(S + 2, p + 1) or tcalc(S * 2, p + 1)
    else:
        if p % 2 != 0:
            return tcalc(S + 1, p + 1) and tcalc(S + 2, p + 1)
        else:
            return tcalc(S + 1, p + 1) or tcalc(S + 2, p + 1)


def calc1(S, p):
    if S >= 26 and p == 1:
        return True
    elif S >= 26 or (S < 26 and p == 5):
        return False

    if S % 2 != 0:
        if p % 2 != 0:
            return calc1(S + 1, p + 1) and calc1(S + 2, p + 1) and calc1(S * 2, p + 1)
        else:
            return calc1(S + 1, p + 1) or calc1(S + 2, p + 1) or calc1(S * 2, p + 1)
    else:
        if p % 2 != 0:
            return calc1(S + 1, p + 1) and calc1(S + 2, p + 1)
        else:
            return calc1(S + 1, p + 1) or calc1(S + 2, p + 1)


def calc2(S, p):
    if S >= 26 and p == 3:
        return True
    elif S >= 26 or (S < 26 and p == 5):
        return False

    if S % 2 != 0:
        if p % 2 != 0:
            return calc2(S + 1, p + 1) and calc2(S + 2, p + 1) and calc2(S * 2, p + 1)
        else:
            return calc2(S + 1, p + 1) or calc2(S + 2, p + 1) or calc2(S * 2, p + 1)
    else:
        if p % 2 != 0:
            return calc2(S + 1, p + 1) and calc2(S + 2, p + 1)
        else:
            return calc2(S + 1, p + 1) or calc2(S + 2, p + 1)


for i in range(1, 26):
    if tcalc(i, 0):
        print(i)
print("----------------------")
for i in range(1, 26):
    if calc1(i, 0):
        print(i)
print("----------------------")
for i in range(1, 26):
    if calc2(i, 0):
        print(i)
print("----------------------")