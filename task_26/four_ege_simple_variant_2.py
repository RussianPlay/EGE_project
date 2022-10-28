with open("26_four_ege_simple_variant_2.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    S, N = map(int, total[0].split())
    sizes = list(sorted(map(int, total[1:]), reverse=True))

min_saved_size = S
k_saved_sizes = 0
for cur_size in sizes:
    if S >= cur_size:
        S -= cur_size
        min_saved_size = min(min_saved_size, cur_size)
        k_saved_sizes += 1

print(k_saved_sizes, min_saved_size)