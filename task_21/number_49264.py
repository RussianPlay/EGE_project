def tcalc(K, S, p):
    if K + S >= 129 and (p == 2 or p == 4):
        return True
    elif (K + S < 129 and p == 4) or K + S >= 129:
        return False
    if p % 2 == 0:
        return tcalc(K + 1, S, p + 1) and tcalc(K, S + 1, p + 1) and tcalc(K * 4, S, p + 1) and tcalc(K, S * 4, p + 1)
    return tcalc(K + 1, S, p + 1) or tcalc(K, S + 1, p + 1) or tcalc(K * 4, S, p + 1) or tcalc(K, S * 4, p + 1)

def calc1(K, S, p):
    if K + S >= 129 and p == 2:
        return True
    elif (K + S < 129 and p == 4) or K + S >= 129:
        return False
    if p % 2 == 0:
        return calc1(K + 1, S, p + 1) and calc1(K, S + 1, p + 1) and calc1(K * 4, S, p + 1) and calc1(K, S * 4, p + 1)
    return calc1(K + 1, S, p + 1) or calc1(K, S + 1, p + 1) or calc1(K * 4, S, p + 1) or calc1(K, S * 4, p + 1)


def calc2(K, S, p):
    if K + S >= 129 and p == 4:
        return True
    elif (K + S < 129 and p == 4) or K + S >= 129:
        return False
    if p % 2 == 0:
        return calc2(K + 1, S, p + 1) and calc2(K, S + 1, p + 1) and calc2(K * 4, S, p + 1) and calc2(K, S * 4, p + 1)
    return calc2(K + 1, S, p + 1) or calc2(K, S + 1, p + 1) or calc2(K * 4, S, p + 1) or calc2(K, S * 4, p + 1)


for b2 in range(1, 125):
    if tcalc(4, b2, 0):
        print(b2)
print("---------------------------------")
for b2 in range(1, 125):
    if calc1(4, b2, 0):
        print(b2)
print("---------------------------------")
for b2 in range(1, 125):
    if calc2(4, b2, 0):
        print(b2)
print("---------------------------------")