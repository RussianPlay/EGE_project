with open("26_school_4.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    N = total[0]
    times = list(map(lambda x: list(map(int, x.split())), total[1:]))

initial_time = 1633305600
times = list(map(lambda x: [initial_time, x[1]] if x[0] == 0 else x, times))
times.sort(key=lambda x: x[0])
mx_processing_amount = -1
res_processing_amount = 0
total_ended_time = times[0][1]

for i in range(1, len(times)):
    if times[i][0] <= total_ended_time:
        res_processing_amount += 1
    else:
        mx_processing_amount = max(mx_processing_amount, res_processing_amount)
        res_processing_amount = 0
        total_ended_time = times[i][1]

print(mx_processing_amount)
