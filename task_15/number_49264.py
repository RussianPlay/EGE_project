mx_A = 0

for A in range(1, 10000):
    lst_of_checks = []
    for x in range(1, 10000):
        f = (70 % A == 0) and ((not(x % A == 0)) <= ((x % 35 == 0) <= (not(x % 63 == 0))))
        lst_of_checks.append(f)
    if all(lst_of_checks):
        mx_A = max(mx_A, A)

print(mx_A)
