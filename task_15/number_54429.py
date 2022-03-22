P = list(range(20, 81))
Q = list(range(35, 58))
data = list(range(10000000))
minimum_length = None
A = []
for x in range(82, 1000):
    check = ((x in data) and ((x in Q) <= (x in P)))
    if not check:
        A.append(x)
    else:
        if A:
            if minimum_length is None:
                minimum_length = max(A) - min(A)
            else:
                minimum_length = min(minimum_length, max(A) - min(A))
            A = []

if minimum_length is None:
    minimum_length = 0
    
print(minimum_length)