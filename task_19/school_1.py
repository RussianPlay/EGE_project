def calc(K, S, p):
    if K + S >= 223 and p == 2:
        return True
    if K + S >= 223 or (K + S < 223 and p == 2):
        return False
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 2, S, p + 1) or calc(K, S * 2, p + 1)


for b2 in range(1, 206):
    if calc(17, b2, 0):
        print(b2)
        break
