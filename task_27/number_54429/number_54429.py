with open("test.txt", "r") as file:
    n = int(file.readline())
    s = []
    quantity_even_n = []
    quantity_odd_n = []
    diff = 10001
    for i in range(n):
        x, y = map(int, file.readline().split())
        minimum = min(x, y)
        s.append(minimum)
        if minimum % 2 == 0:
            quantity_even_n.append(minimum)
        else:
            quantity_odd_n.append(minimum)
        if abs(x - y) % 2 != 0:
            diff = min(diff, abs(x - y))
    quantity_odd_n.sort()
    print(sum(s))
    while len(quantity_even_n) <= len(quantity_odd_n):
        s.remove(quantity_odd_n.pop(0))
    s = sum(s)
    if s % 2 == 0:
        s -= diff
    print(s)