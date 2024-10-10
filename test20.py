#set
# unordered collection of unique elements
mySet1 = {"apple",1, True, "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana", "cherry", "banana"}
print(mySet1)
print(len(mySet1))
mySet1.add("orange")
print(mySet1)
mySet2 = {1,2,3,4,5}
mySet1.update(mySet2)
print(mySet1)
mySet1.discard("orange") 
print(mySet1)
mySet2.clear()
print(mySet2)


setA = {1,2,3,4,5,99}
setB = {4,5,6,7,8}
setD = {1,2,3,4,5,6,7,8,99}

setE = setA.issubset(setD)
print(setA.union(setB))
print(setA.intersection(setB))
print(setA.difference(setB))
print(setB.difference(setA))

setC = setA.copy()
print(setC)

print(setE)
