for i in range(154026, 154044):
    divs = [1, i]
    k = 2
    n = i
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    if len(divs) == 4:
        divs.sort(reverse=True)
        print(divs[1], divs[0])