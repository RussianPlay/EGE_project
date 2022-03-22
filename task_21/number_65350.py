def calc(K, S, p):
    if K + S >= 81 and p % 2 == 0 and p > 1:
        return True
    if ((K + S < 81 and p % 2 == 0) or K + S >= 81) and p > 1:
        return False
    if p % 2 == 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 3, S, p + 1) and calc(K, S * 3, p + 1)
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


for b2 in range(1, 74):
    if calc(7, b2, 0):
        print(b2)