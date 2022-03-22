def calc(K, S, p):
    if K + S >= 81 and p == 3:
        return True
    if (K + S < 81 and p == 3) or K + S >= 81:
        return False
    if p % 2 == 1:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K + S, S, p + 1) and calc(K, S + K, p + 1)
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K + S, S, p + 1) or calc(K, S + K, p + 1)


lst = []
for b2 in range(1, 74):
    if calc(7, b2, 0):
        lst.append(b2)
print(min(lst))
print(max(lst))