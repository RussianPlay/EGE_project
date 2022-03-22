def finding():
    for A in range(1000):
        checks = []
        for x in range(1000):
            for y in range(1000):
                check = ((-5 * y + 3 * x) < A) or (x > 15) or (y > 30)
                checks.append(check)
        if all(checks):
            return A


print(finding())