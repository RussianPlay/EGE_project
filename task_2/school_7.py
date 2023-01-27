from itertools import permutations
s = permutations([0, 1, 2, 3])
d = {0: "x", 1: "y", 2: "z", 3: "w"}
combs = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                combs.append((x, y, z,  w))

for com_comb in s:
    print(*map(lambda x: d[x], com_comb), "F")
    for comb in combs:
        F = (comb[com_comb[2]] <= comb[com_comb[0]]) <= (comb[com_comb[3]] or (not comb[com_comb[1]]))
        if int(F) == 0:
            unsorted_com = [comb[com_comb[0]], comb[com_comb[1]], comb[com_comb[2]], comb[com_comb[3]]]
            unsorted_com.sort(key=lambda x: com_comb.index(x))
            print(*unsorted_com, int(F))
    print("------")


