num = "1" * 33 + "2" * 33
lst_ftr = []
for i in range(100):
    res = num + "3" * i
    while "11" in res or "22" in res or "13" in res or "23" in res:
        res = res.replace("11", "2", 1)
        res = res.replace("22", "1", 1)
        res = res.replace("13", "2", 1)
        res = res.replace("23", "1", 1)
    print(res)
    lst_ftr.append(res.count("3"))
print(lst_ftr)
print(min(lst_ftr))
