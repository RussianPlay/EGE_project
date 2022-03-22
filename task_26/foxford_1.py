with open("foxford_1.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    S, N = map(int, total[0].split())
    sizes = list(map(int, total[1:]))

k = 0
amount = 0
mx_size = 0
sizes.sort()
for size in sizes:
    if (amount + size) < S:
        amount += size
        mx_size = max(mx_size, size)
        k += 1
    else:
        break

cur_part_amount = sum(sizes[:k - 1])
for size in sizes[k:]:
    if (cur_part_amount + size) < S:
        mx_size = max(mx_size, size)

print(k, mx_size)