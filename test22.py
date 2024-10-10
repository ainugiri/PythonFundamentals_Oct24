#looping statement
# while loop


i = 0
while i < 10:
    if i == 5:
        break
    print (i)
    i += 1
    
    
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
    
    

list = ["A","B","C","D","E","F"]
for x in list:
    print(x)

name = ["Giri", "Sekhar", "ABC"]
for x in name:
    if x == "Sekhar":
        continue
    print(x)
    
for x in range(4):
    print(x)

for x in range(2, 6):
    print(x)
else:
    print("Finally finished!")


# NESTED LOOPS 
list1 = ["A", "B", "C"]
list2 = ["1", "2", "3"]
for x in list1:
    for y in list2:
        print(x, y) 