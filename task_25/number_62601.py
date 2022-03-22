cur_divs = []
for n in range(157898, 157990 + 1):
    divs = [1, n]
    k = 2
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    if len(divs) == 6:
        cur_divs.append(list(reversed(sorted(divs[2:])))[:2])


for divs in cur_divs:
    print(' '.join(map(str, divs)))
