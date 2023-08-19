class PrimeNumber:
    a = int(input("Enter number:"))
    c=0
    flag=0
    c=a
  #  k=c/2
    if(c==0 and c==1):
        print("not a prime number")
    else:
        for value in range(2 , int(c**.5)+1):
            if(c%value==0):
                print("its not prime")
                flag=1
    if(flag==0):
        print("its a prime")
