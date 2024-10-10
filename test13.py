x = 200
y = "200"
print(isinstance(x, int))   # check if x is an integer
print(isinstance(y, str))   # check if y is an integer

print(bool(0))          # False 
print(bool(1))          # True
print(bool("value"))    # True
print(bool(""))         # False
print(bool([]))         # False
print(bool(()))         # False
print(bool({}))         # False
print(bool(None))       # False
print(bool(0.0))        # False
print(bool(0j))         # False
print(bool(0.0j))       # False
print(bool(1j))         # True
print(bool(0.1))        # True
print(bool(0.1j))       # True
print(bool(1.1))        # True
print(bool("Giri"))       # True
def myFunc1():
  return True

def myFunc2():
  return False
print("----------------")
print(myFunc1())         # True
print(myFunc2())         # False
print("----------------")