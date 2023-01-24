def tcalc(S, K, p):
    if (K + S) >= 79 and (p == 2 or p == 4):
        return True
    if (K + S) >= 79 or ((K + S) < 79 and p == 4):
        return False

    if p % 2 == 0:
        return tcalc(S + 2, K, p + 1) and tcalc(S, K + 2, p + 1) and tcalc(S * 3, K, p + 1) and tcalc(S, K * 3, p + 1)
    else:
        return tcalc(S + 2, K, p + 1) or tcalc(S, K + 2, p + 1) or tcalc(S * 3, K, p + 1) or tcalc(S, K * 3, p + 1)


def calc1(S, K, p):
    if (K + S) >= 79 and p == 2:
        return True
    if (K + S) >= 79 or ((K + S) < 79 and p == 2):
        return False

    if p % 2 == 0:
        return calc1(S + 2, K, p + 1) and calc1(S, K + 2, p + 1) and calc1(S * 3, K, p + 1) and calc1(S, K * 3, p + 1)
    else:
        return calc1(S + 2, K, p + 1) or calc1(S, K + 2, p + 1) or calc1(S * 3, K, p + 1) or calc1(S, K * 3, p + 1)


def calc2(S, K, p):
    if (K + S) >= 79 and p == 4:
        return True
    if (K + S) >= 79 or ((K + S) < 79 and p == 4):
        return False

    if p % 2 == 0:
        return calc2(S + 2, K, p + 1) and calc2(S, K + 2, p + 1) and calc2(S * 3, K, p + 1) and calc2(S, K * 3, p + 1)
    else:
        return calc2(S + 2, K, p + 1) or calc2(S, K + 2, p + 1) or calc2(S * 3, K, p + 1) or calc2(S, K * 3, p + 1)


for n in range(1, 69 + 1):
    if tcalc(n, 9, 0):
        print(n)
print("-------------------------")
for n in range(1, 69 + 1):
    if calc1(n, 9, 0):
        print(n)
print("-------------------------")
for n in range(1, 69 + 1):
    if calc2(n, 9, 0):
        print(n)