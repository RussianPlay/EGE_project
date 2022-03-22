def calc(b1, S, p):
    if b1 + S >= 79 and p == 2:
        return True
    if b1 + S < 79 and p == 2:
        return False
    return calc(b1 + 2, S, p + 1) or calc(b1, S + 2, p + 1) or calc(b1 * 2, S, p + 1) or calc(b1, S * 2, p + 1)


for i in range(1, 70):
    if calc(9, i, 0):
        print(i)
        break
