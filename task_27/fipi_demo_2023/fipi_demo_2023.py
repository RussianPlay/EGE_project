with open("27_A.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    N = int(total[0])
    lst_med_places = list(map(lambda x: list(map(int, x.split())), total[1:]))

container_capacity = 36
min_amount_delivery = 10**100
for lab_ind in range(len(lst_med_places)):
    amount_delivery = 0
    for med_ind in range(len(lst_med_places)):
        if lab_ind != med_ind:
            if lst_med_places[med_ind][1] % container_capacity != 0:
                num_containers = lst_med_places[med_ind][1] // container_capacity + 1
            else:
                num_containers = lst_med_places[med_ind][1] // container_capacity
            amount_delivery += abs(lst_med_places[lab_ind][0] - lst_med_places[med_ind][0]) * num_containers
    min_amount_delivery = min(min_amount_delivery, amount_delivery)

print(min_amount_delivery)


with open("27_B.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
    N = int(total[0])
    lst_med_places = list(map(lambda x: list(map(int, x.split())), total[1:]))

container_capacity = 36
lst_med_places = list(map(
    lambda x: [x[0], x[1] // container_capacity if x[1] % container_capacity == 0 else x[1] // container_capacity + 1],
    lst_med_places))
first_amount_things = 0
right_side = 0
left_side = 0
total_amounts_delivery = []
for ind in range(1, N):
    first_amount_things += lst_med_places[ind][1] * (lst_med_places[ind][0] - lst_med_places[0][0])
    right_side += lst_med_places[ind][1] # we look at the original

total_amounts_delivery.append(first_amount_things)
for ind in range(1, N):
    left_side += lst_med_places[ind - 1][1]
    total_amounts_delivery.append(
        total_amounts_delivery[-1] - right_side * (lst_med_places[ind][0] - lst_med_places[ind - 1][0])
        + left_side * (lst_med_places[ind][0] - lst_med_places[ind - 1][0]))
    right_side -= lst_med_places[ind][1]

print(min(total_amounts_delivery))


