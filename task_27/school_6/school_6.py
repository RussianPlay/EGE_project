with open("Zadanie_27-B.txt", "r") as file:
    N = file.readline()
    nums = list(map(int, file.readlines()))

cur_pairs = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j]) % 1011 == 40 and i != j and nums[i] > nums[j]:
            cur_pairs.append((nums[i] + nums[j], [nums[i], nums[j]]))

amount_pairs = list(map(lambda x: x[0], cur_pairs))
print(cur_pairs[amount_pairs.index(min(amount_pairs))][1])
