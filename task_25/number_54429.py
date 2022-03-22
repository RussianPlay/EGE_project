prime_numbers = []
number_id = 1
for i in range(1547341, 1547410):
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
    if len(divs) == 2:
        print(number_id, i)
        number_id += 1
