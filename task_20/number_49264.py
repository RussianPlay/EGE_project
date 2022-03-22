def calc(K, S, p):
    if K + S >= 129 and p == 3:
        return True
    elif (K + S < 129 and p == 3) or K + S >= 129:
        return False
    if p % 2 != 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 4, S, p + 1) and calc(K, S * 4, p + 1)
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 4, S, p + 1) or calc(K, S * 4, p + 1)


lst = []
for b2 in range(1, 125):
    if calc(4, b2, 0):
        lst.append(b2)
        
print(" ".join(map(str, sorted(lst))))
