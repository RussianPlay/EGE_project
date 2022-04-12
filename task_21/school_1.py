def tcalc(K, S, p):
    if K + S >= 223 and (p == 2 or p == 4):
        return True
    if K + S >= 223 or (K + S < 223 and p == 4):
        return False

    if p % 2 == 0:
        return tcalc(K + 1, S, p + 1) and tcalc(K, S + 1, p + 1) and tcalc(K * 2, S, p + 1) and tcalc(K, S * 2, p + 1)
    else:
        return tcalc(K + 1, S, p + 1) or tcalc(K, S + 1, p + 1) or tcalc(K * 2, S, p + 1) or tcalc(K, S * 2, p + 1)


def calc1(K, S, p):
    if K + S >= 223 and p == 2:
        return True
    if K + S >= 223 or (K + S < 223 and p == 2):
        return False

    if p % 2 == 0:
        return calc1(K + 1, S, p + 1) and calc1(K, S + 1, p + 1) and calc1(K * 2, S, p + 1) and calc1(K, S * 2, p + 1)
    else:
        return calc1(K + 1, S, p + 1) or calc1(K, S + 1, p + 1) or calc1(K * 2, S, p + 1) or calc1(K, S * 2, p + 1)


for b2 in range(1, 206):
    if tcalc(17, b2, 0):
        print(b2)
print("-------------------------------------")
for b2 in range(1, 206):
    if calc1(17, b2, 0):
        print(b2)

