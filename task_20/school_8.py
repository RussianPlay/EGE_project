def calc(S, p):
    if S > 45 and p == 3:
        return True
    if S > 45 or (S <= 45 and p == 3):
        return False
    if p % 2 != 0:
        return calc(S + 1, p + 1) and calc(S * 2, p + 1)
    else:
        return calc(S + 1, p + 1) or calc(S * 2, p + 1)


for i in range(1, 45 + 1):
    if calc(i, 0):
        print(i)
