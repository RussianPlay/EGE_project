cur_mns = []
for i in range(10000000, 1000000000000):
    N = i
    k = 2
    divs = [1]
    while k * k <= N:
        if N % k == 0:
            divs.append(k)
            k_ch = N // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    Mn = 0

    if len(divs) >= 2:
        divs.sort()
        Mn = Mn + divs[-1] + divs[-2]
    if 0 < Mn < 10000 and i > 10000000:
        cur_mns.append(Mn)
        if len(cur_mns) == 5:
            break

cur_mns.sort()
print(cur_mns)
