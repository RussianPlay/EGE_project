def tcalc(S, p):
    if S > 37 and (p == 4 or p == 2):
        return True
    if (S <= 37 and p == 4) or S > 37:
        return False
    if p % 2 == 0:
        return tcalc(S + 1, p + 1) and tcalc(S + 2, p + 1) and tcalc(S + 3, p + 1) and tcalc(S * 2, p + 1)
    else:
        return tcalc(S + 1, p + 1) or tcalc(S + 2, p + 1) or tcalc(S + 3, p + 1) or tcalc(S * 2, p + 1)


def calc1(S, p):
    if S > 37 and p == 4:
        return True
    if (S <= 37 and p == 4) or S > 37:
        return False
    if p % 2 == 0:
        return calc1(S + 1, p + 1) and calc1(S + 2, p + 1) and calc1(S + 3, p + 1) and calc1(S * 2, p + 1)
    else:
        return calc1(S + 1, p + 1) or calc1(S + 2, p + 1) or calc1(S + 3, p + 1) or calc1(S * 2, p + 1)


def calc2(S, p):
    if S > 37 and p == 2:
        return True
    if (S <= 37 and p == 2) or S > 37:
        return False
    if p % 2 == 0:
        return calc2(S + 1, p + 1) and calc2(S + 2, p + 1) and calc2(S + 3, p + 1) and calc2(S * 2, p + 1)
    else:
        return calc2(S + 1, p + 1) or calc2(S + 2, p + 1) or calc2(S + 3, p + 1) or calc2(S * 2, p + 1)


for i in range(1, 37 + 1):
    if tcalc(i, 0):
        print(i)
print("------------------------")
for i in range(1, 37 + 1):
    if calc1(i, 0):
        print(i)
print("------------------------")
for i in range(1, 37 + 1):
    if calc2(i, 0):
        print(i)


