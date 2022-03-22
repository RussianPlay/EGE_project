def calc(S, K, p):
    if S + K <= 18 and p == 3:
        return True
    if (S + K <= 18 and p == 1) or S + K >= 18:
        return False
    if p % 2 == 0:
        return calc(S - 1, K, p + 1) or calc(S, K - 1, p + 1) or calc(S // 2 if S % 2 == 0 else S // 2 + 1, K, p + 1) or calc(S, S // 2 if K % 2 == 0 else K // 2 + 1, p + 1)
    else:
        return calc(S - 1, K, p + 1) and calc(S, K - 1, p + 1) or calc(S // 2 if S % 2 == 0 else S // 2 + 1, K, p + 1) and calc(S, S // 2 if K % 2 == 0 else K // 2 + 1, p + 1)


for b1 in range(1, 100):
    if calc(b1, 13, 0):
        print(b1)