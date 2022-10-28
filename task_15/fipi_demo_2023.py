for A in range(1, 999999):
    lst_checks = []
    for n in range(1, 10000):
        check = ((n % 2 == 0) <= (not(n % 3 == 0))) or ((n + A) >= 100)
        lst_checks.append(check)
    if all(lst_checks):
        print(A)
        break
