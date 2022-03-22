def calc(K, S, p):
    if (K + S) >= 79 and p == 3:
        return True
    elif ((K + S) < 79 and p == 3) or (K + S) >= 79:
        return False
    if p % 2 != 0:
        return calc(K + 2, S, p + 1) and calc(K, S + 2, p + 1) and calc(K * 3, S, p + 1) and calc(K, S * 3, p + 1)
    else:
        return calc(K + 2, S, p + 1) or calc(K, S + 2, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


for n in range(1, 69 + 1):
    if calc(9, n, 0):
        print(n)
