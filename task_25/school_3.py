k_lst = []

for k in range(1, 1000000):
    if len(k_lst) != 5:
        num = 9 * 10 ** 8 + k
        divs = [num]
        divd = 2
        check_failed = 0
        while divd * divd <= num:
            if num % divd == 0:
                if divd % 2 == 0:
                    divs.append(divd)
                else:
                    check_failed = 1
                    break

                divd_ch = num // divd
                if divd_ch != divd:
                    if divd_ch % 2 == 0:
                        divs.append(divd_ch)
                    else:
                        check_failed = 1
                        break
            divd += 1
        if not check_failed and len(divs) % 2 != 0:
            k_lst.append(k)

print("\n".join(map(str, sorted(k_lst))))
