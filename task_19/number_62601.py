def calc(S, p):
    if S > 37 and p == 2:
        return True
    if (S <= 37 and p == 2) or S > 37:
        return False
    if p % 2 == 0:
        return calc(S + 1, p + 1) and calc(S + 2, p + 1) and calc(S + 3, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 1, p + 1) or calc(S + 2, p + 1) or calc(S + 3, p + 1) or calc(S * 2, p + 1)


for i in range(1, 37 + 1):
    if calc(i, 0):
        print(i)
