def finding():
    for n in range(1, 1000):
        checks = []
        for m in range(1, 1000):
            check = (n % 3 == 0) and (220 % m == 0) <= ((not(n % m == 0)) <= (not(550 % m == 0)))
            checks.append(check)
        if all(checks):
            return n


print(finding())
