for A in range(1, 1000):
    checks = []
    for x in range(1, 100):
        for z in range(1, 100):
            for y in range(1, 100):
                check = ((z % 115 == 0) or (y % 78 == 0) or (x % 51 == 0)) <= ((x * y * z) % A == 0)
                checks.append(check)
    if all(checks):
        print(A)
        break