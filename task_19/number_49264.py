def calc(K, S, p):
    if K + S >= 129 and p == 2:
        return True
    elif (K + S < 129 and p == 2) or K + S >= 129:
        return False
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 4, S, p + 1) or calc(K, S * 4, p + 1)


for b2 in range(1, 125):
    if calc(4, b2, 0):
        print(b2)
        break
