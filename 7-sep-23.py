myTouple=()
homogeneous_Tuple=([1,22,55.9,0,7,2,5,2] )
heterogeneous_Tuple=(["schools",34,"colleges",71.3,"universities",False,666.06])
result=homogeneous_Tuple.count(2)
print("count of 2 result is ", result)
print("homogeneous tuples are", homogeneous_Tuple)

heterogeneous_Tuple.insert(4,88)
print("afer inserting into tuple are :", heterogeneous_Tuple)
print("after slicing the tuple are:", heterogeneous_Tuple[::-2])
hetro =((1,2,3),5,"name",True)
# concatination_Tuple=homogeneous_Tuple+hetro
# print("concatination of both tuples are:", concatination_Tuple)
firtst_tuple=(1,2,3)
second_tuple=([4,5,6])
# combine=firtst_tuple+second_tuple
# print(combine)
second_tuple.append(firtst_tuple)
print("after appending second tuple and first tuple are:", second_tuple)
c=5
print( second_tuple[3][1])
while second_tuple[1]!=0 :
    if len(second_tuple)==c :
        c+=1
        print(second_tuple)


