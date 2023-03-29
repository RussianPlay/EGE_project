for A in range(1, 1000):
    checks = []
    for x in range(1, 1000):
        check = ((x % 2 == 0) <= (not (x % 5 == 0)) or (x + A >= 90))
        checks.append(check)
    if all(checks):
        print(A)
        break
