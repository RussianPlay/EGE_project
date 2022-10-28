def tcalc(S, N, p):
    if S >= N and (p == 2 or p == 4):
        return True
    if S >= N or (S < N and p == 4):
        return False

    if p % 2 == 0:
        return tcalc(S + 2, N, p + 1) and tcalc(S * 3, N, p + 1)
    else:
        return tcalc(S + 2, N, p + 1) or tcalc(S * 3, N, p + 1)


def calc1(S, N, p):
    if S >= N and p == 2:
        return True
    if S >= N or (S < N and p == 2):
        return False

    if p % 2 == 0:
        return calc1(S + 2, N, p + 1) and calc1(S * 3, N, p + 1)
    else:
        return calc1(S + 2, N, p + 1) or calc1(S * 3, N, p + 1)


def calc2(S, N, p):
    if S >= N and p == 4:
        return True
    if S >= N or (S < N and p == 4):
        return False

    if p % 2 == 0:
        return calc2(S + 2, N, p + 1) and calc2(S * 3, N, p + 1)
    else:
        return calc2(S + 2, N, p + 1) or calc2(S * 3, N, p + 1)


for i in range(0, 100):
    if tcalc(5, i, 0):
        print(i)
print("----------------------------------")
for i in range(0, 100):
    if calc1(5, i, 0):
        print(i)
print("----------------------------------")
for i in range(0, 100):
    if calc2(5, i, 0):
        print(i)