def creating_text(n):
    text = ">" + "0" * 39 + "1" * n + "2" * 39
    while ">1" in text or ">2" in text or ">0" in text:
        if ">1" in text:
            text = text.replace(">1", "22>", 1)
        if ">2" in text:
            text = text.replace(">2", "2>", 1)
        if ">0" in text:
            text = text.replace(">0", "1>", 1)
    return text


def checking_for_prime_num(num):
    k = 2
    divs = [1, num]
    while (k * k) <= num:
        if num % k == 0:
            divs.append(k)
            k_ch = num // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    return len(divs) == 2


if __name__ == "__main__":
    for i in range(99999999):
        total_text = creating_text(i)
        amount_digital_values = sum(map(lambda x: int(x) if x.isdigit() else 0, total_text))
        if checking_for_prime_num(amount_digital_values):
            print(i)
            break

