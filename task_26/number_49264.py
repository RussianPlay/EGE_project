with open("26-9_number_49264.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    S, N = map(int, total[0].split())
    sorted_sizes = list(sorted(map(int, total[1:])))

f_size = 0
mx_size = 0
k = 0
for size in sorted_sizes:
    if (f_size + size) < S:
        k += 1
        f_size += size
        mx_size = max(mx_size, size)
    else:
        break

cur_part_amount = sum(sorted_sizes[:k - 1])
for size in sorted_sizes[k:]:
    if (cur_part_amount + size) < S:
        mx_size = max(mx_size, size)

print(k, mx_size)

