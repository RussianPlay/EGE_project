with open("Zimnii_EGE_27_A.txt", "r") as file:
    pairs = list(map(lambda x: list(map(int, x.rstrip().split())), file.readlines()))

mn_diff = 10001
amount = 0
for pair in pairs:
    amount = amount + max(pair)
    diff = abs(pair[0] - pair[1])
    if diff < mn_diff and diff % 4 != 0:
        mn_diff = diff

if amount % 4 == 0 and mn_diff == 10001:
    amount = 0
elif amount % 4 == 0:
    amount -= mn_diff

print(amount)


with open("Zimnii_EGE_27_B.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    N = total[0]
    pairs = list(map(lambda x: list(map(int, x.rstrip().split())), total[1:]))


mn_diff = 10001
amount = 0
for pair in pairs:
    amount = amount + max(pair)
    diff = abs(pair[0] - pair[1])
    if diff < mn_diff and diff % 4 != 0:
        mn_diff = diff

if amount % 4 == 0 and mn_diff == 10001:
    amount = 0
elif amount % 4 == 0:
    amount -= mn_diff

print(amount)
