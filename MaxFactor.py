class MaxFactor:
    max = 0
    for v1 in range(1, 51):
        if(50 % v1 ==0):
            for v2 in range (1, 61):
                if(60 % v2==0) and (v1 == v2):


                    print("common", v2 )

