class Auto:
    n = int(input("enter number:"))
    num=n
    sq = num*num
    while num>0:
        if num%10 != sq%10:
            print("its not a automarphic number")
            break
            num = num // 10
            sq = sq // 10


    else:
            print("automarphiic number")

    #        class Auto:
               # def __init__(self):
        #             n = int(input("Enter number: "))
        #             num = n
        #             sq = num * num
        #             while num > 0:
        #                 if num % 10 != sq % 10:
        #                     print("It's not an automorphic number")
        #                     break
        #                 num = num // 10
        #                 sq = sq // 10
        #             else:
        #                 print("Automorphic number")
        #
        #     # Creating an instance of the Auto class
        # #    auto_instance = Auto()
