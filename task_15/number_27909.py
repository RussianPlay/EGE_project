def calc():
    for A in range(-1000, 100):
        checks = []
        for x in range(1000):
            for y in range(100):
                check = (y + 2 * x < A) or (x > 20) or (y > 30)
                checks.append(check)
        if all(checks):
            return A


print(calc())
