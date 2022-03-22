counter = 0
for i in range(2532000, 2532160 + 1):
    divs = [1, i]
    k = 2
    n = i
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n % k
            if k_ch != k:
                divs.append(k)
        k += 1
    if len(divs) == 2:
        if counter % 3 == 0:
            print(counter + 1, i)
        counter += 1

    