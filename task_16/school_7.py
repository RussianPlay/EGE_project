import sys
sys.setrecursionlimit(50000)


def F(n):
    if n == 1:
        return 2
    else:
        return F(n - 1) * ((3 ** (3 % 5)) / (3 ** (n % 7)))


print(F(1025) / F(1030))