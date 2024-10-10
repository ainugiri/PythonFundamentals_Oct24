myTuple1 = (1,2,3,4,5)
myTuple2 = ("apple", "banana", "cherry")
myTuple3 = (True, False, False, True)
myTuple4 = (1, 2, 3, 4, "apple", "banana", "cherry", True, False)
print(myTuple1)
print(myTuple2)
print(myTuple3)
print(len(myTuple4))
print(myTuple1)

tuple5 = ("orange",)
# myTuple2 = myTuple2 + tuple5
myTuple2 += tuple5
print(myTuple2)

myListfromTuple = list(myTuple2)
print(myListfromTuple)

for x in myTuple2:
    print(x)

print("----------------------")
for i in range(len(myTuple2)):
    print(myTuple2[i])
print("----------------------")