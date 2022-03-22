maximum_number_divs = []
for i in range(286564, 287271):
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
    if len(maximum_number_divs) < len(divs):
        maximum_number_divs = divs
print(len(maximum_number_divs), sorted(
    maximum_number_divs, reverse=True)[1])