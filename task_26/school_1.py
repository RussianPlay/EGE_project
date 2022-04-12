with open("26_school_1.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    N = total[0]
    pairs = list(map(lambda x: x.split(), total[1:]))
    data = {}
    for pair in pairs:
        if pair[0] not in data.keys():
            data[pair[0]] = [int(pair[1])]
        else:
            data[pair[0]].append(int(pair[1]))

    max_row_num = 0
    min_place_num = 100001
    for row_num, place_nums_lst in data.items():
        place_nums_lst.sort()
        print(place_nums_lst)
        if len(place_nums_lst) >= 4:
            for i in range(1, len(place_nums_lst) - 2):
                for j in range(1, len(place_nums_lst) - 2):

                    if i != j and abs(place_nums_lst[i] - place_nums_lst[j]) == 11:
                        max_row_num = max(max_row_num, row_num)
                        min_place_num = min(min_place_num, place_nums_lst[0] + 1)
    print(max_row_num, min_place_num)
