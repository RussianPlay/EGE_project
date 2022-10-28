with open("test.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    pairs = list(map(lambda x: list(map(int, x.split())), total[1:]))

s = {0: 0}
min_s = 0
remainder = 0
for a, b in pairs:
    min_s += min(a, b)
    sums = [s[j] + k for j in s for k in (a, b)]
    s = {x % 7: x for x in sorted(sums)}
remainder = min_s % 7
print(s[remainder])