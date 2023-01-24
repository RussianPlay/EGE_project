def calc(S, K, p):
    if (K + S) >= 79 and p == 2:
        return True
    if (K + S) >= 79 or ((K + S) < 79 and p == 2):
        return False

    return calc(S + 2, K, p + 1) or calc(S, K + 2, p + 1) or calc(S * 3, K, p + 1) or calc(S, K * 3, p + 1)


for n in range(1, 69 + 1):
    if calc(n, 9, 0):
        print(n)
        break
