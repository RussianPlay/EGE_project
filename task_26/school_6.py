with open("26_school_6.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))

S, N = map(int, total[0].split())
cell_sizes = list(sorted(map(int, total[1:])))
lst_contained_cell_sizes = []
amount_contained_cell_sizes = 0

for cell_size in cell_sizes:
    if (amount_contained_cell_sizes + cell_size) <= S:
        lst_contained_cell_sizes.append(cell_size)
        amount_contained_cell_sizes += cell_size
    else:
        break

mx_size = max(lst_contained_cell_sizes)
other_cur_sizes = list(filter(
    lambda x: mx_size < x <= (S - amount_contained_cell_sizes + mx_size),
    cell_sizes))
if other_cur_sizes:
    mx_size = max(other_cur_sizes)

print(f"{len(lst_contained_cell_sizes)},{mx_size}")
