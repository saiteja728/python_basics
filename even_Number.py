class Even:
    r=range(10,16)
    for x in r[2:5]:
        print(x)
    list = [10,12,14,16]
    list2 = ["jva" , "pythohn"]
    list.append(17)
    list.insert(2,23)
   # list.remove()
    list.pop(2)
    list.extend(list2)
    print(list)
    s = "python"
    print(s[0])
    print(s[1:4])
    if s[1] == s[-5]:
        print("happy")