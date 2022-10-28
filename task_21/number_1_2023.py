def tcalc(S, p):
    if S == 1 and (p == 2 or p == 4):
        return True
    elif (S == 1 and (p == 1 or p == 3)) or (S > 1 and p >= 4) or S < 1:
        return False
    if p % 2 == 0:
        if S % 2 == 0 and S % 3 == 0:
            return tcalc(S // 2, p + 1) and tcalc(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return tcalc(S // 2, p + 1) and tcalc(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return tcalc(S - 2, p + 1) and tcalc(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return tcalc(S - 2, p + 1) and tcalc(S - 3, p + 1)
    else:
        if S % 2 == 0 and S % 3 == 0:
            return tcalc(S // 2, p + 1) or tcalc(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return tcalc(S // 2, p + 1) or tcalc(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return tcalc(S - 2, p + 1) or tcalc(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return tcalc(S - 2, p + 1) or tcalc(S - 3, p + 1)


def calc1(S, p):
    if S == 1 and p == 2:
        return True
    elif (S == 1 and (p == 1 or p == 3)) or (S > 1 and p >= 4) or S < 1:
        return False
    if p % 2 == 0:
        if S % 2 == 0 and S % 3 == 0:
            return calc1(S // 2, p + 1) and calc1(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc1(S // 2, p + 1) and calc1(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc1(S - 2, p + 1) and calc1(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc1(S - 2, p + 1) and calc1(S - 3, p + 1)
    else:
        if S % 2 == 0 and S % 3 == 0:
            return calc1(S // 2, p + 1) or calc1(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc1(S // 2, p + 1) or calc1(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc1(S - 2, p + 1) or calc1(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc1(S - 2, p + 1) or calc1(S - 3, p + 1)


def calc2(S, p):
    if S == 1 and p == 4:
        return True
    elif (S == 1 and (p == 1 or p == 3)) or (S > 1 and p >= 4) or S < 1:
        return False
    if p % 2 == 0:
        if S % 2 == 0 and S % 3 == 0:
            return calc2(S // 2, p + 1) and calc2(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc2(S // 2, p + 1) and calc2(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc2(S - 2, p + 1) and calc2(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc2(S - 2, p + 1) and calc2(S - 3, p + 1)
    else:
        if S % 2 == 0 and S % 3 == 0:
            return calc2(S // 2, p + 1) or calc2(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc2(S // 2, p + 1) or calc2(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc2(S - 2, p + 1) or calc2(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc2(S - 2, p + 1) or calc2(S - 3, p + 1)


for i in range(1, 38):
    if tcalc(i, 0):
        print(i)
print("-------------------------------------------------")
for i in range(1, 38):
    if calc1(i, 0):
        print(i)
print("-------------------------------------------------")
for i in range(1, 38):
    if calc2(i, 0):
        print(i)
