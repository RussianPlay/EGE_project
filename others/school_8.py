with open("11ost_school_8.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    N, S = map(int, total[0].split())
    data = dict()
    lst = []
    for t in total[1:]:
        value, key = t.split()
        lst.append((key, int(value)))
    lst.sort(key=lambda x: x[1])
    cur_k_E = 0
    inds = []
    for i in range(len(lst) - 1):
        if lst[i][1] == lst[i + 1][1] and lst[i][0] != "E":
            inds.append(i)
        elif lst[i][1] == lst[i + 1][1] and lst[i][0] == "E":
            lst[inds[0]], lst[i] = lst[i], lst[inds[0]]
            inds.pop(0)
        else:
            inds = []
    for cell in lst:
        if (S - cell[1]) >= 0:
            S -= cell[1]
            if cell[0] == "E":
                cur_k_E += 1
        else:
            break
    print(cur_k_E, S)