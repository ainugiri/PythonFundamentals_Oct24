"""
    List
    store multiple values in a single variable
    myList = [1, 2, 3, 4, 5]
"""
    
myList = [1, 2, 3, 3, 4, 4, 5]
print(myList)   
print(len(myList))  # length of the list    

myList1 = ["papaya", "banana", "cherry","apple"]    
print(myList1)

myList2 = [True, False, False, True]
print(myList2)

myList3 = [1, 2, 3, 4, "apple", "banana", "cherry", True, False]    
print(myList3)

#python collection
# List  :   ordered, changeable, allows duplicate members
# Tuple :   ordered, unchangeable, allows duplicate members
# Set   :   unordered, unindexed, no duplicate members
# Dictionary : unordered, changeable, indexed, no duplicate members

#index start from 0
print(myList3[5])   # banana
print(myList3[4])   # apple

print(myList3[-1])  # False
print(myList3[-2])  # True  


# range of values in the list
# first value is inclusive and second value is exclusive
print(myList3[2:5]) # [3, 4, 'apple']
print(myList3)

#change the value of the list at index 4
myList3[4] = "orange"

print(myList3)  # [1, 2, 3, 4, 'orange', 'banana', 'cherry', True, False]

myList3[4:7] = ["grapes", "mango", "papaya"]
print(myList3)


# add an item in between the list at index 5
myList3.insert(5, "kiwi")
print(myList3)  

myList3.insert(2,"mango")
print(myList3)

myList3.remove("mango")
print(myList3)

myList3.pop(6)
print(myList3)


print(myList1)
myList1.sort(reverse=True)
print(myList1)

myList.sort(reverse=True)
print(myList)

myList4 = myList3.copy()
print(myList4)

myList5 = myList + myList4
print(myList5)