def total_calc(K, S, p):
    if K + S >= 81 and (p == 2 or p == 4):
        return True
    if (K + S < 81 and p == 4) or K + S >= 81:
        return False
    if p % 2 == 0:
        return total_calc(K + 1, S, p + 1) and total_calc(K, S + 1, p + 1) and total_calc(K + S, S, p + 1) and total_calc(K, S + K, p + 1)
    return total_calc(K + 1, S, p + 1) or total_calc(K, S + 1, p + 1) or total_calc(K + S, S, p + 1) or total_calc(K, S + K, p + 1)


def calc1(K, S, p):
    if K + S >= 81 and p == 2:
        return True
    if (K + S < 81 and p == 2) or K + S >= 81:
        return False
    if p % 2 == 0:
        return calc1(K + 1, S, p + 1) and calc1(K, S + 1, p + 1) and calc1(K + S, S, p + 1) and calc1(K, S + K, p + 1)
    return calc1(K + 1, S, p + 1) or calc1(K, S + 1, p + 1) or calc1(K + S, S, p + 1) or calc1(K, S + K, p + 1)


def calc2(K, S, p):
    if K + S >= 81 and p == 4:
        return True
    if (K + S < 81 and p == 4) or K + S >= 81:
        return False
    if p % 2 == 0:
        return calc2(K + 1, S, p + 1) and calc2(K, S + 1, p + 1) and calc2(K + S, S, p + 1) and calc2(K, S + K, p + 1)
    return calc2(K + 1, S, p + 1) or calc2(K, S + 1, p + 1) or calc2(K + S, S, p + 1) or calc2(K, S + K, p + 1)


for b2 in range(1, 74):
    if total_calc(7, b2, 0):
        print(b2)
print("=================")
for b2 in range(1, 74):
    if calc1(7, b2, 0):
        print(b2)
print("=================")
for b2 in range(1, 74):
    if calc2(7, b2, 0):
        print(b2)