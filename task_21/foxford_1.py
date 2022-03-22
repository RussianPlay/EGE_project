def tcalc(K, S, p):
    if (K + S) >= 79 and (p == 2 or p == 4):
        return True
    elif ((K + S) < 79 and p == 4) or (K + S) >= 79:
        return False
    if p % 2 == 0:
        return tcalc(K + 2, S, p + 1) and tcalc(K, S + 2, p + 1) and tcalc(K * 3, S, p + 1) and tcalc(K, S * 3, p + 1)
    else:
        return tcalc(K + 2, S, p + 1) or tcalc(K, S + 2, p + 1) or tcalc(K * 3, S, p + 1) or tcalc(K, S * 3, p + 1)


def calc1(K, S, p):
    if (K + S) >= 79 and p == 2:
        return True
    elif ((K + S) < 79 and p == 2) or (K + S) >= 79:
        return False
    if p % 2 == 0:
        return calc1(K + 2, S, p + 1) and calc1(K, S + 2, p + 1) and calc1(K * 3, S, p + 1) and calc1(K, S * 3, p + 1)
    else:
        return calc1(K + 2, S, p + 1) or calc1(K, S + 2, p + 1) or calc1(K * 3, S, p + 1) or calc1(K, S * 3, p + 1)


def calc2(K, S, p):
    if (K + S) >= 79 and p == 4:
        return True
    elif ((K + S) < 79 and p == 4) or (K + S) >= 79:
        return False
    if p % 2 == 0:
        return calc2(K + 2, S, p + 1) and calc2(K, S + 2, p + 1) and calc2(K * 3, S, p + 1) and calc2(K, S * 3, p + 1)
    else:
        return calc2(K + 2, S, p + 1) or calc2(K, S + 2, p + 1) or calc2(K * 3, S, p + 1) or calc2(K, S * 3, p + 1)


print("-----------------------------------")
for n in range(1, 69 + 1):
    if tcalc(9, n, 0):
        print(n)
print("------------------------------------")
for n in range(1, 69 + 1):
    if calc1(9, n, 0):
        print(n)
print("-------------------------------------")
for n in range(1, 69 + 1):
    if calc2(9, n, 0):
        print(n)
print("--------------------------------------")