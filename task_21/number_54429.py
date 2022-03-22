def calc(K, S, p):
    if K + S >= 75 and (p == 2 or p == 4):
        return True
    if (K + S < 75 and p == 4) or K + S >= 75:
        return False
    if p % 2 == 0:
        return calc(K + 1, S, p + 1) and calc(K, S + 1, p + 1) and calc(K * 2, S, p + 1) and calc(K, S * 2, p + 1)
    return calc(K + 1, S, p + 1) or calc(K, S + 1, p + 1) or calc(K * 2, S, p + 1) or calc(K, S * 2, p + 1)


current_s_values = []
for b2 in range(1, 67):
    if calc(8, b2, 0):
        current_s_values.append(b2)
print(min(current_s_values))