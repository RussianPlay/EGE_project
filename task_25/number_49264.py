mx_num = 0
k = 0

for i in range(125697, 190235):
    n = i
    divs = [1, i]
    k = 2

    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1

    if len(divs) >= 2:
        mx_num = max(mx_num, i)
        k += 1

print(k, mx_num)