N = 0
x1 = "1*0"
x2 = "56*"


def calc():
    for n1 in range(10):
        for n2 in range(10):
            whole_x1 = x1.replace("*", str(n1))
            whole_x2 = x2.replace("*", str(n2))
            try:
                if int(whole_x1, 16) == int(whole_x2, 8):
                    return int(whole_x1, 16)
            except ValueError:
                pass


print(calc())
