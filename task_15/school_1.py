def calculation():
    for A in range(-1000, 1000):
        checks = []
        for n in range(1, 100000):
            check = ((n % 3 == 0) <= (not(n % 5 == 0))) or (n + A >= 70)
            checks.append(check)
        if all(checks):
            return A


print(calculation())
