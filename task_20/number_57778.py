def calc(K, S, p):
    if K + S >= 63 and p == 3:
        return True
    if (K + S < 63 and p == 3) or K + S >= 63:
        return False
    if p % 2 == 1:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 2, S, p + 1) and calc(K, S * 2, p + 1)
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 2, S, p + 1) or calc(K, S * 2, p + 1)


for b2 in range(1, 58):
    if calc(5, b2, 0):
        print(b2)