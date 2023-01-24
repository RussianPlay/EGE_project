for n in range(185348, 185399 + 1):
    num = n
    divs = [] # 1 and current num is not included
    k = 2
    while k * k <= num:
        if num % k == 0:
            divs.append(k)
            k_ch = num // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1

    if len(divs) == 2:
        print(",".join(map(str, divs)))