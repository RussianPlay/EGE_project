def calc(S, p):
    if S == 1 and p == 2:
        return True
    elif (S == 1 and p == 1) or (S > 1 and p >= 2) or S < 1:
        return False
    if S % 2 == 0 and S % 3 == 0:
        return calc(S // 2, p + 1) or calc(S // 3, p + 1)
    elif S % 2 == 0 and S % 3 != 0:
        return calc(S // 2, p + 1) or calc(S - 3, p + 1)
    elif S % 2 != 0 and S % 3 == 0:
        return calc(S - 2, p + 1) or calc(S // 3, p + 1)
    elif S % 2 != 0 and S % 3 != 0:
        return calc(S - 2, p + 1) or calc(S - 3, p + 1)


max_cur_S = 0
for i in range(1, 38):
    if calc(i, 0):
        print(i)
        max_cur_S = max(max_cur_S, i)
print(max_cur_S)



