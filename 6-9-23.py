#create a file list
emptylist=[]
print("the empty list is:",emptylist)
print("the size or number of items in the list is:",len(emptylist))
print("the data type of emptyLIst ", type(emptylist))
homogeneousList = [1,2,3,4,5,6,7,8,9]
heterogeneousList=["names","fruits",10.33,"clss",24,False,5,2,1,34,'Names',True]
print(heterogeneousList[3:6])
hList = list([10,20,30,"marks","school0",True])
c1=0
# for items in hList[::-1]:
#     c1 += 1
#     print("reverse order of",c1,"is ", items)
#     c=0
# for i in hList:
#     c+=1
#     print("item", c,"is", i)
#     print("the data type of 3th one is",type(hList[3]))
nestedList=["myLIst",[1,2,3,4,5],3.45,"fruits",["apple","bannana","mango"]]
print(nestedList[1][3])
print(nestedList[4][0])
nestedList.append("movies")
print("after appending nested list is:", nestedList)
nestedList.insert(1,44)
print("after inserting nested list is:", nestedList)
nestedList.pop()
print("after removing value:",nestedList)
nestedList.remove(3.45)
print("after removing by remove() nested list is:", nestedList)
# nestedList.clear()
print("after clearing values are:", nestedList)
nestedList.insert(5,"frame")
print("deleting the nested list", nestedList)

print("count of nestedlist is:", nestedList.count("fruits"))
print("the data type of nestedlist is:", type(nestedList))