def calc(S, K, p):
    if S + K <= 18 and p == 1:
        return True
    if (S + K < 18 and p == 1) or S + K >= 18:
        return False
    return calc(S - 1, K, p + 1) or calc(S, K - 1, p + 1) or calc(S // 2 - 1, K, p + 1) or calc(S, K // 2 - 1, p + 1)


for b1 in range(1, 100):
    for b2 in range(1, 100):
        if b1 + b2 >= 19:
            if calc(b1, b1, 0):
                print(b1)