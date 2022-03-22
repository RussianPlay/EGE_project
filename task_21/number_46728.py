def calc(b1, S, p):
    if b1 + S >= 79 and (p == 2 or p == 4):
        return True
    if (b1 + S < 79 and p == 4) or b1 + S >= 79:
        return False
    if p % 2 == 1:
        return calc(b1 + 2, S, p + 1) or calc(b1, S + 2, p + 1) or calc(b1 * 2, S, p + 1) or calc(b1, S * 2, p + 1)
    else:
        return calc(b1 + 2, S, p + 1) and calc(b1, S + 2, p + 1) and calc(b1 * 2, S, p + 1) and calc(b1, S * 2, p + 1)


def calc1(b1, S, p):
    if b1 + S >= 79 and p == 2:
        return True
    if (b1 + S < 79 and p == 2) or b1 + S >= 79:
        return False
    if p % 2 == 1:
        return calc1(b1 + 2, S, p + 1) or calc1(b1, S + 2, p + 1) or calc1(b1 * 2, S, p + 1) or calc1(b1, S * 2, p + 1)
    else:
        return calc1(b1 + 2, S, p + 1) and calc1(b1, S + 2, p + 1) and calc1(b1 * 2, S, p + 1) and calc1(b1, S * 2, p + 1)


def calc2(b1, S, p):
    if b1 + S >= 79 and p == 4:
        return True
    if (b1 + S < 79 and p == 4) or b1 + S >= 79:
        return False
    if p % 2 == 1:
        return calc2(b1 + 2, S, p + 1) or calc2(b1, S + 2, p + 1) or calc2(b1 * 2, S, p + 1) or calc2(b1, S * 2, p + 1)
    else:
        return calc2(b1 + 2, S, p + 1) and calc2(b1, S + 2, p + 1) and calc2(b1 * 2, S, p + 1) and calc2(b1, S * 2, p + 1)


for i in range(1, 70):
    if calc(9, i, 0):
        print(i)
print("==========")
for i in range(1, 70):
    if calc1(9, i, 0):
        print(i)
print("==========")
for i in range(1, 70):
    if calc2(9, i, 0):
        print(i)
