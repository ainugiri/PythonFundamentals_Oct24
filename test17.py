x = 10
y = 20
z = 13

if x < y and y > z: # check if x is less than y and y is greater than z
    print("Both conditions are True")
else:
    print("One or both conditions are False")
    

y = 12

if x < y and y > z: # check if x is less than y and y is greater than z
    print("Both conditions are True")
else:
    print("One or both conditions are False")


if x < y or y > z: # check if x is less than y and y is greater than z
    print("One or both conditions are True")
else:
    print("Both conditions are False")

y = 9
if x < y or y > z: # check if x is less than y and y is greater than z
    print("One or both conditions are True")
else:
    print("Both conditions are False")

if not(x < y or y > z): # check if x is less than y and y is greater than z
    print("One or both conditions are NOT True")
else:
    print("Both conditions are NOT False")

'''
 TRUTH TABLE
    AND             OR              NOT
    T and T = T     T or T = T      not T = F
    T and F = F     T or F = T      not F = T
    F and T = F     F or T = T  
    F and F = F     F or F = F
    
'''