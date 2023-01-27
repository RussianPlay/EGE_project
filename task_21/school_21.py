def tcalc(S, p):
    if S >= 82 and (p == 4 or p == 2):
        return True
    if p == 4 or (S >= 82 and p == 3):
        return False

    return tcalc(S + 10, p + 1) or tcalc(S * 2, p + 1)


def calc1(S, p):
    if S >= 82 and p == 2:
        return True
    if p == 4 or (S >= 82 and p == 3):
        return False

    return calc1(S + 10, p + 1) or calc1(S * 2, p + 1)


def calc2(S, p):
    if S >= 82 and p == 4:
        return True
    if p == 4 or (S >= 82 and p == 3):
        return False

    return calc2(S + 10, p + 1) or calc2(S * 2, p + 1)


for i in range(1, 82):
    if tcalc(i, 0):
        print(i)
print("----------")
for i in range(1, 82):
    if calc1(i, 0):
        print(i)
print("--------")
for i in range(1, 82):
    if calc2(i, 0):
        print(i)
