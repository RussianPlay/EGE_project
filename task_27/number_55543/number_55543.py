with open("27-81a.txt", "r") as file:
    total = list(map(lambda x: int(x.rstrip()), file.readlines()))
    N = total[0]
    K = 13
    numbers = total[1:]
    odd_inds = [i if numbers[i] % 2 != 0 else None for i in range(len(numbers))]
    while None in odd_inds:
        odd_inds.remove(None)
    mx_amount = 0
    for i in range(len(odd_inds) // K + 1 if len(odd_inds) / K > len(odd_inds) // K else len(odd_inds) // K):
        amount = 0
        cur_ind_odds = odd_inds[i: i + K]
        for j in range(0, cur_ind_odds[0]):
            if numbers[j] % 2 != 0:
                amount = 0
            else:
                amount += numbers[j]
        if cur_ind_odds[-1] != len(numbers) - 1:
            for num in numbers[cur_ind_odds[-1] + 1:len(numbers)]:
                if num % 2 != 0:
                    break
                else:
                    amount += num

        mx_amount = max(mx_amount, amount + sum(numbers[cur_ind_odds[0]:cur_ind_odds[-1] + 1]))
    print(mx_amount)

