lst = []
for m in range(1000):
    checks = []
    for n in range(10000):
        try:
            check = ((n % (m - 21) == 0) and (n % (40 - m) == 0)) <= (n % 90 == 0)
            checks.append(check)
        except ZeroDivisionError:
            checks.append(False)
    if all(checks):
        lst.append(m)
print(min(lst))
