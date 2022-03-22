N = 99
diff = 0
while diff != 63:
    N += 1
    cur_n = sorted(str(N))
    dis_zero_n = list(filter(lambda x: x != "0", cur_n))
    nmax = "".join(sorted(cur_n, reverse=True))[:2]
    cur_min_n = cur_n.copy()
    cur_min_n.remove(dis_zero_n[0])
    nmin = "".join(dis_zero_n[0]) + cur_min_n[0]
    diff = int(nmax) - int(nmin)
print(N)