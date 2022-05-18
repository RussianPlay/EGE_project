with open("27-B_school_4.txt", "r") as file:
    total = list(map(lambda x: int(x.strip()), file.readlines()))
    N = total[0]
    numbers = total[1:]

mx_amount = -1
total_amounts = []
res_seq = []
for i in numbers:
    res_seq.append(i)
    if len(list(filter(lambda x: x % 2 == 0 and x >= 0, res_seq))) % 30 == 0:
        total_amounts.append(sum(res_seq))
        res_seq = []

cur_amount = 0
for seq_amount in total_amounts:
    if seq_amount > 0:
        cur_amount += seq_amount
    else:
        mx_amount = max(mx_amount, cur_amount)
        cur_amount = 0


total_amounts = []
res_seq = []
for i in numbers[1:]:
    res_seq.append(i)
    if len(list(filter(lambda x: x % 2 == 0 and x >= 0, res_seq))) % 30 == 0:
        total_amounts.append(sum(res_seq))
        res_seq = []

cur_amount = 0
for seq_amount in total_amounts:
    if seq_amount > 0:
        cur_amount += seq_amount
    else:
        mx_amount = max(mx_amount, cur_amount)
        cur_amount = 0

print(mx_amount)
