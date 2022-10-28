import sys
sys.setrecursionlimit(3000)


def F(n):
    if n == 1:
        return n
    elif n > 1:
        return n * F(n - 1)


num_1 = F(2023)
num_2 = F(2020)
print(num_1 / num_2)