def calc(b1, S,  p):
    if b1 + S <= 32 and p == 3:
        return True
    if (b1 + S > 32 and p == 3) or b1 + S <= 32:
        return False
    if p % 2 == 1:
        return calc(b1 - 1, S, p + 1) and \
               calc(b1, S - 1, p + 1) and \
               calc(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) and \
               calc(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)
    else:
        return calc(b1 - 1, S, p + 1) or \
               calc(b1, S - 1, p + 1) or \
               calc(b1 // 2 if b1 % 2 == 0 else b1 // 2 + 1, S, p + 1) or \
               calc(b1, S // 2 if S % 2 == 0 else S // 2 + 1, p + 1)


lst = []
for b2 in range(23, 100000):
    if calc(10, b2, 0):
        lst.append(b2)
print(min(lst), max(lst))
