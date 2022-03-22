def calc(K, S, p):
    if K + S >= 59 and p == 2:
        return True
    if (K + S < 59 and p == 2) or K + S >= 59:
        return False
    return calc(K + 2, S, p + 1) or calc(K, S + 2, p + 1) or calc(K * 2, S, p + 1) or calc(K, S * 2, p + 1)


lst = []
for i in range(1, 54):
    if calc(5, i, 0):
        lst.append(i)
print(min(lst))