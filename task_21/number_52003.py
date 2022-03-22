def total_calc(K, S, p):
    if K + S >= 59 and (p == 2 or p == 4):
        return True
    if (K + S < 59 and p == 4) or K + S >= 59:
        return False
    if p % 2 == 0:
        return total_calc(K + 2, S, p + 1) and total_calc(K, S + 2, p + 1) and total_calc(K * 2, S, p + 1) and total_calc(K, S * 2, p + 1)
    return total_calc(K + 2, S, p + 1) or total_calc(K, S + 2, p + 1) or total_calc(K * 2, S, p + 1) or total_calc(K, S * 2, p + 1)


def calc1(K, S, p):
    if K + S >= 59 and p == 2:
        return True
    if (K + S < 59 and p == 4) or K + S >= 59:
        return False
    if p % 2 == 0:
        return calc1(K + 2, S, p + 1) and calc1(K, S + 2, p + 1) and calc1(K * 2, S, p + 1) and calc1(K, S * 2, p + 1)
    return calc1(K + 2, S, p + 1) or calc1(K, S + 2, p + 1) or calc1(K * 2, S, p + 1) or calc1(K, S * 2, p + 1)


def calc2(K, S, p):
    if K + S >= 59 and p == 4:
        return True
    if (K + S < 59 and p == 4) or K + S >= 59:
        return False
    if p % 2 == 0:
        return calc2(K + 2, S, p + 1) and calc2(K, S + 2, p + 1) and calc2(K * 2, S, p + 1) and calc2(K, S * 2, p + 1)
    return calc2(K + 2, S, p + 1) or calc2(K, S + 2, p + 1) or calc2(K * 2, S, p + 1) or calc2(K, S * 2, p + 1)


for i in range(1, 54):
    if total_calc(5, i, 0):
        print(i)
print("================")
for i in range(1, 54):
    if calc1(5, i, 0):
        print(i)
print("================")
for i in range(1, 54):
    if calc2(5, i, 0):
        print(i)
