A_mx = 0
for A in range(1, 1000):
    lst_checks = []
    for x in range(1, 100000):
        check = (not(x % A == 0) and (x % 21 == 0)) <= (x % 14 == 0)
        lst_checks.append(check)
    if all(lst_checks):
        A_mx = max(A_mx, A)

print(A_mx)
