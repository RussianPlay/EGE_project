with open("17_school_7.txt", "r") as file:
    nums = list(map(int, file.readlines()))
df_mx = sum(map(int, str(max(nums)))) / len(list(map(int, str(max(nums)))))
df_mn = sum(map(int, str(min(nums)))) / len(list(map(int, str(min(nums)))))
k = 9
for i in range(len(nums) // 2):
    num1 = nums[i]
    num2 = nums[(i + 1) * -1]
    if (num1 > df_mn and num2 < df_mx) or (num1 < df_mn and num2 > df_mx):
        k += 1
print(k)