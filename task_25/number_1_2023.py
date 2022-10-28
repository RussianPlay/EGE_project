cur_lst = []
num = 520000
while len(cur_lst) != 5:
    num += 1
    k = 2
    res_num = num
    non_trivial_divs = []
    while k * k <= num:
        if num % k == 0:
            non_trivial_divs.append(k)
            k_ch = num // k
            if k_ch != k:
                non_trivial_divs.append(k_ch)
        k += 1
    if non_trivial_divs and str(sum(non_trivial_divs)) == str(sum(non_trivial_divs))[::-1]:
        cur_lst.append((num, max(non_trivial_divs)))

print("\n".join([f"{cur_num} {cur_div}" for cur_num, cur_div in cur_lst]))