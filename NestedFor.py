class NestedFor:
    list1 = [4,5,6,5,2,2,4]
    list2 = []
    seen =  list()
    for item in list1 :
        if item in seen:
          list2.append(item)

        else:
            seen.append(item)

    print(list2)
 #   print(seen)
