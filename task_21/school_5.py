def tcalc(S, p):
    if S >= 103 and (p == 2 or p == 4):
        return True
    if S >= 103 or (S < 103 and p == 4):
        return False
    if p % 2 == 0:
        return (tcalc(S + 1, p + 1) if (S + 1) % 3 != 0 else False) and \
               (tcalc(S + 2, p + 1) if (S + 2) % 3 != 0 else False) and \
               (tcalc(S * 2, p + 1) if (S * 2) % 3 != 0 else False)

    if p % 2 != 0:
        return (tcalc(S + 1, p + 1) if (S + 1) % 3 != 0 else False) or \
               (tcalc(S + 2, p + 1) if (S + 2) % 3 != 0 else False) or \
               (tcalc(S * 2, p + 1) if (S * 2) % 3 != 0 else False)


def calc1(S, p):
    if S >= 103 and p == 2:
        return True
    if S >= 103 or (S < 103 and p == 2):
        return False
    if p % 2 == 0:
        return (calc1(S + 1, p + 1) if (S + 1) % 3 != 0 else False) and \
               (calc1(S + 2, p + 1) if (S + 2) % 3 != 0 else False) and \
               (calc1(S * 2, p + 1) if (S * 2) % 3 != 0 else False)

    if p % 2 != 0:
        return (calc1(S + 1, p + 1) if (S + 1) % 3 != 0 else False) or \
               (calc1(S + 2, p + 1) if (S + 2) % 3 != 0 else False) or \
               (calc1(S * 2, p + 1) if (S * 2) % 3 != 0 else False)


def calc2(S, p):
    if S >= 103 and p == 4:
        return True
    if S >= 103 or (S < 103 and p == 4):
        return False
    if p % 2 == 0:
        return (calc2(S + 1, p + 1) if (S + 1) % 3 != 0 else False) and \
               (calc2(S + 2, p + 1) if (S + 2) % 3 != 0 else False) and \
               (calc2(S * 2, p + 1) if (S * 2) % 3 != 0 else False)

    if p % 2 != 0:
        return (calc2(S + 1, p + 1) if (S + 1) % 3 != 0 else False) or \
               (calc2(S + 2, p + 1) if (S + 2) % 3 != 0 else False) or \
               (calc2(S * 2, p + 1) if (S * 2) % 3 != 0 else False)


for n in range(1, 102):
    if n % 3 != 0:
        if tcalc(n, 0):
            print(n)
print("----------------------------------------")
for n in range(1, 102):
    if n % 3 != 0:
        if calc1(n, 0):
            print(n)
print("----------------------------------------")
for n in range(1, 102):
    if n % 3 != 0:
        if calc2(n, 0):
            print(n)