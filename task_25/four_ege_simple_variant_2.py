for i in range(135790, 163228 + 1):
    n = i
    k = 2
    divs = []
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1

    amount_divs = sum(divs)
    if amount_divs > 460000:
        print(len(divs), amount_divs)