for i in range(194465, 194550 + 1):
    divs = []
    k = 2
    n = i
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    divs.sort()
    if len(set(divs)) == 4:
        print(i, " ".join(map(str, divs[-2:])))