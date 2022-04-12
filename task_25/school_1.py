num = "12345?6?8"
lst = []

for n1 in range(0, 10):
    for n2 in range(0, 10):
        res = num.replace("?", str(n1), 1)
        res = res.replace("?", str(n2), 1)
        res = int(res)
        if res % 17 == 0:
            lst.append(res)


for num in sorted(lst):
    print(num, num // 17)