for m in range(10000):
    checks = []
    for n in range(1000):
        try:
            check = (n % 18 == 0) <= ((not(n % m == 0)) <= (not(n % 12 == 0)))
            checks.append(check)
        except ZeroDivisionError:
            checks.append(False)
    if all(checks):
        print(m)

