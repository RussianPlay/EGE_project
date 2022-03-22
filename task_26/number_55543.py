with open("26-k6_number_55543.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    N, K = map(int, total[0].split())
    pairs = list(map(lambda x: list(map(int, x.split())), total[1:]))
    costs = list(map(lambda x: x[1] / x[0], pairs))
    for i in range(len(pairs)):
        for j in range(len(pairs) - i - 1):
            kf1 = pairs[j][1] / pairs[j][0]
            kf2 = pairs[j + 1][1] / pairs[j + 1][0]
            if kf1 > kf2 or (kf1 == kf2 and pairs[j][0] < pairs[j + 1][0]):
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
    cur_pairs = pairs[0:K]
    mx_pair = max(cur_pairs, key=lambda x: x[0])
    print(sum(map(lambda x: x[0], cur_pairs)), mx_pair[1])

