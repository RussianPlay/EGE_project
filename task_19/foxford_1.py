def calc(K, S, p):
    if (K + S) >= 79 and p == 2:
        return True
    elif ((K + S) < 79 and p == 2) or (K + S) >= 79:
        return False
    return calc(K + 2, S, p + 1) or calc(K, S + 2, p + 1) or calc(K * 3, S, p + 1) or calc(K, S * 3, p + 1)


lst = []
for n in range(1, 69 + 1):
    if calc(9, n, 0):
        lst.append(n)
print(min(lst))
