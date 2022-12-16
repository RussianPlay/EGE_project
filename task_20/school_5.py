
def calc(S, p):
    if S >= 103 and p == 2:
        return True
    if S >= 103 or (S < 103 and p == 2):
        return False
    if p % 2 != 0:
        return (calc(S + 1, p + 1) if (S + 1) % 3 != 0 else False) and \
               (calc(S + 2, p + 1) if (S + 2) % 3 != 0 else False) and \
               (calc(S * 2, p + 1) if (S * 2) % 3 != 0 else False)

    if p % 2 == 0:
        return (calc(S + 1, p + 1) if (S + 1) % 3 != 0 else False) or \
               (calc(S + 2, p + 1) if (S + 2) % 3 != 0 else False) or \
               (calc(S * 2, p + 1) if (S * 2) % 3 != 0 else False)


for n in range(1, 102):
    if n % 3 != 0:
        if calc(n, 0):
            print(n)