def tcalc(S, p):
    if S >= 129 and (p == 2 or p == 4):
        return True
    if S >= 129 or (S < 129 and p == 4):
        return False
    if p % 2 == 0:
        return tcalc(S + 1, p + 1) and tcalc(S * 2, p + 1)
    return tcalc(S + 1, p + 1) or tcalc(S * 2, p + 1)


def calc1(S, p):
    if S >= 129 and p == 2:
        return True
    if S >= 129 or (S < 129 and p == 2):
        return False
    if p % 2 == 0:
        return calc1(S + 1, p + 1) and calc1(S * 2, p + 1)
    return calc1(S + 1, p + 1) or calc1(S * 2, p + 1)


def calc2(S, p):
    if S >= 129 and p == 4:
        return True
    if S >= 129 or (S < 129 and p == 4):
        return False
    if p % 2 == 0:
        return calc2(S + 1, p + 1) and calc2(S * 2, p + 1)
    return calc2(S + 1, p + 1) or calc2(S * 2, p + 1)


for i in range(1, 129):
    if tcalc(i, 0):
        print(i)
print("----------------------------")
for i in range(1, 129):
    if calc1(i, 0):
        print(i)
print("-----------------------------")
for i in range(1, 129):
    if calc2(i, 0):
        print(i)