def finding():
    for A in range(1000):
        checks = []
        for x in range(1000):
            for y in range(1000):
                check = ((x * y) < 2 * A) or (x >= 19) or (x < (6 * y))
                checks.append(check)
        if all(checks):
            return A


print(finding())