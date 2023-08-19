class Practice:
    x=121
    su=0
    while x!=0 :
        reminder = x%10
        sum = su * 10 + reminder
        x = x//10

    if su == x:
        print("polindrome")
    else:
        print("not polindrome")


