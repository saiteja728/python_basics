try:
    n1 = int(input("enter first number:"))
    n2 = int(input("enter second number:"))
    div = n1/n2
except(ValueError,ZeroDivisionError):
    print("do not enter string,alpha numeric ,special symbols values.. ")
    print("don't enter zero as second value")

else:
    print("value of n1:",n1)
    print("value of n2:",n2)
    print("DIVISION OF BOTH IS:",div)