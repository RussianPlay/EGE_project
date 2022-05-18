def calc(K, S, p):
    if K + S >= 62 and p == 3:
        return True
    if (K + S < 62 and p == 3) or K + S >= 62:
        return False
    if p % 2 != 0:
        return calc(K + 3, S, p + 1) and calc(K * 2, S, p + 1) and calc(K, S + 3, p + 1) and calc(K, S * 2, p + 1)
    else:
        return calc(K + 3, S, p + 1) or calc(K * 2, S, p + 1) or calc(K, S + 3, p + 1) or calc(K, S * 2, p + 1)


for b2 in range(1, 55):
    if calc(7, b2, 0):
        print(b2)
        break
