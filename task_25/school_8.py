for n in range(2 ** 8 + 1, 2 ** 10):
    num = n
    k = 2
    divs = [n]
    while k * k <= num:
        if num % k == 0:
            divs.append(k)
            k_ch = num // k
            if k_ch != k:
                divs.append(k)
        k += 1
    if len(divs) >= 5:
        M = divs[0] * divs[1] * divs[2] * divs[3] * divs[4]
        S = sum(divs)
        if M % 2 != 0 and 0 < S < 10000:
            print(S, M)