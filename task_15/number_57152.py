lst = []
for m in range(1000):
    checks = []
    for n in range(1000):
        try:
            check = ((120 % m == 0) and ((n % 70 == 0) and (n % 30 == 0)) <= (n % m == 0))
            checks.append(check)
        except ZeroDivisionError:
            checks.append(False)
    if all(checks):
        lst.append(m)
print(lst)
print(max(lst))