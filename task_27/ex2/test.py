n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
length_part = len(lst) - 7
mx_part1 = max(lst[:length_part])
mx_part2 = max(lst[length_part:])
maximum_amount = mx_part1 + mx_part2
print(maximum_amount)