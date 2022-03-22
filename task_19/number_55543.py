def calc(K, S, p):
    if K + S >= 99 and p == 2:
        return True
    if (K + S < 99 and p == 2) or K + S >= 99:
        return False
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


for b2 in range(1, 91):
    if calc(8, b2, 0):
        print(b2)
        break
