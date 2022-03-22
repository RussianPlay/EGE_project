with open("27-2b.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    N = int(total[0])
    pairs = total[1:]
mn_diff = 100000000001
amount = 0
for i in range(N):
    num1, num2 = map(int, pairs[i].split())
    amount += max(num1, num2)
    if abs(num1 - num2) % 3 == 0:
        mn_diff = min(mn_diff, abs(num1 - num2))

if amount % 3 != 0:
    amount -= mn_diff
print(amount)

