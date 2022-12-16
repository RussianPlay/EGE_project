for A in range(-1000, 1000):
    lst_checks = []
    for x in range(1, 1000):
        check = ((72 % x == 0) <= (not(120 % x == 0))) or ((A - x) > 100)
        lst_checks.append(check)
    if all(lst_checks):
        print(A)
        break
