def calc(K, S, p):
    if K + S >= 99 and p == 3:
        return True
    if K + S >= 99or (K + S < 99 and p == 3):
        return False
    if p % 2 != 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 3, S, p + 1) and calc(K, S * 3, p + 1)
    else:
        return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


k = 0
for b2 in range(1, 91):
    if calc(8, b2, 0):
        k += 1

print(k)
