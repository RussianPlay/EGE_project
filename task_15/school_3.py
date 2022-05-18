for A in range(-100, 1000):
    checks = []
    for x in range(100):
        for y in range(100):
            check = (x ** 2 + y ** 2 < A) or (x >= 4) or (y > 6)
            checks.append(check)
    if all(checks):
        print(A)
        break
