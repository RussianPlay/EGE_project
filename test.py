def calc(S, p):
    if 100 >= S >= 65 and p == 3:
        return True
    if 100 >= S >= 65 or ((S < 65 or S > 100) and p == 3):
        return False
    if p % 2 != 0:
        return calc(S + 1, p + 1) and calc(S * 3, p + 1)
    if p % 2 == 0:
        return calc(S + 1, p + 1) or calc(S * 3, p + 1)


for n in range(1, 65):
    if calc(n, 0):
        print(n)

