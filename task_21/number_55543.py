def calc1(K, S, p):
    if K + S >= 99 and p == 3:
        return True
    if K + S >= 99or (K + S < 99 and p == 3):
        return False
    if p % 2 != 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 3, S, p + 1) and calc(K, S * 3, p + 1)
    else:
        return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


def calc2(K, S, p):
    if K + S >= 99 and p == 3:
        return True
    if K + S >= 99or (K + S < 99 and p == 3):
        return False
    if p % 2 != 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 3, S, p + 1) and calc(K, S * 3, p + 1)
    else:
        return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


for b2 in range(1, 91):
    if calc1(8, b2, 0):
        print(b2)
print("----------")
for b2 in range(1, 91):
    if calc2(8, b2, 0):
        print(b2)
