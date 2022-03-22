number = 437


def find_divs(n):
    divs = [1, n]
    k = 2
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    return divs


amount_of_bases = 0
for base in range(2, 11):
    number_base_n = ""
    res_num = number
    while res_num != 0:
        number_base_n = number_base_n + str(res_num % base)
        res_num //= base
    number_base_n = number_base_n[::-1]
    divs = find_divs(sum(map(int, list(number_base_n))))
    if len(divs) == 2:
        amount_of_bases += base
print(amount_of_bases)
