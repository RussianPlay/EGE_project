def tcalc(b1, S, p):
    if b1 + S <= 32 and (p == 2 or p == 4):
        return True
    if (b1 + S > 32 and p == 4) or b1 + S <= 32:
        return False
    if p % 2 == 0:
        return tcalc(b1 - 1, S, p + 1) and \
               tcalc(b1, S - 1, p + 1) and \
               tcalc(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) and \
               tcalc(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)
    else:
        return tcalc(b1 - 1, S, p + 1) or \
               tcalc(b1, S - 1, p + 1) or \
               tcalc(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) or \
               tcalc(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)


def calc1(b1, S, p):
    if b1 + S <= 32 and p == 2:
        return True
    if (b1 + S > 32 and p == 2) or b1 + S <= 32:
        return False
    if p % 2 == 0:
        return calc1(b1 - 1, S, p + 1) and \
               calc1(b1, S - 1, p + 1) and \
               calc1(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) and \
               calc1(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)
    else:
        return calc1(b1 - 1, S, p + 1) or \
               calc1(b1, S - 1, p + 1) or \
               calc1(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) or \
               calc1(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)


# def calc2(b1, S, p):
#     if b1 + S <= 32 and p == 4:
#         return True
#     if (b1 + S > 32 and p == 4) or b1 + S <= 32:
#         return False
#     if p % 2 == 0:
#         return calc2(b1 - 1, S, p + 1) and \
#                calc2(b1, S - 1, p + 1) and \
#                calc2(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) and \
#                calc2(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)
#     else:
#         return calc2(b1 - 1, S, p + 1) or \
#                calc2(b1, S - 1, p + 1) or \
#                calc2(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) or \
#                calc2(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)


for b2 in range(23, 1000):
    if tcalc(10, b2, 0):
        print(b2)
print("-------------------------")
for b2 in range(23, 1000):
    if calc1(10, b2, 0):
        print(b2)
print("-------------------------")
# for b2 in range(23, 1000):
#     if calc2(10, b2, 0):
#         print(b2)
# print("-------------------------")