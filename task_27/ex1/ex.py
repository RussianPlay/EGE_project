n = int(input())
amount = 0
mn_diff = 10000


for i in range(n):
    a, b = map(int, input().split())
    amount += max(a, b)
    diff = abs(a - b)
    if mn_diff > diff and diff % 3 != 0:
        mn_diff = abs(a - b)

if amount % 3 == 0:
    amount -= mn_diff
print(amount)
