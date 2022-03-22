with open("27-39b.txt", "r") as file:
    total = list(map(str.rstrip, file.readlines()))
    N = int(total[0])
    tnumbers = total[1:]
numbers = tnumbers.copy()
amount = 0
check = 0
identical_nums = []
symmetric_pairs = []

for i in range(N):
    num = tnumbers[i]
    if len(set(list(num))) == 1:
        numbers.remove(num)
        identical_nums.append(num)

for i in range(N):
    num = tnumbers[i]
    rev_num = "".join(reversed(num))

    if numbers.count(rev_num) > 0 and num in numbers and rev_num in numbers:  # DO. don't stay like this!
        numbers.remove(num)
        numbers.remove(rev_num)
        symmetric_pairs.append((num, rev_num))


identical_nums.sort(reverse=True)
for num in identical_nums:
    if identical_nums.count(num) == 1:
        if check == 0:
            amount += sum(map(int, "".join(num)))
            check = 1
    elif identical_nums.count(num) % 2 == 0:
        amount += sum(map(int, "".join(num)))
    elif identical_nums.count(num) % 2 != 0:
        if check == 0:
            amount += sum(map(int, "".join(num)))
            check = 1
        else:
            amount += sum(map(int, "".join(num)))

for pair in symmetric_pairs:
    amount += sum(map(int, list(pair[0] + pair[1])))

print(amount)