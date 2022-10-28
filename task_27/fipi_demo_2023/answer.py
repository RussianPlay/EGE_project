with open("27_B.txt", "r") as file:
    total = list(map(str.strip, file. readlines()))
N = int(total[0])
dist_and_quantity = list(map(lambda x: list(map(int, x.split())), total[1:]))
points = []
lst_costs = []
right = 0
left = 0
cost = 0
for i in range(len(dist_and_quantity)):
    if dist_and_quantity[i][1] % 36 == 0:
        containers = dist_and_quantity[i][1] // 36
    else:
        containers = dist_and_quantity[i][1] // 36 + 1
    points.append((dist_and_quantity[i][0], containers))
res =[]
# calculation cost for first point
for i in range(1, len(points)):
    cost += (points[i][0] - points[0][0]) * points[i][1]
    right += points[i][1]
    res.append(points[i][1])
lst_costs.append(cost)

# calculation cost for others points
for i in range(1, len(points)):
    left += points[i - 1][1]
    cost = (points[i][0] - points[i - 1][0]) * left + lst_costs[-1] - (points[i][0] - points[i - 1][0]) * right
    right -= points[i][1]
    lst_costs.append(cost)
print(min(lst_costs))