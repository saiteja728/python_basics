# Python program to find the factorial of a number provided by the user.

# change the value for a different result
class Factorial:
    p=121
    sum1=0
    while p!=0 :
        rem = p%10
        sum = sum1*10+rem

        p= p/10

    if(p==sum1):
        print(sum1)
        print(p)
        print('polindrome')
    else:
        print("not plindrome")

