# set elements using following methods:
mySet={}
print(mySet)
print("the size or length of set Is:", len(mySet))
homoSet={1,2,3,0,9,8,7 }
heteroSet={(88,45,67,23,90),"movies",True,'123',550.55}
print("original heteroset() are:", heteroSet)
heteroSet.remove((88,45,67,23,90))
print("original heteroset() are:", heteroSet)
heteroSet.pop()
print("after pop() heteroset is:", heteroSet)
homoSet.remove(0)
print("after remove() heteroset is:", homoSet)
homoSet.discard(1)
print("after discard() homoset are:", homoSet)
homoSet.add(90)
print("after add() homoset are:", homoSet)
heteroSet.clear()
print("clear after :", heteroSet)
# homoSet.add([13,13,14,531])
print("after adding list are:",homoSet )
homoSet.update([33,44,55,66])
print("after adding list are:",homoSet )
homoSet.remove(55)
print("after removing remove() :", homoSet)
print("----------------------------------------------------------")
# set operations
setA={1,2,3,6}
setB={4,5,6}
print("----------------------------------------------------------")
Union =setA.union(setB)
print("union of total set are:",Union)
intersect=setA.intersection(setB)
print("intersection of setA and SetB are",intersect)
print("------------------diffrence-------------------------------------")
setADiff=setA-setB
print("setA diffrence is",setADiff)
setBDiff = setB-setA
print("setB diffrence is",setBDiff)

print("------------symmetric--------------------------")
SetAsym=setA.symmetric_difference(setB)
print("symmetric of setA is",SetAsym)
SetBsym=setB.symmetric_difference(setA)
print("symmetric of setA is",SetBsym)
print("------------------------------------------")
setRemove=Union.remove(5)
print("setRemove()",Union)
Union.intersection(setB)
print("setintersection()",Union)
