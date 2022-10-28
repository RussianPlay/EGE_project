def calc(S, p):
    if S == 1 and p == 3:
        return True
    elif (S == 1 and p == 2) or (S > 1 and p >= 3) or S < 1:
        return False
    if p % 2 != 0:
        if S % 2 == 0 and S % 3 == 0:
            return calc(S // 2, p + 1) and calc(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc(S // 2, p + 1) and calc(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc(S - 2, p + 1) and calc(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc(S - 2, p + 1) and calc(S - 3, p + 1)
    else:
        if S % 2 == 0 and S % 3 == 0:
            return calc(S // 2, p + 1) or calc(S // 3, p + 1)
        elif S % 2 == 0 and S % 3 != 0:
            return calc(S // 2, p + 1) or calc(S - 3, p + 1)
        elif S % 2 != 0 and S % 3 == 0:
            return calc(S - 2, p + 1) or calc(S // 3, p + 1)
        elif S % 2 != 0 and S % 3 != 0:
            return calc(S - 2, p + 1) or calc(S - 3, p + 1)


res_lst = []
for i in range(1, 38):
    if calc(i, 0):
        res_lst.append(i)
print(min(res_lst), max(res_lst))
