def calc(K, S, p):
    if K + S >= 63 and p == 2:
        return True
    if (K + S < 63 and p == 2) or K + S >= 63:
        return False
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 2, S, p + 1) or calc(K, S * 2, p + 1)


lst = []
for b2 in range(1, 58):
    if calc(5, b2, 0):
        lst.append(b2)
print(min(lst))