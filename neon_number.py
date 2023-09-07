class Neon:
    k = int(input("enter a number:"))
    sq = k*k
    s=0
    while sq>0 :
        s=s+sq%10
        sq = sq // 10
    if k==s :
        print("its a neon number",s)
    else:
        print("not a neon number")