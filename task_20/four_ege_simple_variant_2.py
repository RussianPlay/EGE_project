def calc(S, N, p):
    if S >= N and p == 3:
        return True
    if S >= N or (S < N and p == 3):
        return False

    if p % 2 != 0:
        return calc(S + 2, N, p + 1) and calc(S * 3, N, p + 1)
    else:
        return calc(S + 2, N, p + 1) or calc(S * 3, N, p + 1)


for i in range(0, 100):
    if calc(10, i, 0):
        print(i)
