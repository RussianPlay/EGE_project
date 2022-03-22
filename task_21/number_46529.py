def total_calc(S, p):
    if S >= 30 and (p == 2 or p == 4):
        return True
    if (S < 30 and p == 4) or S >= 30:
        return False
    if p % 2 == 0:
        return total_calc(S + 2, p + 1) and total_calc(S + 3, p + 1) and total_calc(S * 2, p + 1)
    else:
        return total_calc(S + 2, p + 1) or total_calc(S + 3, p + 1) or total_calc(S * 2, p + 1)

def calc1(S, p):
    if S >= 30 and p == 2:
        return True
    if (S < 30 and p == 2) or S >= 30:
        return False
    if p % 2 == 0:
        return calc1(S + 2, p + 1) and calc1(S + 3, p + 1) and calc1(S * 2, p + 1)
    else:
        return calc1(S + 2, p + 1) or calc1(S + 3, p + 1) or calc1(S * 2, p + 1)

def calc2(S, p):
    if S >= 30 and p == 4:
        return True
    if (S < 30 and p == 4) or S >= 30:
        return False
    if p % 2 == 0:
        return calc2(S + 2, p + 1) and calc2(S + 3, p + 1) and calc2(S * 2, p + 1)
    else:
        return calc2(S + 2, p + 1) or calc2(S + 3, p + 1) or calc2(S * 2, p + 1)


for b in range(1, 30):
    if total_calc(b, 0):
        print(b)
print("==========")
for b in range(1, 30):
    if calc1(b, 0):
        print(b)
print("==========")
for b in range(1, 30):
    if calc2(b, 0):
        print(b)