# my_list  =[1,2,3,4,5,6,7,8,7]
# copy_list = my_list.copy()
# print("using copy() :",copy_list)
# print("count() is for how may occurences of particular value",my_list.count(7))
# print("index(value)",my_list.index(2))
# #updating
# my_list[0]=2
# print("after updating by using index:",my_list)
# #extending
# my_list.extend({10,22,12})
# print("after extending it adds end of list:",my_list)
# #slicing
# print("using slicing reverse :",my_list[::-1])
# print("SLICE",my_list[::-2])
# my_list.remove(5)
# print("remove(value)",my_list)
# my_list.pop(1)
# print("pop(index) :",my_list)
# my_list.insert(20,7)
# print("inserting elements,insert(index,value):",my_list)
# my_list.append(9)
# print("appending elements:",my_list)
# my_list.clear()
# print("after clearing the elements",my_list)
#
# print("--------------------------------------------------------------------")
# tuple1 =(11,22,33,44,55)
# print(tuple1.count(3))
print("----------------------------------------------------------------------------")
myset ={1,2,3,4,5,6,7,8}
mylist2 ={7,8,9,10,11}
print("symmetric diffrence of  both ",myset.symmetric_difference(mylist2))
print("myset-mylist2 =",myset-mylist2)
print("intersection of both:",myset.intersection(mylist2))
print("union of set is:",myset.union(mylist2))
myset.add(7)
print("add(value)",myset)
myset.pop()
print("pop() ",myset)#removes first element no index
myset.discard(7)
print("discard(value) using",myset)
#diffrence b/w discard and remove is discard will not throw error remove will throw error
#if the value is doesn't exist
myset.remove(6)
print("remove(value)==>",myset)

myset.copy()

print(myset)

