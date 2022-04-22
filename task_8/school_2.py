num1_with_base = "144"
num2_with_base = "24"
answer_with_base = "201"
base = 2
answer = -1
while True:
    try:
        num1 = int(num1_with_base, base)
        num2 = int(num2_with_base, base)
        answer = int(answer_with_base, base)
        if num1 + num2 == answer:
            print(base)
            break
    except Exception:
        pass
    base += 1
