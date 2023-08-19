class Practice_2:
     fact=1
     s=0
     a = int(input("enter number:"))
     b=a
     while(a!=0):
        r = a % 10
        fact = 1
        for values in range(1,r+1):

            fact=values*fact
        s = s+fact
        a = a // 10
     if(b==s) :
        print("its a strong number",s)
     else:
         print("its not a strong number",s)




